#imnport lib
import re
class getInfo:
    def __init__(self):
        #Key words to work with
        names = []
        namesIn = input("Names: ")
        #While input names isn't empty will ask
        while namesIn != '':
            names.append(namesIn)
            namesIn = input("Names: ")
        #Key numbers to work with
        numbers = []
        numbersIn = input("Numbers: ")
        #While input numbers isn't empty will ask
        while numbersIn != '':
            numbers.append(numbersIn)
            numbersIn = input("Numbers: ")
        #Get direction to save the txt
        urltxt = input("Where you wanna save the txt file with the passwords [C:\\pass.txt]: ")
        fileE = True
        while fileE:
            try:
                open(f"{urltxt}", "x")
                fileE = False
            except FileExistsError:
                print("This file alredy exist.")
                fileE = True
        makeList(names, numbers, urltxt)
#Create a class that randomize and create the dictionari out a txt
class makeList:
    ## INIT ##
    def __init__(self, namess, numberss, urltxt):
        #List with final passwords
        self.finalList = []
        #Set global vars
        self.namess = namess
        self.numberss = numberss
        #Use functions and create the txt
        for name1 in namess:
            for name2 in namess:
                self.mixWords(name1, name2)
        for num in numberss:
            for name in namess:
                self.variablesFinalList(name, num)
        with open(f"{urltxt}", "a") as f:
            for x in self.finalList:
                f.write(x + "\n")
    ## FUNCTIONS ##
    #Function to convert words in all possibilities and mix with the numbers
    def variablesFinalList(self, word, num):
        self.finalList.append(word.capitalize())
        self.finalList.append(word.lower())
        self.finalList.append(word.upper())
        self.finalList.append(word.capitalize() + num)
        self.finalList.append(word.lower() + num)
        self.finalList.append(word.upper() + num)
        self.finalList.append(num + word.capitalize())
        self.finalList.append(num + word.lower())
        self.finalList.append(num + word.upper())
    #Collect words
    def joinWords(self, word1, word2):
        self.finalList.append(str(word1) + str(word2))
    #Comprobate if is some caracter with findall re method
    def findWord(self, dic, text):
        x = re.findall(f"[{dic}]", text)
        if x:
            return True
        else:
            return False
    #Put together from the vocals they share
    def mixWords(self, word1, word2):
        l_word1 = list(word1.lower())
        l_word2 = list(word2.lower())
        for index1, letter1 in enumerate(l_word1):
            for index2, letter2 in enumerate(l_word2):
                part1 = ''
                part2 = ''
                if letter1 == letter2 and self.findWord('aeiou', letter1) and self.findWord('aeiou', letter2):
                    part1 = ''.join(l_word1[:index1])
                    part2 = ''.join(l_word2[index2:])
                    self.joinWords(str(part1), str(part2))
        
if __name__ == '__main__':
    getInfo()