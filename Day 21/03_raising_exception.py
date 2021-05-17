def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Ayush")    

a = increment(45)
print(a)