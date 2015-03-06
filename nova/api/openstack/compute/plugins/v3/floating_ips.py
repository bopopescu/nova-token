begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
nl|'\n'
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 Eldar Nugaev, Kirill Shileev, Ilya Alekseyev'
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
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
newline|'\n'
name|'import'
name|'webob'
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
op|'.'
name|'compute'
op|'.'
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'floating_ips'
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
op|'.'
name|'api'
name|'import'
name|'validation'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-floating-ips'"
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ip_view
name|'def'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'floating_ip'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'ip'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'floating_ip'
op|'['
string|"'pool'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'floating_ip'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ips_view
dedent|''
name|'def'
name|'_translate_floating_ips_view'
op|'('
name|'floating_ips'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'floating_ips'"
op|':'
op|'['
name|'_translate_floating_ip_view'
op|'('
name|'ip'
op|')'
op|'['
string|"'floating_ip'"
op|']'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'floating_ips'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_by_floating_ip_addr
dedent|''
name|'def'
name|'get_instance_by_floating_ip_addr'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_instance_id_by_floating_address'
op|'('
nl|'\n'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpNotFoundForAddress'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpMultipleFoundForAddress'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'instance_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'common'
op|'.'
name|'get_instance'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|disassociate_floating_ip
dedent|''
dedent|''
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate_floating_ip'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Forbidden'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CannotDisassociateAutoAssignedFloatingIP'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot disassociate auto assigned floating ip'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPController
dedent|''
dedent|''
name|'class'
name|'FloatingIPController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Floating IPs API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIPController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
DECL|member|show
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
string|'"""Return data about the given floating ip."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'exception'
op|'.'
name|'FloatingIpNotFound'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Floating ip not found for id %s"'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidID'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""Return a list of floating ips allocated to a project."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'floating_ips'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ips_by_project'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'_translate_floating_ips_view'
op|'('
name|'floating_ips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'403'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|'='
name|'None'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'pool'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'body'
name|'and'
string|"'pool'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'='
name|'body'
op|'['
string|"'pool'"
op|']'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'allocate_floating_ip'
op|'('
name|'context'
op|','
name|'pool'
op|')'
newline|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoMoreFloatingIps'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'pool'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No more floating ips in pool %s."'
op|')'
op|'%'
name|'pool'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No more floating ips available."'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpLimitExceeded'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'pool'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"IP allocation over quota in pool %s."'
op|')'
op|'%'
name|'pool'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"IP allocation over quota."'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpPoolNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_translate_floating_ip_view'
op|'('
name|'ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
comment|'# get the floating ip object'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'exception'
op|'.'
name|'FloatingIpNotFound'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Floating ip not found for id %s"'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidID'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'address'
op|'='
name|'floating_ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
comment|'# get the associated instance object (if any)'
nl|'\n'
name|'instance'
op|'='
name|'get_instance_by_floating_ip_addr'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate_and_release_floating_ip'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'floating_ip'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Forbidden'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CannotDisassociateAutoAssignedFloatingIP'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot disassociate auto assigned floating ip'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPActionController
dedent|''
dedent|''
dedent|''
name|'class'
name|'FloatingIPActionController'
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
name|'FloatingIPActionController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
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
name|'self'
op|'.'
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'addFloatingIp'"
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'floating_ips'
op|'.'
name|'add_floating_ip'
op|')'
newline|'\n'
DECL|member|_add_floating_ip
name|'def'
name|'_add_floating_ip'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associate floating_ip to an instance."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'address'
op|'='
name|'body'
op|'['
string|"'addFloatingIp'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'common'
op|'.'
name|'get_instance'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'cached_nwinfo'
op|'='
name|'compute_utils'
op|'.'
name|'get_nw_info_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cached_nwinfo'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'No nw_info cache associated with instance'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fixed_ips'
op|'='
name|'cached_nwinfo'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'No fixed ips associated to instance'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fixed_address'
op|'='
name|'None'
newline|'\n'
name|'if'
string|"'fixed_address'"
name|'in'
name|'body'
op|'['
string|"'addFloatingIp'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'fixed_address'
op|'='
name|'body'
op|'['
string|"'addFloatingIp'"
op|']'
op|'['
string|"'fixed_address'"
op|']'
newline|'\n'
name|'for'
name|'fixed'
name|'in'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'fixed'
op|'['
string|"'address'"
op|']'
op|'=='
name|'fixed_address'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Specified fixed address not assigned to instance'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'fixed_address'
op|':'
newline|'\n'
indent|'            '
name|'fixed_address'
op|'='
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'fixed_ips'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'multiple fixed_ips exist, using the first: '"
nl|'\n'
string|"'%s'"
op|')'
op|','
name|'fixed_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'associate_floating_ip'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'floating_address'
op|'='
name|'address'
op|','
nl|'\n'
name|'fixed_address'
op|'='
name|'fixed_address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpAssociated'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'floating ip is already associated'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoFloatingIpInterface'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'l3driver call to add floating ip failed'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpNotFoundForAddress'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'floating ip not found'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Forbidden'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Unable to associate floating ip %(address)s to '"
nl|'\n'
string|"'fixed ip %(fixed_address)s for instance %(id)s. '"
nl|'\n'
string|"'Error: %(error)s'"
op|')'
op|'%'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
string|"'fixed_address'"
op|':'
name|'fixed_address'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'id'
op|','
string|"'error'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'removeFloatingIp'"
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'floating_ips'
op|'.'
name|'remove_floating_ip'
op|')'
newline|'\n'
DECL|member|_remove_floating_ip
name|'def'
name|'_remove_floating_ip'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Dissociate floating_ip from an instance."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'address'
op|'='
name|'body'
op|'['
string|"'removeFloatingIp'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
comment|'# get the floating ip object'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip_by_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpNotFoundForAddress'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"floating ip not found"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# get the associated instance object (if any)'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'get_instance_by_floating_ip_addr'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
comment|'# disassociate if associated'
nl|'\n'
name|'if'
op|'('
name|'instance'
name|'and'
nl|'\n'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'fixed_ip_id'"
op|')'
name|'and'
nl|'\n'
op|'('
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'id'
op|')'
name|'and'
nl|'\n'
op|'['
name|'instance'
op|'.'
name|'uuid'
op|'=='
name|'id'
op|']'
name|'or'
nl|'\n'
op|'['
name|'instance'
op|'.'
name|'id'
op|'=='
name|'id'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpNotAssociated'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Floating ip is not associated'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Floating ip %(address)s is not associated with instance "'
nl|'\n'
string|'"%(id)s."'
op|')'
op|'%'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
string|"'id'"
op|':'
name|'id'
op|'}'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIps
dedent|''
dedent|''
dedent|''
name|'class'
name|'FloatingIps'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Floating IPs support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FloatingIps"'
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
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'FloatingIPController'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resource'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
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
name|'FloatingIPActionController'
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
dedent|''
dedent|''
endmarker|''
end_unit
