#MIT License

#Copyright (c) 2025 kenftr

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import importlib
import json
import os.path
import sys
import zipfile

from utils.pathManager import path
class loader():
    def __init__(self, app, moduleList, Logger, command, commandGroup, events):
        super().__init__()
        self.app = app
        self.moduleList = moduleList
        self.Logger = Logger

        self.command = command
        self.commandGroup = commandGroup
        self.events = events

        self.moduleEvent = False

    async def load(self):
        self.command, self.commandGroup, self.events = bool(self.command), bool(self.commandGroup), bool(self.events)
        self.Logger.LOADER("Currently checking the module")
        totalModule = [os.path.join(path.modules, f) for f in os.listdir(path.modules) if f.endswith(".zip")]
        self.Logger.LOADER(f"Loading {len(totalModule)}")

        for module in self.moduleList:
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

                if self.events == True:
                    if len(eventsList) > 0:
                        for item in commandList:
                            try:
                                module_name = f"{eventPath}.{item}"
                                eventModule = importlib.import_module(module_name)
                                className = item
                                module = getattr(eventModule, className)
                                cog = module(app=self.app)
                                await self.app.add_cog(cog)
                            except Exception as e:
                                self.Logger.ERROR(message=e)
                                continue
                if self.command == True:
                    if len(commandList) > 0:
                        for item in commandList:
                            try:
                                module_name = f"{commandPath}.{item}"
                                commandModule = importlib.import_module(module_name)
                                className = item
                                module = getattr(commandModule, className)
                                cog = module(app=self.app)
                                await self.app.add_cog(cog)
                            except Exception as e:
                                self.Logger.ERROR(message=e)
                                continue
                if self.commandGroup == True:
                    if len(commandGroupList) > 0:
                        for item in commandGroupList:
                            try:
                                module_name = f"{commandGroup}.{item}"
                                commandModule = importlib.import_module(module_name)
                                className = item
                                module = getattr(commandModule, className)
                                cog = module(app=self.app)
                                await self.app.add_command(cog)
                            except Exception as e:
                                self.Logger.ERROR(message=e)
                                continue
