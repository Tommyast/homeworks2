from fake_math4_1 import divide as f_div
from true_math4_1 import divide as t_div

f_div(12, 0)
t_div(34, 0)

result1 = f_div(69, 3)
result2 = f_div(3, 0)
result3 = t_div(49, 7)
result4 = t_div(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)