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
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'socket'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_my_ip
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
DECL|variable|global_opts
dedent|''
dedent|''
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
string|"'osapi_compute_unique_server_name_scope'"
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
string|"'When set, compute API will consider duplicate hostnames '"
nl|'\n'
string|"'invalid within the specified scope, regardless of case. '"
nl|'\n'
string|'\'Should be empty, "project" or "global".\''
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
name|'getfqdn'
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
string|"'nova.volume.cinder.API'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The full class name of the volume API class to use'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'global_opts'
op|')'
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
name|'rpc'
op|'.'
name|'set_defaults'
op|'('
name|'control_exchange'
op|'='
string|"'nova'"
op|')'
newline|'\n'
name|'cfg'
op|'.'
name|'CONF'
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
dedent|''
endmarker|''
end_unit
