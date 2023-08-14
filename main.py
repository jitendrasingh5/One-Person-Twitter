import datetime, os , time
from replit import db

def add_tweet():
  tweet = input(":")
  timestamp = datetime.datetime.now()
  key1 = f"mes{timestamp}"
  db[key1] = tweet
  time.sleep(1)
  os.system("clear")

def view():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.5)
    counter += 1
    if (counter%10 == 0):
      carryOn = input("Next 10? : ")
      if carryOn.lower() == "no":
        break
  time.sleep(3)
  os.system("clear")


while True:
  print("One Person Twitter")
  print() 
  menu = input("1.Add Tweet\n2.View Tweets\n\n : ")
  print()
  if menu == "1":
    add_tweet()
  elif menu == "2":
    view()
    
  
    
  
  








