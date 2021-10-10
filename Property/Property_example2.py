class Person:
    def __init__(self, first_name, last_name, pasaport) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._pasaport = None

    @property
    def first_name(self):
        print("We´re calling Getter Method")
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        print("We´re calling Setter Method")
        if value.capitalize() != "Christian":
            raise ValueError(f"Can´t recive {value} as a name")
        else:
            self._first_name = value.capitalize()
            print(f"Name was changed for {value.capitalize()}")
        
        

person1 = Person('Robert', 'Giancarlo', 1234)

print(person1.first_name)

person1.first_name = "christian"

print(person1.first_name)