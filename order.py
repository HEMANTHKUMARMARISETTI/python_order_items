print("-------------MENU LIST-------------")
print("Chicken_Biryani=250\nNoodles=150\n")
Chicken_Biryani=250
Noodles=150
sum=0
sum2=0
ch=int(input('How many chicken biryanis you want : '))
n=int(input('How many Noodles you want : '))
sum=ch*Chicken_Biryani+n*Noodles
if(sum>0):
    print('amount : ',sum)
else:
    print('place order properly')
print("-----------------------------------")    
s=str(input("do u want to discard some items \n enter yes or no : "))
if(s=='yes'):
    if(ch>0):
        ch1=int(input('enter how many chicken biryani u want to discard : '))
    
    if(n>0):
        n1=int(input('enter how many noodles u want to discard : '))
    if(n>n1 and ch >ch1):
        sum2=sum-(Chicken_Biryani*(ch1)+Noodles*(n1))
    else:
        print('please order properly')
    print('-------Bill-----')
    print('chicken biryani ordered:',ch-ch1)
    print('noodles ordered : ',n-n1)
    if(sum2>0):
        print("amount : ",sum2)
    else:
        print('place order properly')
elif(s=='no'):
    print('-------Bill-----')
    print('chicken biryani ordered:',ch)
    print('noodles ordered : ',n)
    print("amount : ",sum)
    


    

