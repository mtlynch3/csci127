def hh():
	print(r"""
                   ___  ___
         \  \  /`\ \  \ \  \ \  \
          \__\ \__\ \__' \__' \__\
           \  \ \  \ \    \     \
            \  \ \  \ \    \     \
                    ___         ___  ___
\  \  /`\ \    \    \  \ \    \ \    \    \.  \
 \__\ \__\ \    \    \  \ \  . \ \__  \__  \`\ \
  \  \ \  \ \    \    \  \ \ |`\\ \    \    \ `\\
   \  \ \  \ \___ \___ \__\ \|  `\ \___ \___ \  `\

	""")

def jack():
	print(r"""

          ___
       ___)__|_
  .-*'          '*-,
 /      /|   |\     \
;      /_|   |_\     ;
;   |\           /|  ;
;   | ''--...--'' |  ;
 \  ''---.....--''  /
  ''*-.,_______,.-*' 


	""")
##########################################

print("Jack O Lantern wants to play a game...")
print("Here are the rules:")
print("You will enter a number between 7 and 12")
print("I will roll a 6 sided die")
print("If the values added together equal 13...")
print("You will get a TREAT :D")
print("Otherwise you get a TRICK >:)")

##########################################
import random 

#trick or treat!

user_num = 0
while user_num < 7 or user_num > 12:
	user_num = int(input("Enter your number... if you dare: "))
print("Very well, let's see if", user_num, "was the right choice...")

die_roll = random.randrange(1,7)

print("I have rolled my die... the result is", die_roll)
print(user_num, "+", die_roll,die_roll+user_num)
if die_roll+user_num == 13:
	print("Lucky 13! You get a treat!")
	hh()
else:
	print("Better luck next time, you've been tricked.")
	jack()

print("Thanks for playing!")

##########################################




