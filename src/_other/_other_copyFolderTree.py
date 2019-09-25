import os

srcPath = "D:\Backup"
outPath = "C:\Test"

def resolve():
    assert os.path.exists(srcPath), "source path does not exsits"

    if not os.path.exists(outPath):
        os.makedirs(outPath)

resolve()
for path, folders, files in os.walk(srcPath):
    destPath = path.replace(srcPath, outPath)
    for folder in folders:
        subPath = "\\".join([destPath, folder])
        if not os.path.exists(subPath):
            os.makedirs(subPath)

        if files:
            for file in files:
                open("\\".join([subPath, file]), "w")

