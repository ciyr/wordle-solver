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
    final = wordle.copy()
    while(1):
        x = input("Enter the characters that are in the word(type 'stop' to exit): ")
        if x == "stop":
            break
        char_in = list(x)
        for word in wordle:
            count = 0
            for j in char_in:
                if j in word:
                    count += 1
            if count == len(char_in):
                continue
            else:
                try:
                    final.remove(word)
                except:
                    continue
        y = input("Enter the characters that are definitely not in the word: ")
        if y == "":
            final.append("null")
        else:
            char_out = list(y)
            print(char_out)
            for k in char_out:
                for i in range (0,len(wordle)):
                    if k in wordle[i]:
                        if wordle[i] in final:
                            final.remove(wordle[i])
                        wordle[i] = "12345"
        z = input("Positions of letters: ")
        li = "\n".join(final)
        xlist = re.findall(z,li)
        for m in xlist:
            print(m)
