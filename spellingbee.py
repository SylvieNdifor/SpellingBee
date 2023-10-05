from tkinter import *
from tkinter import messagebox
import random

a = 0
d = 60
def timer():
    global d, a
    if d > 0:
        d-=1
        count_text.config(text=d)
        count_text.after(1000, timer)

    else:
        enter_here.config(state=DISABLED)
        result = right_spelling-wrong_spelling
        instruction_text.config(text=f'Correct words: {right_spelling}\n Wrong words: {wrong_spelling}\n Final score: {result}')
        if result < 10:
            reaction_emoji.config(image=emoji1_image)
            reaction3_emoji.config(image=emoji1_image)


        if result>15:
            reaction_emoji.config(image= emoji2_image)
            reaction3_emoji.config(image= emoji2_image)


        if result>20:
            reaction3_emoji.config(image=emoji3_image)
            reaction3_emoji.config(image=emoji3_image)


        res= messagebox.askyesno('Confirm','Do you want to play again?')
        if res:
            a = 0
            d = 60
            count2_text.config(text='0')
            count_text.config(text='60')
            enter_here.config(state=NORMAL)
            instruction_text.config(text='Type word and hit enter')
            reaction_emoji.place_forget()
            reaction3_emoji.place_forget()


right_spelling=0
wrong_spelling=0

b=0
def start_game(any):
    if enter_here.get()!='':
        global a,right_spelling,wrong_spelling
        a+=1
        count2_text.config(text=a)

        instruction_text.config(text='')
        if d==60:
            timer()
        if enter_here.get()==list1_of_words['text']:
            right_spelling+=1
        else:
            wrong_spelling+=1
        random.shuffle(list_of_words)
        list1_of_words.config(text=list_of_words[0])
        enter_here.delete(0,END)


list_of_words= ['accept','according','catch','century','brother','business','degree','Democrat','education','environmental','federal','financial',
'generation','generation','happy','husband','important','international','knowledge','leader','management','measure','newspaper','nothing','operation','particularly','performance','radio','reason','season','shoulder','teacher','throughout','understand','usually','violence','whatever','Abjure','Future','Picnic','Agonistic',	'Garland'	,'Protect','Airline',	'Gigantic',	'Publish',
'Blackboard',	'Himself',	'Reporter',
'Board',	'Indulge',	'Ring',
'Bookworm',	'Inflatable',	'Salesclerk',
'Butterscotch',	'Inimical',	'Snapshot',
'Camera',	'Interim',	'Shellfish',
'Campus',	'Invest',	'Ship',
'Catfish',	'Jackpot',	'Significance',
'Carsick',	'Kitchenette',	'Sometimes']


window = Tk()

window.title("SPELLINGBEE")
window.geometry('880x750')
window.resizable(0,0)

window.configure( bg= 'orange')
logo_image = PhotoImage(file='time-management.png')
logo = Label(window,image=logo_image)
logo.place(x=270,y=90)
logo.config(bg='orange')
welcome_text  =Label(window,text='Welcome To Spelling Bee', bg= 'orange',fg='black', font=("cambria",45,'bold'))
welcome_text.place(x=140,y=2)

word_text = Label(window,text="WORDS", bg='orange', fg='black', font=('',39,"bold"))
word_text.place(x=50,y=120)

time_text = Label(window,text="TIMER", bg='orange', fg='black' , font=('',40,'bold'))
time_text.place(x=700,y=120)

count_text = Label(window,text='60', bg='orange', fg='black' , font=('',40,'bold'))
count_text.place(x=720,y=200)

count2_text = Label(window,text="0", bg='orange', fg='black' , font=('',40,'bold'))
count2_text.place(x=90,y=200)

enter_here = Entry(window, bd=5,width=55)
enter_here.place(x=190,y=490)
enter_here.focus_set()


instruction_text = Label(window,text='Type word and hit enter', bg='orange', fg='black' , font=('',30,'bold'))
instruction_text.place(x=240,y=545)



random.shuffle(list_of_words)
list1_of_words= Label(window,text=list_of_words[0],bg='orange',font=('',45,'bold'))
list1_of_words.place(x=330,y=410)


emoji1_image= PhotoImage(file='sad.png')
emoji2_image= PhotoImage(file='happiness.png')
emoji3_image= PhotoImage(file='star.png')

reaction_emoji =Label(window,image='',bg='orange')
reaction_emoji.place(x=15,y=650)


reaction3_emoji =Label(window,image= '',bg='orange')
reaction3_emoji.place(x=755,y=650)

window.bind('<Return>',start_game)


window.mainloop()