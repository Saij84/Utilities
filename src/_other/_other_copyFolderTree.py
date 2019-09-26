import os

srcPath = "D:\\Backup\\"
outPath = "C:\\test\\"

def resolve():
    assert os.path.exists(srcPath), "source path does not exsits"
    if not os.path.exists(outPath):
        os.makedirs(outPath)

resolve()

def makeTree(path):
    for filePath, folders, files in os.walk(path):
        destPath = filePath.replace(path, outPath)
        if not os.path.exists(destPath):
            os.makedirs(destPath)
            for file in files:
                print("---->", "\\".join([destPath, file]), "w")
                open("\\".join([destPath, file]), "w")

def testTree(srcPath, trgPath):
    os.walk(sr)