import os
from re import search

for files in os.walk(".\\"):
    if search("git", str(files)):
        continue
    else:
        print(files)