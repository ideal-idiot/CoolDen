import pyttsx3 #importing python text to speech module
import datetime #
import speech_recognition as sr
from random import randint



engine = pyttsx3.init('sapi5')#To implement voice inputs(SPEECH API)
voices = engine.getProperty('voices')
#print(voices)  '''options [<pyttsx3.voice.Voice object at 0x0000024B2B983DC0>, <pyttsx3.voice.Voice object at 0x0000024B2B983A60>]'''
engine.setProperty('voices',voices[0].id) 
#print(voices[0].id)'''David's voice MALE'''

player_wins = 0 
computer_wins = 0



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")
    speak("How about a game of Rock, paper Scissors? Are you up for the challenge? ")
    print("How about a game of Rock, paper Scissors? Are you up for the challenge?(YES/NO)")



def takeCommand():
    #Takes the microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
    
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"

    return query

if __name__=="__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        if "yes" in query:
            speak("Player, how many games do you require to win this tournament, enter it in the keyboard.")
            num = int(input("Enter number of games you wish to play: "))
            if num%2 == 0:
                winning_score = num/2 + 1
            else:
                winning_score = num//2 + 1 
            speak("At any point of time if you wish to exit the game, just say quit")
            speak("Okay, here we go!")
            speak("...rock...")
            speak("...paper...")
            speak("...scissors...")
            while player_wins < winning_score and computer_wins < winning_score:
                print(f"Player Score: {player_wins}, Computer Score: {computer_wins}")

                player = takeCommand().lower()
                if "quit" in query:
                    break
                random_num = randint(0, 2)
                if (random_num == 0):
                    computer = "rock"
                elif (random_num == 1):
                    computer = "paper"
                else:
                    computer = "scissors"
                speak(f"The computer has chosen {computer}")
                print(f"The computer plays: {computer}")

                if computer in player:
                    speak("It's a tie")
                    print("It's a tie!")
                elif "rock" in player:
                    if computer == "paper":
                        speak("Computer has won this match")
                        print("Computer wins :( ")
                        computer_wins += 1
                    else:
                        speak("Player, you have won this match")
                        print("Player wins!")
                        player_wins += 1
                elif "paper"in player:
                    if computer == "rock":
                        speak("Player, you have won this match")
                        print("Player win!")
                        player_wins += 1
                    else:
                        speak("Computer has won this match")
                        print("Computer wins!")
                        computer_wins += 1
                elif  "scissors" in player or "scissor" in player:
                    if (computer == "rock"):
                        speak("Computer has won this match")
                        print("Computer wins!")
                        computer_wins += 1
                    else:
                        speak("Player, you have won this match")
                        print("You win!")
                        player_wins += 1
                elif "quit" in player:
                    speak("Thank you Player. Hope you enjoyed playing this game!")
                    break
                else:
                    speak("Player, you were expected to enter a valid move!")
                    print("Please enter a valid move!")
            speak(f"Here are the final scores: Player you have won {player_wins} games and the computer has won {computer_wins} games")
            print(f"Final Scores are: Player's Score {player_wins}, Computer's Score {computer_wins}")

            if player_wins > computer_wins:
                speak("Congradulations")
                print("CONGRATS, YOU WON!")
            elif player_wins == computer_wins:
                speak("Great tournament! It's a tie!")
                print("IT'S A TIE")
            else:
                speak("Good game Player, better luck next time...") 
                print("OH NO :( THE COMPUTER WON...")
            speak("Would you like to play another tournament?")
            query= takeCommand().lower()
        elif "no" in query:
            speak("Awww. It would have been so much fun. Anyways. Thanks for turning up")
            break
        else:
            speak("Do you want me to repeat myself? Are you in for a game of Rock, Paper, Scissors?")
