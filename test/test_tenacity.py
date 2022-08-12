import random
from tenacity import retry


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise print("raise up")
    else:
        return "Awesome sauce!"


print(do_something_unreliable())
