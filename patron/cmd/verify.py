#    Copyright 2015 OpenStack.
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

"""Starter script for Patron Verify."""

import sys

from oslo_concurrency import processutils
from oslo_config import cfg
from oslo_log import log as logging

from patron import config
from patron import objects
from patron.openstack.common.report import guru_meditation_report as gmr
from patron import service
from patron import utils
from patron import version

CONF = cfg.CONF
CONF.import_opt('topic', 'patron.verify.api', group='verify')


def main():
    config.parse_args(sys.argv)
    logging.setup(CONF, "patron")
    utils.monkey_patch()
    objects.register_all()

    gmr.TextGuruMeditation.setup_autorun(version)

    server = service.Service.create(binary='patron-verify',
                                    topic=CONF.verify.topic,
                                    manager=CONF.verify.manager)
    workers = CONF.verify.workers or processutils.get_worker_count()
    service.serve(server, workers=workers)
    service.wait()
