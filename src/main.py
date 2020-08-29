from pathlib import Path
import config
import sys
import subprocess



args = sys.argv
args.pop(0)


try:
    type_of_workspace = args[0]
    path = Path(args[1])
except:
    raise ValueError("invaild arguments")



if type_of_workspace == "--node":
    print("\n")

    for dir in config.node["dirs"]:
        try:
            subprocess.call(f"mkdir {dir}", shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(dir + "/ created")
        except:
            dirs = str(config.node["dirs"])
            raise ValueError(f"path ({str(path)}) invalid, couldn't create {dirs}")

    print("\n")

    for element in config.node["files"]:
        try:
            with open(str(path) + "\\" + element, "w") as f:
                f.close()
            print(element + " created")
        except:
            files = str(config.node["files"])
            raise ValueError(f"path ({str(path)}) invalid, couldn't create {files}")

    print("\n")

    for command in config.node["commands"]:
        try:
            subprocess.call(command, shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(command + " executed")
        except:
            raise ValueError(f"command ({command}) invalid, couldn't execute")

    print("\n\nWorkspace created.")