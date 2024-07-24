# 내가 쓴 명령어 카운트 기능 구현

## 사용방법
```python
my-history -s {카운트하고싶은 명령어 입력}
my-history -t {출력될 데이터 길이 입력}
my-history -d {데이터 날짜입력}
my-history -t {출력될 데이터 길이 입력} -d {데이터 날짜입력}
```
## v0.2.0코드
```python
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
        top_dt_df = dt_df.head(args.t).loc[:, ['cmd','cnt']].to_string(index=False)
        print(top_dt_df)

    elif args.t:
        top_df = df.head(args.t).loc[:, ['cmd','cnt']].to_string(index=False)
        print(top_df)

    elif args.d:
        date_df = df[df['dt'].str.contains(args.d)]
        selected_date_df = date_df.loc[:, ['cmd','cnt']].to_string(index=False)
        print(selected_date_df)
```


## 코드
```python
import pandas as pd
import sys

a = sys.argv[1]

def cnt():

    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(a)]
    cnt = fdf['cnt'].sum()
    print(cnt)
```
## 수정한 코드
```python
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='내가 실행한 명령어 카운트 기능')
parser.add_argument('--input', required=True, help='카운트할 명령어를 입력하세요
')

def cnt():
    args = parser.parse_args()
    input_command = args.input

    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(input_command)]
    cnt = fdf['cnt'].sum()


    print(cnt)
```

