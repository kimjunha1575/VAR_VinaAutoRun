import os
import re


def findSDF(dir: str) -> list[str] :
    '''
    Input: Directory that contains target SDF files
    Output: List of SDF files in input directory.
    '''
    fullList = os.listdir(dir)
    SDFlist = []
    for file in fullList :
        if file[-4:].lower().__eq__(".sdf") :
            SDFlist.append(file)

    return SDFlist

def yesOrNo(massage: str="") -> bool :
    '''
    Input: String to indicate current state.
    Output: Boolean

    Check before conversion.(print 'massage')
    If user types 'Yes', return True.
    If user types 'No', return False.
    '''

    while True :
        print(massage)
        gostop = input("Type \"Yes\" to execute or \"No\" to stop: ")
        if gostop.lower() == "yes" or gostop == "y" :
            return True
        elif gostop.lower() == "No" or gostop == "n" :
            return False
        else :
            print("Wrong input. Try again.")
            continue


def dirCheck(dir: str) -> None :
    '''
    Input: Directory, list of every file in input directory
    Output: None
    
    Print input dir and up to 10 files in directory.
    '''
    try :
        fileList = os.listdir(dir)
        print("\nSearching files at")
        print(dir)
        print(f"\n{fileList.__len__()} files detected!\n")
        if fileList.__len__() > 10 :
            for i in range(10) :
                print(fileList[i])
        else :
            for file in fileList :
                print(file)
    except FileNotFoundError :
        print("Wrong directory for making file list. Try again.")
    except :
        print("Error at dirCheck(dir)")

def findPDBQT(dir: str) -> list[str] :
    '''
    Input: Directory containing target PDBQT files.
    Output: List of PDBQT files in directory.

    Return a list containing every PDBQT files in input directory.
    '''
    fullList = os.listdir(dir)
    PDBQTlist = list()
    for file in fullList :
        if file[-6:].lower().__eq__(".pdbqt") :
            PDBQTlist.append(file)

    return PDBQTlist


def makeOutputFolder(dir: str, dirName: str, currWD: str) -> str :
    '''
    Input: Directory to make a new folder, new folder's name, current executing function.
    Output: Directory of new folder.

    Make a new folder with 'dirName' and return new folder's directory
    or just return directory of 'dirName' folder.    
    '''
    try :
        temp = f"{dir}/{dirName}"
        os.mkdir(temp)
        return temp

    except FileExistsError :
        return f"{dir}/{dirName}"

def findTXT(dir: str) -> list[str] :
    '''
    Input: Directory of target TXT files.
    Output: List of TXT files in directory.

    Return a list of every txt file in input directory.
    '''
    fullList = os.listdir(dir)
    TXTlist = list()
    for file in fullList :
        if file[-4:].lower().__eq__(".txt") :
            TXTlist.append(file)

    return TXTlist

def findPDB(dir: str) -> list[str] :
    '''
    Input: Directory of target PDB files.
    Output: A list of PDB files in directory.

    Return a list of every PDB files in input directory.
    '''
    fullList = os.listdir(dir)
    PDBlist = list()
    for file in fullList :
        if file[-4:].lower().__eq__(".pdb") :
            PDBlist.append(file)

    return PDBlist

def isValidPDBQT(dir: str, PDBQTName: str) -> bool :
    '''
    Input: Directory of PDBQT files.
    Output: Boolean value of PDBQT file's validity.

    Open PDBQT file to check file's validity.
    Return True if first 5 atoms have different location.
    Return False if at least two atoms among first 5 have the same location.
    '''
    file = open(dir + "/" + PDBQTName, mode= 'r', encoding= "windows-1252")
    lines = file.readlines()
    temp = []
    for line in lines :
        if (line.find("ATOM") == 0) :
            temp.append(line)

    values = []
    for st in temp :
        values.append(re.findall("\d+", st)[2:8])

    values = sorted(values)
    switch = True
    for i in range(values.__len__()-1) :
        if values[i] == values[i+1] :
            switch = False
            break
    
    return switch


'''
def EraseSpecial(x: str) -> str :
    
    Input: String
    Output: String with out special charater.
    
    Erase every special character in input for valid file name.
    
    temp = x.replace("(","")
    temp = temp.replace("'","")
    temp = temp.replace("%","")
    temp = temp.replace("$","")
    temp = temp.replace("!","")
    temp = temp.replace("@","")
    temp = temp.replace("#","")
    temp = temp.replace("^","")
    temp = temp.replace("*","")    
    temp = temp.replace("\"","")    
    temp = temp.replace(")","")
    temp = temp.replace("&","")    
    temp = temp.replace("/","_")
    temp = temp.replace("-","_")
    temp = temp.replace(",", "_and_")
    temp = temp.replace(" ", "_")
    while temp.find("__") != -1 :
        temp = temp.replace("__","_")
    return temp
'''

def isValidSize(fileName: str, min: int, max: int) -> bool :
    '''
    Input: File name string
    Output: Boolean value

    Return True if input file name string has MW value between min and max.
    '''
    start = fileName.find("MW_") + 3
    end = fileName.find("_TARGET")
    mw = float(fileName[start:end])
    if min <= mw <= max :
        return True
    else :
        return False
        
def EraseSpecial(x: str) -> str :
    '''
    Input: String
    Output: String with out special charater.
    
    Erase every special character in input for valid file name.
    '''
    res = re.sub(r"()~!@#$%^&_-/'\"", "", x)

    return res