import streamlit as st
from seo_model import get_seo_keywords, get_trending_keywords
from llm import generate_content
from humanize import hum
import re
import pyttsx3


def clean_markdown(text):
    text = re.sub(r'\*\*|\*|__|_', '', text)
    text = re.sub(r'#+\s?', '', text)
    text = re.sub(r'[-]{3,}', '', text)
    text = re.sub(r'\n{2,}', '\n\n', text)
    return text.strip()


st.set_page_config(page_title="Digital Marketing LLM", layout="wide")
st.title("Digital Marketing Content Generator")

st.sidebar.header("Options")
generate_img = st.sidebar.checkbox("Generate AI Image")
inp = st.text_input("Enter the Title:")

if inp:
    key = get_seo_keywords(inp)
    trend = get_trending_keywords()
    out = generate_content(inp, key, trend)
    clean = clean_markdown(out)

    if 'humanized_content' not in st.session_state or st.session_state.input_title != inp:
        with st.spinner("Humanizing content..."):
            st.session_state.humanized_content = hum(clean)
            st.session_state.input_title = inp

    st.subheader("Humanized Content")
    st.text_area("", st.session_state.humanized_content, height=300)

    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 190)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶ Start Speech"):
            tts_engine.say(st.session_state.humanized_content)
            tts_engine.runAndWait()

    with col2:
        if st.button("⏹ Stop Speech"):
            tts_engine.stop()
