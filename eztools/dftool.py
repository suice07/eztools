'''
Author: Auier qi.mei@outlook.com
Date: 2024-08-07 10:53:34
LastEditors: Auier qi.mei@outlook.com
LastEditTime: 2024-08-12 15:44:51
Copyright (c) 2024 by Auier qi.mei@outlook.com, All Rights Reserved. 
'''
import pandas as pd
def rename_columns(indf, ori_column, new_column):
    '''
        stupid function for single change for column name, will update later
    '''
    indf = indf.rename(columns={
        ori_column: new_column,
    })
    return indf

def keyword_filter(df, checklist):
    '''
        giving a checklist, returns 
            subdf_contains: if any columns in subdf contains the keyword in the checklist
            subdf_not_contains: not any columns contains any keyword in the checklist
    '''
    subdf_contains = df[df.apply(lambda row: any(keyword in str(row.values) for keyword in checklist), axis=1)]
    subdf_not_contains = df[~df.apply(lambda row: any(keyword in str(row.values) for keyword in checklist), axis=1)]
    return subdf_contains, subdf_not_contains

def contains_any(s, checklist):
    if pd.isna(s):
        return False
    return any(item in s for item in checklist)

def pattern_search(s, patterns):
    import re
    if pd.isna(s):
        return False
    return any(bool(re.search(pattern, s)) for pattern in patterns)   

def keyword_column_filter(df, checklist, columnslist, filterfunc=contains_any):
    '''
        given a checklist of keywords, and a columnlist, returns
            subdf_contains: if any column in the column list contains the keyword in the checklist
            subdf_not_contains: not any column in the column list contains any keyword in the keyword checklists
    '''
    subdf_contains = df[df[columnslist].apply(lambda x: x.apply(lambda y: filterfunc(y, checklist)), axis=1).any(axis=1)]
    subdf_not_contains = df[~df[columnslist].apply(lambda x: x.apply(lambda y: filterfunc(y, checklist)), axis=1).any(axis=1)]
    return subdf_contains, subdf_not_contains

def retrieval_column_value(df, col1, value1, col2, valuelist, filter_nan = False):
    '''
        trivial subframes via column value1 and value list, if filter_nan, find the lines that col1 == value1, and col2 is NaN
    '''
    if filter_nan:
        subframe = df[(df[col1] == value1) & (df[col2].isin(valuelist))]
    else:
        subframe = df[(df[col1] == value1) & (df[col2].isna())]
    return subframe