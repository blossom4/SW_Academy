import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    # URLMaker class의 get_url 함수에서 API키값을 더하고,
    k1 = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    # 원하는 정보주소에 맞게 매개변수를 지정해서 key와value를 쌍으로 가져온다.
    movie_id = k1.movie_id(title)
    # id가 존재한다면, recommendations의 정보를 받아서 json파일을 읽을 수 있게 저장한다.
    if movie_id:
        re_info = k1.get_url('movie', f'{movie_id}/recommendations', region='KR', language='ko')
        res = requests.get(re_info)
        b = res.json()
        m_lst = b.get('results')
        titles = []
        # recommendations(dict)에서 'title'에 해당하는 요소들을 title리스트에 더한다.
        for i in range(len(m_lst)):
            titles.append(m_lst[i].get('title'))

        return titles
    # id가 없을 경우 None 반환
    return None
         

if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
