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

import json
import zipfile
from utils.pathManager import path

base = {
    "name": str,
    "module": {
        "mainEvent": str,
        "path": {
            "commands": str,
            "commandGroup": str,
            "events": str
        },
        "events": list,
        "command": list,
        "commandGroup": list
    },
    "require": {
        "plugin": list,
        "packages": list
    }
}


def white(moduleList, Logger):
    """Check if the structure of mapping.json is complete. If it is complete, then mark it as valid."""
    validModule = []
    for module in moduleList:
        try:
            with zipfile.ZipFile(f"{path.modules}/{module}", 'r') as z:
                with z.open("mapping.json") as f:
                    data = json.load(f)
                    missing = [k for k in base if k not in data]
                    if missing:
                        Logger.ERROR(f"{module.split('.')[0]} not valid!")
                        continue
                    Logger.LOADER(f"Module {module.split('.')[0]} valid")
                    validModule.append(module)
        except Exception as e:
            Logger.ERROR(f"{module.split('.')[0]} not valid!")
            continue
    return validModule
