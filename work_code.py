# -*- coding: utf-8 -*-
"""十進位數字轉換成二進位與16進位.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mi44UX_E1wphprF0EVhnIAnQ5zOJroqU
"""

num2 = int(input("輸入數字0-255: "))
num16 = num2
Character16 = "0123456789ABCDEF"
answer2 = ""
answer16 = ""

if num2 == 0:
  answer2 = answer16 = "0"
  print("二進位是",answer2)
  print("十六進位是",answer16)
else:
  for i in range(7, -1, -1):
    if num2 >= 2**i:
      answer2 += "1"
      num2 -= 2**i
    else:
      answer2 += "0"
  print("二進位是",answer2.lstrip('0'))

  for i in range(1, -1, -1):
    if num16 >= 16**i:
      answer16 += Character16[num16 // 16**i % 16]
      num16 -= (num16 // 16**i) * 16**i
    else:
      answer16 += "0"
  print("十六進位是",answer16.lstrip('0'))