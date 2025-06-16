import streamlit as st
import random

# 設定 session_state 用來記錄答案與狀態
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.result = ""

# 標題
st.title("🎲 猜猜我是幾號？")
st.write("我已經偷偷選了一個 1 到 100 的數字，快來猜猜是幾！")

# 玩家輸入
guess = st.number_input("請輸入一個數字（1～100）", min_value=1, max_value=100, step=1)

# 按鈕來提交猜測
if st.button("我要猜！"):
    st.session_state.attempts += 1
    if guess < st.session_state.answer:
        st.session_state.result = "⬆️ 太小了，再大一點！"
    elif guess > st.session_state.answer:
        st.session_state.result = "⬇️ 太大了，再小一點！"
    else:
        st.session_state.result = f"🎉 猜對了！答案就是 {st.session_state.answer}，你總共猜了 {st.session_state.attempts} 次！"
        st.session_state.answer = random.randint(1, 100)  # 重設新遊戲
        st.session_state.attempts = 0

# 顯示結果提示
st.markdown(f"### {st.session_state.result}")

# 重設遊戲按鈕
if st.button("🔄 我要重新開始"):
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.result = ""
    st.success("已經幫你重設遊戲，快來挑戰！")
