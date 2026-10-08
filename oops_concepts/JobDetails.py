class JobDetails:
    def __init__(self,title="",experience="",interested_tech="",favorite_company=""):
        self.title = title
        self.experience = experience
        self.interested_tech = interested_tech
        self.favorite_company = favorite_company
    def printJobDetails(self):
        return f"Title : {self.title}, Experience : {self.experience}, Interested Technology : {self.interested_tech}, Favorite Company : {self.favorite_company}"

    def getDetails(self,title="",experience="",interested_tech="",favorite_company=""):
        self.title = title
        self.experience = experience
        self.interested_tech = interested_tech
        self.favorite_company = favorite_company
