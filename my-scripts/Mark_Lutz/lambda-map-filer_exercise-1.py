#!/usr/bin/python3.4

'''
Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 

Order Number  Book Title and Author Quantity  Price per Item
34587 Learning Python, Mark Lutz  4 40.95
98762 Programming Python, Mark Lutz 5 56.80
77226 Head First Python, Paul Barry 3 32.95
88112 Einführung in Python3, Bernd Klein  3 24.99


Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
Write a Python program using lambda and map.
'''

book_list = [ [34587,'Learning Python, Mark Lutz',4,40.95],
              [98762,'Programming Python, Mark Lutz',5,56.80],
              [77226,'Head First Python, Paul Barry',3,32.95],
              [88112,'Einführung in Python3, Bernd Klein',3,24.99]
            ]

min_order = 100

res_list = list(map(lambda x:(x[0],(x[2]*x[3])+10) if(x[2]*x[3] < min_order)  else (x[0],x[2]*x[3]),book_list))
print(res_list)

res_list = list(map(lambda x:(x[0],x[1] + 10) if(x[1] < min_order)  else (x[0],x[1]),
                        map(lambda x:(x[0],x[2]*x[3]),book_list)))
print(res_list)

res_list = [ (x[0],(x[2]*x[3])+10) if(x[2]*x[3] < min_order)  else (x[0],x[2]*x[3])  for x in book_list ]
print(res_list)


