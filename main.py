# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import ttk
import tkinter

poss_list = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
curr_ans = ""




def minus(total, bad):
    global poss_list
    new_list = []
    for each in total:
        if each not in bad:
            new_list.append(each)
    poss_list = list(set(new_list))


def read_list():
    # Use a breakpoint in the code line below to debug your script
    f = open('words.txt', 'r')
    lines = f.readlines()
    f.close()
    for each in lines:
        poss_list.append(each.strip())

def parse_input(color_in, word_in):
    to_remove = []
    if color_in == "GGGGG":
        quit()
    for idx, col in enumerate(color_in):
        if col == "G":
            for word in poss_list:
                if word not in to_remove:
                    if word_in[idx] != word[idx]:
                        to_remove.append(word)
        elif col == "Y":
            for word in poss_list:
                if word not in to_remove:
                    if word_in[idx] not in word:
                        to_remove.append(word)
                    else:
                        if word_in[idx] == word[idx]:
                            to_remove.append(word)
        elif col == "B":
            for word in poss_list:
                if word not in to_remove:
                    if word_in[idx] in word:
                        to_remove.append(word)
        else:
            print("ERROR")
            quit()
        minus(poss_list, to_remove)


def best_answer():
    all_letters = ["", "", "", "", ""]
    for each in poss_list:
        position = 0
        for letter in each:
            all_letters[position] = all_letters[position] + letter
            position += 1
    lett = [{}, {}, {}, {}, {}]
    for position in range(5):
        for each in alphabet:
            lett[position][each] = all_letters[position].count(each)
    scores = {}
    for each in poss_list:
        curr_score = 0
        position = 0
        for letter in each:
            curr_score += lett[position][letter]
            position += 1
        scores[each] = curr_score
    global curr_ans
    curr_ans= max(scores, key=scores.get)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    read_list()
    best_answer()

    def backspace():
        global user
        if len(user) > 0:
            user = user[:len(user) - 1]
        feedback.set("Please input feedback: " + user)

    def add_black():
        global user
        user += "B"
        feedback.set("Please input feedback: " + user)

    def add_yellow():
        global user
        user += "Y"
        feedback.set("Please input feedback: " + user)

    def add_green():
        global user
        user += "G"
        feedback.set("Please input feedback: " + user)


    def submit():
        global user
        if len(user) == 5:
            parse_input(user, curr_ans)
            best_answer()
            ideal.set("Your next best guess is " + curr_ans)
            user = ""
            feedback.set("Please input feedback: " + user)

    user = ""

    feedback = StringVar()
    feedback.set("Please input feedback: ")

    ideal = StringVar()
    ideal.set("Your next best guess is " + curr_ans)


    frm = ttk.Frame(root, padding=10)
    frm.grid()
    tkinter.Label(frm, text=
    "This bot will output the best possible answer. Please reply in a form of \"GGYBB\",").grid(column=0, row=0)
    tkinter.Label(frm, text=
    "a 5 letter string where G = green, Y = yellow, and B = black depending on what the wordle gives you.").grid(
        column=0, row=1)
    tkinter.Label(frm, textvariable=ideal).grid(column=0, row=2)
    tkinter.Label(frm, textvariable=feedback).grid(column=0, row=3)

    tkinter.Button(frm, text="  ", bg='green', command=add_green).grid(column=0, row=4)
    tkinter.Button(frm, text="  ", bg='black', command=add_black).grid(column=1, row=4)
    tkinter.Button(frm, text="  ", bg='yellow', command=add_yellow).grid(column=2, row=4)

    tkinter.Button(frm, text="Backspace", command=backspace).grid(column=0, row=5)
    tkinter.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
    tkinter.Button(frm, text="Submit", command=submit).grid(column=2, row=5)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
