# decorator

'''
1. 붙이는 함수가 func파라미터로 들어온다.
2. 내부 함수가 실행되고 기존 함수가 실행된다.
    기존 함수가 데코레이터 함수에 먹히는 느낌.
3. 최종 결과를 받환한다. 
'''

def copyright(func): 
    def new_func():
        print("@ daco")
        return func()
        
    return new_func


@copyright
def smile():
    print("😀")


@copyright
def angry():
    print("😕")


@copyright
def love():
    print("🥰")


smile()
angry()
love()


'''
실행결과

@ daco
😀
@ daco
😕
@ daco
🥰
'''