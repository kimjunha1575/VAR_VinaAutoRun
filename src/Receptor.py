import os
import Util

def PrepareReceptor(dir: str, atom: list[str]) -> str :
    '''
    Input: Directory of receptor's PDB file.
    Output: Directory of receptor's template containing affinity map, grid value, prepared PDBQT

    Prepare receptor file by ADFR suite 1.0.
    Return name of receptor.  
    '''
    PDBlist = Util.findPDB(dir)
    print(PDBlist)
    for PDB in PDBlist :

        print(PDB)
        TF = Util.yesOrNo("Is this your receptor PDB file?")

        if TF is True :
            receptorName = PDB[:-4]

            os.system(f"prepare_receptor -r {dir}/{receptorName}.pdb -o {dir}/{receptorName}.pdbqt")

            os.system(f"prepare_gpf.py -r {receptorName}.pdbqt -o {dir}/{receptorName}.gpf")
            os.system(f"cd {dir}")
            os.system(f"autogrid -p {dir}/{receptorName}.gpf -l {dir}/{receptorName}.glg")

            gpfLines = open(f"{dir}/{receptorName}.gpf").readlines
        
            AddAffinityMaps(dir=dir, receptorName=receptorName, gpfLines=gpfLines, atom=atom)

            return receptorName

        else :
            continue



def AddAffinityMaps(dir: str, receptorName: str, gpfLines: list[str], atom: list[str])  -> None :
    '''
    Input: Directory of receptor template, receptor's name, atom for affinity map
    Output: None

    Add specific atom's affinity map at receptor template directory.
    '''

    if atom.__len__() <= 8 :
        newLine = []
        for i in range(atom.__len__()) :

            start = gpfLines[i+8].find('.')
            end = gpfLines[i+8].find(".map")
            newLine = gpfLines[i+8][:start+1] + atom[i] + gpfLines[i+8][end:]

        newGPF = open(f"{dir}/newGPF.gpf", 'w')
        newGPF.writelines(newLine)
        os.system(f"autogrid -p {dir}/{receptorName}.gpf -l {dir}/{receptorName}.glg")
            
    else :
        list1 = atom[0:8]
        list2 = atom[8:]

        AddAffinityMaps(dir=dir, receptorName=receptorName, gpfLines=gpfLines, atom=list1)
        AddAffinityMaps(dir=dir, receptorName=receptorName, gpfLines=gpfLines, atom=list2)