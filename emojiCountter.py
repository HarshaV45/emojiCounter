userCount=0
emoji,emojiCount={},{}
emojiList=[]
message=""

def Results():
  print("\nMessage: "+message)
  print("Emoji"+"\t"+"EmojiCount"+"\t"+"Percentage")
  for i in emojiCount:
    percentage=(emojiCount[i]/userCount)*100
    percentage="{:.2f}".format(percentage)
    print(" "+emoji[i]+" \t\t"+str(emojiCount[i])+"\t\t"+percentage+"%")

emoji={'happy':"\U0001F602",'sad':"\U0001F614",'curious':"\U0001F914",'ok':"\U0001F610",'heart':"\U0001F60D"}
emojiList=['happy','sad','curious','ok','heart']
emojiCount={}
print("Hello Welcome to Emoji Counter!")
print("To start the counter please enter a message")
while 1:
  try:
    message=input()
    if len(message)<1:
      raise Exception
    else:
      break
  except:
    print("Please enter a valid message!")

    
print('\n')
print("Available Emoji's to react for the message are")
temp=1
for i in emoji:
  print("("+str(temp)+") "+emoji[i]+" ["+i+"]")
  temp+=1
while 1:
  print("\nPlease enter number corresponding to the emoji you want to react")
  while 1:
    try:
      userInput=int(input())
      if userInput not in [1,2,3,4,5]:
        raise Exception
      else:
        break
    except:
      print("Please enter a valid number")
  userCount+=1
  userEmoji=emojiList[userInput-1]
  if userEmoji in emojiCount:
    emojiCount[userEmoji]+=1
  else:
    emojiCount[userEmoji]=1
  print('\nWould to you like to react again? : Yes/No')
  while 1:
    try:
      decision=input().lower()
      if decision not in ['yes','no']:
        raise Exception
      else:
        break
    except:
      print("Please enter a valid input")
  if decision=="no":
    Results()
    break