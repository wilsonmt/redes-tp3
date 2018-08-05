
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.files = []

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getFiles(self):
        return self.files

    def getFileNames(self):
        fileNames = ""
        for file in self.files:
            fileNames += " " + str(file[0])
        return fileNames

    def addFile(self, name, content):
        self.files.append([name, content])
