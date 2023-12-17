"""app/v1/views/main.py
"""

from flask import Blueprint, jsonify, redirect, request, url_for

from app.v1.common.utility import err_response
from app.v1.models import db
from app.v1.models.main import Feedback

v1 = Blueprint('v1', __name__, url_prefix='/v1')

@v1.route('/', methods=['GET'])
def default():
    """default
    """
    return "This is v1 API!"

@v1.route('/healthcheck', methods=['GET'])
def healthcheck():
    """healthcheck
    """
    return jsonify({
        'status': 'healthy'
    }), 200

@v1.route('/test', methods=['GET'])
def test():
    """test
    """
    return jsonify({
        'status': 'test'
    }), 200

@v1.route('/feedback', methods=['GET'])
def get_feedback():
    """get_feedback
    """
    feedbacks = Feedback.query.all()
    return jsonify([feedback.to_dict() for feedback in feedbacks]), 200

@v1.route('/feedback', methods=['POST'])
def create_feedback():
    """create_feedback
    """
    data = request.get_json()
    feedback = Feedback(
        service=data['service'],
        title=data['title'],
        detail=data['detail']
    )
    db.session.add(feedback)
    db.session.commit()
    return jsonify(feedback.to_dict()), 200

@v1.errorhandler(404)
@v1.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code