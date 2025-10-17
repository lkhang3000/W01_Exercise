out = open("output.txt", 'w')

out.write("I'm a student\n")

result = round(1 / 7, 5)
out.write(f"Result = {result}\n")

def add(a, b):
    return a + b

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

out.write(f"Sum of {a} and {b} is {add(a, b)}\n")

try:
    inputFile = input('Enter file name: ')
    f = open(inputFile,'r')
    content=f.read()
    out.write(content)
except FileNotFoundError:
    out.write("Cannot find the file")


out.close()
