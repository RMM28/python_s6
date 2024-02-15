#To find Compund Interest
p=float(input("Enter the amount to find compund interest to: "))
r=int(input("Enter the rate of interest as %: "))
t=int(input("Enter the number of years: "))
i_sum=0
print("Year\tStarting Balance\tInterest\tEnding Balance")
for i in range(t):
    interest=float((p*r)/100)
    print(i+1,"\t",p,"\t","%14.2f"%round(interest,2),"\t","%10.2f"%(p+interest))
    p=p+interest
    i_sum+=interest
print("ending balance: $",round(p,2))
print("Total interest earned: $",round(i_sum,2))
