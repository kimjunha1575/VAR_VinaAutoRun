import Util
import os
import Namer


def PrepareLigand(dir: str, nameDict: dict) -> str :
    '''
    input: Directory of ligand SDF files and dict class object for output file naming.
    output: Directory of output folder in input dir which contains prepared ligand files.

    Convert every SDF file to 3D PDBQT file by open babel command.
    Make 'output' folder at input directory and save PDBQT files at output folder.
    '''
    list = Util.findSDF(dir)
    outDir = Util.makeOutputFolder(dir, dirName = "preparation", currWD="Preparing Ligand")
    total = list.__len__()
    count = 0
    print("\nStart ligand preparation.\n")
    for ligand in list :
        try :
            percent = (float(count)/total)*100
            name = Namer.Namer(nameDict, ligand)
            print("\nPreparing ligand..." + "%.2f"%percent + "%")
            print(name + ".pdbqt")
            if Util.isValidSize(fileName=name+".pdbqt",min=200, max=600) is True :
                os.system(f"timeout 3 obabel -i sdf {dir}/{ligand} -o pdbqt -O {outDir}/{name}.pdbqt --gen3d")

                TF = Util.isValidPDBQT(dir=outDir, PDBQTName=name+".pdbqt")
                if TF is True :
                    count += 1
                    print(count, "converted Total\n")
                else :
                    total -= 1
                    os.remove(f"{outDir}/{name}.pdbqt")
                    print("\nInvalid PDBQT! File removed!")
            else :
                total -= 1
                print("Too big or too small ligand! Undruggable!\nSkipping to next ligand...")
        except :
            total -= 1
            print("Error occured during preparing ligand.")
            print("Skipping to next ligand...")
            continue
    print("\nLigand preparation completed.\n")
    return outDir
