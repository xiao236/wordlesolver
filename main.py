# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

poss_list = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

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
    words = ""
    for each in poss_list:
        words = words + each
    lett = {}
    for each in alphabet:
        lett[each] = words.count(each)
    scores = {}
    for each in poss_list:
        curr_score = 0
        for letter in each:
            if each.count(letter) <=1:
                curr_score += lett[letter]
        scores[each] = curr_score
    return max(scores, key=scores.get)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_list()
    print(
        "This bot will output the best possible answer. Please reply in a form of \"GGYBB\", a 5 letter string where G = green, Y = yellow, and B = black depending on what the wordle gives you.")
    user = ""
    while user != "GGGGG":
        curr_ans = best_answer()
        print("best next guess is " + curr_ans)
        user = input()
        user = user.upper()
        if user == "GGGGG":
            quit()
        elif user == "QUIT":
            quit()
        else:
            parse_input(user, curr_ans)

    print("YOU'RE WELCOME")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
