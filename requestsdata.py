import requests
import random
from hackvt2016.app import create_app
from hackvt2016.resource.models import Resource
from hackvt2016.category.models import Category

def main():
    create_app().app_context().push()
    Resource.query.delete()
    load_libraries()
    load_seeds()



def load_seeds():


    """
    max longitudes and latitudes:
    Coordinates

[5:55]  
lat: 42.777 - 44.953
long: (-72.632) - (-73.132)

lat: 44.452 - 44.953
long: (-71.739) - (-72.632)

    """
    random.randrange(73, )

    resources = [
        ('Sports', 'Softball Practice', 'Weekly softball practice - bring gear!', 'Theo Fido', 'tfo@softball.com')
        ('Event', 'Calligraphy Lesson', 'Workshop for Calligraphy Lessons', 'Tanner Riley', 'triley@clriley.com')
        ('Nature Site', 'Geocache', 'Placed in 1971', '', '')
        ('Event', 'Oliver Twist Rehearsal', 'Auditions for the Oliver Twist play', 'Julia Reynolds', 'middleproductions@')
        ('Sports', 'Soccer Game', 'Everyone is invited to a quick soccer game this weekend.', 'Saul Costa', 'saulcosta18222@gmail.com')
        ('Resource', 'AndreWorks Studio', 'Available for reservations', 'Andrew Minor', 'aminor@andreworks.org')
        ('Event', 'Gymnastics Open Hours', 'Open to all age ranges', 'Lydia Kiles', 'opengym@opengym.org')
        ('Museum', 'Middle Age Weapons Musuem', 'Open 10-5 Daily', 'Brianna Wright', 'mawm@museums.org')
        ('Nature Site', 'Hunter Trail', 'Requires appropriate footwear', '', '')
        ('Cool Stuff', 'Alden Partridge Monument', 'In memory of the Norwich University Founder', '', '')
        ('Cool Stuff', 'Ski Range', 'Bring your skis!', '', '')
        ('Sports', 'Karate Lessons', 'Tae Kwon Do', 'Sensei Vivian', 'themaster@thekaratestudio.com')
        ('Nature Site', 'Crystal Mine Lake', 'No lifeguard on duty', 'Trevor Daniels', 'fri@.mns.org')
        ('Resource', 'School Supplies and Book Store', 'For all your education needs!', '', 'theotherstaples@bookstores.com')
        ('Musuem', 'Stone House Historical Center', 'With live in actors', 'Manny Curtis', 'mcurtis@stonehouse.org')
        ('Musuem', 'VT Historical Archives', 'Open 8 to 4 on weekdays', '', 'admin@vtarchives.org')
        ('Resource', 'Musical Studio', 'Instruments and soundrooms available to reserve', '', 'mstudio@vtmusic.net'\)
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