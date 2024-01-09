#!/usr/bin/python3
""" places_reviews view """
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.review import Review
from models.user import User
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def retrieve_all_reviews(place_id):
    """Retrieves the list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = place.reviews
    review_list = []
    for review in reviews:
        review_list.append(review.to_dict())
    return jsonify(review_list)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def retrieve_review(review_id):
    """Retrieves a Review object or raise 404 error if not found"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """
    Deletes a Review object or raise 404 error if not found
    Returns an empty dictionary with the status code 200
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """
    Creates a Review
    Returns the new Review with the status code 201
    """
    if not request.json:
        abort(400, "Not a JSON")
    if 'user_id' not in request.json:
        abort(400, "Missing user_id")
    if 'text' not in request.json:
        abort(400, "Missing text")
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    user = storage.get(User, request.json['user_id'])
    if user is None:
        abort(404)
    review = Review(**request.json)
    review.place_id = place_id
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """
    Updates a Review object
    Return the Review with the status code 200
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    for k, value in request.json.items():
        if k not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, k, value)
    storage.save()
    return jsonify(review.to_dict()), 200
