import torch
#创建张量
x = torch.Tensor(2,4)
print(x)
print(x.type())
print(x.dtype)

#Tensor initialize
list = [[1,2,3],[7,3,4],[9,5,6]]
y = torch.Tensor(list)
print(y)
print(y[1][2])
y[1][2] = 666
print(y)
e = torch.eye(5)
r = torch.zeros(3,4)
h = torch.ones(2,3)
ran = torch.rand(3,4)
print(e,'\n',r,'\n',h,'\n',ran)
t = torch.arange(1,4,0.2)
print(t)
t2 = torch.arange(3,9)
print(t2)
print(torch.cuda.is_available())