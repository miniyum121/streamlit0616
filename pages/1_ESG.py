import streamlit as st
import random

# 隨機運勢
fortunes = [
    "🌞 今天是幸運的一天！",
    "🌧️ 有點陰天，但你的心情很亮！",
    "🍀 一切都會越來越好！",
    "🐱 貓貓祝你平安喜樂～",
    "🎉 好事正在發生！"
]

# 可愛圖片
images = [
    "https://images.unsplash.com/photo-1574158622682-e40e69881006",  # 戴眼鏡貓
    "https://images.unsplash.com/photo-1592194996308-7b43878e84a6",  # 柴犬
    "https://images.unsplash.com/photo-1607746882042-944635dfe10e",  # 雪人
]

# 標題
st.title("🎡 今天的運勢")

# 按鈕
if st.button("點我抽運勢"):
    st.write(random.choice(fortunes))
    st.image(random.choice(images))  # 沒有 use_column_width
else:
    st.write("👉 按上面看看今天的運勢吧！")
