begin_unit
comment|'# Copyright (c) 2013 Boris Pavlovic (boris@pavlovic.me).'
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
name|'oslo_db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
newline|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
name|'as'
name|'oslodbutils'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'exc'
name|'import'
name|'OperationalError'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'ext'
op|'.'
name|'compiler'
name|'import'
name|'compiles'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
op|'.'
name|'expression'
name|'import'
name|'UpdateBase'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'types'
name|'import'
name|'NullType'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
newline|'\n'
nl|'\n'
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
DECL|class|DeleteFromSelect
name|'class'
name|'DeleteFromSelect'
op|'('
name|'UpdateBase'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'table'
op|','
name|'select'
op|','
name|'column'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'table'
op|'='
name|'table'
newline|'\n'
name|'self'
op|'.'
name|'select'
op|'='
name|'select'
newline|'\n'
name|'self'
op|'.'
name|'column'
op|'='
name|'column'
newline|'\n'
nl|'\n'
nl|'\n'
comment|"# NOTE(guochbo): some versions of MySQL doesn't yet support subquery with"
nl|'\n'
comment|"# 'LIMIT & IN/ALL/ANY/SOME' We need work around this with nesting select ."
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'compiles'
op|'('
name|'DeleteFromSelect'
op|')'
newline|'\n'
DECL|function|visit_delete_from_select
name|'def'
name|'visit_delete_from_select'
op|'('
name|'element'
op|','
name|'compiler'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"DELETE FROM %s WHERE %s in (SELECT T1.%s FROM (%s) as T1)"'
op|'%'
op|'('
nl|'\n'
name|'compiler'
op|'.'
name|'process'
op|'('
name|'element'
op|'.'
name|'table'
op|','
name|'asfrom'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'compiler'
op|'.'
name|'process'
op|'('
name|'element'
op|'.'
name|'column'
op|')'
op|','
nl|'\n'
name|'element'
op|'.'
name|'column'
op|'.'
name|'name'
op|','
nl|'\n'
name|'compiler'
op|'.'
name|'process'
op|'('
name|'element'
op|'.'
name|'select'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_shadow_table
dedent|''
name|'def'
name|'check_shadow_table'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This method checks that table with ``table_name`` and\n    corresponding shadow table have same columns.\n    """'
newline|'\n'
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
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'shadow_table'
op|'='
name|'Table'
op|'('
name|'db'
op|'.'
name|'_SHADOW_TABLE_PREFIX'
op|'+'
name|'table_name'
op|','
name|'meta'
op|','
nl|'\n'
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'columns'
op|'='
op|'{'
name|'c'
op|'.'
name|'name'
op|':'
name|'c'
name|'for'
name|'c'
name|'in'
name|'table'
op|'.'
name|'columns'
op|'}'
newline|'\n'
name|'shadow_columns'
op|'='
op|'{'
name|'c'
op|'.'
name|'name'
op|':'
name|'c'
name|'for'
name|'c'
name|'in'
name|'shadow_table'
op|'.'
name|'columns'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'name'
op|','
name|'column'
name|'in'
name|'columns'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'not'
name|'in'
name|'shadow_columns'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Missing column %(table)s.%(column)s in shadow table"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'column'"
op|':'
name|'name'
op|','
string|"'table'"
op|':'
name|'shadow_table'
op|'.'
name|'name'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'shadow_column'
op|'='
name|'shadow_columns'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'shadow_column'
op|'.'
name|'type'
op|','
name|'type'
op|'('
name|'column'
op|'.'
name|'type'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Different types in %(table)s.%(column)s and shadow table: "'
nl|'\n'
string|'"%(c_type)s %(shadow_c_type)s"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'column'"
op|':'
name|'name'
op|','
string|"'table'"
op|':'
name|'table'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'c_type'"
op|':'
name|'column'
op|'.'
name|'type'
op|','
nl|'\n'
string|"'shadow_c_type'"
op|':'
name|'shadow_column'
op|'.'
name|'type'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'name'
op|','
name|'column'
name|'in'
name|'shadow_columns'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'not'
name|'in'
name|'columns'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Extra column %(table)s.%(column)s in shadow table"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'column'"
op|':'
name|'name'
op|','
string|"'table'"
op|':'
name|'shadow_table'
op|'.'
name|'name'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_shadow_table
dedent|''
name|'def'
name|'create_shadow_table'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|'='
name|'None'
op|','
name|'table'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'col_name_col_instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This method create shadow table for table with name ``table_name``\n    or table instance ``table``.\n    :param table_name: Autoload table with this name and create shadow table\n    :param table: Autoloaded table, so just create corresponding shadow table.\n    :param col_name_col_instance:   contains pair column_name=column_instance.\n    column_instance is instance of Column. These params are required only for\n    columns that have unsupported types by sqlite. For example BigInteger.\n    :returns: The created shadow_table object.\n    """'
newline|'\n'
name|'meta'
op|'='
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'table_name'
name|'is'
name|'None'
name|'and'
name|'table'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Specify `table_name` or `table` "'
nl|'\n'
string|'"param"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
op|'('
name|'table_name'
name|'is'
name|'None'
name|'or'
name|'table'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Specify only one param `table_name` "'
nl|'\n'
string|'"`table`"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'table'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'columns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'column'
name|'in'
name|'table'
op|'.'
name|'columns'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'column'
op|'.'
name|'type'
op|','
name|'NullType'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_column'
op|'='
name|'oslodbutils'
op|'.'
name|'_get_not_supported_column'
op|'('
nl|'\n'
name|'col_name_col_instance'
op|','
name|'column'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'columns'
op|'.'
name|'append'
op|'('
name|'new_column'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'columns'
op|'.'
name|'append'
op|'('
name|'column'
op|'.'
name|'copy'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'shadow_table_name'
op|'='
name|'db'
op|'.'
name|'_SHADOW_TABLE_PREFIX'
op|'+'
name|'table'
op|'.'
name|'name'
newline|'\n'
name|'shadow_table'
op|'='
name|'Table'
op|'('
name|'shadow_table_name'
op|','
name|'meta'
op|','
op|'*'
name|'columns'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'shadow_table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'shadow_table'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'db_exc'
op|'.'
name|'DBError'
op|','
name|'OperationalError'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(ekudryashova): At the moment there is a case in oslo.db code,'
nl|'\n'
comment|'# which raises unwrapped OperationalError, so we should catch it until'
nl|'\n'
comment|'# oslo.db would wraps all such exceptions'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'repr'
op|'('
name|'shadow_table'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Exception while creating table.'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ShadowTableExists'
op|'('
name|'name'
op|'='
name|'shadow_table_name'
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
name|'info'
op|'('
name|'repr'
op|'('
name|'shadow_table'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Exception while creating table.'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
