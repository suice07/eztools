'''
Author: Auier qi.mei@outlook.com
Date: 2024-08-23 11:49:44
LastEditors: Auier qi.mei@outlook.com
LastEditTime: 2024-08-23 11:51:12
Copyright (c) 2024 by Auier qi.mei@outlook.com, All Rights Reserved. 
'''
import pandas as pd

def bill_calculator(text_data):
    rows = text_data.strip().split('\n\n')
    data = []
    for row in rows:
        row_data = row.strip().split('\n')
        if len(row_data) == 7:
            date1, date2, description, amount, transaction_id, country, total = row_data
            amount = float(amount.replace('¥ ', ''))
            total = float(total)
            data.append({
                'Date': date1,
                'Date2': date2,
                'Description': description,
                'Amount': amount,
                'Transaction ID': int(transaction_id),
                'Country': country,
                'Total': total
            })
    df = pd.DataFrame(data)
    return df