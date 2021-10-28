height = float(input('Enter the height from which the ball is dropped: '))
bounci_index = float(input('Enter the bounciness index of the ball: '))
bounces = int(input('Enter the number of times the ball is allowed to continue bouncing: '))

distance = height

for i in range(bounces-1):
    height *= bounci_index
    distance += 2*height

distance += height*bounci_index

print('\nTotal distance traveled is: ' + str(distance) + ' units.')