from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Booking:
    def __init__(self, driver):
        self.driver = driver
        self.booking_page_path = (By.XPATH, '/html/body/div[2]/div/div/a[3]')
        self.no_ticket = (By.XPATH, '//*[@id="bookingForm"]/div[2]/input')
        self.types =  (By.XPATH, '//*[@id="bookingForm"]/div[3]/div[2]/input') #interational
        self.destination = (By.XPATH, '//*[@id="destinationSelect"]')
        self.date_in     = (By.XPATH, '//*[@id="travelDate"]')
        self.ticket_class = (By.XPATH, '//*[@id="bookingForm"]/div[6]/div[2]/input') #business
        self.food        = (By.XPATH, '//*[@id="bookingForm"]/div[7]/div[3]/input') #egg
        self.add_ons     = (By.XPATH, '//*[@id="bookingForm"]/div[8]/div[1]/input') #lounge
        self.proceed_btn = (By.XPATH, '//*[@id="bookingForm"]/div[10]/button')
        
    def booking(self):
        wait = WebDriverWait(self.driver, 10)
        
        booking_page = wait.until(EC.visibility_of_element_located((self.booking_page_path)))
        booking_page.click()
        
        
        no_of_tickets = wait.until(EC.presence_of_element_located((self.no_ticket)))
        no_of_tickets.clear()
        no_of_tickets.send_keys(2)
        
        ticket_type = wait.until(EC.visibility_of_element_located((self.types)))
        ticket_type.click()
        
        dropdown_destination = Select(wait.until(EC.visibility_of_element_located((self.destination))))
        dropdown_destination.select_by_visible_text("Japan")
        
        date_input = wait.until(EC.visibility_of_element_located((self.date_in)))
        date_input.send_keys("29102025")
        
        ticket_class = wait.until(EC.presence_of_element_located((self.ticket_class)))
        ticket_class.click()
        
        food_pref = wait.until(EC.presence_of_element_located((self.food)))
        food_pref.click()
        
        add_ons_pref = wait.until(EC.presence_of_element_located((self.add_ons)))
        add_ons_pref.click()
        
        proceed = wait.until(EC.presence_of_element_located((self.proceed_btn)))
        proceed.click()
        