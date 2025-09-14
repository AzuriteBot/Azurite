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
