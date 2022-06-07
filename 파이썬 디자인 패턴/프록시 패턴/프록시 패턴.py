class Actor:
    def __init__(self, actor_name):
        self.isBusy = False
        self.name = actor_name
    
    def occupied(self):
        self.isBusy = True
        print(f"우리 {self.name}이는 현재 다른 스케줄이 있습니다.")

    def available(self):
        self.isBusy = False
        print(f"우리 {self.name}이는 현재 출연 가능합니다.")
        self.isBusy = True

    def getStatus(self):
        return self.isBusy

class Agent:
    def __init__(self, actor_name):
        self.principal = None
        self.actor = Actor(actor_name)

    def work(self):
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    deoksoon_manager = Agent("덕순")
    deoksoon_manager.work()
    deoksoon_manager.work()

"""
# 결과 값.
우리 덕순이는 현재 출연 가능합니다.
우리 덕순이는 현재 다른 스케줄이 있습니다.
"""