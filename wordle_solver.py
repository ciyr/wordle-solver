import re
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    wordle = []
    for i in english_words:
        if len(i) == 5:
            wordle.append(i)
    while(1):
        final = []
        x = input("Ënter the characters that are in the word(type 'stop' to exit): ")
        if x == "stop":
            break
        char_in = list(x)
        for word in wordle:
            count = 0
            for j in char_in:
                if j in word:
                    count += 1
            if count == len(char_in):
                final.append(word)
        y = input("Ënter the characters that are definitely not in the word: ")
        if y == "":
            final.append("null")
        else:
            char_out = list(y)
            for k in char_out:
                for word1 in wordle:
                    if k in word1:
                        wordle.remove(word1)
                        if word1 in final:
                            final.remove(word1)
        for m in final:
            print(m)
