# Workspace

## Overview:

-   stored in workspaces.csv
-   used to store default and generated workspaces

## Syntax:

-   Keyoverview:

```
name,,files,,dirs,,commands,,contents
```

-   Example:

```
custom,,test.csv;;;test.py,,None,,None,,test.csv:::Max Mueller,20,male,max.mueller@gmail.com
```

-   generates the following:

    ```bash
    >>> tree
    ...	test.csv
    ... test.py

    >>> more test.csv
    ... Max Mueller,20,male,max.mueller@gmail.com
    ```

### Seperators:

-   `,,` --> keys

-   `;;;` --> values

-   `:::` --> `file:::content` (seperates filename and its content)

#### Custom Syntax:

-   `<br>` --> creates a linebreak (only usable in contents key field)

## Usage:

```
py setup-workspace.py --<workspace name> <path>

py setup-workspace.py --custom ./
```
