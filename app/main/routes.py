from app.main import bp


@bp.route('/main')
def index():
    return 'This is The Main Blueprint'