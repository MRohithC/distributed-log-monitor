from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "service": self.service,
            "level": self.level,
            "message": self.message,
            "timestamp": self.timestamp.isoformat()
        }

@app.route('/')
def home():
    return "Distributed Log Monitor is running!"

@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    service = data.get('service')
    level = data.get('level')
    message = data.get('message')

    if not service or not level or not message:
        return jsonify({"error": "service, level, and message are required"}), 400

    new_log = Log(
        service=service,
        level=level,
        message=message
    )

    db.session.add(new_log)
    db.session.commit()

    return jsonify({
        "message": "Log saved successfully",
        "log": new_log.to_dict()
    }), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    level = request.args.get('level')
    service = request.args.get('service')

    query = Log.query

    if level:
        query = query.filter_by(level=level)

    if service:
        query = query.filter_by(service=service)

    logs = query.order_by(Log.timestamp.desc()).all()
    return jsonify([log.to_dict() for log in logs])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)