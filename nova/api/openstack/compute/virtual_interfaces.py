begin_unit
comment|'# Copyright (C) 2011 Midokura KK'
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
string|'"""The virtual interfaces extension."""'
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
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-virtual-interfaces'"
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
DECL|function|_translate_vif_summary_view
name|'def'
name|'_translate_vif_summary_view'
op|'('
name|'_context'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for VIF summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'vif'
op|'.'
name|'uuid'
newline|'\n'
name|'d'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'vif'
op|'.'
name|'address'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerVirtualInterfaceController
dedent|''
name|'class'
name|'ServerVirtualInterfaceController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The instance VIF API controller for the OpenStack API.\n    """'
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
name|'ServerVirtualInterfaceController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_items
dedent|''
name|'def'
name|'_items'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'entity_maker'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of VIFs, transformed through entity_maker."""'
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
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'vifs'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_vifs_by_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'vifs'
op|','
name|'req'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
name|'entity_maker'
op|'('
name|'context'
op|','
name|'vif'
op|')'
name|'for'
name|'vif'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'virtual_interfaces'"
op|':'
name|'res'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
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
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of VIFs for a given instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'server_id'
op|','
nl|'\n'
name|'entity_maker'
op|'='
name|'_translate_vif_summary_view'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtualInterfaces
dedent|''
dedent|''
name|'class'
name|'VirtualInterfaces'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Virtual interface support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"VirtualInterfaces"'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
name|'ALIAS'
op|','
nl|'\n'
name|'controller'
op|'='
name|'ServerVirtualInterfaceController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'server'"
op|','
name|'collection_name'
op|'='
string|"'servers'"
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
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
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit