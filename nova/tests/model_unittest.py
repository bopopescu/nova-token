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
name|'datetime'
name|'import'
name|'datetime'
op|','
name|'timedelta'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'compute'
name|'import'
name|'model'
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
nl|'\n'
nl|'\n'
DECL|class|ModelTestCase
name|'class'
name|'ModelTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
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
name|'ModelTestCase'
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
name|'fake_storage'
op|'='
name|'True'
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
name|'model'
op|'.'
name|'Instance'
op|'('
string|"'i-test'"
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'model'
op|'.'
name|'Host'
op|'('
string|"'testhost'"
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost'"
op|','
string|"'nova-testdaemon'"
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_instance
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'model'
op|'.'
name|'Instance'
op|'('
string|"'i-test'"
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-test'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
string|"'m1.tiny'"
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'private_dns_name'"
op|']'
op|'='
string|"'10.0.0.1'"
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
DECL|member|create_host
dedent|''
name|'def'
name|'create_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'model'
op|'.'
name|'Host'
op|'('
string|"'testhost'"
op|')'
newline|'\n'
name|'host'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'host'
newline|'\n'
nl|'\n'
DECL|member|create_daemon
dedent|''
name|'def'
name|'create_daemon'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'daemon'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost'"
op|','
string|"'nova-testdaemon'"
op|')'
newline|'\n'
name|'daemon'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'daemon'
newline|'\n'
nl|'\n'
DECL|member|create_session_token
dedent|''
name|'def'
name|'create_session_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session_token'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'('
string|"'tk12341234'"
op|')'
newline|'\n'
name|'session_token'
op|'['
string|"'user'"
op|']'
op|'='
string|"'testuser'"
newline|'\n'
name|'session_token'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'session_token'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance
dedent|''
name|'def'
name|'test_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""store with create_instace, then test that a load finds it"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'old'
op|'='
name|'model'
op|'.'
name|'Instance'
op|'('
name|'instance'
op|'.'
name|'identifier'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'old'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_instance
dedent|''
name|'def'
name|'test_delete_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then destroy, then make sure loads a new record"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'newinst'
op|'='
name|'model'
op|'.'
name|'Instance'
op|'('
string|"'i-test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'newinst'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_added_to_set
dedent|''
name|'def'
name|'test_instance_added_to_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is listed in global set"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'all'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'i-test'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_associates_project
dedent|''
name|'def'
name|'test_instance_associates_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is listed for the project"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'by_project'
op|'('
name|'instance'
op|'.'
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'i-test'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_associates_ip
dedent|''
name|'def'
name|'test_instance_associates_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is listed for the ip"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'x'
op|'='
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'by_ip'
op|'('
name|'instance'
op|'['
string|"'private_dns_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'x'
op|'.'
name|'identifier'
op|','
string|"'i-test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_associates_node
dedent|''
name|'def'
name|'test_instance_associates_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is listed for the host"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'by_node'
op|'('
name|'FLAGS'
op|'.'
name|'host'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'i-test'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found'
op|')'
newline|'\n'
name|'instance'
op|'['
string|"'host'"
op|']'
op|'='
string|"'test_node'"
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'by_node'
op|'('
string|"'test_node'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'i-test'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_host_class_finds_hosts
dedent|''
name|'def'
name|'test_host_class_finds_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'self'
op|'.'
name|'create_host'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'testhost'"
op|','
name|'model'
op|'.'
name|'Host'
op|'.'
name|'lookup'
op|'('
string|"'testhost'"
op|')'
op|'.'
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_class_doesnt_find_missing_hosts
dedent|''
name|'def'
name|'test_host_class_doesnt_find_missing_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'='
name|'model'
op|'.'
name|'Host'
op|'.'
name|'lookup'
op|'('
string|"'woahnelly'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'None'
op|','
name|'rv'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_host
dedent|''
name|'def'
name|'test_create_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""store with create_host, then test that a load finds it"""'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'create_host'
op|'('
op|')'
newline|'\n'
name|'old'
op|'='
name|'model'
op|'.'
name|'Host'
op|'('
name|'host'
op|'.'
name|'identifier'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'old'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_host
dedent|''
name|'def'
name|'test_delete_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then destroy, then make sure loads a new record"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_host'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'newinst'
op|'='
name|'model'
op|'.'
name|'Host'
op|'('
string|"'testhost'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'newinst'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_added_to_set
dedent|''
name|'def'
name|'test_host_added_to_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is included in list"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_host'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'Host'
op|'.'
name|'all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'testhost'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_daemon_two_args
dedent|''
name|'def'
name|'test_create_daemon_two_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create a daemon with two arguments"""'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'create_daemon'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost'"
op|','
string|"'nova-testdaemon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'d'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_daemon_single_arg
dedent|''
name|'def'
name|'test_create_daemon_single_arg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a daemon using the combined host:bin format"""'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|'"testhost:nova-testdaemon"'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost:nova-testdaemon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'d'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_equality_of_daemon_single_and_double_args
dedent|''
name|'def'
name|'test_equality_of_daemon_single_and_double_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a daemon using the combined host:bin arg, find with 2"""'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|'"testhost:nova-testdaemon"'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost'"
op|','
string|"'nova-testdaemon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'d'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_equality_daemon_of_double_and_single_args
dedent|''
name|'def'
name|'test_equality_daemon_of_double_and_single_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a daemon using the combined host:bin arg, find with 2"""'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'create_daemon'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost:nova-testdaemon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'d'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_daemon
dedent|''
name|'def'
name|'test_delete_daemon'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then destroy, then make sure loads a new record"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_daemon'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'newinst'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost'"
op|','
string|"'nova-testdaemon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'newinst'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_daemon_heartbeat
dedent|''
name|'def'
name|'test_daemon_heartbeat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a daemon, sleep, heartbeat, check for update"""'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'create_daemon'
op|'('
op|')'
newline|'\n'
name|'ts'
op|'='
name|'d'
op|'['
string|"'updated_at'"
op|']'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'2'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'heartbeat'
op|'('
op|')'
newline|'\n'
name|'d2'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
string|"'testhost'"
op|','
string|"'nova-testdaemon'"
op|')'
newline|'\n'
name|'ts2'
op|'='
name|'d2'
op|'['
string|"'updated_at'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'ts2'
op|'>'
name|'ts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_daemon_added_to_set
dedent|''
name|'def'
name|'test_daemon_added_to_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is included in list"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_daemon'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'Daemon'
op|'.'
name|'all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'testhost:nova-testdaemon'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_daemon_associates_host
dedent|''
name|'def'
name|'test_daemon_associates_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is listed for the host"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_daemon'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'Daemon'
op|'.'
name|'by_host'
op|'('
string|"'testhost'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
string|"'testhost:nova-testdaemon'"
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_session_token
dedent|''
name|'def'
name|'test_create_session_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create"""'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'create_session_token'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'('
name|'d'
op|'.'
name|'token'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'d'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_session_token
dedent|''
name|'def'
name|'test_delete_session_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then destroy, then make sure loads a new record"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_session_token'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'newinst'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'('
name|'instance'
op|'.'
name|'token'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'newinst'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_added_to_set
dedent|''
name|'def'
name|'test_session_token_added_to_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is included in list"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_session_token'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
name|'instance'
op|'.'
name|'token'
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_associates_user
dedent|''
name|'def'
name|'test_session_token_associates_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create, then check that it is listed for the user"""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_session_token'
op|'('
op|')'
newline|'\n'
name|'found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'associated_to'
op|'('
string|"'user'"
op|','
string|"'testuser'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
op|'.'
name|'identifier'
op|'=='
name|'instance'
op|'.'
name|'identifier'
op|':'
newline|'\n'
indent|'                '
name|'found'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_generation
dedent|''
name|'def'
name|'test_session_token_generation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|"'username'"
op|','
string|"'TokenType'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'instance'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_generated_session_token
dedent|''
name|'def'
name|'test_find_generated_session_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|"'username'"
op|','
string|"'TokenType'"
op|')'
newline|'\n'
name|'found'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'lookup'
op|'('
name|'instance'
op|'.'
name|'identifier'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'found'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_session_token_expiry
dedent|''
name|'def'
name|'test_update_session_token_expiry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'('
string|"'tk12341234'"
op|')'
newline|'\n'
name|'oldtime'
op|'='
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'['
string|"'expiry'"
op|']'
op|'='
name|'oldtime'
op|'.'
name|'strftime'
op|'('
name|'utils'
op|'.'
name|'TIME_FORMAT'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'update_expiry'
op|'('
op|')'
newline|'\n'
name|'expiry'
op|'='
name|'utils'
op|'.'
name|'parse_isotime'
op|'('
name|'instance'
op|'['
string|"'expiry'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'expiry'
op|'>'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_lookup_when_expired
dedent|''
name|'def'
name|'test_session_token_lookup_when_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|'"testuser"'
op|')'
newline|'\n'
name|'instance'
op|'['
string|"'expiry'"
op|']'
op|'='
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'strftime'
op|'('
name|'utils'
op|'.'
name|'TIME_FORMAT'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'lookup'
op|'('
name|'instance'
op|'.'
name|'identifier'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_lookup_when_not_expired
dedent|''
name|'def'
name|'test_session_token_lookup_when_not_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|'"testuser"'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'lookup'
op|'('
name|'instance'
op|'.'
name|'identifier'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_is_expired_when_expired
dedent|''
name|'def'
name|'test_session_token_is_expired_when_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|'"testuser"'
op|')'
newline|'\n'
name|'instance'
op|'['
string|"'expiry'"
op|']'
op|'='
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'strftime'
op|'('
name|'utils'
op|'.'
name|'TIME_FORMAT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'instance'
op|'.'
name|'is_expired'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_is_expired_when_not_expired
dedent|''
name|'def'
name|'test_session_token_is_expired_when_not_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|'"testuser"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'instance'
op|'.'
name|'is_expired'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_session_token_ttl
dedent|''
name|'def'
name|'test_session_token_ttl'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'SessionToken'
op|'.'
name|'generate'
op|'('
string|'"testuser"'
op|')'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'delta'
op|'='
name|'timedelta'
op|'('
name|'hours'
op|'='
number|'1'
op|')'
newline|'\n'
name|'instance'
op|'['
string|"'expiry'"
op|']'
op|'='
op|'('
name|'now'
op|'+'
name|'delta'
op|')'
op|'.'
name|'strftime'
op|'('
name|'utils'
op|'.'
name|'TIME_FORMAT'
op|')'
newline|'\n'
comment|'# give 5 seconds of fuzziness'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'abs'
op|'('
name|'instance'
op|'.'
name|'ttl'
op|'('
op|')'
op|'-'
name|'FLAGS'
op|'.'
name|'auth_token_ttl'
op|')'
op|'<'
number|'5'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
