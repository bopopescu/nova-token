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
name|'import'
name|'commands'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
comment|'# If ../nova/__init__.py exists, add ../ to Python search path, so that'
nl|'\n'
comment|'# it will override what happens to be installed in /usr/(local/)lib/python...'
nl|'\n'
DECL|variable|possible_topdir
name|'possible_topdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|')'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'possible_topdir'
op|','
string|"'nova'"
op|','
string|"'__init__.py'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'possible_topdir'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'smoketests'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'smoketests'
name|'import'
name|'base'
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
DECL|variable|TEST_PREFIX
name|'TEST_PREFIX'
op|'='
string|"'test%s'"
op|'%'
name|'int'
op|'('
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'*'
number|'1000000'
op|')'
newline|'\n'
DECL|variable|TEST_BUCKET
name|'TEST_BUCKET'
op|'='
string|"'%s_bucket'"
op|'%'
name|'TEST_PREFIX'
newline|'\n'
DECL|variable|TEST_KEY
name|'TEST_KEY'
op|'='
string|"'%s_key'"
op|'%'
name|'TEST_PREFIX'
newline|'\n'
DECL|variable|TEST_GROUP
name|'TEST_GROUP'
op|'='
string|"'%s_group'"
op|'%'
name|'TEST_PREFIX'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AddressTests
name|'class'
name|'AddressTests'
op|'('
name|'base'
op|'.'
name|'UserSmokeTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_000_setUp
indent|'    '
name|'def'
name|'test_000_setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'create_key_pair'
op|'('
name|'self'
op|'.'
name|'conn'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'reservation'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'run_instances'
op|'('
name|'FLAGS'
op|'.'
name|'test_image'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|','
nl|'\n'
name|'key_name'
op|'='
name|'TEST_KEY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_running'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'instance failed to start'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ping'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_dns_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ping instance'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ssh'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_dns_name'
op|','
nl|'\n'
name|'TEST_KEY'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ssh to instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_001_can_allocate_floating_ip
dedent|''
dedent|''
name|'def'
name|'test_001_can_allocate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'allocate_address'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'result'
op|','
string|"'public_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|'='
name|'result'
op|'.'
name|'public_ip'
newline|'\n'
nl|'\n'
DECL|member|test_002_can_associate_ip_with_instance
dedent|''
name|'def'
name|'test_002_can_associate_ip_with_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'associate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_can_ssh_with_public_ip
dedent|''
name|'def'
name|'test_003_can_ssh_with_public_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ssh_authorized'
op|'='
name|'False'
newline|'\n'
name|'groups'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_security_groups'
op|'('
op|'['
string|"'default'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'groups'
op|'['
number|'0'
op|']'
op|'.'
name|'rules'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'rule'
op|'.'
name|'ip_protocol'
op|'=='
string|"'tcp'"
name|'and'
nl|'\n'
name|'int'
op|'('
name|'rule'
op|'.'
name|'from_port'
op|')'
op|'<='
number|'22'
name|'and'
nl|'\n'
name|'int'
op|'('
name|'rule'
op|'.'
name|'to_port'
op|')'
op|'>='
number|'22'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ssh_authorized'
op|'='
name|'True'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'ssh_authorized'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'authorize_security_group'
op|'('
string|"'default'"
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'22'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'22'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ssh'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|','
name|'TEST_KEY'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ssh to public ip'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ssh_authorized'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'revoke_security_group'
op|'('
string|"'default'"
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'22'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'22'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_disassociate_ip_from_instance
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_004_can_disassociate_ip_from_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'disassociate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_can_deallocate_floating_ip
dedent|''
name|'def'
name|'test_005_can_deallocate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'release_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_999_tearDown
dedent|''
name|'def'
name|'test_999_tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'delete_key_pair'
op|'('
name|'self'
op|'.'
name|'conn'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'terminate_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupTests
dedent|''
dedent|''
name|'class'
name|'SecurityGroupTests'
op|'('
name|'base'
op|'.'
name|'UserSmokeTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__public_instance_is_accessible
indent|'    '
name|'def'
name|'__public_instance_is_accessible'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'id_url'
op|'='
string|'"latest/meta-data/instance-id"'
newline|'\n'
name|'options'
op|'='
string|'"-s --max-time 1"'
newline|'\n'
name|'command'
op|'='
string|'"curl %s %s/%s"'
op|'%'
op|'('
name|'options'
op|','
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|','
name|'id_url'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'commands'
op|'.'
name|'getoutput'
op|'('
name|'command'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'instance_id'
op|'!='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Wrong instance id. Expected: %s, Got: %s"'
op|'%'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|','
name|'instance_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|test_001_can_create_security_group
dedent|''
name|'def'
name|'test_001_can_create_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_security_group'
op|'('
name|'TEST_GROUP'
op|','
name|'description'
op|'='
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
name|'groups'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'TEST_GROUP'
name|'in'
op|'['
name|'group'
op|'.'
name|'name'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_can_launch_instance_in_security_group
dedent|''
name|'def'
name|'test_002_can_launch_instance_in_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
string|'"proxy.sh"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'user_data'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'create_key_pair'
op|'('
name|'self'
op|'.'
name|'conn'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'reservation'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'run_instances'
op|'('
name|'FLAGS'
op|'.'
name|'test_image'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'TEST_KEY'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
name|'TEST_GROUP'
op|']'
op|','
nl|'\n'
name|'user_data'
op|'='
name|'user_data'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_running'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'instance failed to start'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_can_authorize_security_group_ingress
dedent|''
name|'def'
name|'test_003_can_authorize_security_group_ingress'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'authorize_security_group'
op|'('
name|'TEST_GROUP'
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'80'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'80'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_access_metadata_over_public_ip
dedent|''
name|'def'
name|'test_004_can_access_metadata_over_public_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'allocate_address'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'result'
op|','
string|"'public_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|'='
name|'result'
op|'.'
name|'public_ip'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'associate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'start_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'not'
name|'self'
op|'.'
name|'__public_instance_is_accessible'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# 1 minute to launch'
nl|'\n'
indent|'                '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'start_time'
op|'>'
number|'60'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
string|'"Timeout"'
op|')'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'disassociate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_can_revoke_security_group_ingress
dedent|''
dedent|''
name|'def'
name|'test_005_can_revoke_security_group_ingress'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'revoke_security_group'
op|'('
name|'TEST_GROUP'
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'80'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'80'
op|')'
op|')'
newline|'\n'
name|'start_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'__public_instance_is_accessible'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# 1 minute to teardown'
nl|'\n'
indent|'            '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'start_time'
op|'>'
number|'60'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
string|'"Timeout"'
op|')'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_999_tearDown
dedent|''
dedent|''
name|'def'
name|'test_999_tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_key_pair'
op|'('
name|'TEST_KEY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_security_group'
op|'('
name|'TEST_GROUP'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'TEST_GROUP'
name|'in'
op|'['
name|'group'
op|'.'
name|'name'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'terminate_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'release_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
