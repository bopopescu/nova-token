begin_unit
comment|'# Copyright (c) AT&T 2012-2013 Yun Mao <yunmao@gmail.com>'
nl|'\n'
comment|'# Copyright (c) IBM 2012 Alexey Roytman <roytman at il dot ibm dot com>.'
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
string|'"""Test the ZooKeeper driver for servicegroup.\n\nYou need to install ZooKeeper locally and related dependencies\nto run the test. It\'s unclear how to install python-zookeeper lib\nin venv so you might have to run the test without it.\n\nTo set up in Ubuntu 12.04:\n$ sudo apt-get install zookeeper zookeeperd python-zookeeper\n$ sudo pip install evzookeeper\n$ nosetests nova.tests.servicegroup.test_zk_driver\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZKServiceGroupTestCase
name|'class'
name|'ZKServiceGroupTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'ZKServiceGroupTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'servicegroup'
op|'.'
name|'API'
op|'.'
name|'_driver'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'drivers'
name|'import'
name|'zk'
newline|'\n'
name|'_unused'
op|'='
name|'zk'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Unable to test due to lack of ZooKeeper"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flags'
op|'('
name|'servicegroup_driver'
op|'='
string|"'zk'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'address'
op|'='
string|"'localhost:2181'"
op|','
name|'group'
op|'='
string|'"zookeeper"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_join_leave
dedent|''
name|'def'
name|'test_join_leave'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'service_id'
op|'='
op|'{'
string|"'topic'"
op|':'
string|"'unittest'"
op|','
string|"'host'"
op|':'
string|"'serviceA'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'join'
op|'('
name|'service_id'
op|'['
string|"'host'"
op|']'
op|','
name|'service_id'
op|'['
string|"'topic'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'leave'
op|'('
name|'service_id'
op|'['
string|"'host'"
op|']'
op|','
name|'service_id'
op|'['
string|"'topic'"
op|']'
op|')'
newline|'\n'
comment|'# make sure zookeeper is updated and watcher is triggered'
nl|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop
dedent|''
name|'def'
name|'test_stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'service_id'
op|'='
op|'{'
string|"'topic'"
op|':'
string|"'unittest'"
op|','
string|"'host'"
op|':'
string|"'serviceA'"
op|'}'
newline|'\n'
name|'pulse'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'join'
op|'('
name|'service_id'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'service_id'
op|'['
string|"'topic'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_id'
op|')'
op|')'
newline|'\n'
name|'pulse'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_id'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
