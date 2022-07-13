from tkinter import Y


my_list=list()
x=0
y=1


for i in range(1,10):
    if(x==0 and y==1):
         my_list.append(x)
         my_list.append(y)
    z=x+y 
    my_list.append(z)
    x=y 
    y=z 
    
print("fibonacci -->",my_list)


