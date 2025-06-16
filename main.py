import streamlit as st

# 頁面基本設定
st.set_page_config(
    page_title="我的優質網頁",
    page_icon="✨",
    layout="wide"
)

# 自訂 CSS 美化文字
st.markdown("""
    <style>
    .big-font {
        font-size:36px !important;
        font-weight: bold;
        color: #4a4a4a;
    }
    .subtle-font {
        font-size:18px;
        color: #6c6c6c;
    }
    </style>
""", unsafe_allow_html=True)

# 頁首圖片 + 標題
st.markdown("<p class='big-font'>👋 歡迎來到我的網站</p>", unsafe_allow_html=True)
st.markdown("<p class='subtle-font'>這是一個用 Streamlit 製作的優質網頁，展示設計、互動與簡約風格。</p>", unsafe_allow_html=True)

# 分欄設計
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📌 關於我")
    st.write("""
        我是一名熱愛資料、設計與網頁製作的創作者。  
        這個網頁是以 Python + Streamlit 架構完成，展示簡潔設計風格。  
        若你也想製作屬於自己的網頁，我可以協助設計！  
    """)
    
    if st.button("📬 聯絡我"):
        st.success("請透過 email@example.com 與我聯繫！")

with col2:
    st.image("https://images.unsplash.com/photo-1520880867055-1e30d1cb001c?w=800", 
             caption="設計中的思考時光")

# 分隔線
st.markdown("---")


# 頁尾
st.markdown("""
---
🧡 感謝你的造訪！(https://streamlit.io)
""")
