
import streamlit as st
import random
from PIL import Image
import time

# タイトル表示
st.title("顔認証によるビリルビン値推定 PoC")

# セッション状態の初期化
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "diagnosis" not in st.session_state:
    st.session_state.diagnosis = None
if "simulate_auth" not in st.session_state:
    st.session_state.simulate_auth = False

# -------------------------------
# 顔認証ステップ（初回のみ）
# -------------------------------
if not st.session_state.authenticated:
    st.subheader("📷 顔認証ステップ")
    if st.button("顔認証を実行"):
        with st.spinner("顔認証中..."):
            time.sleep(2)
        st.session_state.authenticated = True
        st.success("顔認証成功！")

# -------------------------------
# ビリルビン診断ステップ
# -------------------------------
if st.session_state.authenticated:
    st.subheader("🩺 結膜画像とビリルビン値の推定")

    # 再撮影時の顔認証演出（1回だけ発動）
    if st.session_state.simulate_auth:
        with st.spinner("顔認証中..."):
            time.sleep(2)
        st.success("顔認証成功！")
        st.session_state.simulate_auth = False

    # 診断内容が未設定ならランダムに生成
    if st.session_state.diagnosis is None:
        st.session_state.diagnosis = random.choice(["normal", "mild", "high"])

    diagnosis = st.session_state.diagnosis

    if diagnosis == "normal":
        image_path = "normal_eye.jpg"
        tbil = round(random.uniform(0.5, 1.5), 1)
        result = "🟢 ビリルビン値は正常です。"
    elif diagnosis == "mild":
        image_path = "mild_eye.jpg"
        tbil = round(random.uniform(1.6, 3.0), 1)
        result = "🟡 軽度ビリルビンの上昇の可能性があります。\n異常値が続く場合医療機関受診をお勧めいたします。"
    else:
        image_path = "high_eye.jpg"
        tbil = round(random.uniform(3.1, 6.0), 1)
        result = "🔴 ビリルビンの上昇が強く疑われます。\n速やかな医療機関受診をお勧めいたします。"

    # 画像と診断結果の表示
    st.image(image_path, caption="結膜画像", use_container_width=True)
    st.markdown(f"### 💡 推定ビリルビン値: **{tbil} mg/dL**")
    st.markdown(f"### {result}")

    # 再撮影ボタン
    if st.button("🔁 再撮影してもう一度判定する"):
        st.session_state.diagnosis = None
        st.session_state.simulate_auth = True
