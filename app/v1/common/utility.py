"""
v1/common/utility
"""
from flask import jsonify

def err_response(error):
    """err_response
    """
    return jsonify({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })