# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

test_list = [5, 8, 3, 5, 9, 10, 5]
  
print("The original list : " + str(test_list))
  
res = [i * j for i, j in list(zip(test_list, test_list[::-1]))[:4]]
  
print("Pair product of list : " + str(res))