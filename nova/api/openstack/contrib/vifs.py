begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (C) 2011 Midokura KK'
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
comment|'#    under the License'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
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
nl|'\n'
nl|'\n'
DECL|function|_translate_vif_view
name|'def'
name|'_translate_vif_view'
op|'('
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
op|'{'
string|"'id'"
op|':'
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'mac'"
op|':'
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'vif'
op|'['
string|"'network_id'"
op|']'
op|'}'
newline|'\n'
name|'return'
op|'{'
string|"'vif'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_vifs_view
dedent|''
name|'def'
name|'_translate_vifs_view'
op|'('
name|'vifs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'vifs'"
op|':'
op|'['
name|'_translate_vif_view'
op|'('
name|'vif'
op|')'
name|'for'
name|'vif'
name|'in'
name|'vifs'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerVIFController
dedent|''
name|'class'
name|'ServerVIFController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The controller for VIFs attached to servers.\n\n    A child resource of the server.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"vif"'
op|':'
op|'['
nl|'\n'
string|'"id"'
op|','
nl|'\n'
string|'"mac"'
op|','
nl|'\n'
string|'"network_id"'
op|','
nl|'\n'
op|']'
op|'}'
op|'}'
op|'}'
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
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'ServerVIFController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
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
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the vifs of the server."""'
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
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'_translate_vifs_view'
op|'('
name|'vifs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIFs
dedent|''
dedent|''
name|'class'
name|'VIFs'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
DECL|member|get_name
indent|'    '
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"VIFs"'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"os-vifs"'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"VIF support"'
newline|'\n'
nl|'\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"http://docs.openstack.org/ext/vifs/api/v1.1"'
newline|'\n'
nl|'\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"2011-07-11T00:00:00+00:00"'
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
string|"'os-server_vifs'"
op|','
nl|'\n'
name|'ServerVIFController'
op|'('
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
dedent|''
dedent|''
endmarker|''
end_unit
