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

import inspect
import os

class AzuriteLogger:
    base_logger = None

    @staticmethod
    def set_base_logger(logger):
        AzuriteLogger.base_logger = logger

    @staticmethod
    def _get_caller_dir():
        frame = inspect.stack()[2]
        caller_file = frame.filename
        name = f"{os.path.basename(os.path.dirname(caller_file))}"
        return name.split('.')[0]
    @staticmethod
    def INFO(message: str):
        if AzuriteLogger.base_logger:
            callerDir = AzuriteLogger._get_caller_dir()
            AzuriteLogger.base_logger.INFO(f"[{callerDir}] {message}")

    @staticmethod
    def SUCCESS(message: str):
        if AzuriteLogger.base_logger:
            callerDir = AzuriteLogger._get_caller_dir()
            AzuriteLogger.base_logger.SUCCESS(f"[{callerDir}] {message}")

    @staticmethod
    def WARN(message: str):
        if AzuriteLogger.base_logger:
            callerDir = AzuriteLogger._get_caller_dir()
            AzuriteLogger.base_logger.WARN(f"[{callerDir}] {message}")

    @staticmethod
    def ERROR(message: str):
        if AzuriteLogger.base_logger:
            callerDir = AzuriteLogger._get_caller_dir()
            AzuriteLogger.base_logger.ERROR(f"[{callerDir}] {message}")
