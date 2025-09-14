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
import time
from datetime import datetime


import yaml
import discord
from discord.ext import commands

# local libs
from Azurite.Logger import AzuriteLogger
from Azurite.app import getapp
from Initialization import initialization

from utils.Logger import Logger
from utils.pathManager import path
from utils.setupLog import setupLog
from utils.tokenCheck import tokenChecker

from Loader.White import white
from Loader.Install import checkInstall
from Loader.loader import loader

# local ui
from ui.enterToken import enterToken

# local
from local.events.pingCheck import pingCheck

startTime = time.time()

def initLogFile():
    fileName = f"{datetime.now().strftime("%Y-%m-%d")}"
    existing = [f for f in os.listdir(f'logs')
                if f.startswith(fileName)
                and
                f.endswith('.log')]
    fileNum = len(existing) + 1
    return f"{fileName}-{fileNum}.log", fileName, fileNum


def main(Token,
         Logger,
         useEvents, useCommands, useCommandGroup,
         autoPingCheck, autoPingCheckInterval,  autoPingCheckRound):
    app = commands.Bot(intents=discord.Intents.default(), command_prefix='!')

    @app.event
    async def on_ready():

        #init loader and load module
        moduleList = []
        for module in os.listdir(os.path.join('modules')):
            if module.endswith('.zip'):
                moduleList.append(module)
        validModule = white(moduleList, Logger=Logger)
        checkInstall(moduleList=moduleList, Logger=Logger)
        Logger.DEBUG(f"{type(useCommands)}")
        Loader = loader(app=app, moduleList=validModule, Logger=Logger, command=useCommands, commandGroup=useCommandGroup, events=useEvents)
        await Loader.load()

        Logger.SUCCESS("Done, waiting for sync..")

        sync = await app.tree.sync()
        Logger.SUCCESS(message=f"{len(sync)} slash command" if len(sync) == 1 else f"{len(sync)} slash commands")

        #load localevents
        Logger.INFO("Load local events")
        if autoPingCheck == True:
            pingTask = pingCheck(bot=app,Logger=Logger,interval=autoPingCheckInterval, Round=autoPingCheckRound)
            pingTask.start()
        Logger.SUCCESS(message='Bot has started')
        Logger.SUCCESS(message=f"Done after {round(startTime-time.time(), 2)} s")


    if Token != False:
        getapp.set_base_app(app=app)
        app.run(Token)
    else:
        def showUiandCheck():
            while True:
                token = enterToken()
                if tokenChecker(token=token, Logger=Logger):
                    lines = []
                    with open(path.config, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.strip().startswith("Token:"):
                                lines.append(f"Token: '{token}'\n")
                            else:
                                lines.append(line)

                    with open(path.config, 'w', encoding='utf-8') as f:
                        f.writelines(lines)

                    app.run(token)
                    break

        showUiandCheck()



if __name__ == "__main__":

    logName, fileName, fileNum = initLogFile()
    Logger = Logger(logName=logName)

    AzuriteLogger().set_base_logger(logger=Logger) #set base logger for azurite lib

    setupLog(Logger=Logger, fileName=fileName, fileNum=fileNum) #setup log utils/setupLog.py

    #read config.yml
    with open(path.config, 'r', encoding='utf-8') as configData:
        config = yaml.load(stream=configData, Loader=yaml.SafeLoader)

    Token = config['Token']
    mappingFile = config['Loader']['mappingFile']
    useEvents = config['Loader']['events']
    useCommands = config['Loader']['commands']
    useCommandGroup = config['Loader']['commandsGroup']

    #local
    autoPingCheck = config['autoPingCheck']['enable']
    autoPingCheckInterval = config['autoPingCheck']['interval']
    autoPingCheckRound = config['autoPingCheck']['round']

    checkToken = tokenChecker(Token, Logger=Logger) #check token

    if checkToken == False:
        Logger.ERROR("Token not found")
        Token = False

    initialization() #create logs, cache...



    main(Logger=Logger, Token=Token,
         useEvents=useEvents, useCommands=useCommands,
         useCommandGroup=useCommandGroup,
         autoPingCheck=autoPingCheck, autoPingCheckInterval=autoPingCheckInterval, autoPingCheckRound=autoPingCheckRound)

