def separate_word(text):
    return text.replace(',', ' ').split()

def count(text):
    wordlist = separate_word(text)
    repeatedlist = []
    count = []
    for item in wordlist:
        if item not in repeatedlist:
            repeatedlist.append(item)
            count.append(1)
        else:
            count[repeatedlist.index(item)] += 1
    show_score(wordlist, count)

def show_score (wordlist, count):
    for i in range(len(count)):
        print(wordlist[i]+": "+str(count[i]))
        return wordlist[i]+": "+str(count[i])  

# count('ola, bom dia, ola')
# count('oi raphael, tudo bem? sou raphael tambem')

