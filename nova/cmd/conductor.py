begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
string|'"""Starter script for Nova Conductor."""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'topic'"
op|','
string|"'nova.conductor.api'"
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
name|'CONF'
op|','
string|'"nova"'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
name|'objects'
op|'.'
name|'register_all'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
string|"'nova-conductor'"
op|','
nl|'\n'
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'topic'
op|','
nl|'\n'
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'manager'
op|')'
newline|'\n'
name|'workers'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'workers'
name|'or'
name|'processutils'
op|'.'
name|'get_worker_count'
op|'('
op|')'
newline|'\n'
name|'service'
op|'.'
name|'serve'
op|'('
name|'server'
op|','
name|'workers'
op|'='
name|'workers'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
