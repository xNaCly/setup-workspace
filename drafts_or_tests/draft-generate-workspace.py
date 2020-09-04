import os
import pathlib
import uuid

path = "C:\\Desktop1\\setupworkspace"
name = str(uuid.uuid4())[0:4]
exceptarray = [".git",".gitignore","__pycache__","log"]
files = []
dirs = []

for item in os.listdir(path):
        if item in exceptarray:
            continue
        else:
            if os.path.isdir(path + "\\"+ item):
                dirs.append(item)
            else:
                files.append(item)

for folder in dirs:
    if folder in exceptarray:
        continue
    else:
        for item_ in os.listdir(path +"\\"+ folder):
            if folder in exceptarray:
                continue
            else:
                if os.path.isdir(folder + "\\" + item_):
                    dirs.append(folder + "\\" +  item_)
                else:
                    files.append(folder + "\\" +  item_)

try:
    writestring = f"\n{name}|" + ";;".join(files) + "|" + ";;".join(dirs) + "|None|None" 
    with open("workspaces.csv", "a") as f:
        f.write(writestring)
    for x in dirs:
        print("++ .\\" + x)
    for x in files:
        print("++ " + x)
    print("workspace template generated as: " + name)
except:
    raise RuntimeError("Something went wrong")

