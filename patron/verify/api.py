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

"""Handles all requests to the verify service."""

from oslo_config import cfg
from oslo_log import log as logging
import oslo_messaging as messaging

from patron import baserpc
from patron.verify import manager
from patron.verify import rpcapi
from patron.i18n import _LI, _LW
from patron import utils

verify_opts = [
    cfg.BoolOpt('use_local',
                default=False,
                help='Perform patron-verify operations locally'),
    cfg.StrOpt('topic',
               default='verify',
               help='The topic on which verify nodes listen'),
    cfg.StrOpt('manager',
               default='patron.verify.manager.VerifyManager',
               help='Full class name for the Manager for verify'),
    cfg.IntOpt('workers',
               help='Number of workers for OpenStack Verify service. '
                    'The default will be the number of CPUs available.')
]
verify_group = cfg.OptGroup(name='verify',
                               title='Verify Options')
CONF = cfg.CONF
CONF.register_group(verify_group)
CONF.register_opts(verify_opts, verify_group)

LOG = logging.getLogger(__name__)


class LocalAPI(object):
    """A local version of the verify API that does database updates
    locally instead of via RPC.
    """

    def __init__(self):
        # TODO(danms): This needs to be something more generic for
        # other/future users of this sort of functionality.
        self._manager = utils.ExceptionHelper(manager.VerifyManager())

    def verify(self, context, op, target, bypass):
        return self._manager.verify(
            context, op, target, bypass)


class API(LocalAPI):
    """Verify API that does updates via RPC to the VerifyManager."""

    def __init__(self):
        self._manager = rpcapi.VerifyAPI()
        self.base_rpcapi = baserpc.BaseAPI(topic=CONF.verify.topic)

    def verify(self, context, op, target, bypass):
        return self._manager.verify(
            context, op, target, bypass)
