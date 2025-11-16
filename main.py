
class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename) as file:
            lines = file.readlines()
            for line in lines:
                print(line.rstrip())

filereader = FileReader("flower")
filereader.read_file()