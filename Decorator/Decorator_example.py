def primary_funct(aux_funct):

    def initial_funct():
        print("¡Let´s do some calculations!")
    
        print(aux_funct(num1, num2))

        print("We are finish. ¡Congrats!")

    return initial_funct()


num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

@primary_funct
def plus(num1,num2):
    return (num1 + num2)

def subtraction(num1,num2):
    print(f"{num1} - {num2} = {num1-num2}")

primary_funct(subtraction)




