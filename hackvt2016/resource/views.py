# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from hackvt2016.category.models import Category

blueprint = Blueprint('resource', __name__, static_folder='../static')


@blueprint.route('/')
def resources():
    categories = pairwise(Category.query.all())
    return render_template('resources/index.html', categories=categories)

def pairwise(it):
    it = iter(it)
    while True:
        yield next(it), next(it)
