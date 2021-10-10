class Computer:
    def __init__(self, mother, cpu, ram, power_suply, gpu):
        self.status = None
        self.mother = mother
        self.cpu = cpu
        self.ram = ram
        self.power_supply = power_suply
        self.gpu = gpu

    def turn_on(self):
        self.status = "Turned on"
        print("CPU {} is running".format(self.cpu))

    def shut_down(self):
        self.status = "Turned off"
        print("Mother {} is not running".format(self.mother))

    def run_game(self, game):
        self.gpu_temperature = "45C°"
        print(f"Pc is running '{game}' game")

    def close_game(self):
        self.gpu_temperature = "0C°"
        print("Pc close game")

    def get_gpu_temp(self):
        print(f"The temperature of gpu is {format(self.gpu_temperature)}")



pc = Computer("Gigabyte", "Intel Pentium", "8gb", 500, "1060 Strix")

pc.turn_on()
print("PC is {}".format(pc.status))
pc.run_game("The Witcher 3: Wild Hunt")
pc.get_gpu_temp()
pc.close_game()
pc.get_gpu_temp()