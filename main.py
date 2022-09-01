import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


# タイトルの表示
st.title('在庫分析ダッシュボード')

# 文章の表示
st.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})
# st.write(df)  # 下と同じ表を表示出来るが大きさ指定出来ない

# 縦横をピクセル単位で指定
# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))  # 列のマックス値をハイライト表示
st.table(df.style.highlight_max(axis=0))  # スタティックなテーブル　これはソートは出来ない。


# マークダウン　と　パイソンのコードを表示する

# """
# # 章(大見出し)
# ## 節　中見出し
# ### 項　小見出し

# ```python
# print('これは')
# print('バッククォーテーションで囲む')
# print('シングルクォーテーションではない')
# ```
# """

# チャート 折れ線グラフ
# df = pd.DataFrame(
#     np.random.rand(20, 3),  # 20*3の行列を作る　乱数を生成する
#     columns=['a', 'b', 'c']
# )
# st.write(df)  # テーブルを表示
# st.line_chart(df)
# st.area_chart(df)  # 折れ線の下側を色付け
#
# st.bar_chart(df)  # 棒グラフ

# 地図上にマッピング 東京都新宿区あたりをプロット
# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],  # 新宿あたりの緯度経度に変換
#     columns=['lat', 'lon']
# )
# st.map(df)

# 画像を表示
st.write('Display Image')
# img = Image.open('F:\\picture\\２０１４護衛艦はまぎり\\DSC_0596.JPG')
# img = Image.open('F:\\picture2\\巌新気功学テキスト\\１\\IMG_0352.JPG')
# img = Image.open(
#     'C:\\Users\\avent\\Documents\\01爆速PYTHONウェブアプリ作成講座\\a1.JPG')
img = Image.open('a1.JPG')
st.image(img, caption='taikuusentouyoui', use_column_width=True)
