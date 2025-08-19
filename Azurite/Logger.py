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
