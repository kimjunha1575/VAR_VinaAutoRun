
'''
This is template for VinaAutoRun.py.

Files to prepare:
    1. SDF file of library.
    2. PDBQT file of receptor and affinity map files prepared by ADFR suite.

Initiate below variables and run 'VinaAutoRun.py'.
'''

NAME_OF_RECEPTOR = "syntenin-1_pdz_domain"
DIRECTORY_OF_RECEPTOR_TEMPLATE = "/Users/kimjunha/desktop/sbmb/screening_2/syntenin/template"

DIRECTORY_OF_LIGAND_LIBRARY = "/Users/kimjunha/desktop/sbmb/screening_3/library"

DIRECTORY_FOR_RESULT = "/users/kimjunha/desktop/ScreeningResult/csv"

MAXIMUM_AFFINITY_VALUE = -13

MINIMUM_BYTE_FOR_LIGAND_FILE_FILTERING = 1000
MAXIMUM_BYTE_FOR_LIGAND_FILE_FILTERING = 10000

MINIMUM_MOLECULAR_WEIGHT_FOR_SCREENING_LIGAND = 200
MAXIMUM_MOLECULAR_WEIGHT_FOR_SCREENING_LIGAND = 600


'''
import Analyze

dir = "/Users/kimjunha/desktop/screeningresult/raw_data/Preclinical-Clinical-Library_syntenin-1_pdz_domain"
res = Analyze.FindNoble(dir=dir, max= MAXIMUM_AFFINITY_VALUE)
res = Analyze.ValidityFilter(dir=dir, nobleList=res)
Analyze.MakeCSV(dir=DIRECTORY_FOR_RESULT, 
                nobleList=res,
                libraryName=FILENAME_OF_LIBRARY[:-4], 
                receptorName=NAME_OF_RECEPTOR, 
                affinityThreshold=MAXIMUM_AFFINITY_VALUE)
'''
