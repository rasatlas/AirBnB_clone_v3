#!!/usr/bin/python3
""" places_amenities view """
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views
from os import getenv


@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def retrieve_all_place_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenities_list = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = place.amenities
        for amenity in amenities:
            amenities_list.append(amenity.to_dict())
    else:
        amenities = place.amenity_ids
    return jsonify(amenities_list)
