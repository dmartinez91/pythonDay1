# 1)
programming_language = ['java script', 'python', 'C#']

def programmingList(list):
    userInput = input('What is your favorite programming language?')
    if userInput in programming_language:
        print(userInput)
    else:
        print('sorry that is not on the list!') 

programmingList(programming_language) 

# 2)
from random import seed
from random import randint

def randomNumebr(min, max):
  for _ in range(min, max):
	  value = randint(0, 10)
	  print(value)


randomNumebr(9, 10) 

# 3)

def reverseWord():
    text = input('Please enter a word: ')

    wordReversed = (text[:: -1])
    print(wordReversed)

    return

reverseWord()

# 4)

def countDown():
  for number in range (100, -1 , -1):
    if (number %4==0 and number %7==0):
      print('Flamino-Banana!')
    elif(number %7==0):
      print('Flamingo')
    elif(number %4==0):
      print('banana!')
    else:
      print(number)

countDown()

# 5)

firstList = [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]

def numberListGenerator(listNums):
  listLessThan5 = []

  for i in firstList:
    if(firstList[i] < 5):
      listLessThan5.append(i)
      print(listLessThan5)
      
numberListGenerator(firstList)

# 6)

def nameTurns100():
  userName = input('What is your name? ')
  userAge = int(input('Hold old are you? '))
  turnsOnehunder = str((100 - userAge) + 2021)

  print(userName + ' will turn 100 in ' + turnsOnehunder + '.')


nameTurns100()

# 7)

def common_member():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")


common_member()


# 8)

def check(word1, word2):
     
    if(sorted(word1)== sorted(word2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
check('mood', 'doom')


# 9)

def reverseSentence(phrase):
    words = phrase.split(' ') 
  
    reverse_sentence = ' '.join(reversed(words))

    reverseSentenceWords = (reverse_sentence[::-1]) 
  
    return reverseSentenceWords 
  
print(reverseSentence('the man'))


# 10)

def reversePyramid(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(n, 0, -1):
        
        for j in range(0, n-i):
         
            print(end=" ")
        for j in range(0,i):
          print('* ',end='')
        # ending line after each row
        print("\r")

n = int(input('enter how many stars to start: '))
reversePyramid(n)


