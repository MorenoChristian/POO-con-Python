class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = "parked"
        self._motor = Motor(cylinders=4)

    def speed_up(self, type="slow"):
        if type == 'fast':
            self._motor.inject_petrol(10)
            self._motor._temperature = 50
            print("The car is moving fast")
        else:
            self._motor.inject_petrol(3)
            self._motor._temperature = 20
            print("The car is moving slow")

        self._status = 'moving'

class Motor:
    def __init__(self, cylinders, type="petrol"):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_petrol(self, amount):
        pass
    
car1 = Car(2017, 'Lamborgini', 'black')
print(car1._status)
print(isinstance(car1._motor, Motor))
car1.speed_up("slow")
print("the car is {}".format(car1._status))
