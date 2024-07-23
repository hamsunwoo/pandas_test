import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='내가 실행한 명령어 카운트 기능')
parser.add_argument('--input', required=True, help='카운트할 명령어를 입력하세요')

def cnt():
    args = parser.parse_args()
    input_command = args.input

    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(input_command)]
    cnt = fdf['cnt'].sum()

    
    print(cnt)
