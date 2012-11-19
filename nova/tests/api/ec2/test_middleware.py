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
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'ec2'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|conditional_forbid
name|'def'
name|'conditional_forbid'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper wsgi app returns 403 if param \'die\' is 1."""'
newline|'\n'
name|'if'
string|"'die'"
name|'in'
name|'req'
op|'.'
name|'params'
name|'and'
name|'req'
op|'.'
name|'params'
op|'['
string|"'die'"
op|']'
op|'=='
string|"'1'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'OK'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LockoutTestCase
dedent|''
name|'class'
name|'LockoutTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for the Lockout middleware."""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable=C0103'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LockoutTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lockout'
op|'='
name|'ec2'
op|'.'
name|'Lockout'
op|'('
name|'conditional_forbid'
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
comment|'# pylint: disable=C0103'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'clear_time_override'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'LockoutTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_send_bad_attempts
dedent|''
name|'def'
name|'_send_bad_attempts'
op|'('
name|'self'
op|','
name|'access_key'
op|','
name|'num_attempts'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fail x."""'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'num_attempts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?AWSAccessKeyId=%s&die=1'"
op|'%'
name|'access_key'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'lockout'
op|')'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_is_locked_out
dedent|''
dedent|''
name|'def'
name|'_is_locked_out'
op|'('
name|'self'
op|','
name|'access_key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sends a test request to see if key is locked out."""'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?AWSAccessKeyId=%s'"
op|'%'
name|'access_key'
op|')'
newline|'\n'
name|'return'
op|'('
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'lockout'
op|')'
op|'.'
name|'status_int'
op|'=='
number|'403'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lockout
dedent|''
name|'def'
name|'test_lockout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_send_bad_attempts'
op|'('
string|"'test'"
op|','
name|'CONF'
op|'.'
name|'lockout_attempts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_timeout
dedent|''
name|'def'
name|'test_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_send_bad_attempts'
op|'('
string|"'test'"
op|','
name|'CONF'
op|'.'
name|'lockout_attempts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test'"
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'lockout_minutes'
op|'*'
number|'60'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_keys
dedent|''
name|'def'
name|'test_multiple_keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_send_bad_attempts'
op|'('
string|"'test1'"
op|','
name|'CONF'
op|'.'
name|'lockout_attempts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test2'"
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'lockout_minutes'
op|'*'
number|'60'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test2'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_window_timeout
dedent|''
name|'def'
name|'test_window_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_send_bad_attempts'
op|'('
string|"'test'"
op|','
name|'CONF'
op|'.'
name|'lockout_attempts'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test'"
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'lockout_window'
op|'*'
number|'60'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_send_bad_attempts'
op|'('
string|"'test'"
op|','
name|'CONF'
op|'.'
name|'lockout_attempts'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_is_locked_out'
op|'('
string|"'test'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExecutorTestCase
dedent|''
dedent|''
name|'class'
name|'ExecutorTestCase'
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
name|'ExecutorTestCase'
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
name|'executor'
op|'='
name|'ec2'
op|'.'
name|'Executor'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_execute
dedent|''
name|'def'
name|'_execute'
op|'('
name|'self'
op|','
name|'invoke'
op|')'
op|':'
newline|'\n'
DECL|class|Fake
indent|'        '
name|'class'
name|'Fake'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'fake_ec2_request'
op|'='
name|'Fake'
op|'('
op|')'
newline|'\n'
name|'fake_ec2_request'
op|'.'
name|'invoke'
op|'='
name|'invoke'
newline|'\n'
nl|'\n'
name|'fake_wsgi_request'
op|'='
name|'Fake'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'fake_wsgi_request'
op|'.'
name|'environ'
op|'='
op|'{'
nl|'\n'
string|"'nova.context'"
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'ec2.request'"
op|':'
name|'fake_ec2_request'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'executor'
op|'('
name|'fake_wsgi_request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extract_message
dedent|''
name|'def'
name|'_extract_message'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'result'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'return'
name|'tree'
op|'.'
name|'findall'
op|'('
string|"'./Errors'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'find'
op|'('
string|"'Error/Message'"
op|')'
op|'.'
name|'text'
newline|'\n'
nl|'\n'
DECL|member|test_instance_not_found
dedent|''
name|'def'
name|'test_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|not_found
indent|'        '
name|'def'
name|'not_found'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
number|'5'
op|')'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_execute'
op|'('
name|'not_found'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'i-00000005'"
op|','
name|'self'
op|'.'
name|'_extract_message'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_not_found
dedent|''
name|'def'
name|'test_snapshot_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|not_found
indent|'        '
name|'def'
name|'not_found'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SnapshotNotFound'
op|'('
name|'snapshot_id'
op|'='
number|'5'
op|')'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_execute'
op|'('
name|'not_found'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'snap-00000005'"
op|','
name|'self'
op|'.'
name|'_extract_message'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_not_found
dedent|''
name|'def'
name|'test_volume_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|not_found
indent|'        '
name|'def'
name|'not_found'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
number|'5'
op|')'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_execute'
op|'('
name|'not_found'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'vol-00000005'"
op|','
name|'self'
op|'.'
name|'_extract_message'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
