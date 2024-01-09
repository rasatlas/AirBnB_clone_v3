#!/usr/bin/python3
""" places_amenities view """
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views
from os import getenv

db_storage = getenv('HBNB_TYPE_STORAGE')

@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def retrieve_all_place_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenities_list = []
    if db_storage == 'db':
        amenities = place.amenities
        for amenity in amenities:
            amenities_list.append(amenity.to_dict())
    else:
        amenities = place.amenity_ids
    return jsonify(amenities_list)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """
    Deletes a Amenity object or raise 404 error if not found
    Returns an empty dictionary with the status code 200
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if db_storage == 'db':
        place_amenity = place.amenities
    else:
        place_amenity = place.amenity_ids
    if amenity not in place_amenity:
        abort(404)
    place_amenity.remove(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def create_place_amenity(place_id, amenity_id):
    """
    Creates a Amenity
    Returns the new Amenity with the status code 201
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if db_storage == 'db':
        place_amenity = place.amenities
    else:
        place_amenity = place.amenity_ids
    if amenity in place_amenity:
        return jsonify(amenity.to_dict()), 200
    place_amenity.append(amenity)
    place.save()
    return jsonify(amenity.to_dict()), 201
