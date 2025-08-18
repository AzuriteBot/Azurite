import inspect

class AzuriteLogger:
    base_logger = None

    @staticmethod
    def set_base_logger(logger):
        AzuriteLogger.base_logger = logger

    @staticmethod
    def INFO(message: str):
        if AzuriteLogger.base_logger:
            AzuriteLogger.base_logger.INFO(f"[MODULE] {message}")

    @staticmethod
    def SUCCESS(message: str):
        if AzuriteLogger.base_logger:
            AzuriteLogger.base_logger.SUCCESS(f"[MODULE] {message}")

    @staticmethod
    def WARN(message: str):
        if AzuriteLogger.base_logger:
            AzuriteLogger.base_logger.WARN(f"[MODULE] {message}")

    @staticmethod
    def ERROR(message: str):
        if AzuriteLogger.base_logger:
            AzuriteLogger.base_logger.ERROR(f"[MODULE] {message}")
