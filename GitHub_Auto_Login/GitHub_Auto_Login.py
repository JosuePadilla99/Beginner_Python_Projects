####################################################### 
# Auto Login Bot for GitHub
# Creation Date: 12/06/2024 
# Creator: Josue Padilla 
#######################################################  

import time 
from selenium import webdriver  
from selenium.webdriver.common.by import By  
#from selenium.webdriver.chrome.options import Options

    
def login(url, username, password):   
    #options = Options() 
    #options.add_experimental_option('detach', True)
    driver = webdriver.Chrome()#(options=options)
    driver.get(url)
    driver.maximize_window()  
    time.sleep(2)
    user_name_field = driver.find_element(By. ID, 'login_field')
    print('Finding username block') 
    time.sleep(2)
    user_name_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')  
    print('Finding password block') 
    time.sleep(2)
    password_field.send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, "input[value='Sign in']")  
    print('Signing in') 
    login_button.click() 
    input('Press enter to close the browser')  
    driver.close() 

if __name__ == '__main__': 
    url = 'https://github.com/login' 
    user_name = 'JosuePadilla99' 
    pwd = 'Devinbookermvp4!' 
    login(url, user_name, pwd)
    
    
    

