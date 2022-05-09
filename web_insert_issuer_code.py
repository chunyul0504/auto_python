# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 매핑코드 web에 생성할때 사용. 카드사코드/은행코드.
# 매핑 완료 되면 tab-db에는 따로 insert 해줘야함.

# 개발
url = 'http://172.16.6.30:40100/'
user_id = 'sjchoi'
user_pw = 'wheein0417**'
user_otp = '1234'
# 운영
# url = 'http://172.16.2.10:40100/'
# user_id = 'kanak'
# user_pw = 'zjspr1101!'
# user_otp = '1234'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
time.sleep(1)

# 로그인
driver.find_element(By.ID, 'user_id').send_keys(user_id)
time.sleep(1)

driver.find_element(By.ID, 'user_passwd').send_keys(user_pw)
time.sleep(1)

driver.find_element(By.ID, 'loginBtn').click()
time.sleep(2)

if driver.find_element(By.ID, 'defaultModal-ok'):
    driver.find_element(By.ID, 'defaultModal-ok').click()

driver.find_element(By.ID, 'otp_seckey').send_keys(user_otp)
time.sleep(1)

driver.find_element(By.ID, 'BTN_OTP_AUTH').click()
time.sleep(2)

driver.find_element(By.ID, 'defaultModal-close').click()
time.sleep(3)

# 원천사 정보 관리 진입
driver.find_element(By.XPATH, '//*[@id="menuList"]/li[1]/a').click()
time.sleep(0.5)


driver.find_element(By.XPATH, '//*[@id="MENU_100102"]/li[2]/a').click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="MENU_100107"]').click()
time.sleep(1)

# 원천사 조회
driver.find_element(By.ID, 'BTN_OPTRMGMT_SEARCH').click()
time.sleep(1)

# 원천사 등록 시작 반복
# 은행에 법인 선택하게 되어있음.
# 주의 (code_list = name_list) 개수가 같아야함.
# code_list = ['300206', '300207', '300208', '300209', '300210', '300211', '300212', '300213', '300214', '300215', '300216', '300217', '300218', '300219', '300220', '300221', '300222', '300223', '300224', '300225', '300226', '300227', '300228', '300229', '300230', '300231', '300232', '300233', '300234', '300235', '300236', '300237', '300238', '300239', '300240', '300241', '300242', '300243', '300244', '300245', '300246', '300247', '300248', '300249', '300250', '300251', '300252', '300253', '300254', '300255', '300256', '300257', '300258', '300259', '300260', '300261', '300262', '300263', '300264', '300265', '300266', '300267', '300268', '300269', '300270', '300271', '300272']
# name_list = ['주택', '수협', '수출입은행', '농협(10)', '농협중앙', '단위농협', '농협(13)', '농협(14)', '농협(15)', '농협(16)', '농협(17)', '국민', '우리', '조흥', '제일', '서울', '신한', '한미', '대구', '부산', '광주', '제주', '전북', '경남', '새마을금고', '신협', '상호저축은행', '모건스탠리은행', '시티', 'HSBC은행', '도이치은행', '에이비엔암로은행', 'JP모간체이스은행', '미즈호코퍼레이트은행', '미쓰비시도쿄UFJ은행', 'BOA', '우체국', '하나', '신한통합', '금결원(직불)', '동양종합금융증권', '현대증권', '미래에셋증권', '삼성증권', '한국투자증권', '우리투자증권', '교보증권', '하이투자증권', 'HMC투자증권', '키움증권', '이트레이드증권', 'SK증권', '대신증권', '솔로몬투자증권', '한화증권', '하나대투증권', '굿모닝신한증권', '동부증권', '유진투자증권', '메리츠증권', 'NH투자증권', '부국증권', '신영증권', 'LIG투자증권', '직불공통', '케이뱅크', '카카오뱅크']

code_list = [
     '300001'
    , '300002'
    , '300003'
    , '300004'
    , '300005'
    , '300008'
    , '300009'
    , '300010'
    , '300011'
    , '300012'
    , '300013'
    , '300014'
    , '300015'
    , '300016'
    , '300017'
    , '300018'
    , '300019'
    , '300020'
    , '300021'
    , '300022'
    , '300023'
    , '300024'
    , '300025'
    , '300026'
    , '300029'
    , '300030'
    , '300036'
    , '300039'
    , '300040'
    , '300041'
    , '300042'
    , '300047'
    , '300050'
    , '300051'
    , '300079'
    , '300084'
    , '300085'
    , '300099'
    , '3000GT'
    , '300100'
    , '300101'
    , '300102'
    , '300103'
    , '300104'
    , '300201'
    , '300202'
    , '300203'
    , '300204'
    , '300205'
    , '300206'
    , '300207'
    , '300208'
    , '300209'
    , '300210'
    , '300211'
    , '300212'
    , '300213'
    , '300214'
    , '300215'
    , '300216'
    , '300217'
    , '300218'
    , '300219'
    , '300220'
    , '300221'
    , '300222'
    , '300223'
    , '300224'
    , '300225'
    , '300226'
    , '300227'
    , '300228'
    , '300229'
    , '300230'
    , '300231'
    , '300232'
    , '300233'
    , '300234'
    , '300235'
    , '300236'
    , '300237'
    , '300238'
    , '300239'
    , '300240'
    , '300241'
    , '300242'
    , '300243'
    , '300244'
    , '300245'
    , '300246'
    , '300247'
    , '300248'
    , '300249'
    , '300250'
    , '300251'
    , '300252'
    , '300253'
    , '300254'
    , '300255'
    , '300256'
    , '300257'
    , '300258'
    , '300259'
    , '300260'
    , '300261'
    , '300262'
    , '300263'
    , '300264'
    , '300265'
    , '300266'
    , '300267'
    , '300268'
    , '300269'
    , '300270'
    , '300271'
    , '300272'

]
name_list = [
     '비씨카드'
    ,'국민카드'
    ,'외환카드'
    ,'삼성카드'
    ,'신한카드'
    ,'현대카드'
    ,'롯데아멕스'
    ,'구신한카드'
    ,'씨티(구.한미)'
    ,'수협'
    ,'신세계한미'
    ,'우리(구평화)'
    ,'농협(구축협)'
    ,'제주은행'
    ,'광주은행'
    ,'전북은행'
    ,'조흥은행'
    ,'롯데카드'
    ,'롯데카드'
    ,'산업은행'
    ,'주택은행'
    ,'하나은행'
    ,'해외카드사'
    ,'씨티(구.씨티)'
    ,'OK캐쉬백'
    ,'경인에너지'
    ,'KT멤버십'
    ,'SK기프티콘'
    ,'큐피콘'
    ,'쿠프마케팅'
    ,'LGU+멤버십'
    ,'피자헛멤버십&쿠폰'
    ,'카카오카드'
    ,'카카오머니'
    ,'위쳇페이'
    ,'SSG머니'
    ,'알리페이'
    ,'기타'
    ,'KT기프티쇼'
    ,'현대백화점'
    ,'레일플러스'
    ,'롯데LPOINT'
    ,'휴대폰-다날'
    ,'휴대폰-모빌리언스,페이레터'
    ,'한국은행'
    ,'산업은행'
    ,'기업'
    ,'국민'
    ,'외환'
    ,'주택'
    ,'수협'
    ,'수출입은행'
    ,'농협(10)'
    ,'농협중앙'
    ,'단위농협'
    ,'농협(13)'
    ,'농협(14)'
    ,'농협(15)'
    ,'농협(16)'
    ,'농협(17)'
    ,'국민'
    ,'우리'
    ,'조흥'
    ,'제일'
    ,'서울'
    ,'신한'
    ,'한미'
    ,'대구'
    ,'부산'
    ,'광주'
    ,'제주'
    ,'전북'
    ,'경남'
    ,'새마을금고'
    ,'신협'
    ,'상호저축은행'
    ,'모건스탠리은행'
    ,'시티'
    ,'HSBC은행'
    ,'도이치은행'
    ,'에이비엔암로은행'
    ,'JP모간체이스은행'
    ,'미즈호코퍼레이트은행'
    ,'미쓰비시도쿄UFJ은행'
    ,'BOA'
    ,'우체국'
    ,'하나'
    ,'신한통합'
    ,'금결원(직불)'
    ,'동양종합금융증권'
    ,'현대증권'
    ,'미래에셋증권'
    ,'삼성증권'
    ,'한국투자증권'
    ,'우리투자증권'
    ,'교보증권'
    ,'하이투자증권'
    ,'HMC투자증권'
    ,'키움증권'
    ,'이트레이드증권'
    ,'SK증권'
    ,'대신증권'
    ,'솔로몬투자증권'
    ,'한화증권'
    ,'하나대투증권'
    ,'굿모닝신한증권'
    ,'동부증권'
    ,'유진투자증권'
    ,'메리츠증권'
    ,'NH투자증권'
    ,'부국증권'
    ,'신영증권'
    ,'LIG투자증권'
    ,'직불공통'
    ,'케이뱅크'
    ,'카카오뱅크'

]
field_list = [
      'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'card'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
    , 'bank'
]

# 원천사 등록 시작 반복
for code, name, field in zip(code_list, name_list, field_list):
    print('===========================')
    print(code)
    print(name)
    print(field)
    print('===========================')

    # 신규등록 클릭
    driver.find_element(By.ID, 'BTN_OPTRMGMT_NEW').click()
    time.sleep(1)

    # oid = 원천사 ID
    # 기본 채번된거 지우고 등록할 원천사 ID/ 원천사 명 입력
    driver.find_element(By.ID, 'oid').clear()
    driver.find_element(By.ID, 'oid').send_keys(code)
    time.sleep(0.5)
    driver.find_element(By.ID, 'oid_nm').send_keys(name)
    time.sleep(0.5)

    # 원천사 구분 선택(은행 or 카드사)
    driver.find_element(By.ID, 'oid_typebtn').click()
    time.sleep(0.5)

    if field == 'bank':
        driver.find_element(By.XPATH, '//*[@id="oid_typeWrap"]/div/ul/li[2]').click()
    elif field == 'card':
        driver.find_element(By.XPATH, '//*[@id="oid_typeWrap"]/div/ul/li[3]').click()
    else:
        print('필드명 이상함!!! code : '+code+', name : '+name+', field : '+field)
        continue

    time.sleep(0.5)

    # 사업자 구분 선택(법인)
    driver.find_element(By.ID, 'corp_typebtn').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="corp_typeWrap"]/div/ul/li[2]').click()
    time.sleep(0.5)

    # 저장 및 확인
    driver.find_element(By.ID, 'BTN_SAVE').click()
    time.sleep(1)
    driver.find_element(By.ID, 'defaultModal-close').click()
    time.sleep(2)











