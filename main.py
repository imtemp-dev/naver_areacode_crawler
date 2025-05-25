import requests
import json

def get_region_list():
    cookies = {
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'nhn.realestate.article.trade_type_cd': '""',
        'nhn.realestate.article.ipaddress_city': '1100000000',
        '_fwb': '1228ESXyx0yhUfRFcmxcDZB.1748138823864',
        'landHomeFlashUseYn': 'Y',
        'NNB': 'YUJNZU2IPMZGQ',
        'SRT30': '1748138824',
        'SRT5': '1748138824',
        'NAC': '7jtSBogQfGUrA',
        'NACT': '1',
        'REALESTATE': 'Sun%20May%2025%202025%2011%3A07%3A09%20GMT%2B0900%20(Korean%20Standard%20Time)',
        '_fwb': '1228ESXyx0yhUfRFcmxcDZB.1748138823864',
        'BUC': 'u6aapYZkoMo9_rem15b2ieSEhW77iCjbxS1tiHTmD8g=',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDgxMzg4MjksImV4cCI6MTc0ODE0OTYyOX0.w2_WPgP306m4Hcpo9b97JRRS07A1YjebOw8m-a6ojPU',
        'dnt': '1',
        'priority': 'u=1, i',
        'referer': 'https://new.land.naver.com/complexes?ms=37.3595704,127.105399,16&a=APT:ABYG:JGC:PRE&e=RETAIL',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    params = {
        'cortarNo': '0000000000',
    }

    url = 'https://new.land.naver.com/api/regions/list'
    
    try:
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # 요청이 성공했는지 확인
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
        return None

def main():
    region_data = get_region_list()
    if region_data:
        print(json.dumps(region_data, indent=4, ensure_ascii=False))
    else:
        print("지역 데이터를 가져오는 데 실패했습니다.")

if __name__ == "__main__":
    main() 