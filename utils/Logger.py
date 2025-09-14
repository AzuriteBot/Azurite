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
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
os.makedirs(baseDir, exist_ok=True)

class Logger:
    def __init__(self, logName: str):
        self.logName = logName
        super().__init__()

    def _write(self, message: str):
        with open(f"{baseDir}/{self.logName}", 'a', encoding='utf-8') as f:
            f.write(message)
    def _log(self, level: str, color: str, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        console_msg = f"{color}["+ Fore.WHITE + f"{timestamp}{color}] [" + Fore.BLUE + f"Azurite" + Fore.WHITE + f"/{color}{level}] {Style.RESET_ALL}{message}"
        file_msg    = f"{color}[{timestamp}] [{level}] {Style.RESET_ALL}{message}\n"

        print(console_msg)
        self._write(file_msg)

    def INFO(self, message: str):
        self._log("INFO", Fore.LIGHTGREEN_EX, message)
    def SUCCESS(self, message: str):
        self._log("SUCCESS", Fore.GREEN, message)
    def LOAD(self, message: str):
        self._log("LOADING", Fore.YELLOW, message)
    def LOADER(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        console_msg = f"{Fore.MAGENTA}{Style.BRIGHT}[{timestamp}] [LOADER]{Style.RESET_ALL} {message}"
        file_msg    = f"[{timestamp}] [LOADER] {message}\n"
        print(console_msg)
        self._write(file_msg)

    def WARN(self, message: str):
        self._log("WARN", Fore.YELLOW, message)

    def ERROR(self, message: str):
        self._log("ERROR", Fore.RED, message)

    def DEBUG(self, message: str):
        self._log("DEBUG", Fore.CYAN, message)

    def CRITICAL(self, message: str):
        self._log("CRITICAL", Fore.MAGENTA + Style.BRIGHT, message)
