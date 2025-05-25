import requests
import json
import time
import os
from datetime import datetime

class NaverLandCrawler:
    def __init__(self):
        self.cookies = {
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

        self.headers = {
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
        
        self.base_url = 'https://new.land.naver.com/api/regions/list'
        self.result_dir = 'results'
        
        # 결과 디렉토리 생성
        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

    def get_region_data(self, cortar_no='0000000000'):
        """지정된 지역 코드에 대한 하위 지역 정보를 가져옵니다."""
        params = {'cortarNo': cortar_no}
        
        try:
            response = requests.get(
                self.base_url, 
                params=params, 
                cookies=self.cookies, 
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"오류 발생 (지역 코드: {cortar_no}): {e}")
            return None

    def crawl_recursively(self, cortar_no='0000000000', depth=0, max_depth=2):
        """재귀적으로 지역 데이터를 수집합니다."""
        if depth > max_depth:
            return {}
            
        data = self.get_region_data(cortar_no)
        if not data or 'regionList' not in data:
            return {}
            
        result = {
            'current': data,
            'children': {}
        }
        
        # 과도한 요청 방지를 위한 딜레이
        time.sleep(1)
        
        # 하위 지역이 있으면 재귀적으로 수집
        if depth < max_depth:
            for region in data.get('regionList', []):
                child_cortar_no = region.get('cortarNo')
                if child_cortar_no and child_cortar_no != cortar_no:
                    print(f"{'  ' * depth}수집 중: {region.get('cortarName')} ({child_cortar_no})")
                    result['children'][child_cortar_no] = self.crawl_recursively(
                        child_cortar_no, depth + 1, max_depth
                    )
        
        return result

    def save_to_file(self, data, filename=None):
        """수집한 데이터를 파일로 저장합니다."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.result_dir}/region_data_{timestamp}.json"
            
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"데이터가 {filename}에 저장되었습니다.")
        return filename

def main():
    crawler = NaverLandCrawler()
    
    print("네이버 부동산 지역 정보 수집을 시작합니다...")
    
    # 전국 단위 데이터 수집 (depth 2 - 구/군 단위까지)
    all_data = crawler.crawl_recursively(max_depth=2)
    
    # 데이터 저장
    saved_file = crawler.save_to_file(all_data)
    
    print(f"모든 지역 데이터 수집이 완료되었습니다.")
    print(f"결과 파일: {saved_file}")
    
    # 수집된 데이터 중 첫 번째 레벨의 지역 목록만 출력
    if all_data and 'current' in all_data and 'regionList' in all_data['current']:
        regions = all_data['current']['regionList']
        print("\n수집된 주요 지역 목록:")
        for region in regions:
            print(f"- {region['cortarName']} (코드: {region['cortarNo']})")

if __name__ == "__main__":
    main() 