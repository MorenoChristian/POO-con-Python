
def run():
    class Coordinate:
        
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance(self, another_coordinate):
            x_diff = (self.x - another_coordinate.x)**2
            y_diff = (self.y - another_coordinate.y)**2

            return (x_diff + y_diff)**0.5 #with this we can get the square root of those coordinates
            
    coord_1 = Coordinate(3, 30)
    coord_2 = Coordinate(4, 8)

    print(round(coord_1.distance(coord_2), 2))    
    print(isinstance(coord_2, Coordinate))  #with 'isinstance' we can check if object is istance of that class  


if __name__ == '__main__':
    run()
    