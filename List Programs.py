
#1. Find the largest and the smallest numbers in a list.
'''l=eval(input("Enter an integer list: "))
print("Largest number in the list: ",max(l))
print("Smallest number in the list: ",min(l))'''

#------------------------------------------------------------------

#2. Find the third largest number in a list.
'''l=eval(input("Enter an integer list: "))
l.sort()
print("Third largest number in the list: ",l[-3])'''

#------------------------------------------------------------------

#3.Write a python program to take a list of integers.
#Create another list with those numbers in the master list that are less than a number entered by the user.
#Print the new list contents.

'''lnew=[]
l=eval(input("Enter an integer list: "))
n=int(input("Enter a number: "))
l.sort()
for i in l:
    if(i<n):
        lnew.append(i)
print("new list:", lnew)'''

#------------------------------------------------------------------

#4. Write a python program to take a list of integers.
#Create another list to store all the even numbers from the master list and print the new list contents in ascending order.
      
'''l=eval(input("Enter an integer list: "))
m=[]
for i in l:
    if(i%2==0):
        m.append(i)
print("new list containg only even numbers:", m)'''

#------------------------------------------------------------------

#5.Write a python program to take two lists of inegers and return a list containging the elements that
#are common in both the list. Also print the contents of the new lists.

l1=eval(input("Enter 1st integer list: "))
l2=eval(input("Enter 2nd integer list: "))
c_l=[]
s1=len(l1)
s2=len(l2)
for i in range(0,s1):
    if (l1[i] in l2):
        c_l.append(l1[i])
print("new list containg common elements:", c_l)














