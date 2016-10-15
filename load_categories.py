'''
Load's seed category data.
'''
from hackvt2016.app import create_app
from hackvt2016.category.models import Category


def main():
    create_app().app_context().push()
    categories = [
        ('Library', 'book'),
        ('Event', 'map-pin'),
        ('Sports', 'soccer-ball-o'),
        ('Point of Interest', 'search'),
        ('Museum', 'bookmark'),
        ('Resource', 'pencil'),
        ('Nature Site', 'pagelines')]
    for (name, icon) in categories:
        Category.create(name=name, icon=icon)


if __name__ == '__main__':
    main()
