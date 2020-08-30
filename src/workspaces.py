workspaces = {
    "node":{
        "files":["src\\index.js","src\\config.json"],
        "dirs":["src"],
        "commands":["npm init -y"],
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
    },
    "xnacly":{
        "files":["index.js", "config.json"],
        "contents":[
            "index.js:::const config = require(\"./config\");\nconst fetch = require(\"node-fetch\");\n(async() => {\nconsole.log(\"test\")\n})()",
            "config.json:::{\"token\":\"tokentoken\",\n\"prefix\":\"$\"}"
            ]
    }

}