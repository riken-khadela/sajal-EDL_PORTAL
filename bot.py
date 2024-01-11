from audioop import avg
import random, time, os, json
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


import random, time
def random_sleep(a=5,b=9):
    time.sleep(random.randint(a,b))
    
chromedriver_path = os.path.join(os.getcwd(),'chromedriver')
chrome_binary_path = '/usr/bin/google-chrome'
class Bot():
    def __init__(self) :
        self.get_local_driver()
        self.work()
    def return_driver(self) : 
        self.get_driver() 
        return self.check_login() 

    def get_local_driver(self):
        """Start webdriver and return state of it."""
        from selenium import webdriver

        for _ in range(30):
            options = webdriver.ChromeOptions()
            options.add_argument('--lang=en')  # Set webdriver language to English.
            options.add_argument('log-level=3')  # No logs is printed.
            options.add_argument('--mute-audio')  # Audio is muted.
            options.add_argument("--enable-webgl-draft-extensions")
            options.add_argument('--mute-audio')
            options.add_argument("--ignore-gpu-blocklist")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--headless')
            prefs = {"credentials_enable_service": True,
                    'profile.default_content_setting_values.automatic_downloads': 1,
                'download.prompt_for_download': False,  # Optional, suppress download prompt
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True ,
                "profile.password_manager_enabled": True}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--no-sandbox')
            options.add_argument('--start-maximized')    
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--enable-javascript")
            options.add_argument("--enable-popup-blocking")
            try:
                driver = webdriver.Chrome()
                driver.get('https://www.google.com')
                break
            except Exception as e:
                print(e)
        
        self.driver = driver
        return self.driver
    
    def get_driver(self):
        """Start webdriver and return state of it."""
        for _ in range(30):
            """Start webdriver and return state of it."""
            from undetected_chromedriver import Chrome, ChromeOptions
            options = ChromeOptions()
            options.add_argument('--lang=en')  # Set webdriver language to English.
            options.add_argument('log-level=3')  # No logs is printed.
            options.add_argument('--mute-audio')  # Audio is muted.
            options.add_argument("--enable-webgl-draft-extensions")
            options.add_argument('--mute-audio')
            options.add_argument("--ignore-gpu-blocklist")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--headless')
            prefs = {"credentials_enable_service": True,
                    'profile.default_content_setting_values.automatic_downloads': 1,
                'download.prompt_for_download': False,  # Optional, suppress download prompt
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True ,
                "profile.password_manager_enabled": True}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--no-sandbox')
            options.add_argument('--start-maximized')    
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--enable-javascript")
            options.add_argument("--enable-popup-blocking")
            try:
                driver = Chrome(options=options,version_main=119,headless=False)
                driver.get('https://www.google.com')
                break
            except Exception as e:
                print(e)
        
        self.driver = driver
        return self.driver
    
        
    def find_element(self, element, locator, locator_type=By.XPATH,
            page=None, timeout=10,
            condition_func=EC.presence_of_element_located,
            condition_other_args=tuple()):
        """Find an element, then return it or None.
        If timeout is less than or requal zero, then just find.
        If it is more than zero, then wait for the element present.
        """
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                ele = wait_obj.until(EC.presence_of_element_located((locator_type, locator)))
                # ele = wait_obj.until( condition_func((locator_type, locator),*condition_other_args))
            else:
                print(f'Timeout is less or equal zero: {timeout}')
                ele = self.driver.find_element(by=locator_type,
                        value=locator)
            if page:
                print(
                    f'Found the element "{element}" in the page "{page}"')
            else:
                print(f'Found the element: {element}')
            return ele
        except Exception as e:
            if page:
                print(f'Cannot find the element "{element}"'
                        f' in the page "{page}"')
            else:
                print(f'Cannot find the element: {element}')
                
    def click_element(self, element, locator, locator_type=By.XPATH,
            timeout=10):
        """Find an element, then click and return it, or return None"""
        ele = self.find_element(element, locator, locator_type, timeout=timeout)
        
        if ele:
            self.driver.execute_script('arguments[0].scrollIntoViewIfNeeded();',ele)
            self.ensure_click(ele)
            print(f'Clicked the element: {element}')
            return ele

    def input_text(self, text, element, locator, locator_type=By.XPATH,
            timeout=10, hide_keyboard=True):
        """Find an element, then input text and return it, or return None"""
        
        ele = self.find_element(element, locator, locator_type=locator_type,
                timeout=timeout)
        
        if ele:
            for i in range(3):
                try: 
                    ele.clear()
                    ele.send_keys(text)
                    print(f'Inputed "{text}" for the element: {element}')
                    return ele    
                except  :...
    
    def ScrollDown(self,px):
        self.driver.execute_script(f"window.scrollTo(0, {px})")

    def ensure_click(self, element, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
            element.click()
        except :
            self.driver.execute_script("arguments[0].click();", element)
    
    def new_tab(self):
        self.driver.find_element(By.XPATH,'/html/body').send_keys(Keys.CONTROL+'t')

    def random_sleep(self,a=3,b=7):
        import time, os
        random_time = random.randint(a,b)
        print('time sleep randomly :',random_time)
        time.sleep(random_time)

    def getvalue_byscript(self,script = '',reason=''):
        """made for return value from ele or return ele"""
        if reason :print(f'Script execute for : {reason}')
        else:
            print(f'execute_script : {script}')
        value = self.driver.execute_script(f'return {script}')  
        return value
    


    def CloseDriver(self):
        try: 
            self.driver.quit()
            print('Driver is closed !')
        except Exception as e: ...

        
    def TestRunDriver(self,driver : webdriver):
        self.driver = driver
        try :
            self.driver.current_url
            return True
        except : return False

    def close_others_tab(self):
        for window in self.driver.window_handles[1:]:
                self.driver.switch_to.window(window)
                self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        ...
    
    def work(self):
        self.driver.get('https://div.edl.ch/auth/auth/engine/UsernamePassword?set_new_language=en')
        # beag_barr
        # P4r1s13nn3!86
        self.input_text('beag_barr','username','username',By.ID)
        self.input_text('P4r1s13nn3!86','password','password',By.ID)
        self.click_element('submitbutton','submitbutton',By.ID)
        breakpoint()

    
bb = Bot()
bb.get_local_driver()
bb.work()