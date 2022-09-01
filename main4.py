# ツーカラム表示、エクスパンダ―


import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('在庫分析ダッシュボード')
# 画像を表示
st.write('Interractive widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# エクスパンダ―　

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')
