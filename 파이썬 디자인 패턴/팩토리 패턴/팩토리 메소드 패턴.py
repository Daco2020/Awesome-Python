from abc import abstractmethod


# Product 인터페이스
# Section 추상 클래스
class Section:
    @abstractmethod
    def describe(self):
        pass

# ConcreateProduct 클래스
class PersonalSection(Section):
    def describe(self):
        return "개인정보"

class AlbumSection(Section):
    def describe(self):
        return "앨범"

class CareerSection(Section):
    def describe(self):
        return "커리어"


# Creator 추상 클래스
class Profile:
    def __init__(self):
        self.sections = []
        self.createProfile() # profile 인스턴스 생성과 동시에 메서드를 실행시킨다.

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

# ConcreateCreator 클래스
class linkedin(Profile):
    def createProfile(self): # 해당하는 Section을 sections에 담는다.
        self.addSections(PersonalSection())
        self.addSections(CareerSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


# Creator 클래스를 호출하는 클라이언트
if __name__ == '__main__':
    profile_type = input("어떤 프로필을 만드시겠습니까? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("생성한 프로필", type(profile).__name__)
    print("프로필에 포함된 섹션 ::", [section.describe() for section in profile.getSections()])
    

"""
# 결과1.
어떤 프로필을 만드시겠습니까? [LinkedIn or FaceBook]linkedin
생성한 프로필 linkedin
프로필에 포함된 섹션 :: ['개인정보', '커리어']

# 결과2.
어떤 프로필을 만드시겠습니까? [LinkedIn or FaceBook]facebook
생성한 프로필 facebook
프로필에 포함된 섹션 :: ['개인정보', '앨범']
"""