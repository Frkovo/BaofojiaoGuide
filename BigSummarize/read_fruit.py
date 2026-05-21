fruit = []

def read_fruit():
    global fruit
    try:
        fp = open("./Fruit.txt", "r")
        line = fp.readline()
        while line:
            fruit.append(line.strip())
            line = fp.readline()
        fp.close()
    except IOError:
        print("Cannot find fruit file.")

read_fruit()
print(fruit)
