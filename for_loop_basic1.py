#1 Basic
for num in range(0, 151):
    print(num)

#2 multiples of five
for num in range(5, 1000, 5):
    print(num)

# counting the dojo way
for num in range (0, 101):
    if num % 5 == 0:
        print("Coding Dojo")
    else:
        print(num)

#4 whoa that sucker's huge
for num in range (0, 500000):
    if num % 2 != 0:
        print(num)

#5 countdown by fours
for num in range (2018, 0, -4):
    print(num)

#6 Flexible counter
lowNum = 10
highNum = 100
mult = 3
for num in range(lowNum, highNum, mult):
    print(num)