import logging
from bs4 import BeautifulSoup


class HtmlParser():
    def __init__(self,html,hotelInfo) :
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("start - parsing HTML file")
        if html == None:
            message = "html data in None"
            self.logger.exception(message)
            print(message)
            raise ValueError(message)

        if html == "":
            message = "html data in Empty"
            self.logger.exception(message)
            print(message)
            raise ValueError(message)

        self.soup = BeautifulSoup(html,'html.parser')
        self.hotelInfo = hotelInfo
        
        self.__getHotelName()
        
        self.__getAddress()
        self.__getClassification_stars()
        try:
            self.scor = self.soup.find('div',{'class':'featured_review_score'}).find_all('span')
        except:
            self.NotfoundError("Score")

        self.__getReview_points()
        self.__getNumber_of_reviews()
        self.__getDescription()
        self.__getCategory()
        self.__getAlternative_hotels()
        self.logger.info("end - parsing HTML file")
    def NotfoundError(self,str):
        self.logger.warning(f"{str} not found ")
        print(f"{str} not found ")

    def __getHotelName(self):
        self.logger.info("Get hotel name")
        try:
            name = self.soup.find(id='hp_hotel_name').text.strip('\n')
        except:
            name = ""
            self.NotfoundError("hotel name ")
        self.hotelInfo.Hotel_name =name
    def __getAddress(self):
        self.logger.info("Get Address")
        try:
            address = self.soup.find(id='hp_address_subtitle').text.strip('\n')
        except:
            self.NotfoundError("address ")
            address = ""
        self.hotelInfo.Address= address

    def __getClassification_stars(self):
        self.logger.info("Get classification")        
        self.hotelInfo.Classification_stars= ""
        rateclass = "ratings_stars_"
        try:
            for cls in self.soup.find('span',{"class","nowrap hp__hotel_ratings"}).span.i["class"]:
                if  rateclass in cls:
                    self.hotelInfo.Classification_stars =cls[len(rateclass):]
        except:
            self.NotfoundError("Classification_stars")

    def __getReview_points(self):
        self.logger.info("Get review points")
        try:
            reviewpoints=self.scor[0].text.strip('\n')
        except:
            reviewpoints = ""
            self.NotfoundError("reviewpoints")
        self.hotelInfo.Review_points =reviewpoints

    def __getNumber_of_reviews(self):
        self.logger.info("Get number of review")
        try:
            Number_of_reviews=self.scor[1].text.strip('\n') 
        except:
            Number_of_reviews = ""
            self.NotfoundError("Number_of_reviews")

        self.hotelInfo.Number_of_reviews=Number_of_reviews
                
    def __getDescription(self):
        self.logger.info("Get description")
        description = ""
        try:
            for p in self.soup.find('div',{'class':'hotel_description_wrapper_exp'}).find_all('p'):
                description += p.text.strip('\n')
        except:
            self.NotfoundError("description")

        self.hotelInfo.Description=description         
        
    def __getCategory(self):
        self.logger.info("Get Category")
        try:
            room_cat = self.soup.find('div',{'class':'description urt'})
            self.hotelInfo.RoomCategory.last_booking = room_cat.find('div',{'class':'hp_last_booking'}).text.strip('\n')        
            for row in room_cat.table.tbody.find_all('tr'):
                data = row.find_all('td')            
                try:
                    max = data[0].find('span',{'class':'plus_kids'}).text.strip('\n')
                except:
                    max = ""
                roomtype = data[1].text.strip('\n')
                self.hotelInfo.RoomCategory.AddCategory(max,roomtype)
        except:
            self.NotfoundError("RoomCategory")


    def __getAlternative_hotels(self):
        self.logger.info("Get Alternative Hotel")
        try:
            for hotel in self.soup.find(id='althotelsTable').tbody.tr.find_all('td'):
                children = hotel.findChildren(recursive=False)             
                name=children[0].a.text.strip('\n')
                rate=children[0].i.span.text
                link=children[0].a['href']
                description=children[2].text.strip('\n')
                most_recent_booking=children[3].text.strip('\n')
                number_of_reviews=children[4].span.strong.text
                score=children[4].a.find('span',{'class':'average js--hp-scorecard-scoreval'}).text
                bestscore=children[4].a.find('span',{'class':'best'}).text
                self.hotelInfo.AddAlternativeHotels(name,rate,link,description,most_recent_booking,number_of_reviews,score,bestscore)
        except:
            self.NotfoundError("Alternative Hotel")
     
            