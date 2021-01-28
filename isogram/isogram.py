def is_isogram(word):
    wordlist = []
    wordlist[:0] = word
    aux = []
    for word in wordlist:
        if word in aux:
            return False
        if word not in (' ', '-'):
            aux.append(word)
    return True
