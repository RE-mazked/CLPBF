finalList = []
names = []
namesIn = input("Names: ")
while namesIn != '':
    names.append(namesIn)
    namesIn = input("Names: ")
numbers = []
numbersIn = input("Numbers: ")
while numbersIn != '':
    numbers.append(numbersIn)
    numbersIn = input("Numbers: ")

def variablesWords(word, *nums):
    if nums:
        for num in nums: