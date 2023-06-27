import random

fishes = ['고등어','갈치','가다랑어','꽁치','날치','노가리','명태',
          '은어','전어','개복치','정어리','멸치','청어','참치',
          '우럭','도미','무지개송어','숭어','연어','농어','장어',
          '넙치','문어','오징어','복어','해삼','말미잘','멍게',
          '피라미','잉어','붕어','메기','금붕어','송사리','바닷가재',
          '게','미꾸라지','바다거북','자라','피라냐','금태',
          '해파리','클리오네','도루묵','조기','대구','아귀','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어','인어',
          '가리비','바지락','산호','백산호','빙어','칠성장어',
          '고래상어','철갑상어','실러캔스','피라루쿠','청상아리',
          '청새치','킹크랩','거대오징어','크라켄','대왕참치','불가사리',
          '새우','미역','다시마','녹조류','직박구리 씨',
          '쓰레기','돌멩이','유리병','1아티','실패','직박구리 씨',
          '쓰레기','돌멩이','유리병','1아티','실패']

text1 =''
text2 =''


def fishresult():
    fish_result = random.choice(fishes)
    fsize = random.randrange(1,101)
    text1 =''
    text2 =''

    if fish_result == '실패':
        text1 = '이런!'
        text2 = '물고기가 도망갔다. 아무것도 낚지 못했다...'

    elif fish_result == '직박구리 씨':
        text1 = '바닷속을 점검하던 직박구리 씨?!'
        text2 = '\"삐이이익!!!! 파티서펀트!!!!! 이것은 공무집행방해입니다!!!!\" 직박구리 씨는 호통을 치고 날아갔다...'

    elif fish_result == '쓰레기' or fish_result =='돌멩이' or fish_result =='1아티' or fish_result =='유리병':
        text1 = fish_result+'을(를) 낚았다!'
        text2 = '물고기가 아니잖아!'

    elif fish_result == '인어':
        mermaidtems = ['진주','무섭게 생긴 보라색 문어','알록달록한 작은 문어','검은 진주','녹슨 코니콘 주화']
        mermaidtem = random.choice(mermaidtems)

        text1 = '인어를 낚았다...?'
        text2 = '\"어머, 육지의 아이잖아. 나와 거래하지 않을래? 네가 가지고 있는 아티를 하나 주면 좋은 걸 줄게. 이거 봐, 바다속에만 있는 거다?\" 인어는 그렇게 말하며 '+mermaidtem+'를 꺼내들었다.'

    elif fish_result == '고래상어' or fish_result =='철갑상어' or fish_result =='실러캔스' or fish_result =='피라루쿠' or fish_result =='청상아리' or fish_result =='청새치' or fish_result =='킹크랩' or fish_result =='거대오징어' or fish_result =='크라켄'or fish_result == '대왕참치':
        fsize = fsize + 100

        text1 = fish_result+'을(를) 낚았다!'
        text2 = '성과 기록: 무려 '+str(fsize)+'cm?!'
    
    else:
        text1 = fish_result+'을(를) 낚았다!'
        text2 = '성과 기록: '+str(fsize)+'cm'

    return text1, text2
