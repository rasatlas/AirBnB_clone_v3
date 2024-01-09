#!/usr/bin/python3
""" places view """
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def retrieve_all_places(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = city.places
    place_list = []
    for place in places:
        place_list.append(place.to_dict())
    return jsonify(place_list)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def retrieve_place(place_id):
    """Retrieves a Place object or raise 404 error if not found"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """
    Deletes a Place object or raise 404 error if not found
    Returns an empty dictionary with the status code 200
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """
    Creates a Place
    Returns the new Place with the status code 201
    """
    if not request.json:
        abort(400, "Not a JSON")
    if 'user_id' not in request.json:
        abort(400, "Missing user_id")
    if 'name' not in request.json:
        abort(400, "Missing name")
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    user = storage.get(User, request.json['user_id'])
    if user is None:
        abort(404)
    place = Place(**request.json)
    place.city_id = city_id
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """
    Updates a Place object
    Return the Place with the status code 200
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    for key, value in request.json.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_place():
    """
    Retrieves all Place objects depending on the JSON in the request
    """
    if not request.json:
        abort(400, "Not a JSON")
    places = storage.all(Place).values()
    if 'states' in request.json and len(request.json['states']) > 0:
        places = [place for place in places if place.city.state_id in
                  request.json['states']]
    if 'cities' in request.json and len(request.json['cities']) > 0:
        places = [place for place in places if place.city_id in
                  request.json['cities']]
    if 'amenities' in request.json and len(request.json['amenities']) > 0:
        places = [place for place in places if
                  all(amenity.id in [amenity.id for amenity in place.amenities]
                      for amenity in request.json['amenities'])]
    return jsonify([place.to_dict() for place in places])
