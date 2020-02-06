from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	button = browser.find_element_by_id("book")
	my_text = WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"),"$100")
		)
	button.click()

	input1 = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
	input1.send_keys(calc(browser.find_element_by_id("input_value").text))
	button = browser.find_element_by_id("solve")
	button.click()
	time.sleep(5)
	alert = browser.switch_to.alert	
	alert.accept()
	
finally:
	time.sleep(3)
	browser.quit()
