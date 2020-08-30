workspaces = {
    "node":{
        "files":["src\\index.js","src\\config.json","docs\\README.md"],
        "dirs":["src","docs"],
        "commands":["npm init -y"],
        "contents":["src\\index.js:::const fetch = require(\"node-fetch\");\n(async()=>{\nconsole.log(\"test\")\n})()"]
    },
    "python":{
        "files":["src\\main.py", "src\\config.py"],
        "dirs":["src"]
    },
    "html":{
        "files":["src\\index.html", "src\\style.css", "src\\index.js"],
        "dirs":["src"]
    },
    "git":{
        "commands":["git init", "git remote add origin", "git add -A", "git commit -m 'init' ", "git push -u origin master"]
    }
}