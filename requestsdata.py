import requests
from hackvt2016.app import create_app
from hackvt2016.resource.models import Resource
from hackvt2016.category.models import Category

def main():
    create_app().app_context().push()
    thisRequest = requests.get('https://data.vermont.gov/resource/g5rt-gwwe')
    jsonObject = thisRequest.json()

    Resource.query.delete()

    for entry in jsonObject:
        category = 'library'
        latitude = entry.get('location_1').get('latitude')
        longitude = entry.get('location_1').get('longitude')
        title = entry.get('library')
        description = 'website: ' + str(entry.get('web_location'))
        categoryID = Category.query.filter_by(name='Library').first().id

        if latitude and longitude:
            Resource.create(title=title, description=description, category_id=categoryID, latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    main()