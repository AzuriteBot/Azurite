from Azurite import Logger
def on_ready():
    Logger.INFO("Hello world, I am the default module of Azurite")
def on_stop():
    Logger.INFO("Default has been disabled")