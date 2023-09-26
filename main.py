from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


#sobek

import speech_recognition as sr

rozpoznavac = sr.Recognizer()
otazka=""

with sr.Microphone() as mikrofon:
    print("Say something...")
    audio = rozpoznavac.listen(mikrofon)

try:
    otazka = rozpoznavac.recognize_google(audio, language="en")  
    print(f"Recognized: {otazka}")
except sr.UnknownValueError:
    print("Nerozpoznáno")
except sr.RequestError as e:
    print(f"Chyba při požadavku na rozpoznání: {e}")

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



from gtts import gTTS





language = 'cs'


myobj = gTTS(text=odpoved, lang=language, slow=False)


myobj.save("welcome.mp3")


import pygame

pygame.init()

pygame.mixer.init()

zvuk = pygame.mixer.Sound("welcome.mp3")

zvuk.play()

delka = zvuk.get_length() * 1200
pygame.time.wait(int(delka))

pygame.mixer.quit()
