# https://quera.org/college/3078/chapter/8684/lesson/29954/?comments_page=2&comments_filter=ALL&submissions_page=1

all_users = {}
all_albums= {}

def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = {
        'username': username,
        'age': age,
        'city': city,
        'albums': albums,
    }
def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = {
        'name': name,
        'artist name': artist_name,
        'genre': genre,
        'tracks': tracks,
    }

def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    x = 0
    for album_name, album_details in all_albums.items():
        if album_details['artist name'] == artist_name:
            if album_name in all_users[username]['albums']:
                x += album_details['tracks']
    return x

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    x = 0
    for album_name, album_details in all_albums.items():
        if album_details['genre'] == genre:
            if album_name in all_users[username]['albums']:
                x += album_details['tracks']         
    return x
    
def query_age_artist(age, artist_name, all_users, all_albums):
    x = 0
    for user_name, user_details in all_users.items():
        if user_details['age'] == age:
            for album_name, album_details in all_albums.items():
                if album_details['artist name'] == artist_name:
                    for j in all_users[user_name]['albums']:
                        if album_name == j:
                            x += album_details['tracks']        
    return x

def query_age_genre(age, genre, all_users, all_albums):
    x = 0
    for user_name, user_details in all_users.items():
        if user_details['age'] == age:
            for album_name, album_details in all_albums.items():
                if album_details['genre'] == genre:
                    if album_name in all_users[user_name]['albums']:
                        x += album_details['tracks']        
    return x

def query_city_artist(city, artist_name, all_users, all_albums):
    x = 0
    for user_name, user_details in all_users.items():
        if user_details['city'] == city:
            for album_name, album_details in all_albums.items():
                if album_details['artist name'] == artist_name:
                    for j in all_users[user_name]['albums']:
                        if album_name == j:
                            x += album_details['tracks']        
    return x
    
def query_city_genre(city, genre, all_users, all_albums):
    x = 0
    for user_name, user_details in all_users.items():
        if user_details['city'] == city:
            for album_name, album_details in all_albums.items():
                if album_details['genre'] == genre:
                    for j in all_users[user_name]['albums']:
                        if album_name == j:
                            x += album_details['tracks']        
    return x
