'''
Author: Auier qi.mei@outlook.com
Date: 2024-08-07 10:53:34
LastEditors: Auier qi.mei@outlook.com
LastEditTime: 2024-08-07 15:28:10
Copyright (c) 2024 by Auier qi.mei@outlook.com, All Rights Reserved. 
'''
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