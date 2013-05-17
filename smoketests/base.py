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
name|'boto'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
name|'import'
name|'regioninfo'
newline|'\n'
name|'import'
name|'commands'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'paramiko'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'smoketests'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
DECL|variable|SUITE_NAMES
name|'SUITE_NAMES'
op|'='
string|"'[image, instance, volume]'"
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'suite'"
op|','
name|'None'
op|','
string|"'Specific test suite to run '"
op|'+'
name|'SUITE_NAMES'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'ssh_tries'"
op|','
number|'3'
op|','
string|"'Numer of times to try ssh'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SmokeTestCase
name|'class'
name|'SmokeTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|connect_ssh
indent|'    '
name|'def'
name|'connect_ssh'
op|'('
name|'self'
op|','
name|'ip'
op|','
name|'key_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'paramiko'
op|'.'
name|'RSAKey'
op|'.'
name|'from_private_key_file'
op|'('
string|"'/tmp/%s.pem'"
op|'%'
name|'key_name'
op|')'
newline|'\n'
name|'tries'
op|'='
number|'0'
newline|'\n'
name|'while'
op|'('
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'client'
op|'='
name|'paramiko'
op|'.'
name|'SSHClient'
op|'('
op|')'
newline|'\n'
name|'client'
op|'.'
name|'set_missing_host_key_policy'
op|'('
name|'paramiko'
op|'.'
name|'AutoAddPolicy'
op|'('
op|')'
op|')'
newline|'\n'
name|'client'
op|'.'
name|'connect'
op|'('
name|'ip'
op|','
name|'username'
op|'='
string|"'root'"
op|','
name|'pkey'
op|'='
name|'key'
op|','
name|'timeout'
op|'='
number|'5'
op|')'
newline|'\n'
name|'return'
name|'client'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'paramiko'
op|'.'
name|'AuthenticationException'
op|','
name|'paramiko'
op|'.'
name|'SSHException'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'tries'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'tries'
op|'=='
name|'FLAGS'
op|'.'
name|'ssh_tries'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|can_ping
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'can_ping'
op|'('
name|'self'
op|','
name|'ip'
op|','
name|'command'
op|'='
string|'"ping"'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attempt to ping the specified IP, and give up after 1 second."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(devcamcar): ping timeout flag is different in OSX.'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'darwin'"
op|':'
newline|'\n'
indent|'            '
name|'timeout_flag'
op|'='
string|"'t'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'timeout_flag'
op|'='
string|"'w'"
newline|'\n'
nl|'\n'
dedent|''
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
string|"'%s -c1 -%s1 %s'"
op|'%'
nl|'\n'
op|'('
name|'command'
op|','
name|'timeout_flag'
op|','
name|'ip'
op|')'
op|')'
newline|'\n'
name|'return'
name|'status'
op|'=='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|wait_for_running
dedent|''
name|'def'
name|'wait_for_running'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'tries'
op|'='
number|'60'
op|','
name|'wait'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for instance to be running."""'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'tries'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'state'
op|'.'
name|'startswith'
op|'('
string|"'running'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'wait'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|wait_for_deleted
dedent|''
dedent|''
name|'def'
name|'wait_for_deleted'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'tries'
op|'='
number|'60'
op|','
name|'wait'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for instance to be deleted."""'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'tries'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'#NOTE(dprince): raises exception when instance id disappears'
nl|'\n'
indent|'                '
name|'instance'
op|'.'
name|'update'
op|'('
name|'validate'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'wait'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|wait_for_ping
dedent|''
dedent|''
name|'def'
name|'wait_for_ping'
op|'('
name|'self'
op|','
name|'ip'
op|','
name|'command'
op|'='
string|'"ping"'
op|','
name|'tries'
op|'='
number|'120'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for ip to be pingable."""'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'tries'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'can_ping'
op|'('
name|'ip'
op|','
name|'command'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|wait_for_ssh
dedent|''
dedent|''
name|'def'
name|'wait_for_ssh'
op|'('
name|'self'
op|','
name|'ip'
op|','
name|'key_name'
op|','
name|'tries'
op|'='
number|'30'
op|','
name|'wait'
op|'='
number|'5'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for ip to be sshable."""'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'tries'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
name|'ip'
op|','
name|'key_name'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
name|'wait'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|connection_for_env
dedent|''
dedent|''
name|'def'
name|'connection_for_env'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns a boto ec2 connection for the current environment.\n        """'
newline|'\n'
name|'access_key'
op|'='
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'EC2_ACCESS_KEY'"
op|')'
newline|'\n'
name|'secret_key'
op|'='
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'EC2_SECRET_KEY'"
op|')'
newline|'\n'
name|'clc_url'
op|'='
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'EC2_URL'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'access_key'
name|'or'
name|'not'
name|'secret_key'
name|'or'
name|'not'
name|'clc_url'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'Missing EC2 environment variables. Please source '"
nl|'\n'
string|"'the appropriate novarc file before running this '"
nl|'\n'
string|"'test.'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'parts'
op|'='
name|'self'
op|'.'
name|'split_clc_url'
op|'('
name|'clc_url'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'boto_v6'
op|'.'
name|'connect_ec2'
op|'('
name|'aws_access_key_id'
op|'='
name|'access_key'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'secret_key'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'parts'
op|'['
string|"'is_secure'"
op|']'
op|','
nl|'\n'
name|'region'
op|'='
name|'regioninfo'
op|'.'
name|'RegionInfo'
op|'('
name|'None'
op|','
nl|'\n'
string|"'nova'"
op|','
nl|'\n'
name|'parts'
op|'['
string|"'ip'"
op|']'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
name|'parts'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
name|'path'
op|'='
string|"'/services/Cloud'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'boto'
op|'.'
name|'connect_ec2'
op|'('
name|'aws_access_key_id'
op|'='
name|'access_key'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'secret_key'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'parts'
op|'['
string|"'is_secure'"
op|']'
op|','
nl|'\n'
name|'region'
op|'='
name|'regioninfo'
op|'.'
name|'RegionInfo'
op|'('
name|'None'
op|','
nl|'\n'
string|"'nova'"
op|','
nl|'\n'
name|'parts'
op|'['
string|"'ip'"
op|']'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
name|'parts'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
name|'path'
op|'='
string|"'/services/Cloud'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|split_clc_url
dedent|''
name|'def'
name|'split_clc_url'
op|'('
name|'self'
op|','
name|'clc_url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Splits a cloud controller endpoint url."""'
newline|'\n'
name|'parts'
op|'='
name|'httplib'
op|'.'
name|'urlsplit'
op|'('
name|'clc_url'
op|')'
newline|'\n'
name|'is_secure'
op|'='
name|'parts'
op|'.'
name|'scheme'
op|'=='
string|"'https'"
newline|'\n'
name|'ip'
op|','
name|'port'
op|'='
name|'parts'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'ip'"
op|':'
name|'ip'
op|','
string|"'port'"
op|':'
name|'int'
op|'('
name|'port'
op|')'
op|','
string|"'is_secure'"
op|':'
name|'is_secure'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create_key_pair
dedent|''
name|'def'
name|'create_key_pair'
op|'('
name|'self'
op|','
name|'conn'
op|','
name|'key_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
string|"'/tmp/%s.pem'"
op|'%'
name|'key_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'key'
op|'='
name|'conn'
op|'.'
name|'create_key_pair'
op|'('
name|'key_name'
op|')'
newline|'\n'
name|'key'
op|'.'
name|'save'
op|'('
string|"'/tmp/'"
op|')'
newline|'\n'
name|'return'
name|'key'
newline|'\n'
nl|'\n'
DECL|member|delete_key_pair
dedent|''
name|'def'
name|'delete_key_pair'
op|'('
name|'self'
op|','
name|'conn'
op|','
name|'key_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'delete_key_pair'
op|'('
name|'key_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
string|"'/tmp/%s.pem'"
op|'%'
name|'key_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|bundle_image
dedent|''
dedent|''
name|'def'
name|'bundle_image'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'tempdir'
op|'='
string|"'/tmp'"
op|','
name|'kernel'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
string|"'euca-bundle-image -i %s -d %s'"
op|'%'
op|'('
name|'image'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'if'
name|'kernel'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'+='
string|"' --kernel true'"
newline|'\n'
dedent|''
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'output'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|upload_image
dedent|''
name|'def'
name|'upload_image'
op|'('
name|'self'
op|','
name|'bucket_name'
op|','
name|'image'
op|','
name|'tempdir'
op|'='
string|"'/tmp'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
string|"'euca-upload-bundle -b '"
newline|'\n'
name|'cmd'
op|'+='
string|"'%s -m %s/%s.manifest.xml'"
op|'%'
op|'('
name|'bucket_name'
op|','
name|'tempdir'
op|','
name|'image'
op|')'
newline|'\n'
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'output'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|delete_bundle_bucket
dedent|''
name|'def'
name|'delete_bundle_bucket'
op|'('
name|'self'
op|','
name|'bucket_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
string|"'euca-delete-bundle --clear -b %s'"
op|'%'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'output'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_DATA
dedent|''
dedent|''
name|'TEST_DATA'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'boto_v6'
newline|'\n'
DECL|variable|boto_v6
name|'boto_v6'
op|'='
name|'__import__'
op|'('
string|"'boto_v6'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserSmokeTestCase
dedent|''
name|'class'
name|'UserSmokeTestCase'
op|'('
name|'SmokeTestCase'
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
name|'global'
name|'TEST_DATA'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'self'
op|'.'
name|'connection_for_env'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
name|'TEST_DATA'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
