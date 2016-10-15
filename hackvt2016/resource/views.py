# -*- coding: utf-8 -*-
"""User views."""
from sqlalchemy import inspect
from flask import Blueprint, render_template, jsonify, request
from hackvt2016.category.models import Category
from .models import Resource

blueprint = Blueprint('resource', __name__, static_folder='../static')

def pairwise(it):
    it = iter(it)
    while True:
        yield next(it), next(it)


def object_as_dict(obj):
    data = {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
    color = Category.query.filter(Category.id == obj.category_id).first().color
    data['color'] = color
    data['infowindow'] = infowindow(obj)
    return data


def infowindow(resource):
  return '''
    <h3>%s</h3>
    <p>%s</pr>
  ''' % (resource.title, resource.description)


@blueprint.route('/')
def index():
    categories = pairwise(Category.query.all())
    return render_template('resources/index.html', categories=categories)


@blueprint.route('/resources')
def resources():
  ids = map(int, request.args.getlist('ids[]'))
  data = Resource.query.filter(Resource.category_id.in_(ids)).all()
  data = map(object_as_dict, data)
  return jsonify(data)