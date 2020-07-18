from selenium import webdriver
import time
import sys

driver = webdriver.Firefox(executable_path= './geckodriver')

try:
        #command line arguments
	emails = sys.argv[1:]
	for email in emails:
		driver.get('https://haveibeenpwned.com/')
		email_input = driver.find_element_by_id('Account')
		email_input.send_keys(email)
		driver.find_element_by_id('searchPwnage').click()
		time.sleep(3)
		result_negative = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div[1]/h2').text 
		result_positive = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/h2').text
		breached_website = driver.find_elements_by_class_name('pwnedCompanyTitle')
		compromised_data = driver.find_elements_by_class_name('dataClasses')
		print(email)
		print(result_negative+result_positive)
		for i,j in zip(breached_website,compromised_data):
			print('breached website:'+i.text)
			print(j.text)
		print('')
		print('')

except Exception as e:
	print(e)
	#closes the browser
	driver.quit()

