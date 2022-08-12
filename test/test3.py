db = 2



class Repository:
    def __init__(self):
        self.get = PGRepository()

class PGRepository:
    def __init__(self):
        self.db = db
    
    def account(self):
        return 1 + self.db



repo = Repository()

print(repo)
print(repo.__dict__)
print(repo.get.account())
print(repo.__dict__)

