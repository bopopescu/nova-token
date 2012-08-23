begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
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
string|'"""\nUnit Tests for volume types code\n"""'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'session'
name|'as'
name|'sql_session'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
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
name|'volume'
name|'import'
name|'volume_types'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeTypeTestCase
name|'class'
name|'VolumeTypeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for volume type code"""'
newline|'\n'
DECL|member|setUp
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
name|'VolumeTypeTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
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
name|'vol_type1_name'
op|'='
name|'str'
op|'('
name|'int'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vol_type1_specs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'type'
op|'='
string|'"physical drive"'
op|','
nl|'\n'
name|'drive_type'
op|'='
string|'"SAS"'
op|','
nl|'\n'
name|'size'
op|'='
string|'"300"'
op|','
nl|'\n'
name|'rpm'
op|'='
string|'"7200"'
op|','
nl|'\n'
name|'visible'
op|'='
string|'"True"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_create_then_destroy
dedent|''
name|'def'
name|'test_volume_type_create_then_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure volume types can be created and deleted"""'
newline|'\n'
name|'prev_all_vtypes'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_specs'
op|')'
newline|'\n'
name|'new'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_name'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Given data: %s"'
op|')'
op|','
name|'self'
op|'.'
name|'vol_type1_specs'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Result data: %s"'
op|')'
op|','
name|'new'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertEqual'
op|'('
name|'v'
op|','
name|'new'
op|'['
string|"'extra_specs'"
op|']'
op|'['
name|'k'
op|']'
op|','
nl|'\n'
string|"'one of fields does not match'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'new_all_vtypes'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'prev_all_vtypes'
op|')'
op|'+'
number|'1'
op|','
nl|'\n'
name|'len'
op|'('
name|'new_all_vtypes'
op|')'
op|','
nl|'\n'
string|"'drive type was not created'"
op|')'
newline|'\n'
nl|'\n'
name|'volume_types'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'vol_type1_name'
op|')'
newline|'\n'
name|'new_all_vtypes'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'prev_all_vtypes'
op|','
nl|'\n'
name|'new_all_vtypes'
op|','
nl|'\n'
string|"'drive type was not deleted'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_volume_types
dedent|''
name|'def'
name|'test_get_all_volume_types'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that all volume types can be retrieved"""'
newline|'\n'
name|'session'
op|'='
name|'sql_session'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'total_volume_types'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'VolumeTypes'
op|')'
op|'.'
name|'count'
op|'('
op|')'
newline|'\n'
name|'vol_types'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'total_volume_types'
op|','
name|'len'
op|'('
name|'vol_types'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_existent_vol_type_shouldnt_delete
dedent|''
name|'def'
name|'test_non_existent_vol_type_shouldnt_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that volume type creation fails with invalid args"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeTypeNotFoundByName'
op|','
nl|'\n'
name|'volume_types'
op|'.'
name|'destroy'
op|','
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"sfsfsdfdfs"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_repeated_vol_types_shouldnt_raise
dedent|''
name|'def'
name|'test_repeated_vol_types_shouldnt_raise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that volume duplicates don\'t raise"""'
newline|'\n'
name|'new_name'
op|'='
name|'self'
op|'.'
name|'vol_type1_name'
op|'+'
string|'"dup"'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'new_name'
op|')'
newline|'\n'
name|'volume_types'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'new_name'
op|')'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'new_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_volume_types_params
dedent|''
name|'def'
name|'test_invalid_volume_types_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that volume type creation fails with invalid args"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|','
nl|'\n'
name|'volume_types'
op|'.'
name|'destroy'
op|','
name|'self'
op|'.'
name|'ctxt'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|','
nl|'\n'
name|'volume_types'
op|'.'
name|'get_volume_type'
op|','
name|'self'
op|'.'
name|'ctxt'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|','
nl|'\n'
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_get_by_id_and_name
dedent|''
name|'def'
name|'test_volume_type_get_by_id_and_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure volume types get returns same entry"""'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_specs'
op|')'
newline|'\n'
name|'new'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vol_type1_name'
op|')'
newline|'\n'
nl|'\n'
name|'new2'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'new'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'new'
op|','
name|'new2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_search_by_extra_spec
dedent|''
name|'def'
name|'test_volume_type_search_by_extra_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure volume types get by extra spec returns correct type"""'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"type1"'
op|','
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
nl|'\n'
string|'"key2"'
op|':'
string|'"val2"'
op|'}'
op|')'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"type2"'
op|','
op|'{'
string|'"key2"'
op|':'
string|'"val2"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"val3"'
op|'}'
op|')'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"type3"'
op|','
op|'{'
string|'"key3"'
op|':'
string|'"another_value"'
op|','
nl|'\n'
string|'"key4"'
op|':'
string|'"val4"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vol_types'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'extra_specs'"
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"vol_types: %s"'
op|'%'
name|'vol_types'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vol_types'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"type1"'
name|'in'
name|'vol_types'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol_types'
op|'['
string|"'type1'"
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
string|'"key2"'
op|':'
string|'"val2"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vol_types'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'extra_specs'"
op|':'
op|'{'
string|'"key2"'
op|':'
string|'"val2"'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"vol_types: %s"'
op|'%'
name|'vol_types'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vol_types'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"type1"'
name|'in'
name|'vol_types'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"type2"'
name|'in'
name|'vol_types'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vol_types'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'extra_specs'"
op|':'
op|'{'
string|'"key3"'
op|':'
string|'"val3"'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"vol_types: %s"'
op|'%'
name|'vol_types'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vol_types'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"type2"'
name|'in'
name|'vol_types'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_type_search_by_extra_spec_multiple
dedent|''
name|'def'
name|'test_volume_type_search_by_extra_spec_multiple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure volume types get by extra spec returns correct type"""'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"type1"'
op|','
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
nl|'\n'
string|'"key2"'
op|':'
string|'"val2"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"val3"'
op|'}'
op|')'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"type2"'
op|','
op|'{'
string|'"key2"'
op|':'
string|'"val2"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"val3"'
op|'}'
op|')'
newline|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|'"type3"'
op|','
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"val3"'
op|','
nl|'\n'
string|'"key4"'
op|':'
string|'"val4"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vol_types'
op|'='
name|'volume_types'
op|'.'
name|'get_all_types'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'extra_specs'"
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"val3"'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"vol_types: %s"'
op|'%'
name|'vol_types'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vol_types'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"type1"'
name|'in'
name|'vol_types'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"type3"'
name|'in'
name|'vol_types'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol_types'
op|'['
string|"'type1'"
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
string|'"key2"'
op|':'
string|'"val2"'
op|','
string|'"key3"'
op|':'
string|'"val3"'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol_types'
op|'['
string|"'type3'"
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
op|'{'
string|'"key1"'
op|':'
string|'"val1"'
op|','
string|'"key3"'
op|':'
string|'"val3"'
op|','
string|'"key4"'
op|':'
string|'"val4"'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
