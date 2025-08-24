import os
import sys
import platform
from datetime import datetime

import yaml
import discord
from discord.ext import commands

# local libs
from Azurite.Logger import AzuriteLogger
from Initialization import initialization

from utils.Logger import Logger
from utils.pathManager import path
from utils.setupLog import setupLog
from utils.tokenCheck import tokenChecker

from Loader.White import white
from Loader.Install import checkInstall
from Loader.loader import loader

def main(Token, Logger, useEvents, useCommands, useCommandGroup):
    app = commands.Bot(intents=discord.Intents.default(), command_prefix='!')

    @app.event
    async def on_ready():

        moduleList = []
        for module in os.listdir(os.path.join('modules')):
            if module.endswith('.zip'):
                moduleList.append(module)
        validModule = white(moduleList, Logger=Logger)
        checkInstall(moduleList=moduleList, Logger=Logger)
        Loader = loader(app=app, moduleList=validModule, Logger=Logger, command=useCommands, commandGroup=useCommandGroup, events=useEvents)
        await Loader.load()

        Logger.SUCCESS("Done, waiting for sync..")

        sync = await app.tree.sync()
        Logger.SUCCESS(message=f"{len(sync)} slash command" if len(sync) == 1 else f"{len(sync)} slash commands")
        Logger.SUCCESS(message='Bot has started')
    if Token != False:
        app.run(Token)



if __name__ == "__main__":
    fileName = f"{datetime.now().strftime("%Y-%m-%d")}"
    existing = [f for f in os.listdir(f'logs')
                if f.startswith(fileName)
                and
                f.endswith('.log')]
    fileNum = len(existing) + 1
    Logger = Logger(logName=f"{fileName}-{fileNum}.log")

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

    checkToken = tokenChecker(Token) #check token

    if checkToken == False:
        Logger.ERROR("Token not found")
        Token = False

    initialization() #create logs, cache...

    main(Logger=Logger, Token=Token, useEvents=useEvents, useCommands=useCommands, useCommandGroup=useCommandGroup)