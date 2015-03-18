from checkio_referee import RefereeCodeGolf

import settings
import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_MAX_CODE_LENGTH = 150
    BASE_POINTS = 15
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "golf"
