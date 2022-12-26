from Setting import *
from Util import *
from Filters import *
from Analyze import *
from Ligand import *
from Split import *
from Dock import *


# 0. Check settings before run
print("Virtual screening sequence initiated.\nCheck current settings.\n'''")
print(f"Target receptor: {NAME_OF_RECEPTOR}")
print(f"Directory of receptor file and affinity maps: {DIRECTORY_OF_RECEPTOR_TEMPLATE}")
print(f"Directory to find library's SDF file: {DIRECTORY_OF_LIGAND_LIBRARY}")
print(f"Directory to save result: {DIRECTORY_FOR_RESULT}\n'''")

if yesOrNo() is False :
    print("Check your Setting.py and try again.\nKilling program...")
    exit(0)


# 1. Select library to use and make a dict for file naming
FILENAME_OF_LIBRARY = Selector(DIRECTORY_OF_LIGAND_LIBRARY)
NAME_DICT = Namer.Extractor(libraryName=FILENAME_OF_LIBRARY, libraryPath=DIRECTORY_OF_LIGAND_LIBRARY)

# 2. Split sdf library to each single sdf files
DIRECTORY_OF_SPLITTED_LIGAND_LIBRARY = Splitter(dir=DIRECTORY_OF_LIGAND_LIBRARY, 
                                                        receptorName=NAME_OF_RECEPTOR, 
                                                        libraryFileName=FILENAME_OF_LIBRARY)


# 3. Size Filter for speed
FilterBySizeSDF(dir=DIRECTORY_OF_SPLITTED_LIGAND_LIBRARY, 
                        min=MINIMUM_BYTE_FOR_LIGAND_FILE_FILTERING, 
                        max=MAXIMUM_BYTE_FOR_LIGAND_FILE_FILTERING)


# 4. Ligand preparation
DIRECTORY_OF_PREPARED_LIGANDS = PrepareLigand(dir=DIRECTORY_OF_SPLITTED_LIGAND_LIBRARY, 
                                                        nameDict=NAME_DICT)


# 5. Filtering again.
FilterBySizePDBQT(dir=DIRECTORY_OF_PREPARED_LIGANDS, 
                            min=MINIMUM_BYTE_FOR_LIGAND_FILE_FILTERING, 
                            max=MAXIMUM_BYTE_FOR_LIGAND_FILE_FILTERING)
FilterByMWPDBQT(dir=DIRECTORY_OF_PREPARED_LIGANDS, 
                        min=MINIMUM_MOLECULAR_WEIGHT_FOR_SCREENING_LIGAND, 
                        max=MAXIMUM_MOLECULAR_WEIGHT_FOR_SCREENING_LIGAND)


# 6. Run ADV for every single ligand file
DIRECTORY_OF_RAW_OUTPUT = runDocking(receptorTemplateDir=DIRECTORY_OF_RECEPTOR_TEMPLATE, 
                                            ligandFileDir = DIRECTORY_OF_PREPARED_LIGANDS, 
                                            receptorName=NAME_OF_RECEPTOR)
print("Docking completed.")


# 7. Summarize result and make CSV file
print("Analyzing...",end='')

res = FindNoble(dir=DIRECTORY_OF_RAW_OUTPUT, max= MAXIMUM_AFFINITY_VALUE)
res = ValidityFilter(dir=DIRECTORY_OF_RAW_OUTPUT, nobleList=res)
MakeCSV(dir=DIRECTORY_FOR_RESULT, 
                nobleList=res, 
                libraryName=FILENAME_OF_LIBRARY[:-4], 
                receptorName=NAME_OF_RECEPTOR, 
                affinityThreshold=MAXIMUM_AFFINITY_VALUE)


print("completed.")
print("Check the result at")
print(DIRECTORY_FOR_RESULT)
