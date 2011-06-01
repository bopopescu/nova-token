begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Rackspace'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'db'
name|'import'
name|'fakes'
name|'as'
name|'db_fakes'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkTestCase
name|'class'
name|'NetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'fake_call'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_network'
op|'='
name|'True'
op|','
nl|'\n'
name|'network_manager'
op|'='
name|'self'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'netuser'"
op|','
nl|'\n'
string|"'netuser'"
op|','
nl|'\n'
string|"'netuser'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'projects'
op|'='
op|'['
op|']'
newline|'\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_network_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'project'
op|'='
name|'None'
op|','
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFuncs
dedent|''
dedent|''
name|'class'
name|'TestFuncs'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_set_network_host
indent|'    '
name|'def'
name|'test_set_network_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
string|'"fake_test_host"'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'host'
op|')'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_for_instance
dedent|''
name|'def'
name|'test_allocate_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
number|'0'
newline|'\n'
name|'project_id'
op|'='
number|'0'
newline|'\n'
name|'type_id'
op|'='
number|'0'
newline|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_from_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'type_id'
op|'='
name|'type_id'
op|')'
newline|'\n'
name|'print'
name|'ip'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
