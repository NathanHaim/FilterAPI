import os

fileName="words_banned"
temporaryFile ="new_file"

def deleteAllWords():
    try:
        os.remove(fileName)
        with open(fileName,"w") as file:
            file.close()
        return True
    except:
        print("impossible to clean file")
        return False

def addWord(word):
    try:
        with open(fileName,"a") as file:
            file.write(word+"\n")
            file.close()
            print("word added : "+word)
        return True
    except:
        print("impossible add word : "+ word)

def deleteWord(word):
    try:
        with open(temporaryFile,'w') as newFile:
            with open(fileName,"r") as oldFile:
                for line in oldFile:
                    line = line.rstrip()
                    if line != word:
                        newFile.write(line+'\n')
                oldFile.close()
            newFile.close()
        os.remove(fileName)
        os.rename(temporaryFile,fileName)
        print("word deleted : " + word)
        return True
    except:
        print("impossible delete word : " + word)
        return False
