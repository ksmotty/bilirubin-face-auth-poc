
import streamlit as st
import random
from PIL import Image
import time
import os

st.title("顔認証によるビリルビン値推定 PoC")

# 状態を保持
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# 顔認証ステップ
if not st.session_state.authenticated:
    st.subheader("📷 顔認証ステップ")
    if st.button("顔認証を実行"):
        with st.spinner("顔認証中..."):
            time.sleep(2)
        st.session_state.authenticated = True
        st.success("顔認証成功！")

# 診断表示ステップ
if st.session_state.authenticated:
    st.subheader("🩺 結膜画像とビリルビン値の推定")

    diagnosis = random.choice(["normal", "mild", "high"])

    if diagnosis == "normal":
        image_path = "normal_eye.jpg"
        tbil = round(random.uniform(0.5, 1.5), 1)
        result = "🟢 正常"
    elif diagnosis == "mild":
        image_path = "mild_eye.jpg"
        tbil = round(random.uniform(1.6, 3.0), 1)
        result = "🟡 軽度上昇の可能性"
    else:
        image_path = "high_eye.jpg"
        tbil = round(random.uniform(3.1, 6.0), 1)
        result = "⚠️ 黄疸の可能性あり"

    if os.path.exists(image_path):
        st.image(image_path, caption="結膜画像", use_column_width=True)
    else:
        st.warning(f"画像ファイルが見つかりませんでした: {image_path}")

    st.metric(label="推定T-Bil値", value=f"{tbil} mg/dL")
    st.markdown(f"### {result}")
