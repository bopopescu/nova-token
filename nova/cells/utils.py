begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nCells Utility Methods\n"""'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instances_to_sync
name|'def'
name|'get_instances_to_sync'
op|'('
name|'context'
op|','
name|'updated_since'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'deleted'
op|'='
name|'True'
op|','
name|'shuffle'
op|'='
name|'False'
op|','
name|'uuids_only'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a generator that will return a list of active and\n    deleted instances to sync with parent cells.  The list may\n    optionally be shuffled for periodic updates so that multiple\n    cells services aren\'t self-healing the same instances in nearly\n    lockstep.\n    """'
newline|'\n'
name|'filters'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'updated_since'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'['
string|"'changes-since'"
op|']'
op|'='
name|'updated_since'
newline|'\n'
dedent|''
name|'if'
name|'project_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'deleted'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'['
string|"'deleted'"
op|']'
op|'='
name|'False'
newline|'\n'
comment|'# Active instances first.'
nl|'\n'
dedent|''
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
nl|'\n'
name|'context'
op|','
name|'filters'
op|','
string|"'deleted'"
op|','
string|"'asc'"
op|')'
newline|'\n'
name|'if'
name|'shuffle'
op|':'
newline|'\n'
indent|'        '
name|'random'
op|'.'
name|'shuffle'
op|'('
name|'instances'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'uuids_only'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'instance'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
