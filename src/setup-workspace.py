from pathlib import Path
import workspaces
import sys
import subprocess


# get arguments from script call ["setup-workspace.py", "--workspacetype", "path"]
args = sys.argv
# remove first arguments as its the name of the script (setup-workspace.py)
args.pop(0)

# check if all arguments are given 
# >>>> type_of_workspace ["--node","--python","--html","--custom"]
# >>>> path [".", "./", "C:/dir"]
try:
    type_of_workspace = args[0].replace("--", "")
    path = Path(args[1])
except:
    raise ValueError("invaild arguments")

print("\n")

# loop through given workspace template
    # "workspace":{
    #     "files":["folder\\file"],
    #     "dirs":["folder"],
    #     "commands":["command"]
    # }

# loop through folders (workspace["dirs"])
for dir in workspaces.workspaces[type_of_workspace]["dirs"]:
    try:
        subprocess.call(f"mkdir {dir}", shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(dir + "\ created")
    except:
        dirs = str(workspaces.workspaces[type_of_workspace]["dirs"])
        raise ValueError(f"path ({str(path)}) invalid, couldn't create {dirs}")

print("\n")

# loop through files (workspace["files"])
for element in workspaces.workspaces[type_of_workspace]["files"]:
    try:
        with open(str(path) + "\\" + element, "w") as f:
            f.close()
        print(element + " created")
    except:
        files = str(workspaces.workspaces[type_of_workspace]["files"])
        raise ValueError(f"path ({str(path)}) invalid, couldn't create {files}")

print("\n")

# if there are commands, loop through them (workspace["commands"])
try:
    for command in workspaces.workspaces[type_of_workspace]["commands"]:
        try:
            subprocess.call(command, shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(command + " executed")
        except:
            raise ValueError(f"command ({command}) invalid, couldn't execute")
except:
    # runs if no commands are found in workspace 
    pass

print("\n\nWorkspace created.")