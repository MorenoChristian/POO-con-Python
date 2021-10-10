class Programmer:
    # Declare the class constructor
    def __init__(self, name, last_name, skill):
        self.name = name
        self.last_name = last_name
        self.skill = skill

    # Define Class Methods

    def Program(self):
        print("Hi!! i´m {} {} and i´m working in {}".format(self.name, self.last_name, self.skill))


#Create classes that inherate from Programmer class

class Python_developer(Programmer):
    def __init__(self, name, last_name, skill = 'Python'):
        super().__init__(name, last_name, skill)



class Java_developer(Programmer):
    def __init__(self, name, last_name, skill = 'Java'):
        super().__init__(name, last_name, skill)
    

python1 = Python_developer('Christian', 'Moreno')
java1 = Java_developer("Juan", "Carlo")
python1.Program()
java1.Program()
    