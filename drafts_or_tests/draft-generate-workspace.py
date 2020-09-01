import os
import pathlib
import uuid

name = str(uuid.uuid4())[0:4]
path = "../"

except_files_in_generation = [".git", ".gitignore", "__pycache__", "log"]

def test(name, path):
    files = []
    dirs = []
    startdir = os.listdir(path)
    for dir_or_file in startdir:
        if dir_or_file in except_files_in_generation:
            pass
        else:
            try:
                for file in os.listdir(path + "\\" + dir_or_file):
                    if file in except_files_in_generation:
                        pass
                    else:
                        files.append(str(dir_or_file + "\\" + file))
                        if dir_or_file in dirs:
                            pass
                        else:
                            dirs.append(dir_or_file)
            except:
                files.append(dir_or_file)

    try:
        with open("generated_workspaces.csv", "a") as f:
            f.write(
                "\n" + 
                name 
                + ",," + 
                str(files).replace(",",";;;").replace("[","").replace("]","").replace(" ", "").replace("'", "") 
                + ",," + 
                str(dirs).replace(",",";;;").replace("[","").replace("]","").replace(" ", "").replace("'", "")
                + ",," +
                "None" 
                + ",," +
                "None"
            )
        for x in dirs:
            print("++ ./" + x)
        for x in files:
            print("++ " + x)
        print("workspace template generated as: " + name)
    except:
        raise RuntimeError("Something went wrong")

test(name, path)