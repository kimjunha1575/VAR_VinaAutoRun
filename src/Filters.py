import os
import Util

def FilterBySizeSDF(dir: str, min: int, max: int) -> None :
    '''
    Input: String of target directory.
    Output: None

    Remove every SDF files whose size is between not between 'min' and 'max'.
    '''
    list = Util.findSDF(dir)
    path = dir
    for file in list :
        size = os.path.getsize(f"{path}/{file}")
        if not ( min <= size <= max ) :
            os.remove(f"{path}/{file}")


def FilterByMWPDBQT(dir: str, min: int, max: int) -> None :
    '''
    Input: String of target directory.
    Output: None

    Remove every PDBQT files whose name has MW value between 'min' and 'max'.    
    '''
    list = Util.findPDBQT(dir)
    path = dir
    for file in list :
        start = file.find("MW_") + 3
        end = file.find("_TARGET")
        mw = float(file[start:end])
        if not ( min <= mw <= max) :
            os.remove(f"{path}/{file}")

def FilterBySizePDBQT(dir: str, min: int, max: int) -> None :
    '''
    Input: String of target directory.
    Output: None

    Remove every PDBQT files whose size is not between 'min' and 'max'. 
    '''
    list = Util.findPDBQT(dir)
    path = dir
    for file in list :
        size = os.path.getsize(f"{path}/{file}")
        if not ( min <= size <= max ) :
            os.remove(f"{path}/{file}")