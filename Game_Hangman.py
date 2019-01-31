
# coding: utf-8

# # HANGMAN 2019
# ## game rule
# 8 chances to guess a character in hidden word with a hint :]  
# Find it or Die for it
# 
# ## game score
# - 10 point for correct
# - -5 ponit for wrong

# In[202]:


import pandas as pd
from os import listdir
from os.path import isfile, join
import numpy as np
from datetime import datetime

mypath ='./Categories/'
Categories = [f for f in listdir(mypath) if isfile(join(mypath, f))]
hangman = ["     \n     \n     \n     \n     \n     \n____|\n",
           "_____\n    |\n    |\n    |\n    |\n    |\n____|\n",
           "_____\n    |\n O  |\n    |\n    |\n    |\n____|\n",
           "_____\n    |\n O  |\n Y  |\n X  |\n    |\n____|\n",
           "_____\n    |\n O  |\n/Y  |\n X  |\n    |\n____|\n",
           "_____\n    |\n O  |\n/Y\ |\n X  |\n    |\n____|\n",
           "_____\n    |\n O  |\n/Y\ |\n X  |\n/   |\n____|\n",
           "_____\n    |\n O  |\n/Y\ |\n X  |\n/ \ |\n____|\n",
           "_____\n I  |\n O  |\n/Y\ |\n X  |\n/ \ |\n____|\n"]


# In[203]:


## Name Input
print('Please put Your name: ')
name = input()
print('Hello, ' + name)
status = 'play'


# In[204]:


## Select Category
for i in range(len(Categories)) : print(str(i) + '. ' + Categories[i][:-4]) 
print('Select Category : ')
x = input()
print('Let start with ' + Categories[int(x)][:-4])


# In[205]:


## Random word
data = pd.read_csv(mypath + Categories[int(x)]) 
rand = np.random.randint(len(data))
start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# In[206]:


## Start Game
show = list('_ '*len((data.words[rand])))
remain = len((data.words[rand]))
if ' ' in data.words[rand] :
    index = -1
    for i in range(data.words[rand].count(' ')):
        index = data.words[rand].find(' ', index+1)
        show[index*2] = ' '
        remain -= 1
wrong = []
score = 0

print('Hint: ' + data.hints[rand] + '\nMaximum score:' + str(remain * 10)) #answer
print(hangman[0])
print('>>   ' + ''.join(show) + '\tscore ' + str(score) + ' , remaining wrong guess ' + str(remain))

while(len(wrong) < len(hangman)-1):
    answer = input().lower()
    if answer == 'exit':
        print("\nBye Bye ")
        status = 'exit'
        break
    while (not answer.isalpha()) :
        print("Non-Charater: " + answer)
        answer = input().lower()
    while (answer in show or answer in wrong) :
        print("Repeated Charater: " + answer)
        answer = input().lower()

        
    count = data.words[rand].count(answer)
    if count == 0 :
        wrong.append(answer)
        score -= 5
    else :
        index = -1
        for i in range(count) :
            index = data.words[rand].find(answer, index+1)
            show[index*2] = answer
            remain -= 1
            score += 10
            
    print(hangman[len(wrong)])
    print('>>   ' + ''.join(show) + '\tscore ' + str(score) 
          + ' , remaining wrong guess ' + str(remain) 
          + ' , wrong guessed: ' + ' '.join(wrong))
    
    if remain <= 0 :
        print("\n\nCongraturation!!!\n   Score: " + str(score) +"\n")
        status = 'win'
        break
    elif len(wrong) > len(hangman)-2 :
        print("\n\nGame Over!!!\n  Score: " + str(score) + "\n")
        status = 'lose'
stop = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    


# In[207]:


## Save data
save = {'name' : name,
        'start' : start,
        'category' : Categories[int(x)][:-4],
        'correct' : data.words[rand],
        'done' : str(''.join(show)),
        'wrong' : str(' '.join(wrong)),
        'score' : str(score),
        'status' : status,
        'stop' : stop}

### CSV File
filename = './Logs/Hangman.csv'
df = pd.DataFrame(save, index=[0])

if not isfile(filename):
    df.to_csv(filename, index=False)
else :
    with open(filename, 'a') as f:
        df.to_csv(f, header=False, index=False)

