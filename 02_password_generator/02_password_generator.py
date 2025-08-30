import string
import random
print("Welcome to password generator!")


l=list(string.ascii_letters)
s=list(string.punctuation)
n=[0,1,2,3,4,5,6,7,8,9]
# print(s)
# print(l)


letters=int(input("How many letters would you like in your password?\n"))
symbols=int(input("How many symbols wouldyou like in your password?\n"))
numbers=int(input("How many numbers would you like in your password?\n"))

list1=[]
list2=[]
list3=[]

for letter in range(letters):
    final1=random.choice(l)
    list1.append(final1)
for symbols in range(symbols):
    final2=random.choice(s)
    list2.append(final2)
for num in range(numbers):
    final3=random.randint(0,9)
    list3.append(final3)

# print(list1)
# print(list2)
# print(list3)

# l2="".join(list1)❌
# s2="".join(list2)❌
# n2="".join(str(num) for num in list3)❌

for i in range(len(list3)):
    list3[i]=str(list3[i])

final_list=list1+list2+list3
# print(final_list)

# password=l2+s2+n2 ❌

random.shuffle(final_list)
fp="".join(final_list)
print(fp)


# print(dir(string))
# print(dir(random))



