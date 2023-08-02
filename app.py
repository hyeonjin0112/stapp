import streamlit as st
import pandas as pd

# 타이틀, 헤더, 서브헤더
st.title('Title')
st.header('Title *Markdown* 인식')
st.subheader('Title *Markdown* 인식')
st.title('Title')


# 텍스트
st.text('Title *Markdown* 인식못함.')
st.markdown('*markdown* 출력.')

x=10
y=20
st.write('x=',x,'y=',y)

df = pd.DataFrame({'col':[1,2,3]})
df
st.write('데이터프레임', df)

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig,ax = plt.subplots()

ax.hist(arr, bins=20)

fig

code = '''def hello():
     print("Hello,streamlit!")'''
st.code(code, language='python')

#캡션 출력
st.caption ('This')
st.caption ('A _italics_ :blue[colors] :sunglasses:')

#markdown 텍스트 컬러작용


#재미있는 이모티콘을 텍스트에 삽입해 본다
'여름엔 딱좋아 : sunglasses'
'100점~ :smile:'
'100점~ :smile:ㅎㅎ  :thumbsup:최고!!'

agree = st.checkbox('I agree')


if agree:
    st.write('Great!')

#터미널 빠져나가기 : ctrl+c

