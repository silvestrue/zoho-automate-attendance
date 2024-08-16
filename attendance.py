import pickle
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime, time
import sys

# Check if it's Saturday (5) or Sunday (6)
if datetime.now().weekday() in {5, 6}:
    print("It's the weekend. Skipping script execution.")
    sys.exit()

# Introduce a random delay between 0 and 7 minutes
delay_minutes = random.uniform(0, 7)
print(f"Delaying script execution for {delay_minutes:.2f} minutes.")
sleep_time.sleep(delay_minutes * 60)  # Convert minutes to seconds

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the browser with headless options
driver = webdriver.Chrome(options=chrome_options)

# Open the Zoho People login page to set initial cookies
driver.get("https://www.zoho.com/people/")

# Load cookies from the saved cookies file
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    # Set the domain to handle invalid cookie domain error during redirects
    cookie['domain'] = '.zoho.com'
    driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()

# Navigate to the desired page (https://people.zoho.com/COMPANY/zp#home/dashboard)
driver.get("https://people.zoho.com/COMPANY/zp#home/dashboard")

t.sleep(6)

# Check the current time
current_time = datetime.now().time()

if len(sys.argv) != 2:
    print("Usage: python attendance.py [checkin/checkout]")
    sys.exit()

action = sys.argv[1]

# Execute the appropriate action based on the command-line argument
if action == "checkin":
    driver.execute_script("Attendance.Dashboard.WeeklyData.updateCheckOut(true)")
    print("Checked in.")
elif action == "checkout":
    driver.execute_script("Attendance.Dashboard.WeeklyData.updateCheckOut(false)")
    print("Checked out.")
else:
    print(f"Invalid argument: {action}. Use 'checkin' or 'checkout'.")
    
t.sleep(10)    

# Optional: Add a delay or perform additional actions on the desired page

# Close the browser
driver.quit()
