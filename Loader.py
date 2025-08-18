import os.path
import zipfile
import importlib
import json

import sys, subprocess
from utils.Logger import Logger

baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
moduleDir = os.path.join(baseDir, 'modules')
class Loader():
    def __init__(self,app, moduleList, Logger: Logger):
        self.app = app
        self.Logger = Logger
        self.moduleList = moduleList
    def _install(self, name):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
    async def load(self):

        moduleEvent = False

        self.Logger.LOADER("Checking module")
        totalModule = [os.path.join(moduleDir, f) for f in os.listdir(moduleDir) if f.endswith(".zip")]
        self.Logger.LOADER(f"Loading {len(totalModule)} module.")

        for module in self.moduleList:
            self.Logger.LOADER(f"Load module {module}")
            with zipfile.ZipFile(f'{moduleDir}/{module}', 'r') as z:
                if f"main_events.py" in z.namelist():
                    moduleEvent = True
                self.Logger.LOADER(f"Read mapping.json / {module}")
                try:
                    with z.open(f'mapping.json') as f:
                        data = json.load(f)
                except Exception as e:
                    self.Logger.ERROR(e)
            eventsList = data['module']['events']
            commandList = data['module']['command']
            commandGroupList = data['module']['commandGroup']

            LicenseStatus = data['License']['enable']
            LicenseApi = data['License']['api']

            require_Pl = data['require']['plugin']
            require_Package = data['require']['packages']

            self.Logger.INFO("Checking package...")
            for package in require_Package:
                try:
                    if package == "discord.py":
                        importlib.import_module('discord')
                    else:
                        importlib.import_module(package)
                except:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

            sys.path.insert(0, f"{moduleDir}/{module}")


            if moduleEvent == True:
                moduleEvent = importlib.import_module(f'main_events')
                moduleEvent.on_ready()

            if len(commandList) > 0:
                for item in commandList:
                    try:
                        self.Logger.INFO(message=f"Load {item}")
                        module_name = f"commands.{item}"
                        commandModule = importlib.import_module(module_name)
                        className = item
                        A = getattr(commandModule, className)
                        cog = A(app=self.app)
                        await self.app.add_cog(cog)
                        self.Logger.INFO(message=f"Success load {item}")
                    except Exception as e:
                        self.Logger.ERROR(message=e)
                        continue
            if len(commandGroupList) > 0:
                for item in commandGroupList:
                    try:
                        self.Logger.INFO(message=f"Load {item}")
                        module_name = f"commandGroup.{item}"
                        commandModule = importlib.import_module(module_name)
                        className = item
                        A = getattr(commandModule, className)
                        cog = A(app=self.app)
                        await self.app.add_command(cog)
                        self.Logger.SUCCESS(message=f"Success load {item}")
                    except Exception as e:
                        self.Logger.ERROR(message=e)
                        continue

