# import nltk
import colorama
from colorama import Fore, Back, Style
import time
import os
from nltk import tokenize
def typewriter(p):
    if p!="FINAL":
        for i in p:
            # time.sleep(0)
            time.sleep(0.05)
            print(i, end="")
    elif p=="FINAL":
        for i in p:
            time.sleep(0.05)
            # time.sleep(0.05)
            print(Fore.YELLOW + Back.BLACK + i+ Style.RESET_ALL, end="")
 

def clear():
    os.system('cls||echo -e \\\\033c')
    
# nltk.download('punkt')   

colorama.init()
time.sleep(0.5)
p=list()
p="Hello. My name is Ramis Makhmudov. And this is my "
typewriter(p) 
p="FINAL"
typewriter(p)
p=" presentation in a very strange form. I named it GAME. Press Enter to start"
typewriter(p)
input()
while True:
    p="\nYou have three options:\n1. Start a game\n2. Instructions\n3. Finish the game\n\nSo what it is going to be? (Please type a number)\n"
    typewriter(p)
    begin=input()
    if begin == "2":
        with open("Instructions.txt", "r") as file:  
            lines = file.read().splitlines()
            file.close()
            for line in lines:
                for i in line:
                    time.sleep(0.05)
                    # time.sleep(0.05)
                    print(i, end="")
        p="\n\nDid you understand the instructions? Should I return to the main menu? (Yes/No)\n"
        typewriter(p)
        ret=input()
        clear()
        if ret == "Yes":
            p="\nYou have three options:\n1. Start a game\n2. Instructions\n3. Finish the game\n"
            typewriter(p)
            begin=input()
            
    if begin == "1":
            print("Processing", end=" ")
            p="...."
            for i in p:
                time.sleep(1)
                print(i, end=" ")
            clear()
            p="""\nNow you are about to see questions. Type the number and you will see my answer to this question.\n\n
    1.	How have I developed during the course?
    2.	What have I learnt about other students and my teachers?
    3.	How have I been creative?
    4.	How have I engaged with new technologies?
    5.	How the learned material could be useful to me and my future career?\n\n"""
            typewriter(p)
            first = input()
            if first == "1":
                clear()
                p="How I developed during course? Firstly, I improved my speaking skills. Secondly, I discovered new services of using modern technologies for free, that actually gave me some ideas. And thirdly, I have got this interesting adventure to work in groups.\n\n To go back to menu type return\n\nOr if you want to finish the GAME type finish\n"
                typewriter(p)
                q6a=input()
                if q6a == "finish":
                    p="You are about to finish the GAME. Thank you for using this simple program. I know it was boring, but I tried my best. Press Enter to close program"
                    typewriter(p)
                    input()
                    break
                if q6a == "return":
                    clear()
                    p="""\nNow you are about to see questions. Type the number and you will see my answer to this question.\n\n
    1.	How have I developed during the course?
    2.	What have I learnt about other students and my teachers?
    3.	How have I been creative?
    4.	How have I engaged with new technologies?
    5.	How the learned material could be useful to me and my future career?\n\n"""
                    typewriter(p)
                    first = input()
            elif first == "2":
                clear()
                p="What have I learnt about other students and my teachers?\n\nWell, I saw, that my group including me are talk-lovers, all teachers I know are kind, always tried to help, they were involved in the study process.\n\nTo goback to menu type return\n\nOr if you want to finish the GAME type finish\n"
                typewriter(p)
                q6a=input()
                if q6a == "finish":
                    p="You are about to finish the GAME. Thank you for using this simple program. I know it was boring, but I tried my best. Press Enter to close program"
                    typewriter(p)
                    input()
                    break
                if q6a == "return":
                    clear()
                    p="""\nNow you are about to see questions. Type the number and you will see my answer to this question.\n\n
    1.	How have I developed during the course?
    2.	What have I learnt about other students and my teachers?
    3.	How have I been creative?
    4.	How have I engaged with new technologies?
    5.	How the learned material could be useful to me and my future career?\n\n"""
                    typewriter(p)
                    first = input()
            elif first == "3":
                clear()
                p="How have I been creative?\n\nI think that I was creative in many ways. Just take this final presentation, how I made it. Also I use all my imagination to collaborate with other members of our small group to make the video and of course during breaking and then fixing things.\n\nTo goback to menu type return\n\nOr if you want to finish the GAME type finish\n"
                typewriter(p)
                q6a=input()
                if q6a == "finish":
                    p="You are about to finish the GAME. Thank you for using this simple program. I know it was boring, but I tried my best. Press Enter to close program"
                    typewriter(p)
                    input()
                    break
                if q6a == "return":
                    clear()
                    p="""\nNow you are about to see questions. Type the number and you will see my answer to this question.\n\n
    1.	How have I developed during the course?
    2.	What have I learnt about other students and my teachers?
    3.	How have I been creative?
    4.	How have I engaged with new technologies?
    5.	How the learned material could be useful to me and my future career?\n\n"""
                    typewriter(p)
                    first = input()
            elif first == "4":
                clear()
                p="How have I engaged with new technologies?\n\n4.	I created a dozens of images, wrote a poem, some essay. Under myself I mean the process of me giving the AI required information to get it done. Also I`ve used some programming skill, also web-technologies.\n\nTo goback to menu type return\n\nOr if you want to finish the GAME type finish\n"
                typewriter(p)
                q6a=input()
                if q6a == "finish":
                    p="You are about to finish the GAME. Thank you for using this simple program. I know it was boring, but I tried my best. Press Enter to close program"
                    typewriter(p)
                    input()
                    break
                if q6a == "return":
                    clear()
                    p="""\nNow you are about to see questions. Type the number and you will see my answer to this question.\n\n
    1.	How have I developed during the course?
    2.	What have I learnt about other students and my teachers?
    3.	How have I been creative?
    4.	How have I engaged with new technologies?
    5.	How the learned material could be useful to me and my future career?\n\n"""
                    typewriter(p)
                    first = input()
            elif first == "5":
                clear()
                p="How the learned material could be useful to me and my future career?\n\n"
                typewriter(p)
                with open("answer.txt", "r") as file:
                    line2 = file.readline()
                    for line in line2:
                        for i in line:
                            time.sleep(0.05)
                    # time.sleep(0.05)
                            print(i, end="")
                time.sleep(3)
                p="\n\nDo you want some magic(It will transform the text)? Yes/No\n"    
                typewriter(p)
                q5=input()
                if q5 == "Yes":
                    p="You said Yes. Yeah, thats exactly what I wanted. There you go. Here is your maaaagic:\n"
                    typewriter(p)
                    # print("You said {0}. Yeah, thats exactly what I wanted. There you go. Here is your maaaagic:\n".format(q5));
                    a = tokenize.sent_tokenize(line2);
                    c=a;
                    b=list();
                    b.insert(0, a[-1]);
                    a.remove(a[-1]);
                    a.insert(0,b[0]);
                    # print(Fore.RED + a[0]);
                    p="We are taking red-colored sentence from here: \n\n"
                    typewriter(p)
                    print(c[2]+c[1]+Fore.RED + c[0] +Style.RESET_ALL+"\n")
                    time.sleep(4)
                    p="And put it right here at the beginning: \n\n"
                    typewriter(p)
                    print( Fore.RED+ a[0]+" " +Style.RESET_ALL + a[1] + " " + a[2])
                    time.sleep(3)
                    p="\n\nSee the trick? How was it? It made my text more serious and completed."
                    typewriter(p)
                    time.sleep(3)
                    p="\n\nThank you for using my program. Have a nice day! \n\nP.S. To go back to menu type return\n"
                    typewriter(p)
                    # for i in a:
                    #     print(i, end=" ");
                    input()
                if q5 == "No":
                    p="""You said No. Are you sure about that? Because it is really awesome trick. You will be surprised how good this text can be.
                So what do we do? Are we still in the game?\n"""
                    typewriter(p)
                    q5a=input()
                    if q5a == "Yes":
                        p="You said Yes. Yeah, thats exactly what I wanted. There you go. Here is your maaaagic:\n"
                        typewriter(p)
                    # print("You said {0}. Yeah, thats exactly what I wanted. There you go. Here is your maaaagic:\n".format(q5));
                        a = tokenize.sent_tokenize(line2);
                        c=a;
                        b=list();
                        b.insert(0, a[-1]);
                        a.remove(a[-1]);
                        a.insert(0,b[0]);
                        # print(Fore.RED + a[0]);
                        p="We are taking red-colored sentence from here: \n\n"
                        typewriter(p)
                        print(c[2]+c[1]+Fore.RED + c[0] +Style.RESET_ALL+"\n")
                        time.sleep(4)
                        p="And put it right here at the beginning: \n\n"
                        typewriter(p)
                        print( Fore.RED+ a[0]+" " +Style.RESET_ALL + a[1] + " " + a[2])
                        time.sleep(3)
                        p="\n\nSee the trick? How was it? It made my text more serious and completed."
                        typewriter(p)
                        time.sleep(3)
                        p="\n\nThank you for using my program. Have a nice day! \n\nP.S. To go back to menu type return\n"
                        typewriter(p)
                        input()
                    if q5a == "No":
                        p="\nVery sad...in order to finish the game type return and then the exact menu item\n"
                        typewriter(p)
                        input()
    if begin == "3":
        p="You are about to finish the GAME. Thank you for using this simple program. I know it was boring, but I tried my best. To close the program press Enter"
        typewriter(p)
        input()
        break
    # input()
    # print("Hello. My name is Ramis Makhmudov. And this is my "+Fore.YELLOW + Back.BLACK + "FINAL" + Style.RESET_ALL + " presentation in a very strange form. I named it GAME.Press Enter to start")
    # input()
    # print("You have two options:")
    # input()
    # print("1.Start a game")
    # input()