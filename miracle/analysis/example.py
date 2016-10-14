"""
An example analysis script.
"""

from miracle.log import LOGGER


def example(db):
    result = False
    with db.session(commit=False) as session:
        # Open a database transaction, which does not automatically
        # commit at the end.

        # Execute queries or do any other calculation.
        rows = session.execute('select 1').fetchall()
        if rows:
            result = True
    return result


def main(db, argv=None):
    # The entry point function needs to be called main and take a db
    # argument, which gets a configured database class passed in.
    # It also needs to take the argv command line arguments, but can
    # ignore those.

    # Call a function to do the actual work.
    result = example(db)

    # A Python logger is set up automatically, which prints messages
    # to the console, prefixed by a timestamp. For long running scripts
    # this allows one to follow the progress.
    LOGGER.info('Result: %s', result)