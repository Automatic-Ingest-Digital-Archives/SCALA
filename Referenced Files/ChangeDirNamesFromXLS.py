def change_dirnames_from_excel(path, excelpath): # Functie om dirs te hernoemen. 
# Specifiek handig om folders te hernoemen conform specs storage server
# Gaat uit van één excel met een kolom orig_name en new_name. Foldernamen, niet folderpaths
# Werkt recursive
import pandas as pd
import os
    dataframe = pd.read_excel(excelpath, na_filter=False, dtype=object)
    directorylist = dataframe.to_dict('records')
    os.chdir(path)
    for directory in directorylist:
        if os.path.isdir(directory['orig_name']):
            os.renames(directory['orig_name'], directory['new_name'])
            print("Directory", directory['orig_name'], "renamed in", directory['new_name'])
        else:
            print("Directory", directory['orig_name'], 'does not exist.')
