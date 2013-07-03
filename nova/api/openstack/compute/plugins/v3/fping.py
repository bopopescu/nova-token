begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'fping'"
op|')'
newline|'\n'
DECL|variable|authorize_all_tenants
name|'authorize_all_tenants'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
nl|'\n'
string|"'compute'"
op|','
string|"'fping:all_tenants'"
op|')'
newline|'\n'
DECL|variable|fping_opts
name|'fping_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"fping_path"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"/usr/sbin/fping"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Full path to fping."'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'fping_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FpingController
name|'class'
name|'FpingController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'network_api'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'last_call'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|check_fping
dedent|''
name|'def'
name|'check_fping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'os'
op|'.'
name|'access'
op|'('
name|'CONF'
op|'.'
name|'fping_path'
op|','
name|'os'
op|'.'
name|'X_OK'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPServiceUnavailable'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"fping utility is not found."'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|fping
name|'def'
name|'fping'
op|'('
name|'ips'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fping_ret'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
name|'CONF'
op|'.'
name|'fping_path'
op|','
op|'*'
name|'ips'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fping_ret'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'set'
op|'('
op|')'
newline|'\n'
dedent|''
name|'alive_ips'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'fping_ret'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|'"\\n"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|'" "'
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
string|'"alive"'
name|'in'
name|'line'
op|':'
newline|'\n'
indent|'                '
name|'alive_ips'
op|'.'
name|'add'
op|'('
name|'ip'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'alive_ips'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_instance_ips
name|'def'
name|'_get_instance_ips'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'network'
name|'in'
name|'common'
op|'.'
name|'get_networks_for_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|')'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'all_ips'
op|'='
name|'itertools'
op|'.'
name|'chain'
op|'('
name|'network'
op|'['
string|'"ips"'
op|']'
op|','
name|'network'
op|'['
string|'"floating_ips"'
op|']'
op|')'
newline|'\n'
name|'ret'
op|'+='
op|'['
name|'ip'
op|'['
string|'"address"'
op|']'
name|'for'
name|'ip'
name|'in'
name|'all_ips'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'search_opts'
op|'='
name|'dict'
op|'('
name|'deleted'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
string|'"all_tenants"'
name|'in'
name|'req'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'authorize_all_tenants'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'project_id'
op|':'
newline|'\n'
indent|'                '
name|'search_opts'
op|'['
string|'"project_id"'
op|']'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'search_opts'
op|'['
string|'"user_id"'
op|']'
op|'='
name|'context'
op|'.'
name|'user_id'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'check_fping'
op|'('
op|')'
newline|'\n'
name|'include'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|'"include"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'include'
op|':'
newline|'\n'
indent|'            '
name|'include'
op|'='
name|'set'
op|'('
name|'include'
op|'.'
name|'split'
op|'('
string|'","'
op|')'
op|')'
newline|'\n'
name|'exclude'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'include'
op|'='
name|'None'
newline|'\n'
name|'exclude'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|'"exclude"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'exclude'
op|':'
newline|'\n'
indent|'                '
name|'exclude'
op|'='
name|'set'
op|'('
name|'exclude'
op|'.'
name|'split'
op|'('
string|'","'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'exclude'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'instance_list'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
nl|'\n'
name|'context'
op|','
name|'search_opts'
op|'='
name|'search_opts'
op|')'
newline|'\n'
name|'ip_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance_ips'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instance_projects'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'instance_list'
op|':'
newline|'\n'
indent|'            '
name|'uuid'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
name|'if'
name|'uuid'
name|'in'
name|'exclude'
name|'or'
op|'('
name|'include'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'uuid'
name|'not'
name|'in'
name|'include'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'ips'
op|'='
op|'['
name|'str'
op|'('
name|'ip'
op|')'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'.'
name|'_get_instance_ips'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|']'
newline|'\n'
name|'instance_ips'
op|'['
name|'uuid'
op|']'
op|'='
name|'ips'
newline|'\n'
name|'instance_projects'
op|'['
name|'uuid'
op|']'
op|'='
name|'instance'
op|'['
string|'"project_id"'
op|']'
newline|'\n'
name|'ip_list'
op|'+='
name|'ips'
newline|'\n'
dedent|''
name|'alive_ips'
op|'='
name|'self'
op|'.'
name|'fping'
op|'('
name|'ip_list'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'instance_uuid'
op|','
name|'ips'
name|'in'
name|'instance_ips'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|'"project_id"'
op|':'
name|'instance_projects'
op|'['
name|'instance_uuid'
op|']'
op|','
nl|'\n'
string|'"alive"'
op|':'
name|'bool'
op|'('
name|'set'
op|'('
name|'ips'
op|')'
op|'&'
name|'alive_ips'
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"servers"'
op|':'
name|'res'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_fping'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'ips'
op|'='
op|'['
name|'str'
op|'('
name|'ip'
op|')'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'.'
name|'_get_instance_ips'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|']'
newline|'\n'
name|'alive_ips'
op|'='
name|'self'
op|'.'
name|'fping'
op|'('
name|'ips'
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
string|'"project_id"'
op|':'
name|'instance'
op|'['
string|'"project_id"'
op|']'
op|','
nl|'\n'
string|'"alive"'
op|':'
name|'bool'
op|'('
name|'set'
op|'('
name|'ips'
op|')'
op|'&'
name|'alive_ips'
op|')'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Fping
dedent|''
dedent|''
dedent|''
name|'class'
name|'Fping'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fping Management Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Fping"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-fping"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/fping/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-07-06T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|'"os-fping"'
op|','
nl|'\n'
name|'FpingController'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'res'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
