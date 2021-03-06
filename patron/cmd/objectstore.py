
# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Daemon for patron objectstore. Supports S3 API."""

import sys

from oslo_log import log as logging

from patron import config
from patron.objectstore import s3server
from patron.openstack.common.report import guru_meditation_report as gmr
from patron import service
from patron import utils
from patron import version


def main():
    config.parse_args(sys.argv)
    logging.setup(config.CONF, "patron")
    utils.monkey_patch()

    gmr.TextGuruMeditation.setup_autorun(version)

    server = s3server.get_wsgi_server()
    service.serve(server)
    service.wait()
