begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
name|'import'
name|'setuptools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'setup'
name|'as'
name|'common_setup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
DECL|variable|requires
name|'requires'
op|'='
name|'common_setup'
op|'.'
name|'parse_requirements'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'setuptools'
op|'.'
name|'setup'
op|'('
name|'name'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
name|'version'
op|'.'
name|'canonical_version_string'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|"'cloud computing fabric controller'"
op|','
nl|'\n'
DECL|variable|author
name|'author'
op|'='
string|"'OpenStack'"
op|','
nl|'\n'
DECL|variable|author_email
name|'author_email'
op|'='
string|"'nova@lists.launchpad.net'"
op|','
nl|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'http://www.openstack.org/'"
op|','
nl|'\n'
DECL|variable|classifiers
name|'classifiers'
op|'='
op|'['
nl|'\n'
string|"'Environment :: OpenStack'"
op|','
nl|'\n'
string|"'Intended Audience :: Information Technology'"
op|','
nl|'\n'
string|"'Intended Audience :: System Administrators'"
op|','
nl|'\n'
string|"'License :: OSI Approved :: Apache Software License'"
op|','
nl|'\n'
string|"'Operating System :: POSIX :: Linux'"
op|','
nl|'\n'
string|"'Programming Language :: Python'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 2'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 2.7'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|cmdclass
name|'cmdclass'
op|'='
name|'common_setup'
op|'.'
name|'get_cmdclass'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|packages
name|'packages'
op|'='
name|'setuptools'
op|'.'
name|'find_packages'
op|'('
name|'exclude'
op|'='
op|'['
string|"'bin'"
op|','
string|"'smoketests'"
op|']'
op|')'
op|','
nl|'\n'
DECL|variable|install_requires
name|'install_requires'
op|'='
name|'requires'
op|','
nl|'\n'
DECL|variable|include_package_data
name|'include_package_data'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|test_suite
name|'test_suite'
op|'='
string|"'nose.collector'"
op|','
nl|'\n'
name|'setup_requires'
op|'='
op|'['
string|"'setuptools_git>=0.4'"
op|']'
op|','
nl|'\n'
DECL|variable|scripts
name|'scripts'
op|'='
op|'['
string|"'bin/nova-all'"
op|','
nl|'\n'
string|"'bin/nova-api'"
op|','
nl|'\n'
string|"'bin/nova-api-ec2'"
op|','
nl|'\n'
string|"'bin/nova-api-metadata'"
op|','
nl|'\n'
string|"'bin/nova-api-os-compute'"
op|','
nl|'\n'
string|"'bin/nova-rpc-zmq-receiver'"
op|','
nl|'\n'
string|"'bin/nova-cert'"
op|','
nl|'\n'
string|"'bin/nova-clear-rabbit-queues'"
op|','
nl|'\n'
string|"'bin/nova-compute'"
op|','
nl|'\n'
string|"'bin/nova-conductor'"
op|','
nl|'\n'
string|"'bin/nova-console'"
op|','
nl|'\n'
string|"'bin/nova-consoleauth'"
op|','
nl|'\n'
string|"'bin/nova-dhcpbridge'"
op|','
nl|'\n'
string|"'bin/nova-manage'"
op|','
nl|'\n'
string|"'bin/nova-network'"
op|','
nl|'\n'
string|"'bin/nova-novncproxy'"
op|','
nl|'\n'
string|"'bin/nova-objectstore'"
op|','
nl|'\n'
string|"'bin/nova-rootwrap'"
op|','
nl|'\n'
string|"'bin/nova-scheduler'"
op|','
nl|'\n'
string|"'bin/nova-xvpvncproxy'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|py_modules
name|'py_modules'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
endmarker|''
end_unit
