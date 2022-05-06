import numpy as np

class mcp:
    def __init__(self,X):
        self.X=X
    
    def sum(self):
        return np.sum(self.X,axis=1)
    
    def func(self,op):
        y=[] 
        if op=="And":
            b=self.X.shape[1]
        elif op=="Not":
            b=0    
        else:
            b=1 
        for i in range(X.shape[0]):
            aggre=self.sum()[i]
            if op=="Not":
                aggre*=-1
            if aggre >= b:
                y.append([1])
            else:
                y.append([0])
        return y

    
n=int(input("Enter no of rows: "))
m=int(input("Enter no of columns: "))
X=np.random.randint(2,size=(n,m))
Y=np.random.randint(2,size=(n,1))
print("\nSample Truth table:\n",X)
print(X.shape)
mcp_obj=mcp(X)
print("\nOuput of And operation:\n",mcp_obj.func("And"))
print("\nOuput of Or operation:\n",mcp_obj.func("Or"))
print("\nSample Truth table for Not operation:\n",Y)
mcp_obj_not=mcp(Y)
print("\nOuput of Not operation:\n",mcp_obj_not.func("Not"))
print("")   

