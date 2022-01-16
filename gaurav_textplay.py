import pywhatkit
import tkinter
import cv2
from translate import Translator
#text to speech module
from gtts import gTTS
from playsound import playsound


from pytube import YouTube
import time

while True:

    print("\n ****************** \n Some python work")  
    print("1. Convert your typed input into handwritten image, Enter 1")  
    print("2. Automate Whatsapp, WILL BE AVAILIABLE IN NEXT UPDATE")
    print("3. Listen yout favorite song on Youtube")
    print("4. Translate the English text input into some language ")
    print("5. Exit")  
    choice = str(input("Enter the Choice:"))

    if choice=="1":


        # For image -text as per input
        img=str(input("Enter the text you want to get hand written: "))
        pywhatkit.text_to_handwriting(img,save_to="Aljozy.png",rgb=[0,5,7])
        #Image file name for saving
        k=cv2.imread("Aljozy.png")
        cv2.imshow("Here is the image for Handwritten Text",k)
        print('Converted..')

    elif choice=="2":
##        
##        #Whatsapp message sending on specified time
##        import pywhatkit
##        #pywhatkit.sendwhatmsg(reciever's number, message, hour(scheduled) in 24 hr format, minute(scheduled) )
##        pywhatkit.sendwhatmsg('+91 0000000000','hye, this is automated message',14,22)
##        #message will be sent on sender's number at the scheduled time that is (2:22 pm)
        s=4
        print("Bola na next update me milega, fr bhi nhi mann na, BAAKAA")

    elif choice=="3":

##        print("You can either download the song if you have link or you can simply listen out your song by entering just name: ")
##        print ("To Listen out your favorite song press S ")
##        print ("To Download your song using press D ")
##        song=input("Yeah right here : ")
        songplay = "s"

#        songplay=song.lower()
        

        if songplay == "s":
            print("Please enter the song you want to listen below : ")
            ch=str(input())
            t=5

            try:
                print("Your song will be played in - ")
                while t>0:
                    print (t)
                    t-=1
                    time.sleep(1.25)
                    
                print("Playing...")
                pywhatkit.playonyt(ch)
                

            except:
                print("An Error Occured, please check your network or try again later...")

##        elif songplay== "d":
##
##            #enter link
##            link = input("Place the link of youtube video to download:  ")
##            yt = YouTube(link)
##            ys = yt.streams.get_highest_resolution()
##            print("Downloading...")
##            ys.download("Downloads\file")
            
##        else :
##            print ("Oops! Incorrect choice, please try again by chosing from D to download or S for Playing Song ")




    elif choice=="4":
        print("We have right now only 2 languages Japanese and Hindi, will surely add some more of them") 
        jpn = Translator(to_lang="Japanese")
        hn = Translator(to_lang="Hindi")
        print("Please Enter J for Japanese")
        print("Please Enter H for Hindi")
        inp1=input("Yeah right here : ")
        inp3=inp1.lower()
        if inp3=="j" :
            print("Please Enter Text for required translations : ")
            inpj=str(input())
            tj = jpn.translate(inpj)
            myobj = gTTS(text=tj)
            myobj.save("japaneseTranslation.mp3")
            #playsound("japaneseTranslation.mp3")
            print("Your Japanese translated text is : " + tj)

        elif inp3=="h" :
            print("Please Enter Text for required translations : ")
            inph=str(input())
            th = hn.translate(inph)
            myobh = gTTS(text=th)
            myobh.save("HindiTranslation.mp3")
            #playsound("HindiTranslation.mp3")
            print("Your Hindi translated text is : " + th)

            
        else :
            print ("Bro I have already told you we have only 2 languages right now!, please choose from them")


    elif choice=="5":
        print("Thanks for your participation bro ")
        break
        

    else :
        print("Incorrect choice was entered by you!, Please enter your choice from the given parameters")




    
