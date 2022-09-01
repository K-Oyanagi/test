import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('在庫分析ダッシュボード')
# 画像を表示
st.write('Interractive widgets')

# チェックボックスがONならば画像を表示する
if st.checkbox('防空ミサイルの画像を表示する'):
    img = Image.open(
        'C:\\Users\\avent\\Documents\\01爆速PYTHONウェブアプリ作成講座\\a1.JPG')
    st.image(img, caption='taikuusentouyoui', use_column_width=True)


# セレクトボックス
option = st.selectbox(
    'あなたの好きな数字は？',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です'

# テキスト入力

text = st.text_input('あなたの趣味はなんですか？')
'あなたの趣味は', text, 'です'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
