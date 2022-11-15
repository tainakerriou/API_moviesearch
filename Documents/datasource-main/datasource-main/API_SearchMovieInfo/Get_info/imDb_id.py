from Get_info.imBd_result import IMDbResult

#
class IMDbid:

    def find_id(moviesearch):
        #print(IMDbResult.get_infos(moviesearch).content)
        return IMDbResult.get_infos(moviesearch).content['results'][0]['id']