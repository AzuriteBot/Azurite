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

import os
from utils.pathManager import path

from Loader.White import white
from Loader.Install import checkInstall
from Loader.loader import loader

from Azurite import app

async def initLoader(Logger,
                     app,
                     command,
                     commandGroup,
                     events):
    """initialize loader"""


    moduleList = []
    for module in os.listdir(path.modules):
        if module.endswith('.zip'):
            moduleList.append(module)
    validModule = white(moduleList=moduleList, Logger=Logger) #check module, if valid then add to validModule
    checkInstall(moduleList=moduleList, Logger=Logger) # check if the module needs to install any packages
    Loader = loader(app=app, moduleList=validModule, Logger=Logger, command=command, commandGroup=commandGroup, events=events)
    await Loader.load()
