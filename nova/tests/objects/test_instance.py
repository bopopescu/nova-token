begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'datetime'
newline|'\n'
name|'import'
name|'iso8601'
newline|'\n'
name|'import'
name|'netaddr'
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
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'security_group'
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
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceObject
name|'class'
name|'_TestInstanceObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'property'
newline|'\n'
DECL|member|fake_instance
name|'def'
name|'fake_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_instance'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'access_ipv4'
op|'='
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'access_ipv6'
op|'='
string|"'::1'"
op|')'
newline|'\n'
name|'fake_instance'
op|'['
string|"'scheduled_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'terminated_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'deleted_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'launched_at'"
op|']'
op|'='
op|'('
nl|'\n'
name|'fake_instance'
op|'['
string|"'launched_at'"
op|']'
op|'.'
name|'replace'
op|'('
nl|'\n'
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|','
name|'microsecond'
op|'='
number|'0'
op|')'
op|')'
newline|'\n'
name|'fake_instance'
op|'['
string|"'deleted'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'fake_instance'
op|'['
string|"'info_cache'"
op|']'
op|'['
string|"'instance_uuid'"
op|']'
op|'='
name|'fake_instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'fake_instance'
op|'['
string|"'security_groups'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'return'
name|'fake_instance'
newline|'\n'
nl|'\n'
DECL|member|test_datetime_deserialization
dedent|''
name|'def'
name|'test_datetime_deserialization'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'red_letter_date'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
nl|'\n'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1955'
op|','
number|'11'
op|','
number|'5'
op|')'
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'inst'
op|'.'
name|'launched_at'
op|'='
name|'red_letter_date'
newline|'\n'
name|'primitive'
op|'='
name|'inst'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'Instance'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.0'"
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'launched_at'"
op|':'
string|"'1955-11-05T00:00:00Z'"
op|'}'
op|','
nl|'\n'
string|"'nova_object.changes'"
op|':'
op|'['
string|"'uuid'"
op|','
string|"'launched_at'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'primitive'
op|','
name|'expected'
op|')'
newline|'\n'
name|'inst2'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'obj_from_primitive'
op|'('
name|'primitive'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst2'
op|'.'
name|'launched_at'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst2'
op|'.'
name|'launched_at'
op|','
name|'red_letter_date'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ip_deserialization
dedent|''
name|'def'
name|'test_ip_deserialization'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'inst'
op|'.'
name|'access_ip_v4'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'inst'
op|'.'
name|'access_ip_v6'
op|'='
string|"'::1'"
newline|'\n'
name|'primitive'
op|'='
name|'inst'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'Instance'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.0'"
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'::1'"
op|'}'
op|','
nl|'\n'
string|"'nova_object.changes'"
op|':'
op|'['
string|"'uuid'"
op|','
string|"'access_ip_v6'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'primitive'
op|','
name|'expected'
op|')'
newline|'\n'
name|'inst2'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'obj_from_primitive'
op|'('
name|'primitive'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst2'
op|'.'
name|'access_ip_v4'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst2'
op|'.'
name|'access_ip_v6'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst2'
op|'.'
name|'access_ip_v4'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst2'
op|'.'
name|'access_ip_v6'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_without_expected
dedent|''
name|'def'
name|'test_get_without_expected'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
string|"'uuid'"
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'fake_instance'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
string|"'uuid'"
op|')'
newline|'\n'
comment|"# Make sure these weren't loaded"
nl|'\n'
name|'for'
name|'attr'
name|'in'
name|'instance'
op|'.'
name|'INSTANCE_OPTIONAL_FIELDS'
op|':'
newline|'\n'
indent|'            '
name|'attrname'
op|'='
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'attr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'hasattr'
op|'('
name|'inst'
op|','
name|'attrname'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_with_expected
dedent|''
name|'def'
name|'test_get_with_expected'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'uuid'"
op|','
nl|'\n'
name|'instance'
op|'.'
name|'INSTANCE_OPTIONAL_FIELDS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'fake_instance'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'uuid'"
op|','
name|'expected_attrs'
op|'='
name|'instance'
op|'.'
name|'INSTANCE_OPTIONAL_FIELDS'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'instance'
op|'.'
name|'INSTANCE_OPTIONAL_FIELDS'
op|':'
newline|'\n'
indent|'            '
name|'attrname'
op|'='
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'attr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'inst'
op|','
name|'attrname'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_load
dedent|''
name|'def'
name|'test_load'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'fake_uuid'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
name|'fake_inst2'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|','
nl|'\n'
name|'system_metadata'
op|'='
op|'['
op|'{'
string|"'key'"
op|':'
string|"'foo'"
op|','
string|"'value'"
op|':'
string|"'bar'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
string|"'system_metadata'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst2'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'hasattr'
op|'('
name|'inst'
op|','
string|"'_system_metadata'"
op|')'
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'inst'
op|'.'
name|'system_metadata'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sys_meta'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'inst'
op|','
string|"'_system_metadata'"
op|')'
op|')'
newline|'\n'
comment|"# Make sure we don't run load again"
nl|'\n'
name|'sys_meta2'
op|'='
name|'inst'
op|'.'
name|'system_metadata'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sys_meta2'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_remote
dedent|''
name|'def'
name|'test_get_remote'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# isotime doesn't have microseconds and is always UTC"
nl|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'fake_instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
string|"'fake-uuid'"
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_instance'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'id'
op|','
name|'fake_instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'launched_at'
op|','
name|'fake_instance'
op|'['
string|"'launched_at'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'inst'
op|'.'
name|'access_ip_v4'
op|')'
op|','
nl|'\n'
name|'fake_instance'
op|'['
string|"'access_ip_v4'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'inst'
op|'.'
name|'access_ip_v6'
op|')'
op|','
nl|'\n'
name|'fake_instance'
op|'['
string|"'access_ip_v6'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh
dedent|''
name|'def'
name|'test_refresh'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'fake_uuid'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'host'
op|'='
string|"'orig-host'"
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'host'
op|'='
string|"'new-host'"
op|')'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'host'
op|','
string|"'orig-host'"
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'host'
op|','
string|"'new-host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
name|'inst'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save
dedent|''
name|'def'
name|'test_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_inst'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'host'
op|'='
string|"'oldhost'"
op|')'
newline|'\n'
name|'fake_uuid'
op|'='
name|'fake_inst'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_info_cache_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'{'
string|"'user_data'"
op|':'
string|"'foo'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'('
name|'fake_inst'
op|','
name|'dict'
op|'('
name|'fake_inst'
op|','
name|'host'
op|'='
string|"'newhost'"
op|')'
op|')'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'user_data'
op|'='
string|"'foo'"
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'host'
op|','
string|"'newhost'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_deleted
dedent|''
name|'def'
name|'test_get_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_inst'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'id'
op|'='
number|'123'
op|','
name|'deleted'
op|'='
number|'123'
op|')'
newline|'\n'
name|'fake_uuid'
op|'='
name|'fake_inst'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
comment|"# NOTE(danms): Make sure it's actually a bool"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'deleted'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_with_info_cache
dedent|''
name|'def'
name|'test_with_info_cache'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_inst'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
name|'fake_uuid'
op|'='
name|'fake_inst'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'fake_inst'
op|'['
string|"'info_cache'"
op|']'
op|'='
op|'{'
string|"'network_info'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fake_uuid'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_info_cache_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_info_cache_update'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
string|"'bar'"
op|'}'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'info_cache'
op|'.'
name|'network_info'
op|','
nl|'\n'
name|'fake_inst'
op|'['
string|"'info_cache'"
op|']'
op|'['
string|"'network_info'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'info_cache'
op|'.'
name|'instance_uuid'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'info_cache'
op|'.'
name|'network_info'
op|'='
string|"'bar'"
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_with_security_groups
dedent|''
name|'def'
name|'test_with_security_groups'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_inst'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
name|'fake_uuid'
op|'='
name|'fake_inst'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'fake_inst'
op|'['
string|"'security_groups'"
op|']'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
string|"'secgroup1'"
op|','
string|"'description'"
op|':'
string|"'fake-desc'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake-user'"
op|','
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
string|"'updated_at'"
op|':'
name|'None'
op|','
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'name'"
op|':'
string|"'secgroup2'"
op|','
string|"'description'"
op|':'
string|"'fake-desc'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake-user'"
op|','
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
string|"'updated_at'"
op|':'
name|'None'
op|','
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_update'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
op|'{'
string|"'description'"
op|':'
string|"'changed'"
op|'}'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst'
op|'['
string|"'security_groups'"
op|']'
op|'['
number|'0'
op|']'
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
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'inst'
op|'.'
name|'security_groups'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'fake_inst'
op|'['
string|"'security_groups'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'group'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'inst'
op|'.'
name|'security_groups'
op|'['
name|'index'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst'
op|'.'
name|'security_groups'
op|'['
name|'index'
op|']'
op|','
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'security_groups'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'security_groups'
op|'['
number|'0'
op|']'
op|'.'
name|'description'
op|'='
string|"'changed'"
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'security_groups'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_iteritems_with_extra_attrs
dedent|''
name|'def'
name|'test_iteritems_with_extra_attrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance'
op|'.'
name|'Instance'
op|','
string|"'name'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|'.'
name|'items'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'foo'"
op|','
nl|'\n'
op|'}'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceObject
name|'_TestInstanceObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceObject
name|'_TestInstanceObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceListObject
dedent|''
name|'class'
name|'_TestInstanceListObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|fake_instance
indent|'    '
name|'def'
name|'fake_instance'
op|'('
name|'self'
op|','
name|'id'
op|','
name|'updates'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_instance'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'access_ipv4'
op|'='
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'access_ipv6'
op|'='
string|"'::1'"
op|')'
newline|'\n'
name|'fake_instance'
op|'['
string|"'scheduled_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'terminated_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'deleted_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fake_instance'
op|'['
string|"'launched_at'"
op|']'
op|'='
op|'('
nl|'\n'
name|'fake_instance'
op|'['
string|"'launched_at'"
op|']'
op|'.'
name|'replace'
op|'('
nl|'\n'
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|','
name|'microsecond'
op|'='
number|'0'
op|')'
op|')'
newline|'\n'
name|'fake_instance'
op|'['
string|"'info_cache'"
op|']'
op|'='
op|'{'
string|"'network_info'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fake_instance'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
name|'fake_instance'
op|'['
string|"'security_groups'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'fake_instance'
op|'['
string|"'deleted'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'fake_instance'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'fake_instance'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_by_filters
dedent|''
name|'def'
name|'test_get_all_by_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fakes'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'1'
op|')'
op|','
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'2'
op|')'
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_filters'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'ctxt'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
string|"'uuid'"
op|','
string|"'asc'"
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fakes'
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
name|'inst_list'
op|'='
name|'instance'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_filters'
op|'('
nl|'\n'
name|'ctxt'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
string|"'uuid'"
op|','
string|"'asc'"
op|','
name|'expected_attrs'
op|'='
op|'['
string|"'metadata'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'fakes'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'Instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'fakes'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_host
dedent|''
name|'def'
name|'test_get_by_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fakes'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'2'
op|')'
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_host'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'ctxt'
op|','
string|"'foo'"
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fakes'
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
name|'inst_list'
op|'='
name|'instance'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_host'
op|'('
name|'ctxt'
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'fakes'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'Instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'fakes'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'_context'
op|','
name|'ctxt'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_host_and_node
dedent|''
name|'def'
name|'test_get_by_host_and_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fakes'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'2'
op|')'
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_host_and_node'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_all_by_host_and_node'
op|'('
name|'ctxt'
op|','
string|"'foo'"
op|','
string|"'bar'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fakes'
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
name|'inst_list'
op|'='
name|'instance'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_host_and_node'
op|'('
name|'ctxt'
op|','
string|"'foo'"
op|','
nl|'\n'
string|"'bar'"
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'fakes'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'Instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'fakes'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_host_and_not_type
dedent|''
name|'def'
name|'test_get_by_host_and_not_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fakes'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'2'
op|')'
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_host_and_not_type'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_all_by_host_and_not_type'
op|'('
name|'ctxt'
op|','
string|"'foo'"
op|','
nl|'\n'
name|'type_id'
op|'='
string|"'bar'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fakes'
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
name|'inst_list'
op|'='
name|'instance'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_host_and_not_type'
op|'('
name|'ctxt'
op|','
string|"'foo'"
op|','
nl|'\n'
string|"'bar'"
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'fakes'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'Instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'fakes'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_hung_in_rebooting
dedent|''
name|'def'
name|'test_get_hung_in_rebooting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fakes'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'('
number|'2'
op|')'
op|']'
newline|'\n'
name|'dt'
op|'='
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_all_hung_in_rebooting'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'ctxt'
op|','
name|'dt'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fakes'
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
name|'inst_list'
op|'='
name|'instance'
op|'.'
name|'InstanceList'
op|'.'
name|'get_hung_in_rebooting'
op|'('
name|'ctxt'
op|','
name|'dt'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'fakes'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'Instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'fakes'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceListObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceListObject
name|'_TestInstanceListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceListObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceListObject
name|'_TestInstanceListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
