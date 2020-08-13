from selenium import webdriver
import time 
#Fill the respective details below 
LoginIdText = ""
PasswordText = ""
Q1 = ""
Q1Password = ''
Q2 = ""
Q2Password = ''
Q3 = ""
Q3Password = ''

driver = webdriver.Chrome()
driver.get("https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=76F38FD63E4B1BA060D874AECB818BAE.worker3&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/")
LoginId = driver.find_element_by_xpath('//*[@id="user_id"]')
LoginId.send_keys(LoginIdText)
Password = driver.find_element_by_xpath('//*[@id="password"]')
Password.send_keys(PasswordText)
time.sleep(1)
QuestionInput = driver.find_element_by_xpath('//*[@id="answer"]')
Question = driver.find_element_by_xpath('//*[@id="question"]').text
if Question == Q1:
    QuestionInput.send_keys(Q1Password)
elif Question==Q2:
    QuestionInput.send_keys(Q2Password)
elif Question==Q3:
    QuestionInput.send_keys(Q3Password)
Submit = driver.find_element_by_xpath('//*[@id="signin"]/div/div/div/div/form/fieldset/div[4]/div/input[3]')
Submit.click()    


