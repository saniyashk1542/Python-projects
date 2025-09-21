#silent auction 
import os
bidder_list=[]
ans =True
while ans:
    bidder={}
    name=input("What is your name:")
    bidder['name']=name
    bid=int(input("what is your bid:"))
    bidder['bid']=bid
    bidder_list.append(bidder)
    # print(bidder_list)
    # print(bidder)
    print("Are there any other bidders ? Type 'Yes' or 'no ")
    
    ans=input(":")
    if ans=='yes':
        os.system('cls')
    else:
        ans='False'
        os.system('cls')
        break

num=[]
for i in bidder_list:
    num.append(i['bid'])
# print(num)

max=num[0]
for i in range(1,len(num)):
    if num[i]>max:
        max=num[i]
# print(max)


for i in bidder_list:
    if max==i['bid']:
        print(f"The winner is {i['name']} with bid {i['bid']}" )





