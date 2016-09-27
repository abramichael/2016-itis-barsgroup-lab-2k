G = 9.8

def gravity_force(m):
    return m * G

gravity_force = lambda m: m * G

print(gravity_force(78))