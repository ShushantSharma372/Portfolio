from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the desired webpage
    driver.get("https://food.ndtv.com/recipes")  # Replace with the URL of the web page

    # Wait until the element with the link text "Indian" is present
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "AMERICAN"))
    )

    # Click the link
    link.click()

    # Optionally, you can wait for the next page to load or for any specific elements on the next page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "someElementId"))  # Replace with the ID of an element on the new page
    )
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser window
    driver.quit()