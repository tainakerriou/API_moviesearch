#from API_SearchMovieInfo.Get_info.imBd_result import IMDbResult

from Get_info.print_info_movie import PrintInfoMovie
from PIL import Image


movieSearchTitle=input("What movie are you looking for ? ")

try:
    print('rate        : '+PrintInfoMovie.find_rating(movieSearchTitle).content['imDb'])
except:
    print("This movies doesn't exist or there is a mistake in the name entered")
try:
    print(PrintInfoMovie.find_image(movieSearchTitle).content['image'])
except:
    print("No display found")
try:
    print('writers     : '+PrintInfoMovie.find_image(movieSearchTitle).content['writers'])
except:
    print("No writers found")
try:
    print('year        : '+PrintInfoMovie.find_image(movieSearchTitle).content['year'])
except:
    print("No year found")
try:
    print('runtime     : '+PrintInfoMovie.find_image(movieSearchTitle).content['runtimeStr'])
except:
    print("No runtime found")

#print(Image.open('https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_Ratio0.6762_AL_.jpg') )