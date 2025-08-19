import sys,platform,os
import time
def setupLog(Logger, fileName, fileNum):
    Logger.INFO(f"Running python {platform.python_version()}")
    time.sleep(0.2)
    Logger.INFO(f"Python path: {sys.executable}")
    time.sleep(0.2)
    Logger.LOAD(f"Loading Azurite")
    time.sleep(0.2)
    Logger.LOAD(f"Bot path: {os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))}")
    time.sleep(0.2)
    Logger.LOAD(f"Log name: {fileName}-{fileNum}.log")
    time.sleep(0.2)