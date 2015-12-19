begin_unit
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
string|'"""WSGI script for Nova EC2 API\n\nEXPERIMENTAL support script for running Nova EC2 API under Apache2 etc.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
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
name|'from'
name|'paste'
name|'import'
name|'deploy'
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
comment|'# noqa'
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
nl|'\n'
DECL|variable|config_files
name|'config_files'
op|'='
op|'['
string|"'/etc/nova/api-paste.ini'"
op|','
string|"'/etc/nova/nova.conf'"
op|']'
newline|'\n'
name|'config'
op|'.'
name|'parse_args'
op|'('
op|'['
op|']'
op|','
name|'default_config_files'
op|'='
name|'config_files'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
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
DECL|variable|conf
name|'conf'
op|'='
name|'config_files'
op|'['
number|'0'
op|']'
newline|'\n'
name|'eventlet'
op|'.'
name|'monkey_patch'
op|'('
name|'os'
op|'='
name|'False'
op|','
name|'thread'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ec2"'
newline|'\n'
nl|'\n'
DECL|variable|options
name|'options'
op|'='
name|'deploy'
op|'.'
name|'appconfig'
op|'('
string|"'config:%s'"
op|'%'
name|'conf'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|application
name|'application'
op|'='
name|'deploy'
op|'.'
name|'loadapp'
op|'('
string|"'config:%s'"
op|'%'
name|'conf'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
endmarker|''
end_unit