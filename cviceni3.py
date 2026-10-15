def my_range_while(start, stop, step=1):
    vysledek = []
    x= start
    while (x < stop if step > 0 else x > stop):
        vysledek.append(x)
        x += step
    return vysledek

def my_enumerate_for(iterable, start=0):
    vysledek = []
    for i in range(len(iterable)):
        vysledek.append((start + i, iterable[i]))
    return vysledek

def my_enumarate_while(iterable, start=0):
    vysledek = []
    i = 0
    while i < len(iterable):
        vysledek.append((start + i, iterable[i]))
        i += 1
    return vysledek

def my_zip(*iterables):
    vysledek = []
    leght= len(iterables[0])
    i= 0
    while i < leght:
        value= []
        for iterable in iterables:
            value.append(iterable[i])
        vysledek.append(tuple(value))
        i += 1
    return vysledek

if __name__ == "__main__":
    print(my_range_while(0, 10))
    print(my_range_while(0, 10, 2))
    print(my_range_while(5, 15, 3))

    print(my_enumerate_for(['a', 'b', 'c']))

    print(my_enumarate_while(['a', 'b', 'c'], start=1))

    iterables= [
            ["Alice", "Bob", "Karel", "Eva", "Martin"],
            [30, 20, 24, 18, 27],
            [50, 80, 90, 55, 67]
        ]
    print("__________")
    vysledek = list(my_zip(*iterables))
    print(vysledek)   
    for jmeno, vek, vaha in my_zip(*iterables):
        print(f"{jmeno} je {vek} let a váží v {vaha} kg.")