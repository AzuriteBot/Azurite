import time
import psutil

def threadCalc(moduleList):
    totalCore = psutil.cpu_count(logical=True)
    totalThread = psutil.cpu_count(logical=False)
    thread = totalCore + totalThread

    lenModuleList = len(moduleList)
    result = {}

    if lenModuleList > thread:
        min_each = lenModuleList // thread
        extra = lenModuleList % thread

        start = 0
        for t in range(thread):
            end = start + min_each + (1 if t < extra else 0)
            result[f"thread_{t}"] = moduleList[start:end]
            start = end
    else:
        for idx, m in enumerate(moduleList):
            result[f"thread_{idx}"] = [m]

    return result, lenModuleList



# Test
start = time.time()
modules = [f"module_{i}" for i in range(1, 12213891)]
a, b = threadCalc(modules)
elapsed = time.time() - start
print(f"test with {b} module")
print(f"done in {elapsed:.6f} s")
