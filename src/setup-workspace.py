from pathlib import Path
import workspaces
import os
import sys
import subprocess

exceptarray = workspaces.except_files_in_generation 

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
    path = Path(args[1])
except:
    raise ValueError("invaild arguments or not given")


if type_of_workspace == "gen_workspace":
    # HOWTO.md
    # README.md
    # src
    # src\setup-workspace.py
    # src\workspaces.py
    # test.py
    pass

# loop through given workspace template
    # "workspace":{
    #     "files":["folder\\file"],
    #     "dirs":["folder"],
    #     "commands":["command"]
    # }


# loop through folders (workspace["dirs"])
try:
    print("\n")
    for dir in workspaces.workspaces[type_of_workspace]["dirs"]:
        try:
            subprocess.call(f"mkdir {dir}", shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(dir + r"\ created") 
            # raises warning "Anomalous backslash in string: '\ ' " can be ignored!
        except:
            dirs = str(workspaces.workspaces[type_of_workspace]["dirs"])
            raise ValueError(f"path ({str(path)}) invalid, couldn't create {dirs}")
except:
    pass


# loop through files (workspace["files"])
try:
    print("\n")
    for element in workspaces.workspaces[type_of_workspace]["files"]:
        try:
            with open(str(path) + "\\" + element, "w") as f:
                try:
                    for x in workspaces.workspaces[type_of_workspace]["contents"]:
                        content = x.split(":::")
                        if content[0] == element:
                            f.write(content[1])
                except:
                    pass
                f.close()
            print(element + " created")
        except:
            files = str(workspaces.workspaces[type_of_workspace]["files"])
            raise ValueError(f"path ({str(path)}) invalid, couldn't create {files}")
except:
    # runs if no files are found in workspace 
    pass


# if there are commands, loop through them (workspace["commands"])
try:
    print("\n")
    for command in workspaces.workspaces[type_of_workspace]["commands"]:
        try:
            if command == "git remote add origin":
                command = command + " " + args[2]
            # execute given shell commands in given path
            subprocess.call(command, shell = True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(command + " executed")
        except:
            raise ValueError(f"command ({command}) invalid, couldn't execute")
except:
    # runs if no commands are found in workspace 
    pass

print("\n\nWorkspace created.")