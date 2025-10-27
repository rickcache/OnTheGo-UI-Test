from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Trending_Deals:
    def __init__(self, driver):
        self.driver = driver
        self.trending_page_path = (By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a')
        
        
    def trending_page(self):
        wait = WebDriverWait(self.driver, 10)
        
        trending_page = wait.until(EC.element_to_be_clickable(self.trending_page_path))
        trending_page.click()
        
        for i in range(1, 5):
            
            deal_card = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div/div[{i}]')))
            
            actions = ActionChains(self.driver)
            actions.move_to_element(deal_card).perform()
            
            book_button = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[2]/div/div/div[{i}]/div/div/a')))
            book_button.click()
            
            #test takes place
            assert " Book Your Ticket" in self.driver.page_source
            
            #Goes back to the Trending deals page
            self.driver.back()
           
            wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div/div[{i}]')))
   