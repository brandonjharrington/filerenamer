import os

filePath = "C:\\Users\\walter.goulet\\Documents\\Repos\\PMCode\\ChiPy\\data"

def getName(oldFile, path, index):
    newName = path + '\\' + str(index) + oldFile 
    return(newName)

def main():
    dataFiles = os.listdir(path=filePath)
    i = 0
    for dataFile in dataFiles:
        newFile = getName(dataFile, filePath, i)
        i = i + 1
        os.rename(filePath + '\\' + dataFile, newFile)





if __name__ == "__main__":
    main()