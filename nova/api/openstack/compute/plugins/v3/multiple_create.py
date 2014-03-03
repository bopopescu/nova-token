begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-multiple-create"'
newline|'\n'
DECL|variable|MIN_ATTRIBUTE_NAME
name|'MIN_ATTRIBUTE_NAME'
op|'='
string|'"%s:min_count"'
op|'%'
name|'ALIAS'
newline|'\n'
DECL|variable|MAX_ATTRIBUTE_NAME
name|'MAX_ATTRIBUTE_NAME'
op|'='
string|'"%s:max_count"'
op|'%'
name|'ALIAS'
newline|'\n'
DECL|variable|RRID_ATTRIBUTE_NAME
name|'RRID_ATTRIBUTE_NAME'
op|'='
string|'"%s:return_reservation_id"'
op|'%'
name|'ALIAS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MultipleCreate
name|'class'
name|'MultipleCreate'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Allow multiple create in the Create Server v3 API."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"MultipleCreate"'
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
name|'return'
op|'['
op|']'
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
nl|'\n'
comment|'# use nova.api.extensions.server.extensions entry point to modify'
nl|'\n'
comment|'# server create kwargs'
nl|'\n'
DECL|member|server_create
dedent|''
name|'def'
name|'server_create'
op|'('
name|'self'
op|','
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
op|':'
newline|'\n'
comment|'# min_count and max_count are optional.  If they exist, they may come'
nl|'\n'
comment|'# in as strings.  Verify that they are valid integers and > 0.'
nl|'\n'
comment|"# Also, we want to default 'min_count' to 1, and default"
nl|'\n'
comment|"# 'max_count' to be 'min_count'."
nl|'\n'
indent|'        '
name|'min_count'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'MIN_ATTRIBUTE_NAME'
op|','
number|'1'
op|')'
newline|'\n'
name|'max_count'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'MAX_ATTRIBUTE_NAME'
op|','
name|'min_count'
op|')'
newline|'\n'
name|'return_id'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'RRID_ATTRIBUTE_NAME'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'min_count'
op|'='
name|'utils'
op|'.'
name|'validate_integer'
op|'('
name|'min_count'
op|','
nl|'\n'
string|'"min_count"'
op|','
name|'min_value'
op|'='
number|'1'
op|')'
newline|'\n'
name|'max_count'
op|'='
name|'utils'
op|'.'
name|'validate_integer'
op|'('
name|'max_count'
op|','
nl|'\n'
string|'"max_count"'
op|','
name|'min_value'
op|'='
number|'1'
op|')'
newline|'\n'
name|'return_id'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'return_id'
op|','
name|'strict'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'if'
name|'min_count'
op|'>'
name|'max_count'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'min_count must be <= max_count'"
op|')'
newline|'\n'
name|'raise'
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
name|'create_kwargs'
op|'['
string|"'min_count'"
op|']'
op|'='
name|'min_count'
newline|'\n'
name|'create_kwargs'
op|'['
string|"'max_count'"
op|']'
op|'='
name|'max_count'
newline|'\n'
name|'create_kwargs'
op|'['
string|"'return_reservation_id'"
op|']'
op|'='
name|'return_id'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
