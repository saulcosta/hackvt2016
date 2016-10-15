# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template

blueprint = Blueprint('resource', __name__, static_folder='../static')


@blueprint.route('/')
def resources():
    return render_template('resources/index.html')
