from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_gmail_compose_functionality():
    # Replace with the path to your ChromeDriver executable
    PATH = 'chromedriver'

    # Replace with your Gmail credentials
    gmail_username = 'test@gmail.com'
    gmail_password = '9999999999'

    # Replace with the recipient's email address
    recipient_email = 'recipient@gmail.com'

    # Start the Chrome browser
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()

    # Navigate to Gmail
    driver.get('https://mail.google.com/')

    # Log in to Gmail
    driver.find_element(By.NAME, 'identifier').send_keys(gmail_username)
    driver.find_element(By.NAME, 'identifier').send_keys(Keys.RETURN)

    # Wait for password input field to be visible
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))
    )

    # Enter the password
    password_input.send_keys(gmail_password)
    password_input.send_keys(Keys.RETURN)

    # # Wait for the "Compose" button to be visible and click on it
    compose_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Compose']"))
    )
    compose_button.click()


    # Compose the email
    driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys(recipient_email)
    driver.find_element(By.NAME, 'subjectbox').send_keys('Test Email')
    email_body = driver.find_element(By.XPATH, "//div[@role='textbox']")
    ActionChains(driver).move_to_element(email_body).click().send_keys('This is a test email.').perform()

    # Send the email
    driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Send')]").click()

    # Wait for the sent confirmation message
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Message sent')]"))
    )

    # Close the browser
    driver.quit()

# Run the test case
test_gmail_compose_functionality()
