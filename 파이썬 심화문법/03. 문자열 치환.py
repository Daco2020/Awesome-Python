'''
translate는 문자만 변환 합니다. 
예를들어 "Hello, World!"가 있을 경우 H는 숫자 1로, W는 숫자 2로, d는 숫자 3으로 등 지정한 문자를 특정 문자로 변환 시킬 수 있습니다. 
아래와 같이 코드를 작성 하면 변환된 "1ello, 2orl3!" 문자열이 출력 됩니다.
'''

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))


hi = "Hello, World!" 
table = str.maketrans('HWd', '123') 
hi.translate(table)

'''
translate는 문자열을 바꿔주는 메서드입니다. 
인자로 str.maketrans('old','new')를 넣으면 해당 문자열들에 맞춰서 치환해줍니다.
'''