import json

def max_revenue(movies):
    pass
    # 여기에 코드를 작성합니다.
    revenue = [0]
    ids = [0]
    for movie in movies:
        # 각 요소의 id값을 mid에 저장한다.
        mid = movie.get('id')
        # mid를 f스트링을 사용하여 각 세부내역들을 확인한다.
        ids_json = open(f'data/movies/{mid}.json', encoding='UTF8')
        ids_list = json.load(ids_json)
        a = ids_list.get('revenue')
        b = ids_list.get('id')
        if a > revenue[0]:
            revenue[0] = a
            ids[0] = b
    for i in range(len(movies)):
        
        title = movies[i].get('title')
        movie_id = movies[i].get('id')
        if ids[0] == movie_id:
            return title
    
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    
    print(max_revenue(movies_list))
    