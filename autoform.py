from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path="C:\\Users\\Sahil\\Desktop\\chromedriver.exe", options=option)
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSdYSO0HOL67xQAR07FQoW8JZYQAzMUJkY3DlZK4y1SiRh3vtw/viewform')

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
submit=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
textboxes[0].send_keys("Sahil Mula")
textboxes[1].send_keys("21")
textboxes[2].send_keys("sahil.mulla@mmit.edu.in")
radio_buttons[1].click()
submit.click()