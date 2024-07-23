# 내가 쓴 명령어 카운트 기능 구현

## 사용방법
```python
c_cnt {카운트하고싶은 명령어 입력}
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


