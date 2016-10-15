'''
Load's seed category data.
'''
from hackvt2016.app import create_app
from hackvt2016.category.models import Category


def main():
    create_app().app_context().push()
    Category.query.delete()
    categories = [
        ('Library', 'book', '9A2A0A'),
        ('Event', 'map-pin', '77A856'),
        ('Sports', 'soccer-ball-o', '527F8D'),
        ('Cool Stuff', 'search', '4874D4'),
        ('Resource', 'pencil', '634CA4'),
        ('Nature', 'pagelines', '9C5178')]
    for (name, icon, color) in categories:
        Category.create(name=name, icon=icon, color=color)


if __name__ == '__main__':
    main()
