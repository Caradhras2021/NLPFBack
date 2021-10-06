from flask import Blueprint
from controllers.getController import index, getOne, getAll, getTransactions


# caradhras = Blueprint('caradhras', __name__)


# All GET routes

# caradhras.route('/', methods=['GET'])(index)
# caradhras.route('/getOne', methods=['GET'])(getOne)
# caradhras.route('/getAll', methods=['GET'])(getAll)
# caradhras.route('/getTransactions', methods=['GET'])(getTransactions)

# All POST routes
# mongoRoute.route('/create', methods=['POST'])(store)
# mongoRoute.route('/<int:user_id>', methods=['GET'])(show)
# mongoRoute.route('/<int:user_id>/edit', methods=['POST'])(update)
# mongoRoute.route('/<int:user_id>', methods=['DELETE'])(destroy)