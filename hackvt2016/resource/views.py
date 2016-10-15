# -*- coding: utf-8 -*-
"""User views."""

import requests
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
  info = '<h3>%s</h3><p><a href="https://www.google.com/maps/dir/Current+Location/%s,%s" target="_blank">Map</a></p><strong>Description</strong><p>%s</p>' % (resource.title, str(resource.latitude), str(resource.longitude), resource.description)
  if resource.host:
      info += '<strong>Host Name</strong><p>%s</p>' % resource.host
  if resource.email:
      info += '<strong>Contact Info</strong><p>%s</p>' % resource.email
  return info


def geocode(address):
    thisRequest = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyCX_bLPe9VVExFw_89M3viU54AKUzDG1HE' % address)
    jsonObject = thisRequest.json()
    print(jsonObject.get('results')[0])
    if not len(jsonObject):
        return
    data = jsonObject.get('results')[0].get('geometry').get('location')
    return data.get('lat'), data.get('lng')


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


@blueprint.route('/new', methods=['POST'])
def new_resource():
  latitude, longitude = geocode(request.form['address'])
  category = Category.query.filter_by(name=request.form['category']).first()
  if not (category and latitude and longitude):
    return jsonify({})
  Resource.create(
      title=request.form['title'],
      description=request.form['description'],
      host=request.form['host'],
      email=request.form['email'],
      category_id=category.id,
      latitude=latitude,
      longitude=longitude)
  return jsonify({})
