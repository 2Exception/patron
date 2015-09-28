# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Peking University.
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

# Edited by Yang Luo.
# This is the base class for an adapter, deny all acceses.

class BaseAdapter(object):

    def __init__(self):
        self.loaded = False

    def clear(self):
        self.loaded = False

    def is_loaded(self):
        return self.loaded

    def set_policy(self, data, default_rule, overwrite=True, use_conf=True):
        self.loaded = True

    def enforce(self, rule, target, creds):
        return False