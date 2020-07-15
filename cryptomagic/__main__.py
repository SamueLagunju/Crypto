from sys import platform as _platform

print("Verifying OS...")

if _platform == "linux":
    print('Linux OS detected')
elif _platform == "darwin":
    print('Mac OS detected')
elif _platform == "Windows":
    print('Windows OS detected')
