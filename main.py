#importing all necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import speech_recognition as sr



#initializing library speech_recognition
recognizer_variable = sr.Recognizer()

#empty string variable
question=""


#setting up microphone and listening to user speaking
with sr.Microphone() as microphone:
    print("Say something...")
    audio = recognizer_variable.listen(microphone)
#The try block lets you test a block of code for errors.
try:
    question = recognizer_variable.recognize_google(audio, language="en")  
    print(f"Recognized: {question}")
#The except block lets you handle the error.
except sr.UnknownValueError:
    print("Unrecognized")
except sr.RequestError as e:
    print(f"Error with requesting recognition: {e}")
#setting up options() as variable
options = Options()
#  options.add_experimental_option("detach", True)   <-------idk whe he put this here xD

#creates a new instance of the chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

#loads web
driver.get("https://www.deepl.com/translator")
driver.maximize_window()
#puts the program to sleep for 1 second
time.sleep(1)
#finding any button in html code
links = driver.find_elements("xpath", "//button[@class]")
#creating a cycle that finds all buttons that has "accept" on and then clicks on them (for cookies pop up)
for link in links: 
	if "Přijmout" in link.get_attribute("innerHTML"):         # přijmout = accept (clicking on cookies accept pop up window)
		link.click()
		
   #loading bot
links = driver.find_elements("xpath", "//d-textarea[@class]") #finds text area
for link in links: #cycle

	link.send_keys(question) # puts the question of the user to the text area
	break # breaks the cycle



time.sleep(5)
texts = driver.find_elements("xpath","//span[@_d-id]") # finds the translated question
translation=[]  #creating translation list

for text in texts: #cycle
	translation.append(text.get_attribute("innerHTML"))  #adds the text to list
			
del translation[0]  #deleting something unnecessary

answer=""  #creating empty string
for i in translation:   #cycle for every object in list it will do below:
	answer = answer + " " + i  #adds to string the current object in that specific cycle and adds "  " 
	#(spaces between them) and saves them

print(answer)  #show answer in terminal



from gtts import gTTS     #importing library that can create mp3 files





language = 'cs'


myobj = gTTS(text=answer, lang=language, slow=False)


myobj.save("welcome.mp3")


import pygame  #importing library that can play mp3 files

pygame.init()

pygame.mixer.init()

sound = pygame.mixer.Sound("welcome.mp3")   

sound.play()  #playing sound

delka = sound.get_length() * 1200
pygame.time.wait(int(delka))  #waiting before sound ends then quits

pygame.mixer.quit() 
