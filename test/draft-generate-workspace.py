import os
import pathlib

path = "../"

except_files_in_generation = [".git", ".gitignore", "__pycache__", "log"]

def test(path):
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
        # finalfiles = ""
        # finaldirs = ""
        # for file in files:
        #     finalfiles = finalfiles + file  + ";"
        # for dirr in dirs:
        #     finaldirs = finaldirs + dirr  + ";"
        with open("test.csv", "a") as f:
            f.write(f"\n{files},{dirs}")
    except:
        raise RuntimeError("Something went wrong")

test(path)