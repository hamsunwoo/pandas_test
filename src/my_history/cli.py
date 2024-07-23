import pandas as pd
import sys

a = sys.argv[1]

def cnt():

    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(a)]
    cnt = fdf['cnt'].sum()
    print(cnt)
