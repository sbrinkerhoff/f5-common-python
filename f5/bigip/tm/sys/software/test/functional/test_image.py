# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#


from f5.sdk_exception import UnsupportedOperation
import pytest


class TestImage(object):
    def test_create_raises(self, mgmt_root):
        with pytest.raises(UnsupportedOperation):
            mgmt_root.tm.sys.software.images.image.create()

    def test_modify_raises(self, mgmt_root):
        with pytest.raises(UnsupportedOperation):
            mgmt_root.tm.sys.software.images.image.modify()

    def test_update_raises(self, mgmt_root):
        with pytest.raises(UnsupportedOperation):
            mgmt_root.tm.sys.software.images.image.update()

    def test_delete(self, mgmt_root):
        # Until we are able to install ISOs in Jenkins (which will allow us to
        # create images) we cannot test delete
        pass

    def test_load(self, mgmt_root, opt_release):
        # Until we are able to install ISOs in Jenkins (which will allow us to
        # create images) we cannot test load
        pass

    def test_collection(self, mgmt_root):
        # Until we are able to install ISOs in Jenkins (which will allow us to
        # create images) we cannot test collection
        pass
