import numpy as np

def Union(a,b):
	c={}
	for i in a:
		c[i]=max(a[i],b[i])
	return c
	
def Intersection(a,b):
	c={}
	for i in a:
		c[i]=min(a[i],b[i])
	return c	
	
def Complement(a):
	c={}
	for i in a:
		c[i]=round(1-a[i],2)
	return c	

def Difference(a,b):
	c={}
	for i in a:
		c[i]=min(a[i],round(1-b[i],2))
	return c	

def Catesian_Product(a,b):
	c=[]
	for i in a:
		d=[]
		for j in b:
			d.append(min(a[i],b[j]))
		c.append(d)	
	return c		

def Max_Min(a,b):
	c=[]
	for i in range(len(a)):
		d=[]
		for j in range(len(b[0])):
			e=[]
			for k in range(len(b)):
				e.append(min(a[i][k],b[k][j]))
			d.append(max(e))
		c.append(d)
	return c			


a = {"x1": 0.3, "x2": 0.5, "x3":0.12, "x4":0.73}
b = {"x1": 0.8, "x2": 0.2, "x3":1.0, "x4":0.45}

S= [[0.2, 0.7, 0.0, 0.55], [0.2, 0.5, 0.0, 0.5], [0.2, 0.8, 0.0, 0.55], [0.2, 0.27, 0.0, 0.27]]

print("Fuzzy Set A is:",a)
print("Fuzzy Set B is:",b)
print("\n")
print("Union of Set A and B:\n",Union(a,b))
print("Intersection of Set A and B:\n",Intersection(a,b))
print("Complement of Set A:\n",Complement(a))
print("Complement of Set B:\n",Complement(b))
print("Difference of Set A and B:\n",Difference(a,b))
print("Fuzzy Relation by Catesian Product:\n",Catesian_Product(a,b))
print("Max_Min Operation:\n",Max_Min(Catesian_Product(a,b),S))
print("\n")