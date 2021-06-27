import requests


class URLMaker:
    # 기본 URL
    url = 'https://api.themoviedb.org/3'

    # 인스턴스 변수 생성
    def __init__(self, key):
        self.key = key
    # 해당 매개변수들을 기본 URL 뒤에 붙여서 최종 URL을 완성하여 반환한다.
    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
        
    # input받은 url에서 json 파일을 읽을 수 있게 저장한다.
    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()
        # 받아온 list내의 dictionary가 값이 있으면 'id'값에 해당되는 value값을 반환
        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        # list내에 요소가 없으면 None 반환
        else:
            return None

# k1 = URLMaker('3772d6f699613e0eeb91c055ec835a35')
# k1.get_url('movie', 'popular')