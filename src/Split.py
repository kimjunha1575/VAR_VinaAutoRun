import os
import Util

def Splitter(dir: str, receptorName: str, libraryFileName: str) -> str :
    '''
    input: Directory of compound library's SDF file.
    output: Splitted SDF files' directory

    Split a multimol SDF file into each sigle SDF files
    '''

    outputDir = Util.makeOutputFolder(dir = f"{dir}/splitted_libraries", dirName = libraryFileName[:-4] + f"_{receptorName}", currWD= "Split")
    print("\nConverting...")

    os.system(f"obabel -i SDF {dir}/{libraryFileName} -o SDF -O {outputDir}/{libraryFileName[:-4]}_splitted.sdf -m")

    return outputDir



def Selector(dir: str) -> str :
    '''
    Input: Directory of library files.
    Output: Filename of selected library.

    Select library to use virtual screening and return selected library's filename.
    '''
    
    sdfList = Util.findSDF(dir)

    for file in sdfList :

        TF = Util.yesOrNo(f"\nIs this your library?\n'''\n{file}\n'''")
        if TF is True :
            return file

    print("No more SDF files in this directory.")
    print("Killing program...")
    exit(0)