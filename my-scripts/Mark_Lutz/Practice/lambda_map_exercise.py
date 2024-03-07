'''
Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

Order Number    Book Title and Author   Quantity    Price per Item
34587   Learning Python, Mark Lutz  4   40.95
98762   Programming Python, Mark Lutz   5   56.80
77226   Head First Python, Paul Barry   3   32.95
88112   Einführung in Python3, Bernd Klein  3   24.99


Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10 if the value of the order is smaller than 100,00.
Write a Python program using lambda and map.
'''

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

result = [(order[0],order[2]*order[3]) if order[2]*order[3] > 10000 else (order[0],order[2]*order[3]+10) for order in orders ]
print(result)

res = list(map((lambda x:(x[0],x[2]*x[3]) if x[2]*x[3] > 10000 else (x[0],x[2]*x[3]+10)),orders))
print(res)
