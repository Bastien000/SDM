from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time




import speech_recognition as sr

rozpoznavac = sr.Recognizer()
otazka=" hello how are you"





options = Options()
#  options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.deepl.com/translator")
driver.maximize_window()
time.sleep(1)
links = driver.find_elements("xpath", "//button[@class]")
for link in links: 
	if "Přijmout" in link.get_attribute("innerHTML"):         #změnit příjmout na accept
		link.click()
		
   #načtení bota
links = driver.find_elements("xpath", "//d-textarea[@class]")
for link in links: 

	link.send_keys(otazka)
	break



time.sleep(5)
texts = driver.find_elements("xpath","//span[@_d-id]")
preklad=[]

for text in texts:
	preklad.append(text.get_attribute("innerHTML"))
			
del preklad[0]

odpoved=""
for i in preklad:
	odpoved = odpoved + " " + i

print(odpoved)

