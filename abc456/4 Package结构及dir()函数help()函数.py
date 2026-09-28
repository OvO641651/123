import torch

print(torch.cuda.is_available())

#dir()函数：打开torch中的内容（各种方法）
print(dir(torch))

print(dir(torch.cuda.is_available()))

#help()函数：说明书 查看函数的使用方法
help(torch.cuda.is_available)
