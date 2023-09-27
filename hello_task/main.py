def train():
    import os
    x = 3
    y = 10

    if x < y:
        print (x)
        return False
    else:
        print (y)
        return True

if __name__ == '__main__':
    result = train()
    print(result)

