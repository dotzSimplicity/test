# This is something i coded a while back for some reason, i just wanted to put it here so it wouldnt be on my pc


print("NOTICE: Running an Unknown Command will stop the program, Make you spell it right and remember that it is Case-Sensetive")
print("Another NOTICE: This program/script is still in development(Unknown if i will finish it) Therefore there are lots of bugs, You can use 'Bugs?' to check the Known Bugs")
print("Type 'Help' for a list of commands!")
inputmsg = input("Input Message: ")
lastcmd = "Unknown, Most likely not written"
clear = "\n" * 100 

if inputmsg == "Help":
    print("List of commands Below!")
    print("'Hello!' - It's nice to introduce yourself! even to a program...")
    print("'Goodbye!' - Ends the program, A nice way to say bye instead of crashing it")
    print("'Last Command?' - This is incase you can't look up the script/terminal, Just a way to check the last command (before this one) written")
    print("'Bugs?' - Displays the bugs known to the developer")
    print("'Clear' - Clears the Console/Terminal")
    lastcmd = "'Help'"
    inputmsg = input("Input Message: ")
    
if inputmsg == "Last Command?":
    print("The Last Command given before this one is " + lastcmd)
    lastcmd = "'Last Command?'"
    inputmsg = input("Input Message: ")
  
if inputmsg == "Hello!":
    print("Why hello there!")
    lastcmd = "'Hello!'"
    inputmsg = input("Input Message: ")
    
if inputmsg == "Bugs?":
    print("List of Known Bugs Below!")
    print("Running a command twice will end the program")
    print("Running an Unknown Command will also end the program, The solution to this as of right now is to it notify the user that an unknown command was used")
    print("Running the 'Clear' Command will make the program Unusable")
    lastcmd = "'Bugs?'"
    inputmsg = input("Input Message: ")
    
if inputmsg == "Clear":
    print("Hey Look, I'm a random string to make the clear command work, Good job finding me!")
    print("Fun Fact about the Clear command, It just makes 300 new lines!")
    print(clear)
    print(clear)
    print(clear)
    lastcmd = "'Clear'"
    inputmsg = input("Input Message: ")
    
    
if inputmsg == "Goodbye!":
    print("Goodbye, Hope to see you later!")
    print("Program shut down.")