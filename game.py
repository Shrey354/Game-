#Mixing color game in python

color1 = input('Enter first color :').lower()
color2 = input('Enter second color :').lower()
color = [color1 , color2]
if (color1 == color2):
    print('You are mixing same color')
elif 'yellow' in color and 'red' in color:
    print(f'Mixing {color1} and {color2} gives orange')
elif 'red' in color and 'blue' in color :
    print(f'Mixing {color1} and {color2} gives purple')
else: 
    print('Invalid color combination. Please use yellow, red and blue')



#Guessing a number in python
import random
min = 1
max = 20
num = random.randint(min,max)

for i in range(5):
    print('-'*100)
    print(f'Attempt {i+1}/5')
    number = input(f'Enter a secret number between {min} and {max}: ')
    number = int(number)
    if (number< min or number>max):
        print('Out of range')
    elif (number == num):
        print('Correct!')
        break
    elif (number > num):
        print('Too high . Try Again')
    else :
        print('Too low. Try Again')


