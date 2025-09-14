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

import sys,platform,os
import time
import json
from utils.pathManager import path
def setupLog(Logger, fileName, fileNum):
    with open(path.azuritejson, 'r') as f:
        info = json.load(f)
    Logger.INFO(f"Running python {platform.python_version()}")
    time.sleep(0.2)
    Logger.INFO(f"Python path: {sys.executable}")
    time.sleep(0.2)
    Logger.LOAD(f"Loading Azurite {info['version']}")
    time.sleep(0.2)
    Logger.LOAD(f"Bot path: {os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))}")
    time.sleep(0.2)
    Logger.LOAD(f"Log name: {fileName}-{fileNum}.log")
    time.sleep(0.2)