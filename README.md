# 내가 쓴 명령어 카운트 기능 구현

## 사용방법
```python
c_cnt --input "{카운트하고싶은 명령어 입력}"
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

