#yatra_automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class YatraAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    def close_browser(self):
        self.driver.quit()

    def automate_yatra(self):
        self.driver.get("https://www.yatra.com/")
        assert "Yatra.com" in self.driver.title

        # Navigate to Offers
        offers_link = self.driver.find_element(By.LINK_TEXT, "Offers")
        offers_link.click()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Domestic Flights Offers | Deals on Domestic Flight Booking | Yatra.com"))
        assert "Domestic Flights Offers | Deals on Domestic Flight Booking | Yatra.com" in self.driver.title

        # Check the banner text
        banner_text = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Great Offers & Amazing Deals')]")
        assert "Great Offers & Amazing Deals" in banner_text.text

        # Take screenshot
        self.driver.save_screenshot('yatra_offers_page.png')

        # Navigate to Holidays
        holidays_link = self.driver.find_element(By.LINK_TEXT, "Holidays")
        holidays_link.click()

        # List five holiday packages
        packages = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-listing")))
        for package in packages[:5]:
            name = package.find_element(By.CLASS_NAME, "product-title").text
            price = package.find_element(By.CLASS_NAME, "product-price").text
            print(f"Package: {name}, Price: {price}")

def main():
    automation = YatraAutomation()
    try:
        automation.automate_yatra()
    finally:
        automation.close_browser()

if __name__ == "__main__":
    main()

