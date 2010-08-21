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
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'models'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_create
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'instance_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_state
dedent|''
name|'def'
name|'instance_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'.'
name|'set_state'
op|'('
name|'state'
op|','
name|'description'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'instance_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#####################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_create
dedent|''
name|'def'
name|'network_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'models'
op|'.'
name|'Network'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'network_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network_ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_destroy
dedent|''
name|'def'
name|'network_destroy'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'network_ref'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get
dedent|''
name|'def'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_update
dedent|''
name|'def'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'network_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'######################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_allocate_shelf_and_blade
dedent|''
name|'def'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'ExportDevice'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'volume'
op|'='
name|'None'
op|')'
newline|'\n'
name|'export_device'
op|'='
name|'query'
op|'.'
name|'with_lockmode'
op|'('
string|'"update"'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
comment|"# NOTE(vish): if with_lockmode isn't supported, as in sqlite,"
nl|'\n'
comment|'#             then this has concurrency issues'
nl|'\n'
name|'if'
name|'not'
name|'export_device'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'NoMoreBlades'
op|'('
op|')'
newline|'\n'
dedent|''
name|'export_device'
op|'.'
name|'volume_id'
op|'='
name|'volume_id'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'export_device'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
op|'('
name|'export_device'
op|'.'
name|'shelf_id'
op|','
name|'export_device'
op|'.'
name|'blade_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_attached
dedent|''
name|'def'
name|'volume_attached'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'.'
name|'instance_id'
op|'='
name|'instance_id'
newline|'\n'
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|'='
string|"'in-use'"
newline|'\n'
name|'volume_ref'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'mountpoint'
newline|'\n'
name|'volume_ref'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'attached'"
newline|'\n'
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_create
dedent|''
name|'def'
name|'volume_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'models'
op|'.'
name|'Volume'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'volume_ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_destroy
dedent|''
name|'def'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_detached
dedent|''
name|'def'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'volume_ref'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|'='
string|"'available'"
newline|'\n'
name|'volume_ref'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'detached'"
newline|'\n'
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get
dedent|''
name|'def'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Volume'
op|'.'
name|'find'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_shelf_and_blade
dedent|''
name|'def'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'export_device'
op|'='
name|'volume_ref'
op|'.'
name|'export_device'
newline|'\n'
name|'if'
name|'not'
name|'export_device'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'export_device'
op|'.'
name|'shelf_id'
op|','
name|'export_device'
op|'.'
name|'blade_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_update
dedent|''
name|'def'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
