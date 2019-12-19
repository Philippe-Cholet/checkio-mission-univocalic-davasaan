from checkio import api
from checkio.signals import ON_CONNECT
from checkio.referees.code import CheckiORefereeCode

from tests import TESTS
from inspector import inspector

api.add_listener(
    ON_CONNECT,
    CheckiORefereeCode(
        tests=TESTS,
        # check_result=None,
        inspector=inspector,
        # add_close_builtins=None,
        # add_allowed_modules=None,
        # remove_allowed_modules=None,
    ).on_ready,
)
