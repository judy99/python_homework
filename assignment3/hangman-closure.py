# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    res = ["_" for _ in secret_word]
    def hangman_closure(letter):
        if not letter or len(letter) != 1:
            return False
        guesses.append(letter)
        for i in range(len(secret_word)):
            if secret_word[i] in guesses:
                res[i] = secret_word[i]
        print("".join(res))
        if (secret_word == "".join(res)):
            return True
        else:
            return False
    return hangman_closure

x = make_hangman("hello")
l = input("Enter your letter: ")

while not x(l):
    l = input("Enter your letter: ")