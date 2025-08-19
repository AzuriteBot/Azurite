import importlib
import json
import subprocess
import sys
import zipfile

from utils.pathManager import path

def _installPackage(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
def checkInstall(moduleList, Logger):
    for module in moduleList:
        try:
            with zipfile.ZipFile(f"{path.modules}/{module}", 'r') as z:
                with z.open('mapping.json') as f:
                    data = json.load(f)
                    for package in data['require']['packages']:
                        try:
                            if package == "discord.py":
                                importlib.import_module('discord')
                            else:
                                importlib.import_module(package)
                        except:
                            _installPackage(name=package)
        except Exception as e:
            Logger.ERROR(f"Failed to load {module.split('.')[0]}")