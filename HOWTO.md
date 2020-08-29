### How to:

-   execute workspace gen:

    `setup-workspace.py [type of workspace] [File path]`

-   Arguments:
    -   type of [workspace](https://github.com/xNaCly/setup-workspace/blob/master/src/config.py)
    -   file path: `[".", "./", "C:/dir"]`

```
example:
setup-workspace.py --node C:\Users\User\Desktop
```

creates:
<br>
<kbd>
<img src=https://cdn.discordapp.com/attachments/638844015084568597/749205800035287070/unknown.png />
</kbd>

## [Configs](https://github.com/xNaCly/setup-workspace/blob/master/src/config.py):

-   basic configs include:

    -   --node workspace
    -   --python workspace

-   Syntax config/workspaces:
    ```python
        workspaces = {
            "node":{
                "files":["src\\index.js","src\\config.json","docs\\README.md"],
                "dirs":["src","docs"],
                "commands":["npm init -y"]
            },
            "python":{
                "files":["src\\main.py", "src\\config.py"],
                "dirs":["src"]
            },
            "html":{
                "files":["src\\index.html", "src\\style.css", "src\\index.js"],
                "dirs":["src"]
            },
            >>>> custom workspace structure
            "workspace_name_here":{
                "files":["folder\\index.html", "folder\\index.js", "folder\\style.css"],
                "dirs":["folder"]
            }
        }
    ```
    -   to use the custom workspace config:
    ```
    setup-workspace.py --workspace_name_here C:\Users\User\Desktop
    ```
