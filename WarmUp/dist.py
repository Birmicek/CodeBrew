import math

a_x = int(input("Enter X coordinate for point A: "))
a_y = int(input("Enter Y coordinate for point A: "))
b_x = int(input("Enter X coordinate for point B: "))
b_y = int(input("Enter Y coordinate for point B: "))

def calc_distance():
    distance = math.sqrt((a_x - b_x)**2 + (a_y - b_y)**2)
    print('The distance between the points A and B is:', round(distance, 2) )

calc_distance()