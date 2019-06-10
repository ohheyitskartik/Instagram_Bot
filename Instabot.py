"""
 * @author      Kartik Rana
 * @license     MIT
 * @description Instagram Bot for following user's.
 * @requires    Python, Selenium
 * @see         https://github.com/ohheyitskartik/Instagram_Bot
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()


# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome (chrome_options=option)

# Defined ActionChains for Page Down movement
actions = ActionChains(browser)

#----------------------------------------------------------------------
#----------------------------------------------------------------------

# The number of followers you want to follow
follow_count = 20
# Login Email ID for Instagram
Login_Email = ("here")
# Login Password for Instagram
Login_password = ("here")
# Link of the page you want to follow users from
Instapage_link = ("https://www.instagram.com/ghantaa69")

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

print("Initializing Insta Bot.....")

# Go to desired website
browser.get("https://www.instagram.com/accounts/login/?hl=en")
print("Loading Instagram Login Page..")

browser.implicitly_wait(10)

emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]
emailInput.send_keys(Login_Email)
passwordInput.send_keys(Login_password)
passwordInput.send_keys(Keys.ENTER)
print("LoggedIn to Instagram")
time.sleep(4)

browser.get(Instapage_link)
print("Loading Insta Target Page..")
time.sleep(4)

# Xpath for followers link on the instapage page
follower = browser.find_element_by_xpath("//a[contains(@href, '/ghantaa69/followers/')]")
follower.click()
print("Loading Followers list..")

time.sleep(4)


position=1
for _ in range(10):
    position_var = str(position)
   
    # !!!! Scrolls thru the followers list using page down key, to make all elements visible on the list
    # !!!! And to avoid suggestions list while getting elements
    # Xpath for each user box in follower list (use = Position variable,to fit xpath for all users) 
    browser.find_element_by_xpath("//div/li["+position_var+"]/div").click()
    actions.send_keys(Keys.PAGE_DOWN).perform()
    
    # Gets value for every 7th in view user due to large scroll jumps
    position +=7
    print("Scrolling to get all elements")
    time.sleep(1)

time.sleep(2)
print("Starting Itration")
count=0
itration=1
while count < follow_count:
    itration_val= str(itration)
    print("Itration count = ",itration_val)
    
    # Xpath for follow button in follower list (use = Itration_value to fit xpath for all follow buttons)
    followers_num=browser.find_element_by_xpath("(//button[@type='button'])["+itration_val+"]")
    if (followers_num.text == "Follow"):
        followers_num.click()
        
        # Xpath for each user box in follower list (use = Itration_value,to fit xpath for all users)
        # Get the user into view so that the element is visusal 
        element = browser.find_element_by_xpath("//div/li["+itration_val+"]/div")
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        
        # Checks if the user is not already followed or requested , and follow only the new users
        print("Follow count = ",count)
        count +=1
        itration +=1
        time.sleep(2)


    else:
        # Xpath for each user box in follower list (use = Itration_value,to fit xpath for all users)
        # Get the user into view so that the element is visusal
        element = browser.find_element_by_xpath("//div/li["+itration_val+"]/div")
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        browser.execute_script("window.scrollTo(0, 100);")
        time.sleep(2)
        itration +=1
    
print("Task finished succesfully. ", count, " New user's followed - Insta bot || Developed by Kartik Rana")
# Un-comment this to automatically close the browser window after the test is done
#browser.close()
    
    