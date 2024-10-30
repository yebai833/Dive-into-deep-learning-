import torch

x = torch.arange(12)
# reshape函数
X = x.reshape(3, 4)
print(X)
print(x)
# 全部初始化为1
print(torch.ones((2, 3, 4)))
# 全部初始化为随机数（均值为0，标准差为1的标准高斯分布）
print(torch.randn(3, 4))
# 为所需tensor中的元素赋值
print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))
