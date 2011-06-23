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
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
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
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'admin'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
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
string|"'nova.tests.adminapi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminApiTestCase
name|'class'
name|'AdminApiTestCase'
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
name|'AdminApiTestCase'
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
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# set up our cloud'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'admin'
op|'.'
name|'AdminController'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# set up services'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduter'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'scheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'volume'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\n'
nl|'\n'
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
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'proj'"
op|','
string|"'admin'"
op|','
string|"'proj'"
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
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_show
name|'def'
name|'fake_show'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
number|'1'
op|','
string|"'ramdisk_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'machine'"
op|','
string|"'image_state'"
op|':'
string|"'available'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
string|"'show'"
op|','
name|'fake_show'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
string|"'show_by_name'"
op|','
name|'fake_show'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): set up a manual wait so rpc.cast has a chance to finish'
nl|'\n'
name|'rpc_cast'
op|'='
name|'rpc'
op|'.'
name|'cast'
newline|'\n'
nl|'\n'
DECL|function|finish_cast
name|'def'
name|'finish_cast'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rpc_cast'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.2'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'finish_cast'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'super'
op|'('
name|'AdminApiTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_block_external_ips
dedent|''
name|'def'
name|'test_block_external_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure provider firewall rules are created."""'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'block_external_addresses'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.1.1.1/32'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'OK'"
op|','
name|'result'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'Added 3 rules'"
op|','
name|'result'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
