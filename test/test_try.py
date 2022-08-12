a = {}


def z():
    try:
        b = a["as"]
        return 1
    except KeyError:
        return 0
    finally:
        a["zxc"] = 1999


print(z(), a)
