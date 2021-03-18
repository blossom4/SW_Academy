import requests
from tmdb import URLMaker


def popular_count():
    # URLMaker class의 get_url 함수에서 API키값을 더하고,
    url = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    # 원하는 정보주소에 맞게 매개변수를 지정해서 key와value를 쌍으로 가져온다.
    movie = url.get_url('movie', 'popular')
    # 원하는 정보를 받아서 json파일을 읽을 수 있게 저장한다.
    res = requests.get(movie)
    read_res = res.json()
    # 'results'에 해당하는 value값을 저장한다.
    movie_lst = read_res.get('results')
    # movie_lst의 길이를 반환한다.
    return len(movie_lst)


if __name__ == '__main__':
    print(popular_count())