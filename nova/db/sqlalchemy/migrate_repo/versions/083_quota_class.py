begin_unit
comment|'# Copyright 2012 OpenStack LLC.'
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
name|'sqlalchemy'
name|'import'
name|'Boolean'
op|','
name|'Column'
op|','
name|'DateTime'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Integer'
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
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
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
comment|'# New table'
nl|'\n'
name|'quota_classes'
op|'='
name|'Table'
op|'('
string|"'quota_classes'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
name|'create_constraint'
op|'='
name|'True'
op|','
name|'name'
op|'='
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'class_name'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'True'
op|','
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
name|'index'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'resource'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'True'
op|','
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'hard_limit'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'quota_classes'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Table |%s| not created!"'
op|')'
op|','
name|'repr'
op|'('
name|'quota_classes'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'quota_classes'
op|'='
name|'Table'
op|'('
string|"'quota_classes'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'quota_classes'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"quota_classes table not dropped"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
