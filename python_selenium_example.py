import json
import os
from dotenv import load_dotenv
import deathbycaptcha
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Load environment variables from .env file
load_dotenv()

USERNAME = os.getenv('DBC_USERNAME')  # Your DBC username from .env
PASSWORD = os.getenv('DBC_PASSWORD')  # Your DBC password from .env
CAPTCHA_URL = 'https://www.google.com/recaptcha/api2/demo'


def solve_captcha(captcha: dict):
    json_captcha = json.dumps(captcha)
    client = deathbycaptcha.SocketClient(USERNAME, PASSWORD)

    try:
        # First let's check our balance (not needed though)
        balance = client.get_balance()
        print('Balance: %s' % balance)

        print('Solving captcha...')
        client.is_verbose = True
        result = client.decode(type=4, token_params=json_captcha)

        return result.get('text')

    except Exception as e:
        print(f'DeathByCaptcha error: {e}')
        return None


def main():
    if not USERNAME or not PASSWORD:
        print('Missing credentials. Please set DBC_USERNAME and DBC_PASSWORD in .env')
        return

    # Configure Firefox options for local and GitHub Actions usage
    firefox_options = webdriver.FirefoxOptions()

    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    force_headless = os.getenv('HEADLESS', '0') == '1'
    run_headless = is_github_actions or force_headless

    if run_headless:
        print('Running in headless mode')
        firefox_options.add_argument('--headless')

    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-dev-shm-usage')

    # Use a longer timeout in CI/headless mode
    wait_timeout = 30 if run_headless else 10
    print(f'Using wait timeout: {wait_timeout} seconds')
    
    with webdriver.Firefox(options=firefox_options) as driver:  # using firefox
    # with webdriver.Chrome() as driver:  # using Chrome
        driver.set_page_load_timeout(60)
        
        print(f'Navigating to {CAPTCHA_URL}...')
        driver.get(CAPTCHA_URL)
        
        try:
            print('Looking for recaptcha-demo element...')
            element: WebElement = WebDriverWait(driver, wait_timeout).until(
                EC.presence_of_element_located((By.ID, "recaptcha-demo"))
            )
            print('Element found')
        except Exception as e:
            print(f'Error finding element: {e}')
            return
        
        googlekey = element.get_attribute('data-sitekey')
        
        if not googlekey:
            print('Trying alternative method to get sitekey...')
            googlekey = driver.execute_script(
                "return document.getElementById('recaptcha-demo').getAttribute('data-sitekey')"
            )
        
        print('GoogleKey: %s' % googlekey)
        
        if not googlekey:
            print('ERROR: Could not extract sitekey from page')
            return
        
        captcha = {     # not using proxy in this example
            'googlekey': googlekey,
            'pageurl': CAPTCHA_URL}
        
        solution = solve_captcha(captcha)
        if not solution:
            print('No captcha solution (maybe implement retry)...closing')
            return
        
        print('Solution: %s' % solution)
        driver.execute_script(
            "document.getElementById('g-recaptcha-response').value='%s'" % solution
        )
        
        # Click on Check button
        check_button = driver.find_element(By.ID, 'recaptcha-demo-submit')
        check_button.click()
        
        # Wait a bit for the response
        time.sleep(2)
        
        # Check if success
        try:
            success_element = driver.find_element(By.CLASS_NAME, "recaptcha-success")
            print('SUCCESS: %s' % success_element.text)
        except NoSuchElementException as e:
            print("Success message not found: %s" % str(e))


if __name__ == '__main__':
    main()
