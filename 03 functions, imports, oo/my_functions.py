from useful_func import attention, bread_decor

@attention
def hello(lastname="Smith", firstname="John"):
    print "Hello, Dear %s %s!" % (firstname, lastname)

def goodbye(lastname="Smith", firstname="John"):
    print "Good bye, Dear %s %s!" % (firstname, lastname)

@bread_decor(bread_type="black")
def cheese_buter():
    print "Cheese"


if __name__ == "__main__":
    hello("Safin", "Aidar")
    hello()
    hello(firstname="Aidar")
    hello(lastname="Safin")