#NEA
#feguses needs to enter 'Fergus for name then '37' for age which will grant him the ability to check scores
grade = ' '
choice = ' '
z = 0
n = 0
name =' '
age =' '
year =' '
password =' '
passwordcheck ='  '
topic = ' '
difficulty = ' '
check = '1 '
score = 0
size = 10*10*6
filename="studentdata.txt"
q = ['a','a','a','a','a']#array for storing the questions
a = [#2d array for storing possible answers
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    ]
ca = ['1','2','2','1','2']#stores the correct answers for the easy questions
ma = ['2','1','2','1','2']#stores the correct answers for the medium questions
ha = ['2','1','1','2','1']#stores the correct answers for the hard questions
name= input('enter name for registration: ')
while age.isnumeric() == False:#if someone enters a answer thats not a number it will make you refill this section
    age = input('enter age for registration: ')
if (name == 'Fergus')and (age == '37'):#checks to see if it's the teacher logging in
    tchoice = input('''hello fergus would you like to see all infomation or just scores and grades
for grades enter "g" for all infomation enter "a": ''')
    if tchoice == 'a':
        ftw=open(filename, "r")#opens the document with the scores in read mode
        
        while check != '':#when check has no data the loop will replay until there is no data left to read
            while z!=8:

                check = ftw.readline(size)#recalls the information of one student at a time 
                print(check) #prtints this information
                
                z+=1
            input('press enter to see next piece of information')
            z = 0
    input('press enter to end')
    quit()#closes the program
while year.isnumeric() == False:#if someone enters a answer thats not a number it will make you refill this section
    year = input('enter school year for registration: ')
ch = input('are you happy with these deatails? y/n : ')#allows the user to see if they made a mistake while filling out the questions

        
while ch!= 'y' and ch != 'yes' and ch!= 'Y' and ch != 'Yes':#multiple options to prevent the user from having to redo eerything uncecercarily 
    age = ' '
    year = ' '
    name= input('enter name for registration: ')
    while age.isnumeric() == False:
        age = input('enter age for registration: ')
    while year.isnumeric() == False:
        year = input('enter school year for registration: ')
    ch = input('are you happy with these deatails?:  y/n \n')
filename="studentdata.txt"
ftw=open(filename, "a")#opens the file in append mode

while password != passwordcheck:
    password = input('choose password: ')#lets the user choose their password
    passwordcheck = input('re-enter to confirm: ')#makes sure they entered it correctly

input('would you like to do questions y/n: ') 
while (topic!='music')and(topic!='history')and(topic!='computing'):
    topic = input('please chose a topic from; music, history or computing: ')#tells the user their options
while (difficulty!='easy')and(difficulty!='medium')and(difficulty!='hard'):
    difficulty = input('please chose a difficulty from; easy, medium or hard: ')#lets the player choose difficulty

ft=open(topic + '.txt', "r")#opens the selected set of questions
size = 10*10*3

q[0] = ft.readline(size)#copies the quesions into the questions array
q[1] = ft.readline(size)
q[2] = ft.readline(size)
q[3] = ft.readline(size)
q[4] = ft.readline(size)
aw = open(topic+difficulty+'.txt', 'r')#opens the answer filee
n = 0
if difficulty == 'easy':
    while n != 5:
        a[n][0]= aw.readline(size)
        a[n][1]= aw.readline(size)#copies the answers into the answers array
        n += 1
if difficulty == 'medium':
    while n != 5:
        a[n][0]= aw.readline(size)#copies the answers into the answers array
        a[n][1]= aw.readline(size)
        a[n][2]= aw.readline(size)
        n += 1
if difficulty == 'hard':
    while n != 5:
        a[n][0]= aw.readline(size)#copies the answers into the answers array
        a[n][1]= aw.readline(size)
        a[n][2]= aw.readline(size)
        a[n][3]= aw.readline(size)
        n += 1
    
#asking questions

n = 0
while n != 5:
    print('\n',q[n])#displays the question
    print('is it \n',a[n][0],a[n][1],a[n][2],a[n][3])#displays the possible answers
    if difficulty == 'easy':
        choice = input('please enter 1 or 2: ')
    elif difficulty == 'medium':
        choice = input('please enter 1, 2 or 3: ')
    elif difficulty == 'hard':
        choice = input('please enter 1, 2, 3 or 4: ')
    if topic == 'music':
        if choice == ma[n]:#checks if the user got it right
            score += 1
    if topic == 'history':
        if choice == ha[n]:#checks if the user got it right
            score += 1
    if topic == 'computing':
        if choice == ca[n]:#checks if the user got it right
            score += 1
            
    n+=1
ftw.write('name      : '+name+"\n"+'age       : '+age+"\n"+'year      : '+year)
ftw.write("\n"+'password  : '+password+"\n")
ftw.write('topic     : '+topic+"\n"+'difficulty: '+difficulty+"\n")#writes all their information into the student data file

score = str(score)
ftw.write('score     : '+score+'\n')
if score == '5':
    grade = 'A'
if score == '4':
    grade = 'B'
if score == '3':
    grade = 'C'#calculates their grade
if score == '2':
    grade = 'D'
if score == '1':
    grade = 'E'
if score == '0':
    grade = 'F'
ftw.write('grade     : '+grade+'\n')#writes their grade into the student data file
print(grade)
ftw.close()#closes opened files
ft.close()
aw.close()
