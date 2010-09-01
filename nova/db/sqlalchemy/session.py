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
string|'"""\nSession Handling for SQLAlchemy backend\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'create_engine'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'orm'
name|'import'
name|'create_session'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|managed_session
name|'def'
name|'managed_session'
op|'('
name|'autocommit'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper method to grab session manager"""'
newline|'\n'
name|'return'
name|'SessionExecutionManager'
op|'('
name|'autocommit'
op|'='
name|'autocommit'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SessionExecutionManager
dedent|''
name|'class'
name|'SessionExecutionManager'
op|':'
newline|'\n'
indent|'    '
string|'"""Session manager supporting with .. as syntax"""'
newline|'\n'
DECL|variable|_engine
name|'_engine'
op|'='
name|'None'
newline|'\n'
DECL|variable|_session
name|'_session'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'autocommit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_engine'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_engine'
op|'='
name|'create_engine'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
name|'echo'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_session'
op|'='
name|'create_session'
op|'('
name|'bind'
op|'='
name|'self'
op|'.'
name|'_engine'
op|','
nl|'\n'
name|'autocommit'
op|'='
name|'autocommit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_session'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'traceback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'exc_type'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"Rolling back due to failed transaction"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'rollback'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_session'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
