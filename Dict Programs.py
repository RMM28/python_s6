''' 1. Program to count the frequency of words in a string.
2. Given a dictionary x={"k1":'v1',"k2":'v2',"k3":'v3'}, create a dictionary with the opposite mapping
3. Given two dictionaries D1 & D2. WAP to print all commmon keys in both dicts.
'''

#1. Program to count the frequency of words in a string.

'''d={}
c=0
s=input("Enter a sting: ")
s1=s.split(' ')
for i in s1:
    c=s1.count(i)
    d[i]=c
print("dictionary: ",d)'''

#-----------------------------------------------------------------------

#2. Given a dictionary x={"k1":'v1',"k2":'v2',"k3":'v3'},
#create a dictionary with the opposite mapping

'''d=eval(input("Enter an dictionary: "))
dn={}
for i in d:
    dn[d[i]]=i
print("new dictionary with opposite mapping: ",dn)'''

#-----------------------------------------------------------------------

#3. Given two dictionaries D1 & D2.
#Write a program to print all commmon keys in both dicts.

'''d1=eval(input("Enter an dictionary: "))
d2=eval(input("Enter another dictionary: "))
l=[]
for i in d1:
    for j in d2:
        l.append(i)
        break
print("The common keys in both dictionaries are: ",l)'''

#-----------------------------------------------------------------------

#4. - Simulate a billing scenario in a store with two dictionaries 'stock'
#and 'price'. 'Stock' contains the items in the store with count.
#'Price' has the price of each item. The items that are available in the stock
#should be displayed to the user. User can buy any set of items from the stock.
#After purchase total bill of all items bought should be displayed with remaining stock items.

stock={'pen':10,'pencil':20,'notebook':15,'sharpeners':12,'erasers':12}
price={'pen':10,'pencil':5,'notebook':40,'sharpeners':5,'erasers':5}
bill={}
ans='y'
tp=0
print("Welcome to store\nHere are the available stock:\n")
while(ans=='y'):
    print()
    for i in stock:
        print(i,":",stock[i],"-- $",price[i])
    c=input("Enter item name: ")
    n=int(input("Enter quantity: "))
    bill[c]=n
    stock[c]=stock[c]-n
    ans=input("Do you want to continue (y/n):  ")
print("\n Heres the bill:\n")
print("Item\t\tQuantity\tPrice\tTotal Price\n")
for i in bill:
    print(i,"",bill[i]," ",price[i]," ",bill[i]*price[i],sep="\t")
    tp=tp+bill[i]*price[i]
print("Total Bill Amount: ",tp)
    
    






#-----------------------------------------------------------------------

#5. Repeatedly ask the user to enter a team name and how many games a team
#has won or lost. Store this info in a dictionary, with team name as keys and
#values as a list of the form [wins,losses].Use the dictionary to do the following.
#• Print names of all teams.
#• Print name of team with highest wins
#• Print name of team with highest losses
#• Allow user to enter the team name and print the teams win percentage





