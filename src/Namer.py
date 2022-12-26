import re
import Util

def Extractor(libraryName: str, libraryPath: str) -> dict :
    '''
    Input: Two str class objects. 
        1. Name of library includes extension (ex: file.txt). 
        2. Path of the library.
    Output: A dict class object.

    Return a dict class object that contains compound's information.
        ex. output[key] = [compound name, molecular weight, target]
    '''
    libraryFull = open(libraryPath + "/" + libraryName, encoding="windows-1252").readlines()
    librarySingle = []
    temp = []
    num = 1
    nameDict = {}

    #Make separate lists divided by "$$$$"
    for line in libraryFull :
        temp.append(str(num))
        if line.__contains__("$$$$") is False :
            temp.append(line)
        else :
            librarySingle.append(temp)
            temp = []
            num += 1

    #Cut out useless elements
    for i in range(librarySingle.__len__()) :
        startPoint = librarySingle[i].index("M  END\n") + 1
        librarySingle[i] = librarySingle[i][startPoint:-3]

    #Make dict that has a list of name, mw and target as list for each key(number)
    for e in librarySingle :
        mw = "unknown"
        name = "unknown"
        target = "unknown"
        for line in e :
            mwIndex = line.find("<MolWeight>")
            if mwIndex != -1 :
                mw = e[e.index(line) + 2][:-1]
                break
        for line in e :
            tgIndex = line.find("<Target>")
            if tgIndex != -1 :
                target = e[e.index(line) + 2][:-1]
                break
        for line in e :
            nameIndex = line.find("<Name>")
            cdxIndex = line.find(".cdx")
            if nameIndex != -1 :
                name = e[e.index(line) + 2][:-1]
                break
            if cdxIndex != -1 :
                name = e[e.index(line) + 1][:-4]
        
        nameDict[int(e[0])] = [name.replace(' ','_'), mw.replace(' ','_'), target.replace(' ','_')]

    return nameDict



def Namer(info: dict, fileName: str) -> str :
    '''
    input: Output of function Extractor().
    output: Name for output of virtual screening or preparation.

    Return a string contains number, name, molecular weight and target.
        ex: "000005_NAME:Bosutinib_(SKI-606)_MW:530.44616_TARGET:Src"
    '''
    temp = int(re.findall("\d+", fileName)[-1])
    
    name = info[temp][0].replace('-','')
    mw = info[temp][1]
    target = info[temp][2]

    outputName = str(temp).zfill(6) + "_NAME_" + name + "_MW_" + mw + "_TARGET_" + target

    res = Util.EraseSpecial(outputName)

    return res


def MWFilter(fileList: list[str], min: int, max: int)  -> list[str] :
    '''
    Input: A list class object which has file names.
    Output: Input without file names that have too small or too big MW value.

    Return a new list of file names that has MW between 'min' and 'max'.    
    '''
    res = []
    for file in fileList :
        start = file.find("MW_") + 3
        end = file.find("_TARGET")
        mw = float(file[start:end])
        if min <= mw <= max :
            res.append(file)

    return res
