from pathlib import Path
import workspaces
import sys
import subprocess



args = sys.argv
args.pop(0)


try:
    type_of_workspace = args[0].replace("--", "")
    path = Path(args[1])
except:
    raise ValueError("invaild arguments")

print("\n")
for dir in workspaces.workspaces[type_of_workspace]["dirs"]:
    try:
        subprocess.call(f"mkdir {dir}", shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(dir + "\ created")
    except:
        dirs = str(workspaces.workspaces[type_of_workspace]["dirs"])
        raise ValueError(f"path ({str(path)}) invalid, couldn't create {dirs}")
print("\n")
for element in workspaces.workspaces[type_of_workspace]["files"]:
    try:
        with open(str(path) + "\\" + element, "w") as f:
            f.close()
        print(element + " created")
    except:
        files = str(workspaces.workspaces[type_of_workspace]["files"])
        raise ValueError(f"path ({str(path)}) invalid, couldn't create {files}")
print("\n")
try:
    for command in workspaces.workspaces[type_of_workspace]["commands"]:
        try:
            subprocess.call(command, shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(command + " executed")
        except:
            raise ValueError(f"command ({command}) invalid, couldn't execute")
except:
    pass

print("\n\nWorkspace created.")