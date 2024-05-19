import time
from flask import Blueprint
# from flask import Flask
import logging
import numpy as num

from .data.match_data import MATCHES
# app = Flask(__name__)

# logging.basicConfig(filename='flask.log', level=logging.DEBUG)
# logger = logging.getLogger(__name__)

bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404
    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()
    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    fave_numbers_1 = num.array(fave_numbers_1)
    fave_numbers_2 = num.array(fave_numbers_2)
    if num.any(num.isin(fave_numbers_2, fave_numbers_1, invert=True)):
        return False
    # for number in fave_numbers_2:
    #     if number not in fave_numbers_1:
    #         return False

    return True
