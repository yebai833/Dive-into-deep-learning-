import torch

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
# 运算符
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
# 幂运算
print(torch.exp(x))
# 连接多个tensor
a = torch.arange(12, dtype=torch.float32).reshape((3, 4))
b = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
X = torch.cat((a, b), dim=0)  # 沿着第0维连接
Y = torch.cat((a, b), dim=1)  # 沿着第1维连接
print(X)
print(Y)
# 逻辑运算
print(a == b)
print(a > b)
print(a <= b)
