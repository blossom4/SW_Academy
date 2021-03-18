import json

def dec_movies(movies):
    title_list = []
    for i in range(len(movies)):
        month = movies[i].get('release_date')
        if '-12-' in month:
            title = movies[i].get('title')
            title_list.append(title)
    return title_list
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))