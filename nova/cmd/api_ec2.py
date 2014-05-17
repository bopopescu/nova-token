begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""Starter script for Nova EC2 API."""'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'report'
name|'import'
name|'guru_meditation_report'
name|'as'
name|'gmr'
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
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'enabled_ssl_apis'"
op|','
string|"'nova.service'"
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
name|'gmr'
op|'.'
name|'TextGuruMeditation'
op|'.'
name|'setup_autorun'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
name|'should_use_ssl'
op|'='
string|"'ec2'"
name|'in'
name|'CONF'
op|'.'
name|'enabled_ssl_apis'
newline|'\n'
name|'server'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|"'ec2'"
op|','
name|'use_ssl'
op|'='
name|'should_use_ssl'
op|','
nl|'\n'
name|'max_url_len'
op|'='
number|'16384'
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
name|'server'
op|'.'
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
