import gevent
from gunicorn.workers.ggevent import GeventWorker


class GeventWorker(GeventWorker):
    """
    This is a custom gunicorn worker class, based on the standard
    gevent worker but with an extra nicety:

    * a timeout enforced on each individual request, rather than on
      inactivity of the worker as a whole.
    """

    def handle_request(self, *args):  # pragma: no cover
        """
        Apply the configured 'timeout' value to each individual request.
        Note that self.timeout is set to half the configured timeout by
        the arbiter, so we use the value directly from the config.
        """
        with gevent.Timeout(self.cfg.timeout):
            return super(GeventWorker, self).handle_request(*args)
