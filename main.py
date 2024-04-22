""" 
Name: Christopher Tscheschlog 
Student ID: 815262017 
Class: CEN 4072- Software Testing 
Instructor: Dr. Deepa Devasenapathy 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://www.ai-media.tv/")
time.sleep(2)


def test_links_solutions(tabIndex, itemIndex):
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "header-navigation__wrapper")
    
    list_items = navigation_list.find_elements(By.TAG_NAME, "div")
    
    links = list_items[tabIndex].find_elements(By.XPATH, "//a[@class='desktop-navigation-megamenu__link-menu-item']")

    links[itemIndex].click()
    time.sleep(2)
    
def test_links_products(tabIndex, itemIndex):
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "header-navigation__wrapper")
    
    list_items = navigation_list.find_elements(By.TAG_NAME, "div")
    
    links = list_items[tabIndex].find_elements(By.XPATH, "//div[@class='desktop-navigation-megamenu__tab-list']")
    
    print(links[0].get)
    

    buttons = links[0].find_elements(By.XPATH, "//button[@class='desktop-navigation-megamenu__tab-btn']")

    # button = buttons.find_elements(By.TAG_NAME, "button")
    

    # links[itemIndex].click()
    time.sleep(3)

def test_links_why_ai(tabIndex, itemIndex):
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "header-navigation__wrapper")
    
    list_items = navigation_list.find_elements(By.TAG_NAME, "div")
    
    links = list_items[tabIndex].find_elements(By.XPATH, "//a[@class='desktop-navigation-megamenu__link-menu-item']")

    links[itemIndex].click()
    time.sleep(2)
    
def test_links_company(tabIndex, itemIndex):
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "header-navigation__wrapper")
    
    list_items = navigation_list.find_elements(By.TAG_NAME, "div")
    
    links = list_items[tabIndex].find_elements(By.XPATH, "//a[@class='desktop-navigation-megamenu__link-menu-item']")

    links[itemIndex].click()
    time.sleep(2)
    
def test_links_knowledge(tabIndex, itemIndex):
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "header-navigation__wrapper")
    
    list_items = navigation_list.find_elements(By.TAG_NAME, "div")
    
    links = list_items[tabIndex].find_elements(By.XPATH, "//a[@class='desktop-navigation-megamenu__link-menu-item']")

    links[itemIndex].click()
    time.sleep(2)
    
def test_links_upcoming_events(tabIndex, itemIndex):
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "header-navigation__wrapper")
    
    list_items = navigation_list.find_elements(By.TAG_NAME, "div")
    
    links = list_items[tabIndex].find_elements(By.XPATH, "//a[@class='desktop-navigation-megamenu__link-menu-item']")

    links[itemIndex].click()
    time.sleep(2)
            
# Test the navbar links
def test_navbar_links(tabIndex, itemIndex):
    
    # Loop through each li element
    # Find the ul with the specific class
    navigation_list = driver.find_element(By.CLASS_NAME, "desktop-navigation__list")

    # Locate all li elements within the ul
    list_items = navigation_list.find_elements(By.TAG_NAME, "li")
    
    # Find the button within the li element
    button = list_items[tabIndex].find_element(By.CLASS_NAME, "desktop-navigation__menu-link")
    button.click()
    time.sleep(2)
    
    if(tabIndex == 0):
        test_links_solutions(tabIndex, itemIndex)
    elif(tabIndex == 1):
        test_links_products(tabIndex, itemIndex)
    elif(tabIndex == 2):
        test_links_why_ai(tabIndex, itemIndex)
    elif(tabIndex == 3):
        test_links_company(tabIndex, itemIndex)
    elif(tabIndex == 4):
        test_links_knowledge(tabIndex, itemIndex)
    else:
        test_links_upcoming_events(tabIndex, itemIndex)
    
    time.sleep(2)
            

# Run the test solutions links
# for i in range(6):
#     test_navbar_links(0, i) #TODO: test each page as well
#     driver.back()

test_navbar_links(1, 0)

# Close the browser
driver.quit()