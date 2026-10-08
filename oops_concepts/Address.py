class Address:
    def __init__(self,street="",city="",state="",zipcode=""):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
    def printAddress(self):
        return f"Stree : {self.street}, city : {self.city}, state : {self.state}, Code : {self.zipcode}"

    def getAddress(self,street="",city="",state="",zipcode=""):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
