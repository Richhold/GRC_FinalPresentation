import colorama
from nltk import tokenize
from colorama import Fore, Back, Style
import os
def clear():
    os.system('cls||echo -e \\\\033c')
colorama.init()
# print(Fore.RED + 'Красный текст')
# print(Back.BLUE + 'Синий фон')
# print(Style.RESET_ALL)
# print('Снова обычный текст')
# input()
with open("answer.txt", "r") as file:
    line = file.readline()
print(line);
# # a = tokenize.sent_tokenize(line);
# # b=list();
# # b.insert(0, a[-1]);
# # a.remove(a[-1]);
# # a.insert(0,b[0]);
# print("\n");
# for i in a:
#     print(i, end=" ");

q5=input("Do you want some magic(It will transform the text)? Yes/No\n")
# 1. Yes
# 2. No
# """)
if q5 == "Yes":
    print("You said {0}. Yeah, thats exactly what I wanted. There you go. Here is your maaaagic:\n".format(q5));
    a = tokenize.sent_tokenize(line);
    c=a;
    b=list();
    b.insert(0, a[-1]);
    a.remove(a[-1]);
    a.insert(0,b[0]);
    # print(Fore.RED + a[0]);
    print("We are taking red-colored sentence from here: \n\n", c[2]+c[1]+Fore.RED + c[0] +Style.RESET_ALL+"\n")
    print("And put it right here at the beginning: \n\n", Fore.RED+ a[0]+" " +Style.RESET_ALL + a[1] + " " + a[2] + "\n\nSee the trick? How was it? It made my text more serious and completed.\n\n Thank you for using my program. Have a nice day! \n\n P.S. Press Enter on keyboard to finish the game.")
    # for i in a:
    #     print(i, end=" ");
if q5 == "No":
    q5a=input("""You said {0}. Are you sure about that? Because it is really awesome trick. You will be surprised how good this text can be.
So what do we do? Are we still in the game?\n""".format(q5));
    if q5a == "Yes":
        clear()
        print("You said {0}. Yeah, thats exactly what I wanted. There you go. Here is your maaaagic:\n".format(q5a));
        a = tokenize.sent_tokenize(line);
        b=list();
        b.insert(0, a[-1]);
        a.remove(a[-1]);
        a.insert(0,b[0]);

        print("We are taking red-colored sentence from here: \n\n", a[2]+a[1]+Fore.RED + a[0] +Style.RESET_ALL)
        print("And put it right here in the beginning: \n\n", Fore.RED+ a[0]+" " +Style.RESET_ALL + a[1] + " " + a[2] + "\n\nSee the trick? How was it? It made my text more serious and completed.\n\n Thank you for using my program. Have a nice day! \n\n P.S. Press Enter on keyboard to finish the game.")
    if q5a == "No":
        print("\nVery sad...But still, thank you for using my programm. Have a good day!")
input()
    