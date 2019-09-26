import os

class CopyFolderTree:
    def __init__(self, srcPath, outPath):
        self.srcPath = srcPath
        self.outPath = outPath

    def resolve(self):
        assert os.path.exists(self.srcPath), "source path does not exists"

    def makeTree(self):
        self.resolve()
        for filePath, folders, files in os.walk(self.srcPath):
            destPath = filePath.replace(self.srcPath, self.outPath)
            if not os.path.exists(destPath):
                os.makedirs(destPath)
                for file in files:
                    open("\\".join([destPath, file]), "w")
            else:
                for file in files:
                    open("\\".join([destPath, file]), "w")
        print("Folders/Files Created!")

    def testTree(self):
        for filePath, folders, files in os.walk(self.srcPath):
            compairPath = filePath.replace(self.outPath, self.srcPath)
            assert os.path.exists(compairPath), "{} does not exist".format(compairPath)
            for file in files:
                checkFilePath = "\\".join([compairPath, file])
                assert os.path.isfile(checkFilePath), "{} does not exist".format(checkFilePath)
        print("Folder StructureTest OK!")

ctp = CopyFolderTree("Z:\\", "C:\\NASTree\\")
ctp.makeTree()
ctp.testTree()