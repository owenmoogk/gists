import torch

# x = torch.ones(2,2)
# y = torch.rand(2,2)
# print(y)
# print(y[0,0])

import numpy as np

# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b)
# print(type(a), type(b))

# if torch.cuda.is_available():
#     print('true')
# else:
#     print('nah')

# gradients
# x = torch.ones(5, requires_grad=True)
# print(x)

# x = torch.randn(3, requires_grad=True)
# print(x)

# GRADIENT CALCULATION
x = torch.randn(3, requires_grad=True)
print(x)
y = x+2
print(y)
z = y*y+2

print(y.grad_fn())
print(x.grad)