from flask import Blueprint
from controllers.getController import getAll, index


caradhras = Blueprint('caradhras', __name__)


# All GET routes
caradhras.route('/getAll', methods=['GET'])(getAll)
caradhras.route('/', methods=['GET'])(index)


# All POST routes
# mongoRoute.route('/create', methods=['POST'])(store)
# mongoRoute.route('/<int:user_id>', methods=['GET'])(show)
# mongoRoute.route('/<int:user_id>/edit', methods=['POST'])(update)
# mongoRoute.route('/<int:user_id>', methods=['DELETE'])(destroy)