import sys,platform,os
def setupLog(Logger, fileName, fileNum):
    Logger.INFO(f"Running python {platform.python_version()}")
    Logger.INFO(f"Python path: {sys.executable}")
    Logger.LOAD(f"Loading Azurite")
    Logger.INFO(f"Bot path: {os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))}")
    Logger.INFO(f"Log name: {fileName}-{fileNum}.log")