### How to:

-   execute workspace gen:

    `setup-workspace.py` `<type of workspace>` `<File path>` `[git repo link]`

-   Arguments:
    -   type of [workspace](https://github.com/xNaCly/setup-workspace/blob/master/src/workspaces.py)
    -   file path: `[".", "./", "C:/dir"]`

```bash
example:

>>>> setup-workspace.py --node C:\Users\<user>\Desktop

>>>> tree /f
    C:.
    │   package.json
    │
    ├───docs
    │       README.md
    │
    └───src
            config.json
            index.js
```

## [Workspaces](https://github.com/xNaCly/setup-workspace/blob/master/src/workspaces.py):

-   default workspaces include:

    -   --node
    -   --python
    -   --html
    -   --git
        <br>
        (usage requires gitrepo link: `setup-workspace.py --git C:\Users\<user>\Desktop https://github.com/<user>/test.git`)

-   Syntax config/workspaces:

    ```python
    >>>> custom workspace syntax (workspaces.py):

        "workspace_name_here":{
            "files":["folder\\index.html", "folder\\index.js", "folder\\style.css"],
            "dirs":["folder"],
            "commands":["shell-commands"]
        }
    ```

    -   to use the custom workspace config:

    ```
    setup-workspace.py --workspace_name_here C:\Users\<user>\Desktop
    ```
