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
name|'sqlalchemy'
name|'import'
name|'Boolean'
op|','
name|'Column'
op|','
name|'DateTime'
op|','
name|'Integer'
op|','
name|'MetaData'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Table'
op|','
name|'Text'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Add disk_available_least column to compute_nodes table.'
nl|'\n'
comment|'# Thinking about qcow2 image support, both compressed and virtual disk size'
nl|'\n'
comment|'# has to be considered.'
nl|'\n'
comment|'# disk_available stores "total disk size - used disk(compressed disk size)",'
nl|'\n'
comment|'# while disk_available_least stores'
nl|'\n'
comment|'# "total disk size - used disk(virtual disk size)".'
nl|'\n'
comment|'# virtual disk size is used for kvm block migration.'
nl|'\n'
nl|'\n'
DECL|variable|compute_nodes
name|'compute_nodes'
op|'='
name|'Table'
op|'('
string|"'compute_nodes'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|disk_available_least
name|'disk_available_least'
op|'='
name|'Column'
op|'('
string|"'disk_available_least'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'default'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'compute_nodes'
op|'.'
name|'create_column'
op|'('
name|'disk_available_least'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"progress column not added to compute_nodes table"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'compute_nodes'
op|'.'
name|'drop_column'
op|'('
name|'disk_available_least'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
