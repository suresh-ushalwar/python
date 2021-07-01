'''# while Loop
variable=initilization
while (Test Condition)
{
	body of Loop
	increment/decremet variable
}

Syntax In Python

while (Test Condition):
	body of Loop
	increment/decremet variable 
else:
	code for false while_Condition
# Example


i = 1
while (i < 6):
  print(i)
  i += 1
else:
	print("No more elements to iterate")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
else:
	print("No more elements to iterate")


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


 #2 for Loop
  #Syntax In Python
 for elements in sequence:
 	body of Loop
 else:
 	code when no item in sequence


for(initilization,Condition,increment/decremet)
{
	
	body of 
}
#Example

fruits=["mango","bananna","apple"]
for ele in fruits:
	#print(ele)
	#if ele=="bananna":
		#continue
	print(ele)
else:
	print("No more elements in list ")
list1=[10,20,30,40]
pro=1
for ele in list1:
	pro=pro*ele
print("Product of elements in list=",pro)

i=0
while i<10:
	print("HI..")
	i=i+1

for ele in range(5,10,2):  
	print("Hi",ele)
#------(0,1,2,3,4,5,6,7,8,9)'''


number=int(input("ENter any Integer Number:"))
if(number%7==0):
	print("Given Number is Divisible by 7")
else:
	print("Given Number is Not Divisible by 7")