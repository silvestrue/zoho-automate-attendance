import pickle
import time
from selenium import webdriver

# Initialize the browser
driver = webdriver.Chrome()

# Open the Zoho People website
driver.get("https://people.zoho.com/openlm/zp#home/dashboard")

# Add a delay to allow time for manual authentication
time.sleep(180)  # Adjust the delay as needed (in seconds)

# Get and print cookies
cookies = driver.get_cookies()
print(cookies)

# Save cookies to a file
with open("cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

# Close the browser
driver.quit()