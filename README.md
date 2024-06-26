# VAR_VinaAutoRun
Simple automation of 1:N molecular docking process performed by [AutoDock Vina](https://vina.scripps.edu/) (1.2).

## Process
0. (Before run)Check the input files and directories.
1. Select library of ligands.
2. Split sdf file into individual ligand files.
3. Filter ligands by size.
4. Prepare ligands for docking.
5. Filter ligands by size and MW.
6. Dock ligands to the receptor.
7. Summarize the results.

## Dependencies
- [AutoDock Vina](https://vina.scripps.edu/)
- ADFRsuite 1.0
- Open Babel 3.1.1
- Gypsum-DL 1.0.0
- Python 3.8.5
- pdb-tools 2.0