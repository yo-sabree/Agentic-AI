import streamlit as st
from seo_model import get_seo_keywords, get_trending_keywords
from llm import generate_content
from image import generate_image
from humanize import hum
import re


def clean_markdown(text):
    text = re.sub(r'\*\*|\*|__|_', '', text)
    text = re.sub(r'#+\s?', '', text)
    text = re.sub(r'[-]{3,}', '', text)
    text = re.sub(r'\n{2,}', '\n\n', text)
    return text.strip()


st.title("Digital Marketing LLM")
generate_img = st.checkbox("Generate AI Image")

inp = st.text_input("Enter the Title: ")

if inp:
    key = get_seo_keywords(inp)
    trend = get_trending_keywords()
    out = generate_content(inp, key, trend)
    clean = clean_markdown(out)

    with st.spinner("Humanizing content..."):
        humanized_content = hum(clean)

    st.subheader("Humanized Content")
    st.write(humanized_content)

    if generate_img:
        st.subheader("Image")
        image = generate_image(inp)
        if image:
            st.image(image, caption=f"{inp}")
        else:
            st.error("Could not generate an image.")
