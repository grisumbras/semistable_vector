#
# Copyright (c) 2025 Dmitry Arkhipov (grisumbras@yandex.ru)
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
#

from conan import ConanFile

class SemistableVectorConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'

    requires = ['boost-core/[>0-a,include_prerelease]']
    tool_requires = ['b2/[*]']
    python_requires = ['b2-tools/[>0,include_prerelease]']

    def layout(self):
        self.folders.build = 'build'
        self.folders.generators = 'build/generators'

    def generate(self):
        b2_tools = self.python_requires['b2-tools'].module
        deps = b2_tools.B2Deps(self)
        deps.generate()

        tc = b2_tools.B2Toolchain(self)
        tc.generate()
