# Software License Agreement (GPL)
#
# \file      __init__.py
# \authors   Paul Bovbel <pbovbel@locusrobotics.com>
# \copyright Copyright (c) (2017,), Locus Robotics, All rights reserved.
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging
import logging.config
import os
import subprocess
import yaml

logger = logging.getLogger(__name__)


def configure_logging():
    try:
        with open(os.environ['ROS_PYTHON_LOG_CONFIG_FILE']) as config:
            logging.config.dictConfig(yaml.safe_load(config))
    except KeyError:
        logging.basicConfig()


def check_call(cmd, *args, **kwargs):
    logger.info(' '.join(cmd))
    return subprocess.check_call(cmd, *args, **kwargs)
