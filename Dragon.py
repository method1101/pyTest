class Dragon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def roar(self):
        print(f"{self.name} roars.")

    def hunt(self):
        print(f"{self.name} hunts.")

    def duration(self):
        print(f"{self.name} is: {str(self.age)} years old.")