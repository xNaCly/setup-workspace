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
