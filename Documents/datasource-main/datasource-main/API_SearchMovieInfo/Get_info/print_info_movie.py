import requests
from Get_info.get_key import GetKeyInfo

from Get_info.imDb_id import IMDbid
from Get_info.versioning_event import VersioningEvent


class PrintInfoMovie:

    def find_rating(moviesearch):
        MovieIdFind=IMDbid.find_id(moviesearch)
        _find_url='https://imdb-api.com/en/API/Ratings/'+"k_dz8a6i8j"+'/'+MovieIdFind
        response =  requests.get(_find_url)
        return VersioningEvent(status_code=response.status_code, content=response.json())

    def find_image(moviesearch):
        MovieIdFind=IMDbid.find_id(moviesearch)
        _find_url='https://imdb-api.com/en/API/Title/'+"k_dz8a6i8j"+'/'+MovieIdFind+'/Image'
        response =  requests.get(_find_url)
        return VersioningEvent(status_code=response.status_code, content=response.json())
    