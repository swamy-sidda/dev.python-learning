from oops_concepts import Address
from oops_concepts import FamilyDetails
from oops_concepts import JobDetails

class DetailsPage:
    def getaddress(self,street="",city="",state="",zipcode=""):
        address=  Address()
        address.getAddress(street,city,state,zipcode)
        Address.Address.printAddress()

    def getfamilydetails(self,name="", age="", status="", father="", mother=""):
        familyDetails= FamilyDetails()
        familyDetails.getDetails(name,age,status,father,mother)
        familyDetails.printFamilyDetails()

    def getjobDetails(self,title="",experience="",interested_tech="",favorite_company=""):
        jobDetails=JobDetails()
        JobDetails.getDetails(title,experience,interested_tech,favorite_company)
        jobDetails.printJobDetails()


    def all_details(self):
        detailsPage = DetailsPage()
        detailsPage.getaddress()
        detailsPage.getfamilydetails()
        detailsPage.getjobDetails()