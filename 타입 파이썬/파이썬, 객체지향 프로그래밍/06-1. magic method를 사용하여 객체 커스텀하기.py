class Robot:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __call__(self):
        return f"{self.name}이 호출되었습니다."

robot_a = Robot("robot_a")

print(robot_a())

# https://daco2020.tistory.com/279