from flask import Blueprint, render_template
from flask_login import current_user, login_required

from webapp.user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/admin')
@admin_required
def admin_index():
    title = 'Control panel'
    return render_template('admin/index.html', page_title=title)
