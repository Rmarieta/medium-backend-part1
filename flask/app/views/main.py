from flask import Blueprint

main_bp = Blueprint('main', __name__)

# IMPORTANT : leave the root route to the Elastic Beanstalk Load Balancer health check, it performs a GET to '/' every 5 seconds and expects a '200'
@main_bp.route('/', methods=['GET'])
def EB_healthcheck():
    return 'OK', 200


# @main_bp.route('/add', methods=['POST'])
# def add():
#     data = request.get_json()

#     new_event = Event(
#     )
#     db.session.add(new_event)
#     db.session.commit()

#     return 'OK', 200