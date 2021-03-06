begin_unit
comment|'#   Copyright 2012 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
string|'"""The Extended Server Attributes API extension."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'api_version_request'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-extended-server-attributes"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_soft_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|soft_authorize
name|'soft_authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_soft_authorizer'
op|'('
string|"'servers'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerAttributesController
name|'class'
name|'ExtendedServerAttributesController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ExtendedServerAttributesController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extend_server
dedent|''
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server'
op|','
name|'instance'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"OS-EXT-SRV-ATTR:hypervisor_hostname"'
newline|'\n'
name|'server'
op|'['
name|'key'
op|']'
op|'='
name|'instance'
op|'.'
name|'node'
newline|'\n'
nl|'\n'
name|'properties'
op|'='
op|'['
string|"'host'"
op|','
string|"'name'"
op|']'
newline|'\n'
name|'if'
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.3'"
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mriedem): These will use the OS-EXT-SRV-ATTR prefix below'
nl|'\n'
comment|"# and that's OK for microversion 2.3 which is being compatible"
nl|'\n'
comment|'# with v2.0 for the ec2 API split out from Nova. After this,'
nl|'\n'
comment|'# however, new microversoins should not be using the'
nl|'\n'
comment|'# OS-EXT-SRV-ATTR prefix.'
nl|'\n'
indent|'            '
name|'properties'
op|'+='
op|'['
string|"'reservation_id'"
op|','
string|"'launch_index'"
op|','
nl|'\n'
string|"'hostname'"
op|','
string|"'kernel_id'"
op|','
string|"'ramdisk_id'"
op|','
nl|'\n'
string|"'root_device_name'"
op|','
string|"'user_data'"
op|']'
newline|'\n'
dedent|''
name|'for'
name|'attr'
name|'in'
name|'properties'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attr'
op|'=='
string|"'name'"
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
string|'"OS-EXT-SRV-ATTR:instance_%s"'
op|'%'
name|'attr'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(mriedem): Nothing after microversion 2.3 should use the'
nl|'\n'
comment|'# OS-EXT-SRV-ATTR prefix for the attribute key name.'
nl|'\n'
indent|'                '
name|'key'
op|'='
string|'"OS-EXT-SRV-ATTR:%s"'
op|'%'
name|'attr'
newline|'\n'
dedent|''
name|'server'
op|'['
name|'key'
op|']'
op|'='
name|'instance'
op|'['
name|'attr'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_server_host_status
dedent|''
dedent|''
name|'def'
name|'_server_host_status'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server'
op|','
name|'instance'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_status'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance_host_status'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'server'
op|'['
string|"'host_status'"
op|']'
op|'='
name|'host_status'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
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
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_extend'
op|'='
name|'False'
newline|'\n'
name|'authorize_host_status'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'authorize_extend'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.16'"
op|')'
name|'and'
nl|'\n'
name|'soft_authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'show:host_status'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'authorize_host_status'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'authorize_extend'
name|'or'
name|'authorize_host_status'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'db_instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'show' method."
nl|'\n'
name|'if'
name|'authorize_extend'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'db_instance'
op|','
name|'req'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'authorize_host_status'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_server_host_status'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'db_instance'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_extend'
op|'='
name|'False'
newline|'\n'
name|'authorize_host_status'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'authorize_extend'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.16'"
op|')'
name|'and'
nl|'\n'
name|'soft_authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'show:host_status'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'authorize_host_status'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'authorize_extend'
name|'or'
name|'authorize_host_status'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'instances'
op|'='
name|'req'
op|'.'
name|'get_db_instances'
op|'('
op|')'
newline|'\n'
comment|'# Instances is guaranteed to be in the cache due to'
nl|'\n'
comment|"# the core API adding it in its 'detail' method."
nl|'\n'
name|'if'
name|'authorize_host_status'
op|':'
newline|'\n'
indent|'                '
name|'host_statuses'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instances_host_statuses'
op|'('
nl|'\n'
name|'instances'
op|'.'
name|'values'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'authorize_extend'
op|':'
newline|'\n'
indent|'                    '
name|'instance'
op|'='
name|'instances'
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'instance'
op|','
name|'req'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'authorize_host_status'
op|':'
newline|'\n'
indent|'                    '
name|'server'
op|'['
string|"'host_status'"
op|']'
op|'='
name|'host_statuses'
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerAttributes
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtendedServerAttributes'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extended Server Attributes support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ExtendedServerAttributes"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'ExtendedServerAttributesController'
op|'('
op|')'
newline|'\n'
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'servers'"
op|','
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'extension'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
