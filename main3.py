import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


# サイドバー


st.title('在庫分析ダッシュボード')
# 画像を表示
st.write('Interractive widgets')

# チェックボックスがONならば画像を表示する
if st.sidebar.checkbox('防空ミサイルの画像を表示する'):
    img = Image.open(
        'C:\\Users\\avent\\Documents\\01爆速PYTHONウェブアプリ作成講座\\a1.JPG')
    st.image(img, caption='taikuusentouyoui', use_column_width=True)


# セレクトボックス
option = st.sidebar.selectbox(
    'あなたの好きな数字は？',
    list(range(1, 11))
)
text = st.sidebar.text_input('あなたの趣味はなんですか？')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)


'あなたの好きな数字：', option
'あなたの趣味：', text
'コンディション：', condition
