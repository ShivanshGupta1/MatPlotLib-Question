#!/usr/bin/env python
# coding: utf-8

# In[36]:


import matplotlib.pyplot as plt
myFile = open("courseStudents.txt",'r')
labels = myFile.readline().split(" ")
xlabel = labels[0]
ylabel = labels[1].replace("\n","")
x = []
y = []
val = ""
valuesl = ""
for i in range(0,5):
    values = myFile.readline().split(" ")
    x.append(values[0])
    y.append(values[1])
for i in range(0,len(y)):
    if i!=len(y)-1:
        l=len(y[i])
        y[i]= int(y[i][0:l-1])
    else:
        y[i]=int(y[i])
print(y) 
z=[3,2,3,4,1]
plt.bar(x,y,label = "students",color='b',width=0.4)
plt.bar(x,z,label="teachers",color='r')
plt.legend()
plt.title(xlabel + ' vs '+ ylabel)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()


# In[ ]:





# In[ ]:




