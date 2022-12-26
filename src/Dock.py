import os
import Util

def runDocking(receptorTemplateDir: str, ligandFileDir: str, receptorName: str) -> str:
    '''
    Input: String of receptor file's directory, ligand files' directory, name of receptor.
    Output: Directory of output files.

    Find every PDBQT file in 'ligandFileDir' and execute molecular docking by AutoDock Vina for each PDBQT file.
    Save output log file(.txt) and PDBQT file in a folder.
    Return the folder's directory.    
    '''
    ligandList = Util.findPDBQT(ligandFileDir)
    total = ligandList.__len__()
    outputDir = Util.makeOutputFolder(dir=ligandFileDir, dirName=receptorName, currWD= "Docking")
    count = 0
    print("Start docking.\n")
    for ligand in ligandList :
        percent = (float(count)/total) * 100
        print("Docking..." + "%.1f"%percent + "%")
        print(ligand)
        os.system(f"vina --ligand {ligandFileDir}/{ligand} --out {outputDir}/{ligand} --maps {receptorTemplateDir}/{receptorName} --num_modes 3 --exhaustiveness 16 --scoring ad4 > {outputDir}/{ligand[:-6]}.txt")
        try :
            TF = Util.isValidPDBQT(dir=outputDir,PDBQTName=ligand)
            if TF :
                count += 1
                print(count, "completed\n")
                
            else :
                os.remove(f"{outputDir}/{ligand}")
                print("\nInvalid PDBQT! File removed!")
                total -= 1
        except :
            total -= 1
            print("\nError during docking. Skip to next.")
    print("\nDocking completed.\n")
    return outputDir
