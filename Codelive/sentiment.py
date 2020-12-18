score = {}
freq = {}
find = {}

def main():
    start()


def read():
    while True:
        file = input('Learning data file name? ')
        try:
            f = open(file, 'r')

        except FileNotFoundError:
            continue
        break

    for i in f:
        i = i.casefold().split(' ')
        for j in i:
            if j in score and j in freq:
                score[j] += int(i[0])
                freq[j] += 1
            elif j not in score and j.isalpha() and j not in freq:
                score[j] = int(i[0])
                freq[j] = 1
                find[j] = 0




def func1(i):
    scr = round((score[i] / freq[i]), 2)
    return scr


def func2():
    key = list(score.keys())
    sm = 0
    fr = 0
    for k in key:
        sm += score[k]
        fr += freq[k]
    scr = round((sm / fr), 2)
    return scr

def func3():
    key = list(score.keys())
    for k in key:
        t = round((score[k] / freq[k]), 2)
        find[k] = t

    dict(sorted(find.items(), key=lambda item: item[1]))
    print('Maximum score is', find[list(find.keys())[0]])



def start():
    check = 0

    read()
    while check != 5:
        choose = int(input('What would you like to do?' + '\n'
                           + '1: Get the score of a word' + '\n'
                           + '2: Get the average score of words in a file' + '\n'
                           + '3: Find the highest / lowest scoring words in a file' + '\n'
                           + '4: Sort the words in a file into positive.txt and negative.txt' + '\n'
                           + '5: Exit the program' + '\n'
                           + 'Enter a number 1 - 5: '))

        if choose == 1:
            inpt_1 = str(input('which word? '))
            s = func1(inpt_1)
            print('score =', s)
            if s > 2.01:
                print(inpt_1, 'is', 'positive')
            elif s < 1.99:
                print(inpt_1, 'is', 'negative')
            else:
                print(inpt_1, 'is', 'neutral')
            print()

        if choose == 2:
            s = func2()
            print('score =', s)
            check = input('Am I right [yes/no]')
            if check == 'yes':
                continue
            else:
                tmp = int(input('Re enter'))
                s = tmp
            print()

        if choose == 3:
            func3()



main()
