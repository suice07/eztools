'''
Author: Auier qi.mei@outlook.com
Date: 2024-08-07 10:19:04
LastEditors: Auier qi.mei@outlook.com
LastEditTime: 2024-08-07 10:22:21
Copyright (c) 2024 by Auier qi.mei@outlook.com, All Rights Reserved. 
'''
import json

def dictdump(indict, outpath):
    with open(outpath, "w", encoding='utf-8') as f:
        json.dump(indict, f, ensure_ascii=False, indent=2)
    return outpath

def loaddict(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data