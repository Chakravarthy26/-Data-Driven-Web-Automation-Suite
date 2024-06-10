from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class TimesheetAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    def close_browser(self):
        self.driver.quit()

    def automate_timesheet(self, username, password):
        self.driver.get("https://www.becognizant.com/")

        # Login
        username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
        password_input = self.driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Navigate to Timesheet
        timesheet_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "ESA Timesheet")))
        timesheet_link.click()

        # Get last three weeks records
        week_records = []
        weeks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "week-record")))
        for week in weeks[:3]:
            date_range = week.find_element(By.CLASS_NAME, "date-range").text
            hours = week.find_element(By.CLASS_NAME, "hours").text
            week_records.append((date_range, hours))

        # Store in Excel
        df = pd.DataFrame(week_records, columns=['Date Range', 'Hours'])
        df.to_excel('timesheet_records.xlsx', index=False)

def main():
    automation = TimesheetAutomation()
    try:
        automation.automate_timesheet(username='your_username', password='your_password')
    finally:
        automation.close_browser()

if __name__ == "__main__":
    main()

