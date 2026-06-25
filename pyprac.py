#conditional statements (chapter 3)
# nested decision 
x = 42
if x > 1 :
    print('more than one')
    if x < 100 :
        print('less than 100')
print('all done')

# else if statement and elif statement
x = 0
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else :
    print('large')
print('all done')

#try and except statement: insurance policy for your code
astr = 'Hello Bob'
try: 
    istr = int(astr)
except: 
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except: 
    istr = -1

print('Second', istr)

#try/except and input statement
rawstr = input('Enter a number: ')
try: 
    ival = int(rawstr)
except: 
    ival = -1
if ival > 0 :
    print('Nice work')
else: 
    print('Not a number')
    
# input and if/else problem
hours = input('Enter Hours: ')
h = float(hours)
rate = input('Enter Rate: ')
r = float(rate)

if h <= 40 :
    pay = h * r
else :
    pay = (40 * r) + ((h - 40) * (r * 1.5))
print('Pay:', pay)

#def keyword: remembers the function and its name
def thing():
    print('Hello')

print('Fun')

#loops (keyword: while, for)
n = 5
while n > 0:
    print(n)
    n = n + 1
print('Blastoff!')
print(n)

#if nothing changes in a loop, it will run forever. This is called an infinite loop.

#break statement: stops the loop when a certain condition is met
while True:
    line = input('ask to stop or loop runs infinitely: ')
    if line == 'stop' :
        break
    print(line)
print('Done!')

#continue statement: skips the rest of the code in the loop and goes back to the top of the loop
while True:
    line = input('ask to stop or loop runs infinitely: ')
    if line[0] == '#' :
        continue
    if line == 'stop' :
        break
    print(line)
print('Done!')

#simple definite loop: for loop
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

subjects = ['Statistics', 'Economics', 'Python']
for subject in subjects :
    print('Studying:', subject)
print('Done!')

#finding the largest value in a loop
l = -1
print('Before:', l)
for number in [14, 5, 43, 90, 10, 12] :
    if number > l :
        l = number
        print(l, number)
print('After:', l)

#summing values in a loop
zork = 0
for numbers in [3, 41, 12, 9, 74, 15] :
    zork = zork + numbers
    print(zork, numbers)
print('Sum:', zork)

#average values in a loop
count = 0
sum = 0
for numbers in [3, 41, 12, 9, 74, 15] :
    count = count + 1
    sum = sum + numbers
    print(count, sum/count)

print('count:', count, 'avg:', sum/count)

# boolean values only include True and False. They are case sensitive.
x = False
for values in [58, 41, 12, 3, 74, 15] :
    if values == 3 :
        x = True
    print(x, values)

# None is a special value in Python that represents the absence of a value or a null value. 
# It is often used to indicate that a variable has not been assigned a value yet or that a function does not return anything.
# using None to find the smallest value in a loop
smallest = None
for numbers in [41, 9, 15, 3, 74, 12] :
    if smallest is None :
        smallest = numbers
    elif numbers < smallest :
        smallest = numbers
    print(smallest, numbers)
print(smallest, numbers)

#assignment
largest = None
smallest = None

while True:
    num = input("Enter value: ")
    
    if num == "done":
        break
    try :
        inum = int(num)

        if largest is None:
            largest = inum
        elif fnum > largest:
            largest = inum

        if smallest is None:
            smallest = inum
        elif inum < smallest:
            smallest = inum

    except: 
        print("Invalid input")
        continue

    print(largest, smallest)