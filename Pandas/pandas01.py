"""
Pandas 란??

Pandas 는 파이썬에서 사용하는 데이터분석 라이브러리로, 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있게 되며 
보다 안정적으로 대용량의 데이터들을 처리하는데 매우 편리한 도구이다.

pandas 를 사용하기 위해서는 pandas 를 설치한 이후에 import 를 시켜줘야 한다

import pandas as pd

"""

import numpy as np # numpy 도 함께 import
import pandas as pd

# Series 정의하기
obj = pd.Series([4,7,-5,3])
obj

#Series 의 값만 확인하기
obj.values

#Series 의 인덱스 확인하기
obj.index

#Series 의 자료형 확인하기
obj.dtypes

#인덱스를 바꿀 수 있다.
obj2 = pd.Series([4,7,-5,3]), index= ['d','b','a','c']
obj2

#python 의 dictionary 자료형을 Series data 로 만들수 있다.
#dictionary 의 key가 Series 의 index가 된다.
sdata = {'Kim': 35000, 'Beomwoo': 67000, 'Joan': 12000, 'Choi': 4000}
obj3 = pd.Series(sdata)
obj3

obj3.name = 'Salary'
obj3.index.name = 'Names'
obj3

#index 변경
obj3.index = ['A','B','C','D']
obj3

##Data Frame
#data frame 정의하기
#이전에 DataFrame에 들어갈 데이터를 저의해주어야 하는데,
#이는 python 의 dictionary 또는 numpy의 array로 정의 할 수 있다.

data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
df

#행과 열의 구조를 가진 데이터가 생긴다

#행 방향의 index
df.index

#열 방향의 index
df.colums

#값 얻기
df.values

#각 인덱스에 대한 이름 설정하기
df.index.name = "Num"
df.columns.name = "Info"
df

#DataFrome을 만들며서 columns 와 index를 설정할 수 있다.
df2 = pd.DataFrame(data, columns=['year', 'name', 'points', 'penalty'],
                  index=['one', 'two', 'three', 'four', 'five'])
df2

"""
DataFrame을 정의하면서, data로 들어가는 python dictionary와 columns의 순서가 달라도 알아서 맞춰서 정의된다.
하지만 data에 포함되어 있지 않은 값은 NaN(Not a Number)으로 나타나게 되는데,
이는 null과 같은 개념이다.
NaN값은 추후에 어떠한 방법으로도 처리가 되지 않는 데이터이다.
따라서 올바른 데이터 처리를 위해 추가적으로 값을 넣어줘야 한다.

"""

# describe() 함수는 DataFrame의 계산 가능한 값들에 대한 다양한 계산 값을 보여준다.
df2.describe()

## DataFrame Indexing
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
           "year": [2014, 2015, 2016, 2015, 2016],
           "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])
df


#3-1. DataFrame 에서 열을 선택하고 조작하기
df['year']

#위와 동일
df.year 

df['year','points']

#특정 열에 대해 위와 같이 선택하고, 우리가 원한느 값을 대입할 수 있다.
df['penalty'] = 0.5
df
#penalty 속성의 값이 다 0.5

# 또는
df['penalty'] = [0.1, 0.2, 0.3, 0.4, 0.5] # python의 List나 numpy의 array


#새로운 열을 추가하기
df['zeros'] = np.arange(5)

#Series를 추가할 수도 있다.
val = pd.Series([-1.2,-1.5,-1.7], index=['two','four','five'])
df['debt'] =val
df

df['net_points'] = df['points'] - df['penalty']
df['high_points'] = df['net_points'] > 2.0
df


# 열 삭제하기
del df['high_points']
del df['net_points']
del df['zeros']

df


# DataFrame 에서 행을 선택하고 조작하기

#0번째 부터 2번까지 가져온다
#뒤에 써준 숫자번쨰의 행은 뺀다.
df[0:3]


#.loc 또는 iloc 함수를 사용하는 방법
df.loc['two']

df.loc['two':'four']

df.loc['two':'four','points']

df.loc[:,'year'] # == df['year']



##4부터 다시보기
