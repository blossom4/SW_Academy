import json
from pprint import pprint


def movie_info(movies, genres):
    
    # 여기에 코드를 작성합니다. 
    total = []
    for index in range(len(movies)):       
        result = {}
        id1 = movies[index].get('id')
        title = movies[index].get('title')
        poster_path = movies[index].get('poster_path')
        vote_average = movies[index].get('vote_average')
        overview = movies[index].get('overview')
        genre_ids = movies[index].get('genre_ids')

        result['id'] = id1
        result['title'] = title
        result['poster_path'] = poster_path
        result['vote_average'] = vote_average
        result['overview'] = overview
        result['genre_ids'] = genre_ids
        
        names = []
        for i in range(len(movies[index].get('genre_ids'))):
            for j in range(len(genres)):
                if genres[j].get('id') == movies[index].get('genre_ids')[i]:
                    names += [genres[j].get('name')]
        result['genre_names'] = result.pop('genre_ids')
        result['genre_names'] = names
        total.append(result)
    return total
            

        
        
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))