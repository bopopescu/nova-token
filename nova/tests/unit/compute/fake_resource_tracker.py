begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'resource_tracker'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeResourceTracker
name|'class'
name|'FakeResourceTracker'
op|'('
name|'resource_tracker'
op|'.'
name|'ResourceTracker'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Version without a DB requirement."""'
newline|'\n'
nl|'\n'
DECL|member|_create
name|'def'
name|'_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_write_ext_resources'
op|'('
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_node'
op|'='
name|'values'
newline|'\n'
name|'self'
op|'.'
name|'compute_node'
op|'['
string|"'id'"
op|']'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_update
dedent|''
name|'def'
name|'_update'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_write_ext_resources'
op|'('
name|'self'
op|'.'
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_service
dedent|''
name|'def'
name|'_get_service'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
