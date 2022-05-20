#importing modules
import wikipedia
import random
import time
import datetime
from colorama import Fore

#starting animation
print(Fore.YELLOW +"booting...")

#assining values
real_time=time.strftime("%H:%M:%S %P")
daytime=int(time.strftime("%H"))
wish=""
numbers="1234567890"
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letlength="0123456789"

#user
time.sleep(1)
print("\033[H\033[J")
print("hello,what can I call you?")
user=input(":")
print("\033[H\033[J")
if daytime >=0 and daytime<=12:
		wish="Good morning"
if daytime>12 and daytime<=15:
		 wish="Good afternoon"
if daytime>15:
		wish="Good evening"
print(Fore.GREEN+wish,user)

#conversation
while True:
	inp=input(":")
	search=inp
	ans=inp.upper()
	if ans =="HI" or  ans=="HELLO" or "MORNING" in ans or "EVENING" in ans or "AFTERNOON" in ans:
		print("how can I help you?")
	elif "TIME" in ans and "SET" not in ans  or "TIME" in ans and "NOW" in ans and "SET" not in ans:
		print("it's",real_time)
	elif "DAY" in ans or "TODAY" in ans or "DATE" in ans:
		day=time.strftime("%A")
		date=time.strftime("%F")
		print("today is",day,"date:",date)
	elif "THANK"  in ans :
		print("nice to assist you")
	elif "RANDOM" in ans or "PICK" in ans:
			if "LETTER" in ans:
				randnum="".join(random.sample(letters,1 ))
				print("here is the random letter",randnum)
			if "NUMBER" in ans:
				if "DIGIT" in ans:
					below=int(input("number of digits you want in your number:"))
					randnum="".join(random.sample(numbers,below ))
					print(randnum)
				else:
			 		let_length_rand=int("".join(random.sample(letlength,1)))
			 		randnum="".join(random.sample(numbers,let_length_rand))
			 		print(randnum)
	elif "KILL" in ans:
		print("Sorry,I cant kill anyone")
	elif "NO" in ans and "NEED" in ans or "WANT" in ans:
		print("okey")
	elif "TIMER" in ans and "SET" in ans or "WAIT" in ans:
		print("ok")
		timer=int(input("how long:"))
		while True:
			timer-=1
			time.sleep(1)
			if timer>9:
				print(Fore.WHITE +str(timer))
			if timer<10 and timer>6:
				print(Fore.YELLOW+str(timer))
			if timer<7 and timer>3:
				print(Fore.MAGENTA+str(timer))
			if timer<4:
				print(Fore.RED+str(timer))
			if timer<1:
				print(Fore.GREEN+"time up!")
				time.sleep(3)
				print("\033[H\033[J")
				break
	elif ans=="":
		pass
	elif "favourite" in ans:
	    if "colour" in ans:
	        print("its black")
	    if "food" in ans:
	        print("l love biriyani")
	    if "film" in ans:
	        print("Avengers:endgame")       
	else:#wikipedia search
		result = wikipedia.search(search)
		print(result)
		print("\n")
		time.sleep(.5)
		print("there are lots of contents")
		print("\n")
		time.sleep(0.5)
		print("here is the results about one of them")
		print("\n")
		print(wikipedia.summary(search,sentences=2))
		print("\n")
		print("\n")
		time.sleep(2)
		print("If you want to know more type yes")
		more=input(":").upper()
		if more=="YES":
			print(wikipedia.summary(search))
			