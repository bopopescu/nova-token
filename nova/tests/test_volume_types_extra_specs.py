begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2011 University of Southern California'
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
string|'"""\nUnit Tests for volume types extra specs code\n"""'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_session'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeTypeExtraSpecsTestCase
name|'class'
name|'VolumeTypeExtraSpecsTestCase'
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
name|'VolumeTypeExtraSpecsTestCase'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vol_type1'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"TEST: Regular volume test"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vol_type1_specs'
op|'='
name|'dict'
op|'('
name|'vol_extra1'
op|'='
string|'"value1"'
op|','
nl|'\n'
name|'vol_extra2'
op|'='
string|'"value2"'
op|','
nl|'\n'
name|'vol_extra3'
op|'='
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vol_type1'
op|'['
string|"'extra_specs'"
op|']'
op|'='
name|'self'
op|'.'
name|'vol_type1_specs'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'volume_type_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'vol_type1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|'='
name|'ref'
op|'.'
name|'id'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'vol_type1_specs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'vol_type1_specs'
op|'['
name|'k'
op|']'
op|'='
name|'str'
op|'('
name|'v'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'vol_type2_noextra'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"TEST: Volume type without extra"'
op|')'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'volume_type_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'vol_type2_noextra'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vol_type2_id'
op|'='
name|'ref'
op|'.'
name|'id'
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
comment|'# Remove the instance type from the database'
nl|'\n'
indent|'        '
name|'db'
op|'.'
name|'volume_type_purge'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_type_purge'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type2_noextra'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'super'
op|'('
name|'VolumeTypeExtraSpecsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_specs_get
dedent|''
name|'def'
name|'test_volume_type_specs_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'self'
op|'.'
name|'vol_type1_specs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'volume_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_extra_specs_delete
dedent|''
name|'def'
name|'test_volume_type_extra_specs_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'self'
op|'.'
name|'vol_type1_specs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'del'
name|'expected_specs'
op|'['
string|"'vol_extra2'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'volume_type_extra_specs_delete'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|','
nl|'\n'
string|"'vol_extra2'"
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'volume_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_extra_specs_update
dedent|''
name|'def'
name|'test_volume_type_extra_specs_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'self'
op|'.'
name|'vol_type1_specs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'expected_specs'
op|'['
string|"'vol_extra3'"
op|']'
op|'='
string|'"4"'
newline|'\n'
name|'db'
op|'.'
name|'volume_type_extra_specs_update_or_create'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vol_extra3'
op|'='
number|'4'
op|')'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'volume_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_extra_specs_create
dedent|''
name|'def'
name|'test_volume_type_extra_specs_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'self'
op|'.'
name|'vol_type1_specs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'expected_specs'
op|'['
string|"'vol_extra4'"
op|']'
op|'='
string|"'value4'"
newline|'\n'
name|'expected_specs'
op|'['
string|"'vol_extra5'"
op|']'
op|'='
string|"'value5'"
newline|'\n'
name|'db'
op|'.'
name|'volume_type_extra_specs_update_or_create'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vol_extra4'
op|'='
string|'"value4"'
op|','
nl|'\n'
name|'vol_extra5'
op|'='
string|'"value5"'
op|')'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'volume_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_get_with_extra_specs
dedent|''
name|'def'
name|'test_volume_type_get_with_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_type'
op|'='
name|'db'
op|'.'
name|'volume_type_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_type1_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'volume_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_specs'
op|')'
newline|'\n'
nl|'\n'
name|'volume_type'
op|'='
name|'db'
op|'.'
name|'volume_type_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type2_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'volume_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_get_by_name_with_extra_specs
dedent|''
name|'def'
name|'test_volume_type_get_by_name_with_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_type'
op|'='
name|'db'
op|'.'
name|'volume_type_get_by_name'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'volume_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_specs'
op|')'
newline|'\n'
nl|'\n'
name|'volume_type'
op|'='
name|'db'
op|'.'
name|'volume_type_get_by_name'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type2_noextra'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'volume_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_get_all
dedent|''
name|'def'
name|'test_volume_type_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'self'
op|'.'
name|'vol_type1_specs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'types'
op|'='
name|'db'
op|'.'
name|'volume_type_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'types'
op|'['
name|'self'
op|'.'
name|'vol_type1'
op|'['
string|"'name'"
op|']'
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
name|'expected_specs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'types'
op|'['
name|'self'
op|'.'
name|'vol_type2_noextra'
op|'['
string|"'name'"
op|']'
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
