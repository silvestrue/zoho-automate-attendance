# Zoho Automatic Attendance
These scripts will help automate the check-in / check-out process that many employees have to do for Zoho People.

Uses Selenium for the web component.

# Usage
1. Run "capture cookies.py" first. This will open up a regular Chrome browser with the login page for your Zoho company specific portal. Login with password and any other 2FA method that is required. This will create a "cookies.pkl" file that contains the cookies we need for auto-login.
2. Run "attendance.py" with either "checkin" or "checkout" as the sole argument. The script runs in headless mode.

You might want to either create a task in Task Scheduler or a cron job for your particular Linux distribution.

Enjoy!

# Note
Make sure to edit both scripts and replace the people.zoho.com/COMPANY/ url with your company's specific name.
