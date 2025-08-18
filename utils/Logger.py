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
        console_msg = f"{color}[{timestamp}] [{level}] {Style.RESET_ALL}{message}"
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
