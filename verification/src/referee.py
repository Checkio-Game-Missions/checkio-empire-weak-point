from checkio_referee import RefereeCodeGolf


import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_MAX_CODE_LENGTH = 200
    BASE_POINTS = 15
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
