from flask import request, jsonify
from app import db
from app.api import bp
from app.api.errors import bad_request
from app.models import Message

@bp.route('/messages', methods=['POST'])
def save_message():
    data = request.get_json()
    if 'date' not in data or 'time' not in data or 'message' not in data:
        return bad_request('must include all fields')

    message = Message()
    message.from_dict(data)
    
    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'message successfully saved'}), 201
