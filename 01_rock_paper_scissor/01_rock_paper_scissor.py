import random
print("LETS PLAY... ROCK 🪨,PAPER 📃,SCISSOR ✂️!!!")
l=['🪨','📃','✂️']

print("what do u choose:\n ROCK 🪨 :type 0\n PAPER 📃:type 1\n SCISSOR ✂️ :type 2")
user=int(input("enter ur choice here:"))
try:
    print(f"You Chose:{l[user]}")
except Exception as e:
    print("Invalid Input")


computer=random.randint(0,2)
print(f"I choose : {l[computer]}")

if(user==computer):
    print("oohhhh ...its a draw")
elif(user==2 and computer==0):
    print("booo! you loose")
elif(user==0 and computer==2):
    print("Ahh ..u win ")
elif(computer>user):
    print("booo! you loose")
elif(user>computer):
    print("Ahh ..u win ")
else:
    print("Invalid input")
    


