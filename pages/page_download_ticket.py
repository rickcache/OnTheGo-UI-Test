from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
import os
import time

class Download:
    
    def __init__(self, driver):
        self.driver = driver
        self.download_path = (By.XPATH, '/html/body/div[2]/div/div/div[1]/table/tbody/tr/td[11]/a')
        # download directory from conftest
        self.download_dir = os.path.join(os.getcwd(), "downloads")
    
    def download(self):
        download_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.download_path)
        )
        download_btn.click()
        
    def verify_file(self, filename, timeout=10):
        """Check if file exists in download folder"""
        file_path = os.path.join(self.download_dir, filename)
        for _ in range(timeout):
            if os.path.exists(file_path):
                return True
            time.sleep(1)
        return False        