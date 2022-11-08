from flask import Blueprint, jsonify
from src.services.marathon_service import MarathonEventService
from src.models.marathon import MarathonSchema
from src.constants import ENDPOINTS

marathon_api_bp = Blueprint('marathon_api',__name__, url_prefix=ENDPOINTS.MARATHONS.value)

@marathon_api_bp.route('')
def get_marathons():
    schema = MarathonSchema(many=True)
    all_marathons = MarathonEventService.get_all()
    marathons = schema.dump(all_marathons)
    return jsonify(marathons)