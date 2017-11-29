from flask import Blueprint,render_template, abort
from simpledu.models import User


user = Blueprint('user', __name__, url_prefix='/user')



@user.route('/<username>')
def index(username):
    s = username.strip('')
    query_result = User.query.filter_by(username=s).first()
    if query_result:
        return render_template('user.html', users=query_result)
    else:
        abort(404)