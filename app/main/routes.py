from app.main import bp


@bp.route('/blue')
def index():
    return 'This is The Main Blueprint'