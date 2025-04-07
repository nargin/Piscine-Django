def my_var():
    x0a = 42
    x0b = "42"
    x0c = "quarante-deux"
    x0d = 42.0
    x0e = True
    x0f = [42]
    x10 = {42: 42}
    x11 = (42,)
    x12 = set()

    print(f"{x0a} est de type {type(x0a)}")
    print(f"{x0b} est de type {type(x0b)}")
    print(f"{x0c} est de type {type(x0c)}")
    print(f"{x0d} est de type {type(x0d)}")
    print(f"{x0e} est de type {type(x0e)}")
    print(f"{x0f} est de type {type(x0f)}")
    print(f"{x10} est de type {type(x10)}")
    print(f"{x11} est de type {type(x11)}")
    print(f"{x12} est de type {type(x12)}")

if __name__ == "__main__":
    my_var()