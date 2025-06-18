#A python program that checks whether a number is even or not
#A python program that checks whether a letter is a vowel or consonant
#A python program that returns the perimeter of a rectangle

#Program 1

number=int(input("Enter a number:"))

if number ==0:
    print(number,"is a neutral  number")

elif number % 2==0:
    print(number,"is an even number5")

else:
    print(number,"is an odd number")

print()

#Program 2

letter=input("Enter a letter:")

if letter or ['a','e','i','o','u']:
    print(letter,"is a vowel")

else:
    print(letter,"is a consonant")

print()


#Program 3

length=int(input("Enter the length of the rectangle:"))
width=int(input("Enter the width of the rectangle:"))

perimeter=2*(length+width)
print()
print("The perimeter of the rectangle is",perimeter)


