import google.generativeai as genai
from PIL import Image
import io
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

def generate_image(prompt):
    """Generate an image using Gemini AI."""
    model = genai.GenerativeModel("imagen-3.0-generate-002")

    try:
        response = model.generate_content([prompt], stream=False)
        if response.media:
            img_data = response.media[0].binary
            img = Image.open(io.BytesIO(img_data))
            return img
        else:
            return None
    except Exception as e:
        print(f"Error generating image: {e}")
        return None
