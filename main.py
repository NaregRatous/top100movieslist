import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url, verify=False, timeout=60)


print("BYE222222222")
soup = BeautifulSoup(response.text, 'html.parser')

movie_titles = []

movies = soup.find_all(name='h3', class_='title')
print(movies)
movies_list = []
for movie in movies:
    movies_list.append(movie.getText())

print(movies_list)

with open ("movie_list.txt" , "w", encoding="utf-8") as file:
    for _ in movies_list[::-1]:
        file.write(_ + "\n")


print("BYE")
