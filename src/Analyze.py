import Util

def FindNoble(dir: str, max: float) -> list[str] :
    '''
    Input: Directory of raw data, maximum value for choose noble.
    Output: List containing name of log files.

    Find outputs have lower affinity value then 'max'.
    '''
    list = Util.findTXT(dir)
    nobleList = []
    count = 0
    for txt in list :
        try :
            fileName = f"{dir}/{txt}"
            file = open(fileName, 'r')
            res = file.readlines()[34]
            res_first = res[11:17].replace(' ','')
            res_float = float(res_first)
            if res_float < max :
                if res_float == -1 :
                    print(res)
                    print(res_first)
                    print(res_float)
                count += 1
                nobleList.append(txt + ": " + res_first)

        except :
            pass
    print(f"Found {count} noble candidates!")

    return nobleList

import Util



def ValidityFilter(dir: str, nobleList: list[str]) -> list[str] :
    '''
    Input: Directory of raw data, list containing output log files of noble compounds
    Output: List of output files for only valid structure.

    Remove elements in input list that at least two atom have same location.
    '''
    res = []
    count = 0
    for noble in nobleList :
        try :
            fileName = noble[:noble.find(": -")-4] + ".pdbqt" #이후에 수정해서 사용
            TF = Util.isValidPDBQT(dir, fileName)
            if TF is True :
                res.append(noble)
            else :
                count += 1
        except :
            count += 1

            continue
    print(f"{count} invalid candidates removed from result.")
    return res


def MakeCSV(dir: str, nobleList: list[str], libraryName: str, receptorName: str, affinityThreshold: float) -> None :
    '''
    Input: Directory for save result, list of noble compounds, library name, receptor name
    Output: None

    Write a sorted CSV file containing screening result. 
    '''
    valueList = []
    res = open(file=f"{dir}/{receptorName}&{libraryName}_below_({affinityThreshold}).csv", mode='w')
    for file in nobleList :

        nIndex = file.find("_NAME_")
        mIndex = file.find("_MW_")
        tIndex = file.find("_TARGET_")
        aIndex = file.find(": -")

        num = file[ : nIndex]
        name = file[nIndex + 6 : mIndex]
        mw = file[mIndex + 4 : tIndex]
        target = file[tIndex + 8 :aIndex - 4]
        affinity = "%.2f"%float(file[aIndex + 2 : ].replace('\n',''))

        valueList.append(f"{num},{name},{mw},{target},{affinity}\n")
        
    valueList.sort(key = lambda x : x.split(',')[4])
    res.write("NUMBER,NAME,MW,TARGET,AFFINITY\n")
    res.writelines(valueList)
    res.close()