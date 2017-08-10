# -*- coding: utf-8 -*-
# Copyright (c) 2017 SubDownloader Developers - See COPYING - GPLv3

from enum import Enum
import os

from subdownloader.compat import Path


class ClientType(Enum):
    CLI = 'cli'
    GUI = 'gui'


def client_get_path():
    """
    Get path to the client modules.
    :return: path as a string
    """
    return Path(__file__).absolute().parent


class IllegalArgumentException(Exception):
    def __init__(self, msg):
        self.msg = msg
