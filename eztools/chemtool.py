'''
Author: Auier qi.mei@outlook.com
Date: 2024-08-23 10:20:42
LastEditors: Auier qi.mei@outlook.com
LastEditTime: 2024-08-23 10:24:14
Copyright (c) 2024 by Auier qi.mei@outlook.com, All Rights Reserved. 
'''
import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools

def write_pics(df, columname, savingpath):
    '''
        write pics(2D Molecule structure) according to the smiles in given df
    '''
    df['Mol Image'] = [Chem.MolFromSmiles(s) for s in df[columname]]
    PandasTools.SaveXlsxFromFrame(df, savingpath, molCol=columname)
    return savingpath
