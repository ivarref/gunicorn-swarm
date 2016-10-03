#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import uuid
import time
import random

from gunicorn.app.base import BaseApplication
from flask import Flask
from gunicorn.six import iteritems

def get_app():
    app = Flask(__name__)
    r = str(uuid.uuid4())
    @app.route('/')
    def root():
        time.sleep(0.1 * random.random()) # do some work
        return r
    return app

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()
    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)
    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        'workers' : '4',
        'bind' : '0.0.0.0:8080'
    }
    StandaloneApplication(get_app(), options).run()
