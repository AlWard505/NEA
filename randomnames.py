import random

from random import *
n = 'test'
x=0
filename ="studentdata.txt"
ftw=open(filename, "a+")
while x != 30:
    n = str(x)
    ftw.write('name      : '+n+"\n"+'age       : '+n+"\n"+'year      : '+n)
    ftw.write("\n"+'password  : '+n+"\n")
    i = randint(1,3)
    if i == 1:
        topic = 'music'
    if i == 2:
        topic = 'history'
    else:
        topic = 'computing'
    i = randint(1,3)
    if i == 1:
        difficulty = 'easy'
    if i == 2:
        difficulty = 'medium'
    else:
        difficulty = 'hard'
    ftw.write('topic     : '+topic+"\n"+'difficulty: '+difficulty+"\n")
    score = randint(0,5)
    if score == 5:
        grade = 'A'
    if score == 4:
        grade = 'B'
    if score == 3:
        grade = 'C'
    if score == 2:
        grade = 'D'
    if score == 1:
        grade = 'E'
    if score == 0:
        grade = 'F'
    score = str(score)
    ftw.write('score     : '+score+'\n'+'grade     : '+grade+'\n')
    x+=1
    
        
