from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def downloadReport(driver):
	download_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]/div[1]/div/div[3]/button')))
	download_button.click()

	selectall_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="columnName__undefined"]')))
	selectall_button.click()

	downloadfinal = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]/div[2]/div[2]/div/div[3]/div[4]/div/button')))
	downloadfinal.click()

	circle_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "svg-circle")))
	circle_button.click()


def closePopUp(driver):
	close_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]/div/span/span/span')))
	close_button.click()


def login(driver, page, username, password):
	driver.get(page)

	input_box = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "text-field")))
	input_box.send_keys(username)

	submit_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "EnterEmailFormFilled")))
	submit_button.click()

	pass_box = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "text-field")))
	pass_box.send_keys(password)

	login_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "LoginFormFormFilled")))
	login_button.click()

def main():
	driver = webdriver.Chrome()
	driver.maximize_window()

	page = "https://onboarding.payu.in/app/account"
	username = "info.ammucare@gmail.com"
	password = "Actcare@2020"

	login(driver, page, username, password)
	closePopUp(driver)
	downloadReport(driver)
	time.sleep(10)
	driver.quit()


if __name__=="__main__":
    main()
