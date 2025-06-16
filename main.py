import streamlit as st

# 設置頁面標題
st.title("Mini的個人網頁")

# 添加文本輸入框
name = st.text_input("請輸入你的名字:")

# 根據用戶的輸入顯示結果
if name:
    st.write(f"你好，{name}！歡迎來到我的網頁！")
else:
    st.write("請輸入你的名字。")
