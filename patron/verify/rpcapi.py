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

"""Client side of the verify RPC API."""

from oslo_config import cfg
import oslo_messaging as messaging
from oslo_serialization import jsonutils

from patron.objects import base as objects_base
from patron import rpc

CONF = cfg.CONF

rpcapi_cap_opt = cfg.StrOpt('verify',
        help='Set a version cap for messages sent to verify services')
CONF.register_opt(rpcapi_cap_opt, 'upgrade_levels')


class VerifyAPI(object):
    """Client side of the verify RPC API

    API version history:

    * 1.0 - Initial version.

    """

    VERSION_ALIASES = {
        'kilo': '1.0',
    }

    def __init__(self):
        super(VerifyAPI, self).__init__()
        target = messaging.Target(topic=CONF.verify.topic, version='1.0')
        version_cap = self.VERSION_ALIASES.get(CONF.upgrade_levels.verify,
                                               CONF.upgrade_levels.verify)
        # serializer = objects_base.NovaObjectSerializer()
        self.client = rpc.get_client(target,
                                     version_cap=version_cap,
                                     serializer=None)

    def verify(self, context, op, target, bypass):
        cctxt = self.client.prepare()
        return cctxt.call(context, 'verify', op=op, target=target, bypass=bypass)
