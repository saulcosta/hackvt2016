import requests
from hackvt2016.app import create_app
from hackvt2016.resource.models import Resource

def main():
    create_app().app_context().push()
    thisRequest = requests.get("https://data.vermont.gov/resource/g5rt-gwwe")
    jsonObject = thisRequest.json()
    jsonObject[0]

    #print(jsonObject)



    for entry in jsonObject:
    	category = "library"
    	location = "location"
    	title = entry.get("library")
    	description = "Town Public Library"
    	host = ""
    	email = ""
    	locationID = 1
    	categoryID = 1


    #Resource.create(title=title, description=description,host=host, email=email,location_id=locationID,category_id=categoryID)
    Resource.create(title=title, description=description,host=host, email=email)


    	#pull each attribute from data set


    #print(jsonObject[0].get("type_access"))

    #create csv reader

    #

if __name__ == '__main__':
    main()