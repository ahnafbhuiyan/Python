import webbrowser
import os
import subprocess
import wikipedia
import wolframalpha
import tkinter as tk
import time

#(Oct 6, 2019)
#Create clock and clock related stuff

#(Jan 21,2020)
#Voice commands
#Communicate with arduino 
#Find other commands to put in
#play music
#Schedule
#Speach recognition

client  = wolframalpha.Client('XYLA93-ELUAJ924UK')

    #Function for google searching 
def googleSearch (word):
    address = 'http://www.google.com/#q='
    search = address+word

    webbrowser.open(search)

    #Function for Wikipedia searching 
def wikiSearch(word):
    print(wikipedia.summary(word))

    #Function for Wolframalpha
def wolframalpha():
    res = client.query(input("what you searching?"))
    output = next(res.results).text
    print(output)

    #Function for time(Jan 21,2020)
def checkTime():
    t = time.time()
    print (time.ctime(t))

    
def main():
    while True:
        start = input ("What would you like to do?")
        start = start.lower()
                
    #Commands depending on what is inputted (start)

        if start=='exit':#Exit type beat
            exit()
        elif start == "help": #help, a list of the current functions Added (Jan 21,2020)
            print ("So far I can search on Google, Wikipedia and Wolfram Alpha")

        #Wikipedia
        elif start == "wikipedia":
            search = input("What do you want to search?")
            wikiSearch(search)
        #Wolframalpha
        elif start == "wolframalpha":
            wolframalpha()

        #Google function calling
        #If the words "start" or "what" are in the input, it will take out the word 'search' (if used) and call google with the question
            
        #Taking out the word 'search' to search google with 
        elif 'search' in start:
            word = start.split(" ") 
            word.remove('search')
            start = ' '    
            googleSearch(start.join(word))#now put the list back into one string

        elif 'date' in start or 'time' in start:
            checkTime()

        #If word 'what inputted, searches  using that input
        else:
            googleSearch(start)
        
        

if __name__=='__main__':
    main()
