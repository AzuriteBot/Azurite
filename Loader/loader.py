import importlib
import json
import os.path
import sys
import zipfile

from utils.pathManager import path
class loader():
    def __init__(self, app, moduleList, Logger):
        self.app = app
        self.moduleList = moduleList,
        self.Logger = Logger

        self.moduleEvent = False
        super().__init__()

    async def load(self):
        self.Logger.LOADER("Currently checking the module")
        totalModule = [os.path.join(path.modules, f) for f in os.listdir(path.modules) if f.endswith(".zip")]
        self.Logger.LOADER(f"Loading {len(totalModule)}")

        for moduleList in self.moduleList:
            for module in moduleList:
                self.Logger.LOADER(f"Load module {module.split('.')[0]}")
                with zipfile.ZipFile(f"{path.modules}/{module}", 'r') as z:
                    try:
                        with z.open("mapping.json") as f:
                            data = json.load(f)
                        mainEvent = data['module']['mainEvent']

                        eventPath = data['module']['path']['events']
                        commandPath = data['module']['path']['commands']
                        commandGroup = data['module']['path']['commandGroup']

                        eventsList = data['module']['events']
                        commandList = data['module']['command']
                        commandGroupList = data['module']['commandGroup']
                    except Exception as e:
                        self.Logger.ERROR(e)
                    if mainEvent in z.namelist():
                        self.moduleEvent = True
                    sys.path.insert(0, f"{path.modules}/{module}")
                    if self.moduleEvent == True:
                        moduleEvent = importlib.import_module(mainEvent.split('.')[0])
                        moduleEvent.on_ready()

                    if len(eventsList) > 0:
                        for item in commandList:
                            try:
                                module_name = f"{eventPath}.{item}"
                                eventModule = importlib.import_module(module_name)
                                className = item
                                A = getattr(eventModule, className)
                                cog = A(app=self.app)
                                await self.app.add_cog(cog)
                            except Exception as e:
                                self.Logger.ERROR(message=e)
                                continue
                    if len(commandList) > 0:
                        for item in commandList:
                            try:
                                module_name = f"{commandPath}.{item}"
                                commandModule = importlib.import_module(module_name)
                                className = item
                                A = getattr(commandModule, className)
                                cog = A(app=self.app)
                                await self.app.add_cog(cog)
                            except Exception as e:
                                self.Logger.ERROR(message=e)
                                continue
                    if len(commandGroupList) > 0:
                        for item in commandGroupList:
                            try:
                                module_name = f"{commandGroup}.{item}"
                                commandModule = importlib.import_module(module_name)
                                className = item
                                A = getattr(commandModule, className)
                                cog = A(app=self.app)
                                await self.app.add_command(cog)
                            except Exception as e:
                                self.Logger.ERROR(message=e)
                                continue

