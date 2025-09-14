from datetime import datetime
import os
def initLogFile():
    fileName = f"{datetime.now().strftime("%Y-%m-%d")}"
    existing = [f for f in os.listdir(f'logs')
                if f.startswith(fileName)
                and
                f.endswith('.log')]
    fileNum = len(existing) + 1
    return f"{fileName}-{fileNum}.log", fileName, fileNum