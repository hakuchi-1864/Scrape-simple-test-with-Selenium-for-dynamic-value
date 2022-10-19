from selenium import webdriver
# allow us to instruct the behaviour of the web browser


def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")  #maximed web browser
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://py4e-data.dr-chuck.net/regex_sum_42.txt")
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/pre")
  return element.text


print(main())
