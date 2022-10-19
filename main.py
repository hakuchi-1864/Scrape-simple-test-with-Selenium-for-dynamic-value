from selenium import webdriver
# allow us to instruct the behaviour of the web browser

import time #to get dynamic value

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")  #maximed web browser
  options.add_argument("disable-dev-shm-usage")
  # avoid some issue when you use linux web browser
  options.add_argument("no-sandbox")
  #browser for security use sandboxing if we want our scripts to have greater privileges on that particular web page
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  # 15 and 16 that help selenium to avoid detection from the web browse
  # we need to provide options above->20 and now empty
  driver = webdriver.Chrome(options=options)
  # we need to connect it a web page
  driver.get("http://automated.pythonanywhere.com/")

  return driver

# we want to extract only number to do this
def clean_text(text):
  """"Exctract only the temperature from the text"""
  output= float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(4)
  # to get extract from the web page
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  # we say we want to acces value, using xpath 
  return clean_text(element.text)

print(main())
