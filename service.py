import re

def checkSentence(sentence):
    f=open('words_banned','r')
    for line in f:
        line = line.rstrip()
        exp = createRegularExpression(line)
        sentence = re.sub(exp,"****",sentence)
    return sentence


def createRegularExpression(line):
    low = line.lower()
    up = line.upper()
    expression = ""
    for i in range(len(line)):
        expression+="[" + up[i] + low[i] + "]+"
    return expression