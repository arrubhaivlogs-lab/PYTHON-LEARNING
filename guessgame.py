import random

num=random.randint(1,10)

tries=0
max_tries=3

while tries<max_tries:
    
     guess=int(input("please guess a no.between 1 to 10(max attempt is 3):"))
    
     if guess==num:
         tries+=1
         print("won")
         break
        
     elif num>guess:
         tries+=1
         print("go higher")
         
     elif num< guess:
         tries+=1
         print("go lower")
         
     else:
         tries+=1
         print("wrong")
         
     print("no. of times you guessed",tries)
else:
    print("you lost")
    print("the num was",num)
