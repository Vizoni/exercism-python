def getAcronym(phrase):
    listOfWords = phrase.split()
    acronym = ''
    for word in listOfWords:
        acronym += word[0]
    return acronym.upper()

print(getAcronym(input()))