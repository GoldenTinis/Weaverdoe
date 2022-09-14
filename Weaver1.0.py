from random import randint

with open("4_words.txt") as f:
    words = f.read().splitlines()
with open("4Dictionary.txt") as f:
    dictionary = f.read().splitlines()

def two_random_words():
    word1 = words[randint(0, len(words))]
    word2 = words[randint(0, len(words))]
    while word2 == word1:
        word2 = words[randint(0, len(words))]
    return [word1, word2]


def check_win(current_word, win_word):
    return current_word == win_word


def print_board(game_words, history):
    print(game_words[0] + " ---> " + game_words[1])
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
    ans = "y"
    while ans == "y" or ans == "yes":
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


run_weaver()