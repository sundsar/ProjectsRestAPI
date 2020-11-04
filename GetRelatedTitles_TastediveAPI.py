import requests


def get_movies_from_tastedive(name):
    """
    Takes in a string that is name of a movie and returns a dict that is
    TasteDive results that are associated with that string
    """
    from mykeysmodule import mykeys
    mykeys['q'] = name
    baseurl = "https://tastedive.com/api/similar"
    paramdict = mykeys
    resp = requests.get(baseurl, paramdict)
    pyobj = resp.json()
    return pyobj


def extract_movie_titles(dictionary):
    """
    Takes in the dictionary returned by get_movies_from_tastedive() and returns a list of movie titles
    """
    results = dictionary['Similar']['Results']
    lstmt = [d['Name'] for d in results]
    return lstmt


def get_related_titles(lstmt):
    """
    Takes in the list returned by extract_movie_titles(), gets related movies for each list item,
    appends all the titles into one single list and returns the final list
    """
    lst = []
    for mtitle in lstmt:
        dtitle = get_movies_from_tastedive(mtitle)
        mlst = extract_movie_titles(dtitle)
        for movie in mlst:
            if movie not in lst:
                lst.append(movie)
    return lst


movie_name = input("Enter a movie Title: ")
print(get_related_titles(extract_movie_titles(
    get_movies_from_tastedive(movie_name))))
