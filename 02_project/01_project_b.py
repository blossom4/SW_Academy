import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    # URLMaker class의 get_url 함수에서 API키값을 더하고,
    url = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    # 원하는 정보주소에 맞게 매개변수를 지정해서 key와value를 쌍으로 가져온다.
    movie = url.get_url('movie', 'popular')
    # 원하는 정보를 받아서 json파일을 읽을 수 있게 저장한다.
    res = requests.get(movie)
    read_res = res.json()
    # 'results'에 해당하는 value값을 저장한다.
    movie_lst = read_res.get('results')
    # 8점 이상 리스트  정의
    eight_lst = []
    # movie_lst의 길이만큼 반복한다.
    for i in range(len(movie_lst)):
        # 리스트의 vote_average의 value 값이 8이상이면 eight_lst에 더한다.
        if movie_lst[i].get('vote_average') >= 8:
            eight_lst.append(movie_lst[i])
    
    return eight_lst


if __name__ == '__main__':
    pprint(vote_average_movies())    
