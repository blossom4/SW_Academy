import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    # URLMaker class의 get_url 함수에서 API키값을 더하고,
    url = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    # 원하는 정보주소에 맞게 매개변수를 지정해서 key와value를 쌍으로 가져온다.
    movie = url.get_url('movie', 'popular')
     # 원하는 정보를 받아서 json파일을 읽을 수 있게 저장한다.
    res = requests.get(movie)
    read_res = res.json()
    # 'results'에 해당하는 value값을 저장한다.
    movie_lst = read_res.get('results')
    # 평점들을 담을 리스트 정의
    avgs = []
    # 최종 결과를 담을 리스트 정의
    final = []
    # 영화리스트의 길이만큼 반복한다.
    for i in range(len(movie_lst)):
        # 'vote_average' 의 value 값을 저장해서 avgs리스트에 더한다.
        avgs.append(movie_lst[i].get('vote_average'))     
        # 점수들을 담은 avgs리스트를 정렬해서 마지막 5개의 요소를 따로 저장한다.
        sorted_lst = sorted(avgs)
        rank = sorted_lst[-5:]
    # 2중 for문을 돌면서 rank에 저장되어있는 5개의 평점과,
    # 'vote_averge'의 value값이 같으면, 영화정보들을 final리스트에 더한다.
    for j in range(len(movie_lst)):
        for k in range(len(rank)):
            if rank[k] == movie_lst[j].get('vote_average'):
                final.append(movie_lst[j])
            
    return final


if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())