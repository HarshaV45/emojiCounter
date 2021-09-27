userCount=0   #No of users
emoji,emojiCount={},{} 
emojiList=[]
message=""

def Results():# A Function to display the results of the emoji count
  print("\nMessage: "+message)
  print("Emoji"+"\t"+"EmojiCount"+"\t"+"Percentage")
  for i in emojiCount:
    percentage=(emojiCount[i]/userCount)*100 # Percentage of emojis selected by the user
    percentage="{:.2f}".format(percentage)
    print(" "+emoji[i]+" \t\t"+str(emojiCount[i])+"\t\t"+percentage+"%")

emoji={'happy':"\U0001F602",'sad':"\U0001F614",'curious':"\U0001F914",'ok':"\U0001F610",'heart':"\U0001F60D"} # emoji name paired with emojiID's
emojiList=['happy','sad','curious','ok','heart'] # Emojis in the form of list
emojiCount={} # A Dictonary to store the count of emojis 

#Welcome Message
print("Hello Welcome to Emoji Counter!")
print("To start the counter please enter a message")
while 1:
  try:
    message=input() # Prompting the user to input the messge
    if len(message)<1:
      raise Exception # Raising an exception if the input is invalid
    else:
      break
  except:
    print("Please enter a valid message!") # Exception 

#Users Part
print('\n')
print("Available Emoji's to react for the message are")
temp=1
for i in emoji:# Printing the emojis avaliable 
  print("("+str(temp)+") "+emoji[i]+" ["+i+"]")
  temp+=1
while 1:
  print("\nPlease enter number corresponding to the emoji you want to react")
  while 1:
    try:
      userInput=int(input())# Taking the users input to increase the count of emojis for the message
      if userInput not in [1,2,3,4,5]:#Checking for exceptions
        raise Exception 
      else:
        break
    except:
      print("Please enter a valid number") # Exception

  userCount+=1 # Incrementing the user count for every emoji
  userEmoji=emojiList[userInput-1]
  if userEmoji in emojiCount:# Updating the value of emoji count in dictonary
    emojiCount[userEmoji]+=1
  else:
    emojiCount[userEmoji]=1
  print('\nWould to you like to react again? : Yes/No')# Prompting the user to either continue or exit
  while 1:
    try:
      decision=input().lower()#Taking the decision of the user
      if decision not in ['yes','no']:#Checking for exceptions
        raise Exception
      else:# If no Exception occurred
        break
    except:
      print("Please enter a valid input")
  if decision=="no":# Stoping the program
    Results()#Displaying the results of the emoji count
    break
