from datetime import datetime
import logging


class Chrono(object):
    checkpoint = None
    connection = None
    is_enabled = True

    def __init__(self, is_enabled):
        self.is_enabled = is_enabled
        self.checkpoint = datetime.now()

    def save(self, title):
        if self.is_enabled:
            now = datetime.now()
            delta = now - self.checkpoint
            logging.info('Chrono: %s [%dms]', title,
                         round(delta.total_seconds() * 1000))
            self.checkpoint = now
