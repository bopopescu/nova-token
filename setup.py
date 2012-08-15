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
DECL|variable|depend_links
name|'depend_links'
op|'='
name|'common_setup'
op|'.'
name|'parse_dependency_links'
op|'('
op|')'
newline|'\n'
DECL|variable|project
name|'project'
op|'='
string|"'nova'"
newline|'\n'
nl|'\n'
nl|'\n'
name|'setuptools'
op|'.'
name|'setup'
op|'('
nl|'\n'
DECL|variable|name
name|'name'
op|'='
name|'project'
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
name|'common_setup'
op|'.'
name|'get_version'
op|'('
name|'project'
op|','
string|"'2013.2'"
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
DECL|variable|dependency_links
name|'dependency_links'
op|'='
name|'depend_links'
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
DECL|variable|entry_points
name|'entry_points'
op|'='
op|'{'
nl|'\n'
string|"'console_scripts'"
op|':'
op|'['
nl|'\n'
string|"'nova-all = nova.cmd.all:main'"
op|','
nl|'\n'
string|"'nova-api = nova.cmd.api:main'"
op|','
nl|'\n'
string|"'nova-api-ec2 = nova.cmd.api_ec2:main'"
op|','
nl|'\n'
string|"'nova-api-metadata = nova.cmd.api_metadata:main'"
op|','
nl|'\n'
string|"'nova-api-os-compute = nova.cmd.api_os_compute:main'"
op|','
nl|'\n'
string|"'nova-baremetal-deploy-helper'"
nl|'\n'
string|"' = nova.cmd.baremetal_deploy_helper:main'"
op|','
nl|'\n'
string|"'nova-baremetal-manage = nova.cmd.baremetal_manage:main'"
op|','
nl|'\n'
string|"'nova-rpc-zmq-receiver = nova.cmd.rpc_zmq_receiver:main'"
op|','
nl|'\n'
string|"'nova-cells = nova.cmd.cells:main'"
op|','
nl|'\n'
string|"'nova-cert = nova.cmd.cert:main'"
op|','
nl|'\n'
string|"'nova-clear-rabbit-queues = nova.cmd.clear_rabbit_queues:main'"
op|','
nl|'\n'
string|"'nova-compute = nova.cmd.compute:main'"
op|','
nl|'\n'
string|"'nova-conductor = nova.cmd.conductor:main'"
op|','
nl|'\n'
string|"'nova-console = nova.cmd.console:main'"
op|','
nl|'\n'
string|"'nova-consoleauth = nova.cmd.consoleauth:main'"
op|','
nl|'\n'
string|"'nova-dhcpbridge = nova.cmd.dhcpbridge:main'"
op|','
nl|'\n'
string|"'nova-manage = nova.cmd.manage:main'"
op|','
nl|'\n'
string|"'nova-network = nova.cmd.network:main'"
op|','
nl|'\n'
string|"'nova-novncproxy = nova.cmd.novncproxy:main'"
op|','
nl|'\n'
string|"'nova-objectstore = nova.cmd.objectstore:main'"
op|','
nl|'\n'
string|"'nova-rootwrap = nova.cmd.rootwrap:main'"
op|','
nl|'\n'
string|"'nova-scheduler = nova.cmd.scheduler:main'"
op|','
nl|'\n'
string|"'nova-spicehtml5proxy = nova.cmd.spicehtml5proxy:main'"
op|','
nl|'\n'
string|"'nova-xvpvncproxy = nova.cmd.xvpvncproxy:main'"
nl|'\n'
op|']'
nl|'\n'
op|'}'
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
