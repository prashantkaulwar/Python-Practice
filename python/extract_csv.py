import pandas as pd

df = pd.read_csv('tbl_master_transaction_User_ID_5705.csv')
pending_id = df['Pending ID ']
refund_trace_number = df['Refund Trace Number']
for_sub = pending_id.str.lstrip('P')
for_sub = pd.to_numeric(for_sub)
final_for_sub = for_sub.subtract(1000000)


'''
list_val = final_for_sub.tolist()
'''
#print(pending_id.tolist())	
#print(refund_trace_number.tolist())
'''
result = dict(zip(list_val,refund_trace_number.tolist()))
'''
#print(result)
#print(df.columns)
#print(dir(df))
'''
import json

f = open('json_result.txt','w')
json.dump(result, f)
'''
