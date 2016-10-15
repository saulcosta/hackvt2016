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
    for index in xrange(10):
        resources = [
            ('Sports', 'Softball Practice', 'Weekly softball practice - bring gear!', 'Theo Fido', 'tfo@softball.com'),
            ('Event', 'Calligraphy Lesson', 'Workshop for Calligraphy Lessons on Tuesdays', 'Tanner Riley', 'triley@clriley.com'),
            ('Nature Site', 'Geocache', 'Placed in 1971.', '', ''),
            ('Event', 'Oliver Twist Auditions', 'Auditions for the Oliver Twist play begin at 3PM.', 'Julia Reynolds', 'middleproductions@yahoo.com'),
            ('Sports', 'Soccer Game', 'Everyone is invited to a quick soccer game this weekend.', 'Saul Costa', 'saulcosta18222@gmail.com'),
            ('Resource', 'AndreWorks Studio', 'Available for reservations!', 'Andrew Minor', 'aminor@andreworks.org'),
            ('Event', 'Gymnastics Open Hours', 'Open to all age ranges!', 'Lydia Kiles', 'opengym@opengym.org'),
            ('Museum', 'Middle Age Weapons Musuem', 'Open 10-5 Daily!', 'Brianna Wright', 'mawm@museums.org'),
            ('Nature Site', 'Hunter Trail', 'Requires appropriate footwear.', '', ''),
            ('Cool Stuff', 'Alden Partridge Monument', 'In memory of the Norwich University Founder.', '', ''),
            ('Sports', 'Ski Range', 'Bring your skis!', '', ''),
            ('Sports', 'Karate Lessons', 'Tae Kwon Do', 'Sensei Vivian', 'themaster@thekaratestudio.com'),
            ('Nature Site', 'Crystal Mine Lake', 'No lifeguard on duty!', 'Trevor Daniels', 'fri@.mns.org'),
            ('Resource', 'School Supplies and Book Store', 'For all your education needs!', '', 'theotherstaples@bookstores.com'),
            ('Musuem', 'Stone House Historical Center', 'With live-in actors!', 'Manny Curtis', 'mcurtis@stonehouse.org'),
            ('Musuem', 'VT Historical Archives', 'Open 8 to 4 on weekdays.', '', 'admin@vtarchives.org'),
            ('Resource', 'Musical Studio', 'Instruments and soundrooms available to reserve!', '', 'mstudio@vtmusic.net')

            ('Museum', 'Black Manor Historical House', 'Provides historical reenactments on Mondays and Thursdays!', 'Tia Ramirez', 'tramirez@blackmanor.edu')

            ('Nature Site', 'Red Fern Bike Trail', 'Maps are available at all entrances.', '', 'infotrails@parksandrecvt.gov')
            ('Nature Site', 'Westerman Bird Viewing Platform', '', '', 'infobirds@parksandrecvt.gov')
            ('Nature Site', 'Holmes Stargazing Platform', 'Parking is available down the road.', '', 'jweng@vtastronomy.org')

            ('Event', 'Ski Race', 'Open to grades 1-5', 'Scoville J Danis"' 'scjda12@yahoos.org')
            ('Event', 'Guitar Lessons', 'Specialty: acoustic', 'Wren Fido', 'fido@onestopguitar.com')
            ('Event', 'Stargazing', 'Bring a coat and blanket for the Fall stargazing event!', 'Julian Weng', 'jweng@vtastronomy.org')
            ('Event', 'Band Tryouts', 'Instrument rentals can be arranged beforehand with the contact person.' 'Valerie Collins', 'vcollins@themusicstudio.org')


            ('Cool Stuff', 'Sundial', 'Built in 1834', '', '')
            ('Cool Stuff', 'Geodome', '', '', '')
            ('Cool Stuff', 'Historical Cemetery', 'Established in 1782', '', '')
            ('Cool Stuff', 'Old Weeping Willow Tree', 'Planted 1900', '', '')

            ('Sports', 'Horseback Riding Lessons', 'Beginner to Advanced lessons provided!', 'Leonard McGarth', 'horseback@horsebackvt.info')
            ('Sports', 'Hockey Tryouts', 'Open to grades 5-8, gear provided.', 'Olivia Olsen', 'olsen@watervillemiddle.com')
            ('Sports', 'Swimming Lessons', 'Group classes and one-on-one mentoring offered.', '', 'lessons@swimvt.com')
            ('Sports', 'Cross Country Practice', 'We will be starting with a 3 mile run on Tuesday.', 'Gina Woo', 'gwoo@tritonhs.com')





        ]
        for (category, title, description, host, email) in resources:
            category = Category.query.filter_by(name=category).first()
            if not category:
                continue
            Resource.create(
                category_id=category.id,
                title=title,
                description=description,
                host=host,
                email=email,
                longitude=random.uniform(-73.132, -72.632) if index <= 7 else random.uniform(-72.632, -71.739),
                latitude=random.uniform(42.777, 44.953) if index <= 7 else random.uniform(44.452, 44.953))


def load_libraries():
    thisRequest = requests.get('https://data.vermont.gov/resource/g5rt-gwwe')
    jsonObject = thisRequest.json()

    for entry in jsonObject:
        category = 'library'
        latitude = entry.get('location_1').get('latitude')
        longitude = entry.get('location_1').get('longitude')
        title = entry.get('library') + ' Library'
        description = 'Local library.'
        email = None
        if entry.get('web_location'):
            email = entry.get('web_location')
        categoryID = Category.query.filter_by(name='Library').first().id

        if latitude and longitude:
            Resource.create(title=title, description=description, category_id=categoryID, latitude=latitude, longitude=longitude, email=email)


if __name__ == '__main__':
    main()
