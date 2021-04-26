#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate
from app import create_app
import logging


app = create_app()
manager = Manager(app)

logging.basicConfig(filename='flash_card.log', level=logging.INFO)


if __name__ == '__main__':
    manager.run()
