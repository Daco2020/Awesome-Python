## 퍼사드(인터페이스)
class EventManager(object):
    def __init__(self):
        print("웨딩플래너 : 제가 당신을 도와드릴게요.\n\n")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


## 서브시스템(구현)
# 호텔리어 - 호텔 담당
class Hotelier(object):
    def __init__(self):
        print("호텔리어 : 안녕하세요.\n")
    
    def book_hotel(self):
        print("호텔리어 : 예약을 도와드리겠습니다.\n\n")

# 플로리스트 - 꽃 담당
class Florist(object):
    def __init__(self):
        print("플로리스트 : 안녕하세요.\n")

    def set_flower_requirements(self):
        print("플로리스트 : 장미와 백합을 준비하겠습니다.\n\n")

# 요리조달자 - 요리 담당
class Caterer(object):
    def __init__(self):
        print("요리사 : 안녕하세요.\n")

    def set_cuisine(self):
        print("요리사 : 뷔페를 준비하겠습니다.\n\n")

# 음악가 - 연주 담당
class Musician(object):
    def __init__(self):
        print("뮤지션 : 안녕하세요.\n")

    def set_music_type(self):
        print("뮤지션 : 재즈를 준비하겠습니다.\n\n")


## 클라이언트
class You(object):
    def __init__(self):
        print("나 : 결혼식 준비를 해야해!\n")
    def ask_event_manager(self):
        print("나 : 웨딩플래너에게 연락해보자!\n\n")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("나 : 다들 고마워요!\n")

you = You()
you.ask_event_manager()

# 출력 결과

'''
나 : 결혼식 준비를 해야해!
나 : 웨딩플래너에게 연락해보자!

웨딩플래너 : 제가 당신을 도와드릴게요.

호텔리어 : 안녕하세요.
호텔리어 : 예약을 도와드리겠습니다.

플로리스트 : 안녕하세요.
플로리스트 : 장미와 백합을 준비하겠습니다.

요리사 : 안녕하세요.
요리사 : 뷔페를 준비하겠습니다.

뮤지션 : 안녕하세요.
뮤지션 : 재즈를 준비하겠습니다.

나 : 다들 고마워요!
'''