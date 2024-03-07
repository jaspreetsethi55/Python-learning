def my_range(num,start=0,interval=1):
    if(interval > 0):
        while(num > start):
            print(start)
            
            start = start + interval
    elif(interval < 0):
        while(num < start):
            print(start)

            start = start + interval



my_range(-10,start=8,interval=-2)
