def attention(f):

    def wrapper(*args, **kwargs):
        print "Hey, guys, attention please!"
        f(*args, **kwargs)

    return wrapper


def bread_decor(bread_type=""):
    def bread(f):
        def wrapper(*args, **kwargs):
            print (bread_type + " bread").strip()
            f()
            print (bread_type + " bread").strip()

        return wrapper

    return bread
