print(r"""
  ____  _____  ___  _  _    ____   __    ____  ____  ____    ___   ___  ____  ___  ___  _____  ____ 
 (  _ \(  _  )/ __)( )/ )  (  _ \ /__\  (  _ \( ___)(  _ \  / __) / __)(_  _)/ __)/ __)(  _  )(  _ \
  )   / )(_)(( (__  )  (    )___//(__)\  )___/ )__)  )   /  \__ \( (__  _)(_ \__ \\__ \ )(_)(  )   /
 (_)\_)(_____)\___)(_)\_)  (__) (__)(__)(__)  (____)(_)\_)  (___/ \___)(____)(___/(___/(_____)(_)\_)
                                                                                                   """)

print(" lets play with computers!!"
      "Wait for end results !!")
import random
import time
computer =["stone","paper","scissor"]
for i in range(0,3):
   x = input("stone/paper/scissor :")
   l1=0
   l2=0
   human = x.lower()
   if human not in computer:
       exit("wrong input !"
             "Please try again !!")
   else:
    a = random.choice(computer)
    print("waiting for computer")
    time.sleep(0.5)
    print("computer :",a)
    time.sleep(0.5)
    if human== a :
        print("")


    elif human!=a:
      if human=="stone" and a== "paper":
         l2 +=1
      elif human=="paper" and a== "stone":
        l1 += 1
      elif human=="stone" and a== "scissor":
        l1 += 1
      elif human=="scissor" and a== "stone":
        l2 += 1
      elif human=="paper" and a== "scissor":
        l2 += 1
      elif human=="scissor" and a== "paper":
        l1 += 1
if l1>l2:
    print(r"""              __    __   ___   ____       __  __
  |  |  | /   \ |  |  |    |  |__|  | /   \ |    \     |  ||  |
  |  |  ||     ||  |  |    |  |  |  ||     ||  _  |    |  ||  |   
  |___, ||     ||  :  |    |  `__'  ||     ||  |  |     __  __ 
  |     ||     ||     |     \      / |     ||  |  |    |  ||  |
  |____/  \___/  \__,_|      \_/\_/   \___/ |__|__|    |__||__|

                                                               """)
elif l1==l2:
    print(r"""  
  |   \  |    \  /    ||  |__|  |    |  ||  |
  |    \ |  D  )|  o  ||  |  |  |    |  ||  |
  |  D  ||    / |     ||  |  |  |    |__||__|
  |     ||    \ |  _  ||  `  '  |     __  __ 
  |     ||  .  \|  |  | \      /     |  ||  |
  |_____||__|\_||__|__|  \_/\_/      |__||__|
                                            """)


else:
    print(r"""   __ __   ___   __ __      _       ___      ___ ___
  |  |  | /   \ |  |  |    | |     /   \ / ___/  /  _]    |  ||  |
  |  |  ||     ||  |  |    | |    |     (   \_  /  [_     |  ||  |
  |  ~  ||  O  ||  |  |    | |___ |  O  |\__  ||    _]    |__||__|
  |___, ||     ||  :  |    |     ||     |/  \ ||   [_      __  __ 
  |     ||     ||     |    |     ||     |\    ||     |    |  ||  |
  |____/  \___/  \__,_|    |_____| \___/  \___||_____|    |__||__|
                                                                  """)

