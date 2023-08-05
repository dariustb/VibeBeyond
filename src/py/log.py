''' log.py - Python module for logging errors and debug info '''

# pylint: disable = W0401, W0614

from py.constants import *

HEADER = '[' + APP_NAME.upper() + ']:'

def log_error(function_object, error_message):
    ''' logs error onto stdout '''
    print()
    print(HEADER, 'error:',
          '(' + function_object.__name__ + ')',
          error_message)
