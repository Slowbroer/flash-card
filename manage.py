#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate
from app import create_app
from route import api


app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    manager.run()