import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import win32api
import win32con
import win32gui

def set_wallpaper():
    # Setting up options for Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Running in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Path to the browser driver
    driver_path = 'C:/User/chromedriver-win64/chromedriver.exe'

    # Initializing the driver service
    service = Service(driver_path)

    # Initializing the driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        try:
            # Opening the website
            driver.get('https://rand.by/en/image')

            # Explicit wait for the "Generate" button to load
            wait = WebDriverWait(driver, 10)
            generate_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button/span[text()="Generate"]')))

            # Clicking the "Generate" button
            generate_button.click()

            # Waiting for the image to generate
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'flex.flex-wrap.content-top.gap-4.mb-4')))

            # Finding and saving the image
            image_element = driver.find_element(By.XPATH, '//div[@class="flex flex-wrap content-top gap-4 mb-4"]/img')
            image_url = image_element.get_attribute('src')

            # Downloading the image
            response = requests.get(image_url)
            if response.status_code == 200:
                image_path = 'generated_image.jpg'
                with open(image_path, 'wb') as file:
                    file.write(response.content)
                print("Image successfully saved.")

                # Setting the image as the desktop wallpaper
                SPI_SETDESKWALLPAPER = 20
                SPIF_UPDATEINIFILE = 0x01
                SPIF_SENDWININICHANGE = 0x02

                # Ensuring the image path is absolute
                abs_image_path = os.path.abspath(image_path)

                # Setting the wallpaper
                win32gui.SystemParametersInfo(SPI_SETDESKWALLPAPER, abs_image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
            else:
                messagebox.showerror("Error", "Failed to download the image.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        # Closing the driver
        driver.quit()

# Creating the window
root = tk.Tk()
root.title("Set Wallpaper")

# Creating the button
button = tk.Button(root, text="Set Wallpaper", command=set_wallpaper)
button.pack(pady=20)

# Running the main loop
root.mainloop()