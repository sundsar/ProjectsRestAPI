import requests
import json

def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    paramdict = {'q': name , 'type': 'movies', 'limit': 5,'k' : '373314-Coursera-EE57IXJZ' }
    resp = requests.get(baseurl,paramdict)
    #print(resp.url)
    pyobj = resp.json()
    return pyobj

def extract_movie_titles(dictionary):
    results = dictionary['Similar']['Results']
    lstmt = [d['Name'] for d in results]
    return lstmt

def get_related_titles(lstmt):
    lst = []
    for mtitle in lstmt:
        dtitle = get_movies_from_tastedive(mtitle)
        #print(dtitle)
        mlst = extract_movie_titles(dtitle)
        #print(mtitle,mlst)
        for movie in mlst:
            if movie not in lst:
                lst.append(movie)
    return lst

dictionary = get_movies_from_tastedive('Black Panther')
lstmt = extract_movie_titles(dictionary)
print(get_related_titles(lstmt))
