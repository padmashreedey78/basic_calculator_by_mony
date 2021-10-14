num1=input("enter first number:")
num2=input("enter second number:")

#type casting


num1_change=int(num1)
num2_change=int(num2)
#print(type(num1_change))
#print(type(num2_change))



print("select an option from the following options:")
print('1.add')
print("2.subtract")
print("3.multiply")
print("4.divide")


select_option =input('enter an option:')

select_option_change= int (select_option)


if select_option_change==1:
    print("addition result:%s" %(num1_change+num2_change))
elif select_option_change==2:
    print("subtraction result:%s"%(num1_change-num2_change))
elif select_option_change==3:
    print("mutiplication result:%s"%(num1_change*num2_change))
elif select_option_change==4:
    print("division result:%s"%(num1_change/num2_change))
else :
    print("invalid option selected!")
