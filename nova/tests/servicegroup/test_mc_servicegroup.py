begin_unit
comment|'# Copyright (c) 2013 Akira Yoshiyama <akirayoshiyama at gmail dot com>'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This is derived from test_db_servicegroup.py.'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
name|'fixtures'
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
name|'service'
newline|'\n'
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
DECL|class|ServiceFixture
name|'class'
name|'ServiceFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'binary'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ServiceFixture'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'binary'
op|'='
name|'binary'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'serv'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ServiceFixture'
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
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.test_service.FakeManager'"
op|','
nl|'\n'
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'serv'
op|'.'
name|'kill'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MemcachedServiceGroupTestCase
dedent|''
dedent|''
name|'class'
name|'MemcachedServiceGroupTestCase'
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
name|'MemcachedServiceGroupTestCase'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'servicegroup_driver'
op|'='
string|"'mc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'down_time'
op|'='
number|'3'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_new_services'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'service_down_time'
op|'='
name|'self'
op|'.'
name|'down_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
name|'test'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_host'
op|'='
string|"'foo'"
newline|'\n'
name|'self'
op|'.'
name|'_binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'self'
op|'.'
name|'_topic'
op|'='
string|"'unittest'"
newline|'\n'
name|'self'
op|'.'
name|'_ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_memcached_driver
dedent|''
name|'def'
name|'test_memcached_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'ServiceFixture'
op|'('
name|'self'
op|'.'
name|'_host'
op|','
name|'self'
op|'.'
name|'_binary'
op|','
name|'self'
op|'.'
name|'_topic'
op|')'
op|')'
op|'.'
name|'serv'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
name|'hostkey'
op|'='
name|'str'
op|'('
string|'"%s:%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_topic'
op|','
name|'self'
op|'.'
name|'_host'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'hostkey'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'self'
op|'.'
name|'down_time'
op|')'
newline|'\n'
nl|'\n'
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
name|'service_ref'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'test'
op|'.'
name|'TimeOverride'
op|'('
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'self'
op|'.'
name|'down_time'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'_report_state'
op|'('
name|'serv'
op|')'
newline|'\n'
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
nl|'\n'
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
name|'service_ref'
op|')'
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'self'
op|'.'
name|'down_time'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_binary'
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
name|'service_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all
dedent|''
name|'def'
name|'test_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host1'
op|'='
name|'self'
op|'.'
name|'_host'
op|'+'
string|"'_1'"
newline|'\n'
name|'host2'
op|'='
name|'self'
op|'.'
name|'_host'
op|'+'
string|"'_2'"
newline|'\n'
name|'host3'
op|'='
name|'self'
op|'.'
name|'_host'
op|'+'
string|"'_3'"
newline|'\n'
nl|'\n'
name|'serv1'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'ServiceFixture'
op|'('
name|'host1'
op|','
name|'self'
op|'.'
name|'_binary'
op|','
name|'self'
op|'.'
name|'_topic'
op|')'
op|')'
op|'.'
name|'serv'
newline|'\n'
name|'serv1'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'serv2'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'ServiceFixture'
op|'('
name|'host2'
op|','
name|'self'
op|'.'
name|'_binary'
op|','
name|'self'
op|'.'
name|'_topic'
op|')'
op|')'
op|'.'
name|'serv'
newline|'\n'
name|'serv2'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'serv3'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'ServiceFixture'
op|'('
name|'host3'
op|','
name|'self'
op|'.'
name|'_binary'
op|','
name|'self'
op|'.'
name|'_topic'
op|')'
op|')'
op|'.'
name|'serv'
newline|'\n'
name|'serv3'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
name|'host1'
op|','
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
name|'host2'
op|','
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
name|'host3'
op|','
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
nl|'\n'
name|'host1key'
op|'='
name|'str'
op|'('
string|'"%s:%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_topic'
op|','
name|'host1'
op|')'
op|')'
newline|'\n'
name|'host2key'
op|'='
name|'str'
op|'('
string|'"%s:%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_topic'
op|','
name|'host2'
op|')'
op|')'
newline|'\n'
name|'host3key'
op|'='
name|'str'
op|'('
string|'"%s:%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_topic'
op|','
name|'host3'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'host1key'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'self'
op|'.'
name|'down_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'host2key'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'self'
op|'.'
name|'down_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'host3key'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'_topic'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'host1'
op|','
name|'services'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'host2'
op|','
name|'services'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'host3'
op|','
name|'services'
op|')'
newline|'\n'
nl|'\n'
name|'service_id'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'get_one'
op|'('
name|'self'
op|'.'
name|'_topic'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'service_id'
op|','
name|'services'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_is_up
dedent|''
name|'def'
name|'test_service_is_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'ServiceFixture'
op|'('
name|'self'
op|'.'
name|'_host'
op|','
name|'self'
op|'.'
name|'_binary'
op|','
name|'self'
op|'.'
name|'_topic'
op|')'
op|')'
op|'.'
name|'serv'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
name|'fake_now'
op|'='
number|'1000'
newline|'\n'
name|'down_time'
op|'='
number|'5'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'service_down_time'
op|'='
name|'down_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'timeutils'
op|','
string|"'utcnow_ts'"
op|')'
newline|'\n'
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
name|'hostkey'
op|'='
name|'str'
op|'('
string|'"%s:%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_topic'
op|','
name|'self'
op|'.'
name|'_host'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Up (equal)'
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|'+'
name|'down_time'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'hostkey'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'down_time'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_ref'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
comment|'# Up'
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|'+'
name|'down_time'
op|'-'
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'hostkey'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'down_time'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_ref'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
comment|'# Down'
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|'+'
name|'down_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'hostkey'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'down_time'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
comment|'# Down'
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_now'
op|'+'
name|'down_time'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'hostkey'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'down_time'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_state
dedent|''
name|'def'
name|'test_report_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'ServiceFixture'
op|'('
name|'self'
op|'.'
name|'_host'
op|','
name|'self'
op|'.'
name|'_binary'
op|','
name|'self'
op|'.'
name|'_topic'
op|')'
op|')'
op|'.'
name|'serv'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'_ctx'
op|','
name|'self'
op|'.'
name|'_host'
op|','
name|'self'
op|'.'
name|'_binary'
op|')'
newline|'\n'
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
nl|'\n'
comment|'# updating model_disconnected'
nl|'\n'
name|'serv'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'_report_state'
op|'('
name|'serv'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'serv'
op|'.'
name|'model_disconnected'
op|')'
newline|'\n'
nl|'\n'
comment|'# handling exception'
nl|'\n'
name|'serv'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'_report_state'
op|'('
name|'serv'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'serv'
op|'.'
name|'model_disconnected'
op|')'
newline|'\n'
nl|'\n'
name|'delattr'
op|'('
name|'serv'
op|','
string|"'model_disconnected'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'mc'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'_report_state'
op|'('
name|'serv'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'serv'
op|'.'
name|'model_disconnected'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
