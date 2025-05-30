# 네이버 부동산 지역 정보 크롤러

이 프로젝트는 네이버 부동산 API를 사용하여 지역 목록 정보를 가져오는 파이썬 스크립트입니다.

## 설치 방법

1. 필요한 패키지 설치:
```
pip install -r requirements.txt
```

## 사용 방법

### 기본 사용법
다음 명령어로 기본 스크립트를 실행합니다:
```
python main.py
```

실행 결과로 네이버 부동산의 지역 목록 데이터가 JSON 형식으로 출력됩니다.

### 재귀적 크롤링
더 발전된 재귀적 크롤링을 위해 다음 명령어를 실행합니다:
```
python crawler.py
```

이 스크립트는:
1. 전국 단위의 지역 정보를 수집합니다 (시/도 단위까지)
2. 각 지역에 대한 하위 지역 정보를 재귀적으로 수집합니다
3. 수집된 데이터를 `results` 폴더에 JSON 파일로 저장합니다
4. 수집된 주요 지역 목록을 콘솔에 출력합니다

## 주의사항
- API 요청 시 사용되는 인증 토큰과 쿠키는 유효 기간이 있습니다.
- 필요에 따라 `crawler.py` 파일의 인증 정보를 업데이트해야 할 수 있습니다.
- 과도한 요청은 IP 차단을 유발할 수 있으니 주의하세요. 