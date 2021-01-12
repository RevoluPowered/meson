# Copyright 2020 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''This module provides the configuration for the MSVC compiler
    it is hoped we can extend it to intel compiler in the future but for now its msvc only'''

import os

class MSVCDetector:

    def environment_has_msvc_configured(self, current_env):
        return False

    def configure_msvc_environment(self, current_env):
        print("Hello world!")
        # algorithms for non legacy msvc compiler design
        # based on my work at https://gist.github.com/RevoluPowered/df2827158fd4011d5b25dab501c04123

        # lookup or download vswhere
        # run vswhere
        # exec query MSVC latest from vswhere
        # store environment
        # get_directory of the vcvarsall file
        # set up platform 32 bit or 64 bit
        # diff *all* set environment variables from vswhere vs environment before hand
        pass
