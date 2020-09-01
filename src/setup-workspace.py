from pathlib import Path
import os
import sys
import subprocess

exceptarray = None
workspaces_dict = {}

with open("./config.csv", "r") as f:
    exceptarray = f.read().split("\n")[1].split(",")

with open("./workspaces.csv","r") as f:
    workspaces = f.read().split("\n")
    workspaces.pop(0)

for workspace in workspaces:
    workspace = workspace.replace("\\\\","\\").split(",,")
    #node, src\\index.js;src\\config.json, src, npm init -y
    workspaces_dict[workspace[0]] = {
        "files": workspace[1].split(";;;"),
        "dirs": workspace[2].split(";;;"),
        "commands": workspace[3].split(";;;"),
        "contents": workspace[4].replace("<br>","\n").split(";;;")
    }


# get arguments from script call ["setup-workspace.py", "--workspacetype", "path"]
args = sys.argv
# remove first arguments as its the name of the script (setup-workspace.py)
args.pop(0)

# check if all arguments are given 
# >>>> type_of_workspace ["--node","--python","--html","--custom"]
# >>>> path [".", "./", "C:/dir"]
# >>>> --git
# >>>> githubrepolink
try:
    type_of_workspace = args[0].replace("--", "")
except:
    raise ValueError("invaild arguments or not given")

path = Path(args[1])

if type_of_workspace == "gen_workspace":
    pass


# loop through folders (workspace["dirs"])
try:
    print("\n")
    for dir in workspaces_dict[type_of_workspace]["dirs"]:
        if dir == "None":
            continue
        try:
            subprocess.call(f"mkdir {dir}", shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(dir + r"\ created") 
            # raises warning "Anomalous backslash in string: '\ ' " can be ignored!
        except:
            dirs = str(workspaces_dict[type_of_workspace]["dirs"])
            raise ValueError(f"path ({str(path)}) invalid, couldn't create {dirs}")
except:
    pass


# loop through files (workspace["files"])
try:
    print("\n")
    for element in workspaces_dict[type_of_workspace]["files"]:
        if element == "None":
            continue
        try:
            with open(str(path) + "\\" + element, "w") as f:
                try:
                    for x in workspaces_dict[type_of_workspace]["contents"]:
                        content = x.split(":::")
                        if content[0] == element:
                            f.write(content[1])
                except:
                    pass
                f.close()
            print(element + " created")
        except:
            files = str(workspaces_dict[type_of_workspace]["files"])
            raise ValueError(f"path ({str(path)}) invalid, couldn't create {files}")
except:
    # runs if no files are found in workspace 
    pass


# if there are commands, loop through them (workspace["commands"])
try:
    print("\n")
    for command in workspaces_dict[type_of_workspace]["commands"]:
        try:
            if command == "git remote add origin":
                command = command + " " + args[2]
            elif command == "None":
                continue
            # execute given shell commands in given path
            subprocess.call(command, shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(command + " executed")
        except:
            raise ValueError(f"command ({command}) invalid, couldn't execute")
except:
    # runs if no commands are found in workspace 
    pass

print("\n\nWorkspace created.")