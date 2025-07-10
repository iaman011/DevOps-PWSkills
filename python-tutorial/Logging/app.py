# First, we import the logging module, which allows us
# to record events that happen while our program runs.
import logging

# Now, we configure the logging system using basicConfig().
# Here, we are setting:
# - filename: where all the logs will be saved (app_log.txt)
# - level: minimum severity of messages to be recorded (DEBUG and above)
# - format: how each log message will look (with time, log level, and message)
logging.basicConfig(
    filename="app_log.txt",
    level=logging.DEBUG,  # <== there was a missing comma here in your code
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Now, let's record messages of different severity levels:

# This is a debug message — useful for developers to debug the program.
logging.debug('Debug Message')

# This is an info message — to record general information about the program’s flow.
logging.info('Info Message')

# This is a warning message — to alert about something unexpected but not an error.
logging.warning('Warning Message')

# This is an error message — to log a serious issue that has happened.
logging.error('Error Message')

# This is a critical message — for very severe situations like system failure.
logging.critical('Critical Message')

'''
log - debug: detailed information for diagnosting problems
log info: general info about the programs startime/ end 
timelog warning: indication of something unexpected
log critical: highest priority: serious / fatal problem in program 
'''
