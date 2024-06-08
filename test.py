import requests

def get_movie_data(api_key):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    api_key = '2123ae880ddb82d7f86b90eef77fe95f'
    movie_data = get_movie_data(api_key)
    if movie_data:
        print("Movie data retrieved successfully:")
        for movie in movie_data['results']:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}, Overview: {movie['overview']}")
    else:
        print("Failed to retrieve movie data.")
