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
comment|'# Copyright 2012 Red Hat, Inc.'
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
nl|'\n'
string|'"""Command-line flag library.\n\nEmulates gflags by wrapping cfg.ConfigOpts.\n\nThe idea is to move fully to cfg eventually, and this wrapper is a\nstepping stone.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_args
name|'def'
name|'parse_args'
op|'('
name|'argv'
op|','
name|'default_config_files'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'FLAGS'
op|'.'
name|'disable_interspersed_args'
op|'('
op|')'
newline|'\n'
name|'return'
name|'argv'
op|'['
op|':'
number|'1'
op|']'
op|'+'
name|'FLAGS'
op|'('
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|','
nl|'\n'
name|'project'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'default_config_files'
op|'='
name|'default_config_files'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnrecognizedFlag
dedent|''
name|'class'
name|'UnrecognizedFlag'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DECLARE
dedent|''
name|'def'
name|'DECLARE'
op|'('
name|'name'
op|','
name|'module_string'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'module_string'
name|'not'
name|'in'
name|'sys'
op|'.'
name|'modules'
op|':'
newline|'\n'
indent|'        '
name|'__import__'
op|'('
name|'module_string'
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'name'
name|'not'
name|'in'
name|'flag_values'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'UnrecognizedFlag'
op|'('
string|"'%s not defined by %s'"
op|'%'
op|'('
name|'name'
op|','
name|'module_string'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_my_ip
dedent|''
dedent|''
name|'def'
name|'_get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Returns the actual ip of the local machine.\n\n    This code figures out what source address would be used if some traffic\n    were to be sent out to some well known address on the Internet. In this\n    case, a Google DNS server is used, but the specific address does not\n    matter much.  No traffic is actually sent.\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'csock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'connect'
op|'('
op|'('
string|"'8.8.8.8'"
op|','
number|'80'
op|')'
op|')'
newline|'\n'
op|'('
name|'addr'
op|','
name|'port'
op|')'
op|'='
name|'csock'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'addr'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"127.0.0.1"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|core_opts
dedent|''
dedent|''
name|'core_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'connection_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Deprecated (use compute_driver instead): Virtualization '"
nl|'\n'
string|"'api connection type : libvirt, xenapi, or fake'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sql_connection'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'sqlite:///$state_path/$sqlite_db'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The SQLAlchemy connection string used to connect to the '"
nl|'\n'
string|"'database'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'api_paste_config'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"api-paste.ini"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'File name for the paste.deploy config for nova-api'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pybasedir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|"'../'"
op|')'
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the nova python module is installed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'bindir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir/bin'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where nova binaries are installed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'state_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Top-level directory for maintaining nova\'s state"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'lock_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory to use for lock files'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|debug_opts
name|'debug_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'fake_network'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If passed, use fake network devices and addresses'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'sql_connection_debug'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
name|'help'
op|'='
string|"'Verbosity of SQL debugging information. 0=None, '"
nl|'\n'
string|"'100=Everything'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'sql_connection_trace'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Add python stack traces to SQL as comment strings'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'FLAGS'
op|'.'
name|'register_cli_opts'
op|'('
name|'core_opts'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_cli_opts'
op|'('
name|'debug_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|global_opts
name|'global_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'my_ip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'_get_my_ip'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'ip address of this host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'region_list'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|"'list of region=fqdn pairs separated by commas'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'aws_access_key_id'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'admin'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'AWS Access ID'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'aws_secret_access_key'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'admin'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'AWS Access Key'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'glance_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'default glance hostname or ip'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'glance_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'9292'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'default glance port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'glance_api_servers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'$glance_host:$glance_port'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of the glance api servers available to nova '"
nl|'\n'
string|"'([hostname|ip]:port)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'glance_num_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number retries when downloading an image from glance'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'s3_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3333'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'port used when accessing the s3 api'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'s3_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'hostname or ip for openstack to use when accessing '"
nl|'\n'
string|"'the s3 api'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'s3_dmz'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'hostname or ip for the instances to use when accessing '"
nl|'\n'
string|"'the s3 api'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cert_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cert'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic cert nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'compute'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic compute nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'console'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic console proxy nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'scheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic scheduler nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'volume'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic volume nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'network'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic network nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'api_rate_limit'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'whether to rate limit the api'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'enabled_apis'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'ec2'"
op|','
string|"'osapi_compute'"
op|','
string|"'osapi_volume'"
op|','
string|"'metadata'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'a list of APIs to enable by default'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ec2_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the ip of the ec2 api server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ec2_dmz_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the internal ip of the ec2 api server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ec2_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8773'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the port of the ec2 api server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ec2_scheme'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the protocol to use when connecting to the ec2 api '"
nl|'\n'
string|"'server (http, https)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ec2_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/services/Cloud'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the path prefix used to call the ec2 api server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'osapi_compute_ext_list'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Specify list of extensions to load when using osapi_'"
nl|'\n'
string|"'compute_extension option with nova.api.openstack.'"
nl|'\n'
string|"'compute.contrib.select_extensions'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.standard_extensions'"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'osapi compute extension to load'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'osapi_volume_ext_list'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Specify list of extensions to load when using osapi_'"
nl|'\n'
string|"'volume_extension option with nova.api.openstack.'"
nl|'\n'
string|"'volume.contrib.select_extensions'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'osapi_volume_extension'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.volume.contrib.standard_extensions'"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'osapi volume extension to load'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_scheme'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the protocol to use when connecting to the openstack api '"
nl|'\n'
string|"'server (http, https)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/v1.1/'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the path prefix used to call the openstack api server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_compute_link_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base URL that will be presented to users in links '"
nl|'\n'
string|"'to the OpenStack Compute API'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_glance_link_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base URL that will be presented to users in links '"
nl|'\n'
string|"'to glance resources'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'osapi_max_limit'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the maximum number of items returned in a single '"
nl|'\n'
string|"'response from a collection resource'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'metadata_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the ip for the metadata api server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'metadata_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8775'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the port for the metadata api port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_project'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'openstack'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the default project to use for openstack'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_image'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'ami-11111'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'default image to use, testing only'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_instance_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'m1.small'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'default instance type to use, testing only'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'null_kernel'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nokernel'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'kernel image that indicates not to use a kernel, but to '"
nl|'\n'
string|"'use a raw disk image instead'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vpn_image_id'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'image id used when starting up a cloudpipe vpn server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vpn_key_suffix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'-vpn'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Suffix to add to project name for vpn key and secgroups'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'auth_token_ttl'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds for auth tokens to linger'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sqlite_db'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.sqlite'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the filename to use with sqlite'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'sqlite_synchronous'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If passed, use synchronous mode for sqlite'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'sql_idle_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'timeout before idle sql connections are reaped'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'sql_max_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'maximum db connection retries during startup. '"
nl|'\n'
string|"'(setting -1 implies an infinite retry count)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'sql_retry_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'interval between retries of opening a sql connection'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.compute.manager.ComputeManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the Manager for compute'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.console.manager.ConsoleProxyManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the Manager for console proxy'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cert_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cert.manager.CertManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the Manager for cert'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'instance_dns_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.dns_driver.DNSDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the DNS Manager for instance IPs'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'instance_dns_domain'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the DNS Zone for instance IPs'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'floating_ip_dns_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.dns_driver.DNSDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the DNS Manager for floating IPs'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.manager.VlanManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the Manager for network'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.volume.manager.VolumeManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the Manager for volume'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.manager.SchedulerManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'full class name for the Manager for scheduler'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of this node.  This can be an opaque identifier.  '"
nl|'\n'
string|"'It is not necessarily a hostname, FQDN, or IP address. '"
nl|'\n'
string|"'However, the node name must be valid within '"
nl|'\n'
string|"'an AMQP key, and if using ZeroMQ, a valid '"
nl|'\n'
string|"'hostname, FQDN, or IP address'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'node_availability_zone'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'availability zone of this node'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'memcached_servers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Memcached servers or None for in process cache.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'instance_usage_audit_period'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'month'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'time period to generate instance usages for.  '"
nl|'\n'
string|"'Time period must be hour, day, month or year'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'bandwith_poll_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'interval to pull bandwidth usage info'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'start_guests_on_host_boot'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to restart guests when the host reboots'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'resume_guests_state_on_host_boot'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to start guests that were running before the '"
nl|'\n'
string|"'host rebooted'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_ephemeral_format'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The default format an ephemeral_volume will be '"
nl|'\n'
string|"'formatted with on creation.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'root_helper'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'sudo'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Deprecated: command to use for running commands as root'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rootwrap_config'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Path to the rootwrap configuration file to use for '"
nl|'\n'
string|"'running commands as root'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.linux_net'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for network creation'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_ipv6'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'use ipv6'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'enable_instance_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allows use of instance password during '"
nl|'\n'
string|"'server creation'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'password_length'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'12'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Length of generated instance admin passwords'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'monkey_patch'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to log monkey patching'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'monkey_patch_modules'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'nova.api.ec2.cloud:nova.notifier.api.notify_decorator'"
op|','
nl|'\n'
string|"'nova.compute.api:nova.notifier.api.notify_decorator'"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'List of modules/decorators to monkey patch'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'allow_resize_to_same_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allow destination machine to match source for resize. '"
nl|'\n'
string|"'Useful when testing in single-host environments.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reclaim_instance_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Interval in seconds for reclaiming deleted instances'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'zombie_instance_updated_at_window'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'172800'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds zombie instances are cleaned up.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'service_down_time'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'maximum time since last check-in for up service'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_schedule_zone'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'availability zone to use when user doesn\\'t specify one'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'isolated_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Images to run on isolated host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'isolated_hosts'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Host reserved for specific images'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cache_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'all'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Cache glance images locally. `all` will cache all'"
nl|'\n'
string|"' images, `some` will only cache images that have the'"
nl|'\n'
string|"' image_property `cache_in_nova=True`, and `none` turns'"
nl|'\n'
string|"' off caching entirely'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_cow_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to use cow images'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_api_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.compute.api.API'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The full class name of the compute API class to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_api_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.api.API'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The full class name of the network API class to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_api_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.volume.api.API'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The full class name of the volume API class to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'security_group_handler'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.sg.NullSecurityGroupHandler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The full class name of the security group handler class'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_access_ip_network_name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of network to use to set access ips for instances'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'auth_strategy'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'noauth'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The strategy to use for auth: noauth or keystone.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'non_inheritable_image_properties'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'cache_in_nova'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|','
nl|'\n'
string|"'user_id'"
op|','
nl|'\n'
string|"'image_type'"
op|','
nl|'\n'
string|"'backup_type'"
op|','
nl|'\n'
string|"'min_ram'"
op|','
nl|'\n'
string|"'min_disk'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'These are image properties which a snapshot should not'"
nl|'\n'
string|"' inherit from an instance'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'defer_iptables_apply'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to batch up the application of IPTables rules'"
nl|'\n'
string|"' during a host restart and apply all at the end of the'"
nl|'\n'
string|"' init phase'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'global_opts'
op|')'
newline|'\n'
endmarker|''
end_unit
