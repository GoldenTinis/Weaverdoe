import random
f = open("4_words.txt", "rt")
words = f.read().splitlines()
f.close()
f = open("4Dictionary.txt", "rt")
dictionary = f.read().splitlines()
f.close()


def two_random_words():
    num1 = random.randint(0, len(words))
    num2 = random.randint(0, len(words))
    while num2 == num1:
        num2 = random.randint(0, len(words))
    word1 = words[num1]
    word2 = words[num2]
    return [word1, word2]


def check_win(current_word, win_word):
    if current_word == win_word:
        return True


def print_board(word01, history):
    print(word01[0] + " ---> " + word01[1])
    if history != []:
        print("\n".join(history))


def anticheat(current, history):
    if current not in dictionary:
        return True
    for i in range(len(current)):
        if current[i] != history[-1][i]:
            if current[i-3] != history[-1][i-3]:
                return True
            elif current[i-2] != history[-1][i-2]:
                return True
            elif current[i-1] != history[-1][i-1]:
                return True
    return False


def backspace(current, history, times):
    while times != 0:
        history.pop()
        current = history[-1]
        times -= 1
    return current, history


def run_weaver():
    while True:
        current = ""
        twowords = two_random_words()
        history = [twowords[0][:]]
        print_board(twowords, history)
        while True:
            current = input()
            if len(current) == 5 and current[0:4] == "back" and current[-1].isnumeric() and int(current[-1]) < len(history):
                current, history = backspace(current, history, int(current[-1]))
                print_board(twowords, history)
                continue
            if current == "restart":
                current, history = backspace(current, history, len(history) - 1)
                print_board(twowords, history)
                continue
            if current == "end":
                break
            if anticheat(current, history):
                print("Word not allowed.")
                current = history[-1]
                continue
            if current == twowords[1]:
                break
            history.append(current)
        ans = input("Play again? (y/n): ").lower()
        if ans == "y" or ans == "yes":
            continue
        else:
            break


run_weaver()