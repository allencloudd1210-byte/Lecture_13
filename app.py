import streamlit as st
import streamlit.components.v1 as components

# 1. 設定網頁標題與佈局 (設為 wide 寬版模式，讓圖表好看一點)
st.set_page_config(page_title="台灣氣象儀表板", layout="wide")

# 2. 讀取 HTML 檔案內容
# 注意：encoding='utf-8' 很重要，不然中文會亂碼
def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 3. 載入剛剛寫好的 weather.html
html_string = load_html_file("weather.html")

# 4. 使用 Streamlit 的 components 功能渲染 HTML
# height=800 是為了確保有足夠的高度顯示你的圖表，scrolling=True 允許捲動
components.html(html_string, height=850, scrolling=True)