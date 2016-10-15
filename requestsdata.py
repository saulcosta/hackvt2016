import requests
from hackvt2016.app import create_app
from hackvt2016.resource.models import Resource
from hackvt2016.category.models import Category

def main():
    create_app().app_context().push()
    Resource.query.delete()
    load_libraries()
    load_seeds()



def load_seeds():
    resources = [
        ('Sports', 'Soccer Game', 'Everyone is invited to a quick soccer game this weekend.', 'Saul Costa', 'saulcosta18222@gmail.com')
    ]
    for (category, title, description, host, email, longitude, latitude) in resources:
        categoryID = Category.query.filter_by(name=category).first().id
        Resource.create(
            category_id=categoryID,
            title=title,
            description=description,
            host=host,
            email=email,
            longitude=longitude,
            latitude=latitude)


def load_libraries():
    thisRequest = requests.get('https://data.vermont.gov/resource/g5rt-gwwe')
    jsonObject = thisRequest.json()

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