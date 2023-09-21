def printFirstWord(sentence):
    sentenceList = sentence.split(" ")
    print('The first word is:', sentenceList[0])

printFirstWord(input('Type some text: '))