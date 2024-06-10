#makemytrip_automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakeMyTripAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    def close_browser(self):
        self.driver.quit()

    def automate_makemytrip(self):
        self.driver.get("https://www.makemytrip.com/")
        assert "MakeMyTrip" in self.driver.title

        # Close the login popup if it appears
        try:
            close_popup = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'langCardClose')]"))
            )
            close_popup.click()
        except:
            pass

        # Navigate to Offers
        offers_link = self.driver.find_element(By.LINK_TEXT, "Offers")
        offers_link.click()
        WebDriverWait(self.driver, 10).until(EC.title_contains("MakeMyTrip Offers"))
        assert "MakeMyTrip Offers" in self.driver.title

        # Take screenshot
        self.driver.save_screenshot('makemytrip_offers_page.png')

        # Navigate to Holiday Packages
        holidays_link = self.driver.find_element(By.LINK_TEXT, "Holidays")
        holidays_link.click()

        # List five holiday packages
        packages = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "makeFlex")))
        for package in packages[:5]:
            try:
                name = package.find_element(By.CLASS_NAME, "packageTitle").text
                price = package.find_element(By.CLASS_NAME, "blackText").text
                print(f"Package: {name}, Price: {price}")
            except:
                continue

def main():
    automation = MakeMyTripAutomation()
    try:
        automation.automate_makemytrip()
    finally:
        automation.close_browser()

if __name__ == "__main__":
    main()

