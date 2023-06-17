import random
from datetime import datetime

#Get Current date and time for reference of when password was generated
now = datetime.now()
dateTimeFormatted = now.strftime('%d/%m/%Y %H:%M')

randomLetter1 = chr(random.randint(ord('A'), ord('Z')))
randomLetter2 = chr(random.randint(ord('a'), ord('z')))
randomLetter3 = chr(random.randint(ord('a'), ord('z')))

randomNumber1 = str(random.randint(0,9))
randomNumber2 = str(random.randint(0,9))


randomLetter4 = chr(random.randint(ord('A'), ord('Z')))

charList = ['!', '@', '#', '$', '%', '^', '&', '*']
listNum = random.randint(0,8)

randomSymbols=''
if (listNum<8):
    randomSymbols += charList[listNum]
    randomSymbols += charList[listNum]

else:
    randomSymbols = '()'

password = randomLetter1+randomLetter2+randomLetter3+randomNumber1+randomNumber2+randomLetter4+randomSymbols
print(password)
print('date and time = ', dateTimeFormatted)
