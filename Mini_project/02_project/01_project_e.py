import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    # URLMaker class의 get_url 함수에서 API키값을 더하고,
    k1 = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    # 원하는 정보주소에 맞게 매개변수를 지정해서 key와value를 쌍으로 가져온다.
    movie_id = k1.movie_id(title)
    # id가 존재한다면, credits의 정보를 받아서 json파일을 읽을 수 있게 저장한다.
    if movie_id:
        crd = k1.get_url('movie', f'{movie_id}/credits', region='KR', language='ko')
        res = requests.get(crd)
        b = res.json()
        cast_lst = []
        crew_lst = []
        # 'cast_id'의 value값이 10보다 작은 경우 리스트에 'name'의 value값을 더한다.
        for i in b.get('cast'):
            if i.get('cast_id') < 10:
                cast_lst.append(i.get('name'))
        # department의 value가 Directing이면 'name'의 value값을 리스트에 더한다.
        for j in b.get('crew'):
            if j.get('department') == 'Directing':
                crew_lst.append(j.get('name'))
        # 두 리스트를 value 값으로 갖는 dictionary를 반환
        return {
            'cast' : cast_lst,
            'crew' : crew_lst
        }
            


if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None