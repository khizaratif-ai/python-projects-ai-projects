from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebAutomation:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self, username, password):
        self.driver.get("https://demoqa.com/login")

        username_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "userName"))
        )
        password_box = self.driver.find_element(By.ID, "password")

        username_box.clear()
        password_box.clear()

        username_box.send_keys(username)
        password_box.send_keys(password)

        login_btn = self.driver.find_element(By.ID, "login")
        self.driver.execute_script("arguments[0].click();", login_btn)

        # Wait until login completes
        self.wait.until(EC.url_contains("profile"))

    def fill_form(self, fullname, email, current_address, permanent_address):

        # Go directly to Text Box page
        self.driver.get("https://demoqa.com/text-box")

        fullname_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "userName"))
        )

        email_box = self.driver.find_element(By.ID, "userEmail")
        current_box = self.driver.find_element(By.ID, "currentAddress")
        permanent_box = self.driver.find_element(By.ID, "permanentAddress")

        fullname_box.send_keys(fullname)
        email_box.send_keys(email)
        current_box.send_keys(current_address)
        permanent_box.send_keys(permanent_address)

        submit_btn = self.driver.find_element(By.ID, "submit")

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            submit_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit_btn
        )

    def close(self):
        if self.driver:
            self.driver.quit()