from functools import wraps
from flask import abort
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.tipo_user:
            abort(403)# aqui eu poderia mandar rendenrizar para outra pagina ao inves de abortar
        return f(*args, **kwargs)
    return decorated_function
