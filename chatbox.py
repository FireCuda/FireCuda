import speech_recognition
import pyttsx3  
from datetime import date,datetime

robot_ear=speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""
#ear-listening
while True:
    with speech_recognition.Microphone() as mic:
        print("Chatboxt: I'm listening ")
        audio=robot_ear.listen(mic)
    print("Chatbox:.....")
    try:
        you=robot_ear.recognize_google(audio)
    except:
        you=""

#brain-understand
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Lam"
    elif "teacher" in you:
        robot_brain = "I just know HaHuynh who teach you RTOS"
    elif "created" in you:
        robot_brain = "I was done by Lam on March 3, 2021"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "good bye"
        #Chatbox talk & exit program
        print("Chatbox: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain="I can not hear you"
#mouth-talk
    print("Chatbox: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()