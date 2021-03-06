begin_unit
comment|'# Copyright 2015 IBM Corp.'
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
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
nl|'\n'
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
name|'import'
name|'preserve_ephemeral_rebuild'
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
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-preserve-ephemeral-rebuild"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PreserveEphemeralRebuild
name|'class'
name|'PreserveEphemeralRebuild'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Allow preservation of the ephemeral partition on rebuild."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"PreserveEphemeralOnRebuild"'
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
name|'return'
op|'['
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
nl|'\n'
DECL|member|server_rebuild
dedent|''
name|'def'
name|'server_rebuild'
op|'('
name|'self'
op|','
name|'rebuild_dict'
op|','
name|'rebuild_kwargs'
op|','
nl|'\n'
name|'body_deprecated_param'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'preserve_ephemeral'"
name|'in'
name|'rebuild_dict'
op|':'
newline|'\n'
indent|'            '
name|'rebuild_kwargs'
op|'['
string|"'preserve_ephemeral'"
op|']'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
nl|'\n'
name|'rebuild_dict'
op|'['
string|"'preserve_ephemeral'"
op|']'
op|','
name|'strict'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_server_rebuild_schema
dedent|''
dedent|''
name|'def'
name|'get_server_rebuild_schema'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'preserve_ephemeral_rebuild'
op|'.'
name|'server_rebuild'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
