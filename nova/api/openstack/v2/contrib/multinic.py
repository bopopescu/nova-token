begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""The multinic extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
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
op|'.'
name|'v2'
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
name|'log'
name|'as'
name|'logging'
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
string|'"nova.api.openstack.v2.contrib.multinic"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Note: The class name is as it has to be for this to be loaded as an'
nl|'\n'
comment|'# extension--only first character capitalized.'
nl|'\n'
DECL|class|Multinic
name|'class'
name|'Multinic'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Multiple network support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Multinic"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"NMN"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/multinic/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-06-09T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize the extension.\n\n        Gets a compute.API object so we can call the back-end\n        add_fixed_ip() and remove_fixed_ip() methods.\n        """'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'Multinic'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ext_mgr'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the actions the extension adds, as required by contract."""'
newline|'\n'
nl|'\n'
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Add the add_fixed_ip action'
nl|'\n'
name|'act'
op|'='
name|'extensions'
op|'.'
name|'ActionExtension'
op|'('
string|'"servers"'
op|','
string|'"addFixedIp"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_add_fixed_ip'
op|')'
newline|'\n'
name|'actions'
op|'.'
name|'append'
op|'('
name|'act'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add the remove_fixed_ip action'
nl|'\n'
name|'act'
op|'='
name|'extensions'
op|'.'
name|'ActionExtension'
op|'('
string|'"servers"'
op|','
string|'"removeFixedIp"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_remove_fixed_ip'
op|')'
newline|'\n'
name|'actions'
op|'.'
name|'append'
op|'('
name|'act'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'actions'
newline|'\n'
nl|'\n'
DECL|member|_get_instance
dedent|''
name|'def'
name|'_get_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Server not found"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_fixed_ip
dedent|''
dedent|''
name|'def'
name|'_add_fixed_ip'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds an IP on a given network to an instance."""'
newline|'\n'
nl|'\n'
comment|'# Validate the input entity'
nl|'\n'
name|'if'
string|"'networkId'"
name|'not'
name|'in'
name|'input_dict'
op|'['
string|"'addFixedIp'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing \'networkId\' argument for addFixedIp"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'network_id'
op|'='
name|'input_dict'
op|'['
string|"'addFixedIp'"
op|']'
op|'['
string|"'networkId'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'add_fixed_ip'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'network_id'
op|')'
newline|'\n'
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
DECL|member|_remove_fixed_ip
dedent|''
name|'def'
name|'_remove_fixed_ip'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes an IP from an instance."""'
newline|'\n'
nl|'\n'
comment|'# Validate the input entity'
nl|'\n'
name|'if'
string|"'address'"
name|'not'
name|'in'
name|'input_dict'
op|'['
string|"'removeFixedIp'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing \'address\' argument for removeFixedIp"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'address'
op|'='
name|'input_dict'
op|'['
string|"'removeFixedIp'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'remove_fixed_ip'
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
name|'exceptions'
op|'.'
name|'FixedIpNotFoundForSpecificInstance'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Unable to find address %r"'
op|')'
op|'%'
name|'address'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
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
dedent|''
dedent|''
endmarker|''
end_unit
