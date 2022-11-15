import requests
from Get_info.get_key import GetKeyInfo

from Get_info.versioning_event import VersioningEvent


class IMDbResult:
    
    def get_infos(moviesearch):
        key=GetKeyInfo.get_key()
      #  url = "https://imdb-api.com/en/API/SearchMovie/"+str(GetKeyInfo.get_key())+"/"+moviesearch
        url= "https://imdb-api.com/en/API/SearchMovie/"+key+"/"+moviesearch
        try:
          response =  requests.get(url)
        except: 
          print("None movie found with this input, try again")
        return VersioningEvent(status_code=response.status_code, content=response.json())