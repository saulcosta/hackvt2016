import requests
from hackvt2016.app import create_app
from hackvt2016.resource.models import Resource
from hackvt2016.category.models import Category

def main():
    create_app().app_context().push()
    thisRequest = requests.get("https://data.vermont.gov/resource/g5rt-gwwe")
    jsonObject = thisRequest.json()
    jsonObject[0]

    Resource.query.delete()



    for entry in jsonObject:
        category = "library"
        location = "location"
        title = entry.get("library")
        description = "Town Public Library"
        host = ""
        email = ""
        categoryID = Category.query.filter_by(name='Library').first().id


        Resource.create(title=title, description=description,host=host, email=email, category_id=categoryID)

if __name__ == '__main__':
    main()