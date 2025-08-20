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
