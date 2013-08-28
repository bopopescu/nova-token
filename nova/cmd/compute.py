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
string|'"""Starter script for Nova Compute."""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'rpcapi'
name|'as'
name|'conductor_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
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
string|"'compute_topic'"
op|','
string|"'nova.compute.rpcapi'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_local'"
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
DECL|function|block_db_access
name|'def'
name|'block_db_access'
op|'('
op|')'
op|':'
newline|'\n'
DECL|class|NoDB
indent|'    '
name|'class'
name|'NoDB'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__getattr__
indent|'        '
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.compute'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|"'No db access allowed in nova-compute: '"
op|','
name|'exc_info'
op|'='
name|'True'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'DBNotAllowed'
op|'('
string|"'nova-compute'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|'.'
name|'IMPL'
op|'='
name|'NoDB'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'objects'
op|'.'
name|'register_all'
op|'('
op|')'
newline|'\n'
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
string|"'nova'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'use_local'
op|':'
newline|'\n'
indent|'        '
name|'block_db_access'
op|'('
op|')'
newline|'\n'
name|'objects_base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|'='
name|'conductor_rpcapi'
op|'.'
name|'ConductorAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
string|"'nova-compute'"
op|','
nl|'\n'
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
name|'db_allowed'
op|'='
name|'False'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'serve'
op|'('
name|'server'
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
