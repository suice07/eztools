'''
Author: Auier qi.mei@outlook.com
Date: 2024-08-07 10:53:34
LastEditors: Auier qi.mei@outlook.com
LastEditTime: 2024-08-07 10:54:29
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