# プログレスバーを表示する

import streamlit as st
from PIL import Image
import time


st.title('在庫分析ダッシュボード')
# 画像を表示
st.write('プログレスバーの表示')
'start!!!!'
latestIteration = st.empty()  # 空の要素を追加 for文の前に書いてあるから同じ場所にアップデートされていく
bar = st.progress(0)  # ０から１００で表示する
for i in range(100):
    latestIteration.text(f'iteration {i+1}')
    bar.progress(i + 1)  # これがバーを伸ばしている
    time.sleep(0.03)  # これで成長スピードを調整している
'ダウンロード完了！！！！！'

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
