
class HotelCategory:
    def __init__(self,max,roomType) :
        self.max = max
        self.Room_type = roomType
    def tojson(self):
        return {
            "max": self.max,
            "Room_type": self.Room_type
        }

class RoomCategory:  
    def __init__(self): 
      self.last_booking = ""
      self.category =[]
    
    def AddCategory(self,max,roomType):
        self.category.append(HotelCategory(max,roomType))

    def tojson(self):
        return {
            "last_booking": self.last_booking,
            "category": self.category
        }

class AlternativeHotels:
    def __init__(self,name,rate,link,description,most_recent_booking,number_of_reviews,score,bestscore) :
        self.name=name
        self.rate=rate
        self.link=link
        self.description=description
        self.most_recent_booking=most_recent_booking
        self.number_of_reviews=number_of_reviews
        self.score=score
        self.bestscore=bestscore
    def tojson(self):
        return {
            "name": self.name,
            "rate": self.rate,
            "link": self.link,
            "description": self.description,
            "most_recent_booking": self.most_recent_booking,
            "number_of_reviews": self.number_of_reviews,
            "score": self.score,
            "bestscore": self.bestscore
        }


class HotelInfo():
    def __init__(self) :
        self.Hotel_name = ""
        self.Address = ""
        self.Classification_stars = ""
        self.Review_points = ""
        self.Number_of_reviews = ""
        self.Description = ""
        self.RoomCategory = RoomCategory()
        self.Alternative_hotels = []
    def AddAlternativeHotels(self,name,rate,link,description,most_recent_booking,number_of_reviews,score,bestscore) :
        self.Alternative_hotels.append(AlternativeHotels(name,rate,link,description,most_recent_booking,number_of_reviews,score,bestscore))
    def tojson(self):
        return {
            "Hotel_name": self.Hotel_name,
            "Address": self.Address,
            "Classification_stars": self.Classification_stars,
            "Review_points": self.Review_points,
            "Number_of_reviews": self.Number_of_reviews,
            "Description": self.Description,
            "RoomCategory": self.RoomCategory,
            "Alternative_hotels": self.Alternative_hotels
        }



 