from flask import Blueprint, jsonify
from .services import get_current_time

date_time_blueprint = Blueprint('date_time', __name__)

@date_time_blueprint.route('/current-time', methods=['GET'])
def current_time():
    time_data = get_current_time()
    return jsonify(time_data)
