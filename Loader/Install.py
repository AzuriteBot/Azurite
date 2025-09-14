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