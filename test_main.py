""" 
Name: Christopher Tscheschlog 
Student ID: 815262017 
Class: CEN 4072- Software Testing 
Instructor: Dr. Deepa Devasenapathy 
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="class")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    web_driver = webdriver.Chrome(options=options)
    web_driver.get("https://www.ai-media.tv")
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()

@pytest.mark.usefixtures("driver")
class TestNavBarLinks:
    
    def reopen_navbar(self, tabIndex):
        navigation_list = self.driver.find_element(By.CLASS_NAME, "desktop-navigation__list")
        list_items = navigation_list.find_elements(By.TAG_NAME, "li")
        button = list_items[tabIndex].find_element(By.CLASS_NAME, "desktop-navigation__menu-link")
        button.click()
        time.sleep(2)

    @pytest.mark.parametrize("tabIndex, itemIndex", [
        # Solutions Tab
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        # Products Tab
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (1, 10), (1, 11), (1, 12), 
        (1, 20), (1, 21), (1, 22), 
        (1, 30), (1, 31), (1, 32), (1, 33), (1, 34), 
        (1, 40), (1, 41), 
        # Why Ai-Media Tab
        (2, 0), 
        # Company Tab
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), 
        # Knowledge Tab
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
        (4, 10), (4, 11), (4, 12), (4, 13), (4, 14),
        (4, 20), (4, 21), (4, 22),
        (4, 30), (4, 31),
        # Upcoming Events Tab
        (5, 0) 
    ])
    def test_links(self, tabIndex, itemIndex):
        self.reopen_navbar(tabIndex)
        if tabIndex == 0:
            self.try_links_solutions(tabIndex, itemIndex)
        elif tabIndex == 1:
            self.try_links_products(tabIndex, itemIndex)
        elif tabIndex == 2:
            self.try_links_why_ai(tabIndex, itemIndex)
        elif tabIndex == 3:
            self.try_links_company(tabIndex, itemIndex)
        elif tabIndex == 4:
            self.try_links_knowledge_hub(tabIndex, itemIndex)
        else:
            self.try_links_upcoming_events(tabIndex, itemIndex)
        time.sleep(2)

    
    def try_links_solutions(self, tabIndex, itemIndex):
        # Find the ul with the specific class
        wait = WebDriverWait(self.driver, 10)
        navigation_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-navigation__wrapper")))
        
        list_items = navigation_list.find_elements(By.TAG_NAME, "div")
        
        links = list_items[tabIndex].find_elements(By.XPATH, "//a[@class='desktop-navigation-megamenu__link-menu-item']")

        links[itemIndex].click()
        time.sleep(2)
        pass
        
    def try_links_products(self, tabIndex, itemIndex): # tens place for sidebar, ones for paragraphs & overview
        # Waiting for the sidebar to load completely
        wait = WebDriverWait(self.driver, 10)
        sidebar_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "desktop-navigation-megamenu__navigation-menu-side-container")))

        # Find all buttons within the sidebar
        buttons = sidebar_container.find_elements(By.CLASS_NAME, "desktop-navigation-megamenu__tab-btn")
        
        buttons[(int)(itemIndex/10)].click()
        
        def get_chosen_id(index):
            match index:
                case 0:
                    return "tabbed-navigation-lexi_ai-powered_tool_kit-0"
                case 1:
                    return "tabbed-navigation-caption_delivery-1"
                case 2:
                    return "tabbed-navigation-caption_display-2"
                case 3:
                    return "tabbed-navigation-caption_services-3"
                case 4:
                    return "tabbed-navigation-icap_cloud_network-4"
        
        time.sleep(2)
        def choosen_item(tab, index): 
            item = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='45585b1e88746c3bee607b6151c0404d']")))
            item = item.find_element(By.XPATH, f"//div[@id='{get_chosen_id((tab))}']")
            
            match index:
                case 0: 
                    item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-top")
                    item = item.find_element(By.TAG_NAME, "a") 
                    return item
                case _:
                    item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-bottom")
                    item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-bottom-detail")
                    item = item.find_elements(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-bottom-link")[index - 1]
                    return item

        
        option = choosen_item((int)(itemIndex/10), itemIndex % 10)
        print(option.get_attribute('innerHTML'))
        
        option.click()
        
        time.sleep(2)
        pass

    def try_links_why_ai(self, tabIndex, itemIndex):
        # Find the ul with the specific class
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='7ca8a566c0a1cf7d44b304961acc8054']")))
 
        item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__list")
        item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__link-menu-container")
        item = item.find_element(By.TAG_NAME, "a")
        
        print(item.get_attribute('innerHTML'))
        item.click()       
 
        time.sleep(2)
        pass
        
    def try_links_company(self, tabIndex, itemIndex):
        # Find the ul with the specific class
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='677cfc22318e748edb66a17dbbf4d92b']")))
        
        item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__list")
        item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__link-menu-container")
        
        item = item.find_elements(By.TAG_NAME, "a")[itemIndex]
        
        print(item.get_attribute('innerHTML'))
        
        if itemIndex != 0:
            item.click()
        else:
            item.click()
            time.sleep(2)
            self.driver.back()
    
        time.sleep(2)
        pass
        
    def try_links_knowledge_hub(self, tabIndex, itemIndex):
        
        wait = WebDriverWait(self.driver, 20)
        sidebar_container = wait.until(EC.visibility_of_element_located((By.ID, "ea2583efcb7ebbe9e521b3ba09733ce5")))
        sidebar_container = sidebar_container.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__list")
        sidebar_container = sidebar_container.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__navigation-menu-side-container")
        sidebar_container = sidebar_container.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-list")

        # Find all buttons within the sidebar
        buttons = sidebar_container.find_elements(By.TAG_NAME, "button")
        
        buttons[(int)(itemIndex/10)].click()
        
        def get_chosen_tab(index):
            match index:
                case 0:
                    return "tabbed-navigation-insights-0"
                case 1:
                    return "tabbed-navigation-technical_documentation-1"
                case 2:
                    return "tabbed-navigation-downloads-2"
                case 3:
                    return "tabbed-navigation-faqs-3"
        
        time.sleep(2)
        def choosen_item(tab, index): 
            item = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='ea2583efcb7ebbe9e521b3ba09733ce5']")))
            item = item.find_element(By.XPATH, f"//div[@id='{get_chosen_tab((tab))}']")
                        
            match index:
                case 0: 
                    item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-top")
                    item = item.find_element(By.TAG_NAME, "a") 
                    return item
                case _:
                    item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-bottom")
                    item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-bottom-detail")
                    item = item.find_elements(By.CLASS_NAME, "desktop-navigation-megamenu__tab-pane-bottom-link")[index - 1]
                    return item

        
        option = choosen_item((int)(itemIndex/10), itemIndex % 10)
        print(option.get_attribute('innerHTML'))
        
        option.click()
        if itemIndex == 14 or itemIndex == 22:
            time.sleep(3)
            self.driver.back()            
        
        time.sleep(2)
        pass
        
    def try_links_upcoming_events(self, tabIndex, itemIndex):
         # Waiting for the sidebar to load completely
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='d0a30f45a24b4215830f75bfa2fec499']")))
        
        item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__list")
        item = item.find_element(By.CLASS_NAME, "desktop-navigation-megamenu__link-menu-container")
        
        item = item.find_elements(By.TAG_NAME, "a")[itemIndex]
        item.click()
        
        time.sleep(2)
        pass
        
    def reopen_navbar(self, tabIndex):
        # Loop through each li element
        # Find the ul with the specific class
        wait = WebDriverWait(self.driver, 10)
        navigation_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "desktop-navigation__list")))

        # Locate all li elements within the ul
        list_items = navigation_list.find_elements(By.TAG_NAME, "li")
        
        # Find the button within the li element
        button = list_items[tabIndex].find_element(By.CLASS_NAME, "desktop-navigation__menu-link")
        button.click()
        time.sleep(2)
        pass

# To run a test
if __name__ == "__main__":    
    
    test_instance = TestNavBarLinks()
    
