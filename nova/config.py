begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'db'
name|'import'
name|'options'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'debugger'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|_DEFAULT_SQL_CONNECTION
name|'_DEFAULT_SQL_CONNECTION'
op|'='
string|"'sqlite:///'"
op|'+'
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'nova.sqlite'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_args
name|'def'
name|'parse_args'
op|'('
name|'argv'
op|','
name|'default_config_files'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'options'
op|'.'
name|'set_defaults'
op|'('
name|'CONF'
op|','
name|'connection'
op|'='
name|'_DEFAULT_SQL_CONNECTION'
op|','
nl|'\n'
name|'sqlite_db'
op|'='
string|"'nova.sqlite'"
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'set_defaults'
op|'('
name|'control_exchange'
op|'='
string|"'nova'"
op|')'
newline|'\n'
name|'debugger'
op|'.'
name|'register_cli_opts'
op|'('
op|')'
newline|'\n'
name|'CONF'
op|'('
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|','
nl|'\n'
name|'project'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'version'
op|'='
name|'version'
op|'.'
name|'version_string'
op|'('
op|')'
op|','
nl|'\n'
name|'default_config_files'
op|'='
name|'default_config_files'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'init'
op|'('
name|'CONF'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
