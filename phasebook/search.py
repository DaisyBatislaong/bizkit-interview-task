from flask import Blueprint, request, Flask

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


import logging
app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!


    users_match = []
    search_order= [key for key, value in args.items()]
    encountered_ids = []
    for user in USERS:
        app.logger.info(encountered_ids)

        if args.get('id') and (args['id'] == user['id']) and user['id'] not in encountered_ids:
            match_order = search_order.index('id')
            users_match.append((user, match_order))
            encountered_ids.append(user['id'])

        # for matching age
        if args.get('age') and (int(args['age']) - 1 <= user['age'] <= int(args['age'])+1) and user['id'] not in encountered_ids: 
            match_order = search_order.index('age')
            users_match.append((user, match_order))
            encountered_ids.append(user['id'])
        
        # For matcing names
        if args.get('name') and user['id'] not in encountered_ids: 
            search_name = args.get('name', '').split()
            user_names = user['name'].split()
            if all(word in user_names for word in search_name):
                match_order = search_order.index('name')
                app.logger.info(match_order)
                users_match.append((user, match_order))
                encountered_ids.append(user['id'])

        if args.get('occupation') and any(char in user['occupation'] for char in args['occupation']) and user['id'] not in encountered_ids:
            match_order = search_order.index('occupation')
            users_match.append((user, match_order))
            encountered_ids.append(user['id'])

    sorted_data = sorted(users_match, key=lambda x: x[1])
    sorted_user_data = [user_data[0] for user_data in sorted_data]
    return sorted_user_data
