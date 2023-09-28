import time
import pyautogui
from translate import Translator
import speech_recognition as sr
from gtts import gTTS
import pygame

#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System

recog1 = sr.Recognizer()
mc = sr.Microphone()

jazyky={"en":"english","cs":"check","de":"german"} #check je proto protože to neumí

langInput="en"
MyText = ""
def Jarvisteposloucha():
    while True:
        time.sleep(1)
        print("adsfadfa")
        with mc as source:
            print("Start")
            recog1.adjust_for_ambient_noise(source,) 
            print("adsfadfa")
            
            audiojarvis = recog1.listen(source)
            print("adsfadfa")
        print("adsfadfa")
           
        try: 
            print("adsfadfa")

            MyText = recog1.recognize_google(audiojarvis, language=langInput,)
            print("adsfadfa")

        except sr.UnknownValueError:
            print("Error")
        else:
            MyText=MyText.lower()
            print(MyText)
            listening(MyText)
            break

def listening(text):
    if 'jarvis' in text or 'jarvisy' in text or 'jarvi' in text or 'jarv' in text or "john lewis" in text or "artemis" in text or "chatteris" in text or "jura whisky" in text:	
        with mc as source:
            print("Listening")
            recog1.adjust_for_ambient_noise(source, duration=0.2)
            #recog1.listen(source=source,phrase_time_limit=0.2,timeout=0.5,)
            audiolistening = recog1.listen(source)

        try:
            get_sentence = recog1.recognize_google(audiolistening, language=langInput)  
            print(f"Recognized: {get_sentence}")
            
            translator = Translator(to_lang="en", from_lang=langInput)  
            translated_text = translator.translate(get_sentence)


            if "change language" in translated_text.lower() or "change your language" in translated_text.lower() or "change the language" in translated_text.lower():
                changelanguage()
            else:
                gptodpoved(translated_text)
        except sr.UnknownValueError:
            print("Do not recognized")
            Jarvisteposloucha()
        except sr.RequestError as e:
            print(f"Chyba při požadavku na rozpoznání: {e}")
            Jarvisteposloucha()
        
        
    else:
        Jarvisteposloucha()
    
def changelanguage():

    #přehraj něco jako řekni jazyk
    with mc as source:
        print("Listening to language")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audiolistening = recog1.listen(source)
    try:
        global langInput
        get_sentence = recog1.recognize_google(audiolistening, language=langInput)  
        print(f"Recognized: {get_sentence}")
        sentence=get_sentence.lower()
        for klic, hodnota in jazyky.items():
            if hodnota in sentence:
                print(klic)
                
                langInput=klic
                print("Jazyk zmněněn")
                break
        else:
            print("Nepodporovaný jazyk")  

    except sr.UnknownValueError:
            print("Do not recognized")
    except sr.RequestError as e:
        print(f"Chyba při požadavku na rozpoznání: {e}")
    
    
    Jarvisteposloucha()

def gptodpoved(otazka):
    pyautogui.hotkey('win', 'r')
    pyautogui.write(r"C:\\Users\\stepan\\Documents\\seabas\\elevator.mp3")
    pyautogui.press('enter') #otevření notepadu
    time.sleep(1)

    pyautogui.click(1750,0) # vypnutí hudbyC:\\Users\\stepan\\Documents\\seabas\\elevator.mp3

    time.sleep(0.2)
    
    pyautogui.click(1750,0) # vypnutí VS
    time.sleep(0.2)

    pyautogui.click(230,150) #otevření menu
    time.sleep(0.2)
    pyautogui.click(400,230) # nový chat
    time.sleep(1)

    pyautogui.click(580,380)  # občasné vymazaní thredů
    pyautogui.click(580,380) 

    pyautogui.click(548,415) 
    pyautogui.click(800,900)
    time.sleep(0.2)

    pyautogui.write(otazka)
    pyautogui.press('enter')
    time.sleep(11)                    # čas na odpoved
    pyautogui.click(220,270)

    pyautogui.hotkey("ctrl", "a")       #otevření notepadu
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey('win', 'r')
    pyautogui.write(r"C:\\Users\\stepan\\Documents\\seabas\\data.txt")     # zmněň na tvojí adresu pro notepad
    pyautogui.press('enter') #otevření notepadu
    time.sleep(1)

    pyautogui.click(800,900)      #práce v notepadu
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl","s")
    pyautogui.hotkey("alt","f4")

    with open(r"C:\\Users\\stepan\\Documents\\seabas\\data.txt", 'r') as soubor: # zmněň na tvojí adresu pro file data.txt
        obsah = soubor.read()
    print(obsah)

    pyautogui.hotkey('win', 'r')
    pyautogui.write(r"C:\\Users\\stepan\\Documents\\seabas\\data.txt")  # zmněň na tvojí adresu pro notepad
    pyautogui.press('enter')   #otevření notepadu
    time.sleep(1)

    pyautogui.hotkey("ctrl", "a")     #práce v notepadu
    pyautogui.press("del")
    pyautogui.hotkey("ctrl", "s")
    pyautogui.hotkey("alt","f4")

    obsah = obsah[6:]
    sayanswer(obsah)

def sayanswer(odpoved):

    print(odpoved)
    translator = Translator(to_lang=langInput, from_lang="en")  
    translated_text = translator.translate(odpoved)
    print(translated_text)

    myobj = gTTS(text=translated_text, lang=langInput, slow=False)
    myobj.save("welcome.mp3")
    
    pygame.init()
    pygame.mixer.init()
    
    zvuk = pygame.mixer.Sound("welcome.mp3")
    zvuk.play()
    delka = zvuk.get_length() * 1200
    pygame.time.wait(int(delka))
    pygame.mixer.quit()
    
    Jarvisteposloucha()



Jarvisteposloucha()



#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System
#J.A.R.V.I.S. == Just A Rather Very Intelligent System

