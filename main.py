#!/usr/bin/env python3

import os
import sys
import json
import speak
import random
import smtplib
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr


with open('conversation_data.json') as json_data:
    data = json.load(json_data)

def speakup(text):
    print(text)
    lang='en'
    speak.tts(text,lang)
  
def mycommand():
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        try:
            r.adjust_for_ambient_noise(source)
            print('\t\n\tSPEAKUP_m Listening....')
            print('OR SAY "HELP ME" TO GET THE LIST OF COMMANDS')
            audio=r.listen(source)
            text=r.recognize_google(audio)
            # text=input('Enter your command')
            text = text.lower()
            print(f'COMMAND:-{text}')
            return text
        except Exception as e:
            print("COULDN'T HEAR ANYTHING")

def time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speakup(f"Hey there!, Good Morning! the time is {strTime}")

    elif hour>=12 and hour<18:
        speakup(f"Hey, Good Afternoon! the time is {strTime}")

    else:
        speakup(f"Good Night... Hope you had a lovely day!... the time is {strTime}")


def files():
    speakup('SURE . SHOULD I WRITE A FILE?')
    option=mycommand()
    if option=='yes':
        speakup('SURE SIR. WHAT SHOULD BE THE NAME OF THE FILE?')
        name=mycommand()
       #name=input('ENTER NAME OF THE FILE:')
        file=open(name,'w')
        speakup('FILE HAS BEEN CREATED SIR.')
        speakup('ALRIGHT. please WRITE whatever you want')
        words=mycommand()
        #words=input('ENTER:')
        file.write(words)
        file.close()
        speakup('EVERYTHING YOU SAID HAS BEEN ENTERED IN THE FILE.')
        speakup('DONE SIR, DO YOU WANT TO REPEAT THE PROCESS ALL OVER AGAIN?')
        res=mycommand()
        if res=='yes':
            files()
        else:
            speakup('Okay Got It.')
            return mycommand()

    elif option=='no':
        speakup('SO SHOULD I READ ANY FILE?')
        #resp2=input('enter:')
        resp2=mycommand()
        if resp2=='yes':
            speakup('OKAY. PLEASE TELL ME THE NAME OF THE FILE')
            f_name=mycommand()
            #f_name=input('ENTER:')
            ff=open(f_name,'r')
            data=ff.read()
            speakup(data)
            ff.close
            speakup('DONE SIR, DO YOU WANT TO REPEAT THE PROCESS ALL OVER AGAIN?')
            res=mycommand()
            if res=='yes':
                files()
            else:
                speakup('I am going back to my normal mode.')
                return mycommand()
    else:
        speakup(random.choice(sorry))
        return mycommand()
def cloud(key):
    path='firefox'
    url=('https://duckduckgo.com/?q='+key)
    webbrowser.get(path).open(url)

def send_mail():
    sender="ENTER SENDER'S MAIL ADDRESS HERE"
    pswd="ENTER SENDER'S PASSWORD"
    speakup("SURE..ENTER THE RECEIVER'S MAIL ADDRESS-")
    recp=input('MAIL ADDRESS')
    try:
        speakup('ALRIGHT.. WHAT SHOULD I SAY?')
        content=mycommand()
        speakup('JUST A MOMENT. I M SENDING YOUR MAIL SIR!')
        mail=smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender,pswd)
        mail.sendmail(sender,recp,content)
        speakup('DONE SIR.  MAIL HAS BEEN SENT TO THE PERSON')
        
        speakup('WOULD YOU LIKE TO SEND ANOTHER MAIL?')
        res=mycommand()
        if res=='yes':
            return send_mail()
        else:
            return mycommand()
    except Exception as e:
        print(f'Error Occured{e}')

   
def wiki():
    try:
        speakup('What would you like to know about?')
        ans=mycommand()
        data=wikipedia.summary(ans ,sentences=2)
        speakup(data)
        speakup('HEY! IF YOU NEED MORE INFORMATION I CAN BROWSE THE INTERNET FOR YOU . SHOULD I?')
        # resp=input('ENTER')
        resp=mycommand()
        if resp=='yes':
            speakup('SURE! JUST A MINUTE')
            cloud(ans)
        else:
            return wiki()

        speakup('WOULD YOU LIKE TO KNOW SOMETHING ELSE ?')
        # res=input('enter')
        res=mycommand()
        if res=='yes':
            return wiki()
        else:
            return mycommand()
    except Exception as e:
        print('COULD NOT FIND WHAT YOU A LOOKING FOR!  TRY AGAIN')


def read_out():
    t = input("Paste the text here")
    speakup(t)
   
def myzara(text):
    if text == 'help me':
        print('-'*55,'LIST OF COMMANDS','-'*55,''.center(os.get_terminal_size().columns))
        print('\n')
        print("say 'ACTIVATE FILE MODE' to -> Read, Write and Save A file With Voice Command\n".center(os.get_terminal_size().columns))
        print("say 'SEND MAIL' to -> SEND A MAIL TO ANYONE\n".center(os.get_terminal_size().columns))
        print("say 'SEARCH THE WEB' to -> BROWSE ANYTHING ON THE WEB\n".center(os.get_terminal_size().columns))
        print("say 'TIME' to -> KNOW ABOUT CURRENT TIME\n".center(os.get_terminal_size().columns))
        print("say 'READ OUT' to -> MAKE ME READ SOMETHING\n".center(os.get_terminal_size().columns))
        print("say 'SHUT DOWN' to -> TO STOP THE PROGRAM\n".center(os.get_terminal_size().columns))
        print('-'*55,'GO AHEAD! GIMME A COMMAND','-'*55,''.center(os.get_terminal_size().columns))

    elif text in data['intents'][4]['responses']:
        time()
    elif text in data['intents'][5]['responses']:
        read_out()
    elif text in data['intents'][6]['responses']:
        send_mail()
    elif text in data['intents'][3]['responses']:
        wiki()
    elif text in data['intents'][7]['responses']:
        files()
    
    elif text in data['intents'][0]['pattern']:
        speakup(random.choice(data['intents'][0]['responses']))

    elif text in data['intents'][1]['pattern']:
        speakup(random.choice(data['intents'][1]['responses']))

    elif text in data['intents'][8]['responses']:
        speakup("SHUTTING DOWN ON YOUR COMMAND")
        sys.exit()

    else:
        speakup(random.choice(data['intents'][2]['responses']))
while True:
    myzara(mycommand())
 

