begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 Ken Pepple'
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
string|'"""Built-in volume type properties."""'
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
name|'exception'
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
string|"'nova.volume.volume_types'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates volume types."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'volume_type_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
name|'name'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB error: %s'"
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Cannot create volume_type with "'
nl|'\n'
string|'"name %(name)s and specs %(extra_specs)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy
dedent|''
dedent|''
name|'def'
name|'destroy'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Marks volume types as deleted."""'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'volume_type'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_type_destroy'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Volume type %s not found for deletion'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown volume type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|purge
dedent|''
dedent|''
dedent|''
name|'def'
name|'purge'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Removes volume types from database."""'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'volume_type'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_type_purge'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Volume type %s not found for purge'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown volume type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_all_types
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_all_types'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
number|'0'
op|','
name|'search_opts'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all non-deleted volume_types.\n\n    Pass true as argument if you want deleted volume types returned also.\n\n    """'
newline|'\n'
name|'vol_types'
op|'='
name|'db'
op|'.'
name|'volume_type_get_all'
op|'('
name|'context'
op|','
name|'inactive'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'search_opts'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Searching by: %s"'
op|')'
op|'%'
name|'str'
op|'('
name|'search_opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_check_extra_specs_match
name|'def'
name|'_check_extra_specs_match'
op|'('
name|'vol_type'
op|','
name|'searchdict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'searchdict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
op|'('
name|'k'
name|'not'
name|'in'
name|'vol_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
nl|'\n'
name|'or'
name|'vol_type'
op|'['
string|"'extra_specs'"
op|']'
op|'['
name|'k'
op|']'
op|'!='
name|'v'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
comment|'# search_option to filter_name mapping.'
nl|'\n'
dedent|''
name|'filter_mapping'
op|'='
op|'{'
string|"'extra_specs'"
op|':'
name|'_check_extra_specs_match'
op|'}'
newline|'\n'
nl|'\n'
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'type_name'
op|','
name|'type_args'
name|'in'
name|'vol_types'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# go over all filters in the list'
nl|'\n'
indent|'            '
name|'for'
name|'opt'
op|','
name|'values'
name|'in'
name|'search_opts'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'filter_func'
op|'='
name|'filter_mapping'
op|'['
name|'opt'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|'# no such filter - ignore it, go to next filter'
nl|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'filter_func'
op|'('
name|'type_args'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'result'
op|'['
name|'type_name'
op|']'
op|'='
name|'type_args'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'vol_types'
op|'='
name|'result'
newline|'\n'
dedent|''
name|'return'
name|'vol_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_volume_type
dedent|''
name|'def'
name|'get_volume_type'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single volume type by id."""'
newline|'\n'
name|'if'
name|'id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'volume_type'
op|'='
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ctxt'
name|'is'
name|'None'
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
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'volume_type_get'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown volume type: %s"'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_volume_type_by_name
dedent|''
dedent|''
name|'def'
name|'get_volume_type_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single volume type by name."""'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'volume_type'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'volume_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown volume type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_key_value_present
dedent|''
dedent|''
name|'def'
name|'is_key_value_present'
op|'('
name|'volume_type_id'
op|','
name|'key'
op|','
name|'value'
op|','
name|'volume_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'volume_type_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'volume_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'volume_type'
op|'='
name|'get_volume_type'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_type_id'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'volume_type'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|')'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'volume_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|'!='
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_vsa_drive
dedent|''
dedent|''
name|'def'
name|'is_vsa_drive'
op|'('
name|'volume_type_id'
op|','
name|'volume_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'is_key_value_present'
op|'('
name|'volume_type_id'
op|','
nl|'\n'
string|"'type'"
op|','
string|"'vsa_drive'"
op|','
name|'volume_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_vsa_volume
dedent|''
name|'def'
name|'is_vsa_volume'
op|'('
name|'volume_type_id'
op|','
name|'volume_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'is_key_value_present'
op|'('
name|'volume_type_id'
op|','
nl|'\n'
string|"'type'"
op|','
string|"'vsa_volume'"
op|','
name|'volume_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_vsa_object
dedent|''
name|'def'
name|'is_vsa_object'
op|'('
name|'volume_type_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'volume_type_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'volume_type'
op|'='
name|'get_volume_type'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_type_id'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'is_vsa_drive'
op|'('
name|'volume_type_id'
op|','
name|'volume_type'
op|')'
name|'or'
nl|'\n'
name|'is_vsa_volume'
op|'('
name|'volume_type_id'
op|','
name|'volume_type'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
