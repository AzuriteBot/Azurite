import os

def initialization():
    baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

    os.makedirs(f"{baseDir}/cache", exist_ok=True)
    os.makedirs(f"{baseDir}/logs", exist_ok=True)
