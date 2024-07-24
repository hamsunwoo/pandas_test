import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='내가 실행한 명령어 카운트 기능')

parser.add_argument('-s', help='카운트할 명령어를 입력하세요')
parser.add_argument('-t', type=int, help='출력될 데이터 길이를 지정하세요.')
parser.add_argument('-d', help='날짜를 입력하세요. YYYY-MM-DD')

def cnt():

    df = pd.read_parquet("~/data/parquet")
    
    args = parser.parse_args()

    if not (args.s or args.t or args.d):
        print("명령어를 입력해주세요.")
        return
   
    if args.s:
        fdf = df[df['cmd'].str.contains(args.s)]
        cnt = fdf['cnt'].sum()
        print(f'{args.s} 사용 횟수는 {cnt}회 입니다.')

    if args.t and args.d:
        dt_df = df[df['dt'].str.contains(args.d)]
        top_dt_df = dt_df.head(args.t).to_string(index=False)
        print(top_dt_df)

    elif args.t:
        top_df = df.head(args.t)
        selected_df = top_df.loc[:, ['cmd','cnt']].to_string(index=False)
        print(selected_df)

    elif args.d:
        date_df = df[df['dt'].str.contains(args.d)]
        selected_date_df = date_df.loc[:, ['cmd','cnt']].to_string(index=False)
        print(selected_date_df)

