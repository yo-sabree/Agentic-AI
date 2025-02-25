from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import time

def hum(text):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://docsbot.ai/tools/writing/ai-text-humanizer")
        time.sleep(3)

        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div/div/div[1]/div/div/form/div/textarea"))
        )
        textarea.send_keys(text)

        convert_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div/div/div[1]/div/div/form/div/button"))
        )
        convert_button.click()

        time.sleep(60)

        copy_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div[4]/button[1]"))
        )
        copy_button.click()

        time.sleep(2)

        humanized_text = pyperclip.paste()

        driver.quit()
        return humanized_text.strip()

    except Exception as e:
        driver.quit()
        return f"⚠️ Error: {str(e)}"
