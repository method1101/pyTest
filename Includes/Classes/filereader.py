class FileReader:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read_file(self) -> None:
        with open(self.filename) as file:
            lines = file.readlines()
            for line in lines:
                print(line.rstrip())
