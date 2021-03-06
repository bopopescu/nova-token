begin_unit
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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'migrate'
name|'import'
name|'exceptions'
name|'as'
name|'versioning_exceptions'
newline|'\n'
name|'from'
name|'migrate'
op|'.'
name|'versioning'
name|'import'
name|'api'
name|'as'
name|'versioning_api'
newline|'\n'
name|'from'
name|'migrate'
op|'.'
name|'versioning'
op|'.'
name|'repository'
name|'import'
name|'Repository'
newline|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
name|'as'
name|'db_utils'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
name|'import'
name|'null'
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
name|'db_session'
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
newline|'\n'
nl|'\n'
DECL|variable|INIT_VERSION
name|'INIT_VERSION'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'INIT_VERSION'
op|'['
string|"'main'"
op|']'
op|'='
number|'215'
newline|'\n'
name|'INIT_VERSION'
op|'['
string|"'api'"
op|']'
op|'='
number|'0'
newline|'\n'
DECL|variable|_REPOSITORY
name|'_REPOSITORY'
op|'='
op|'{'
op|'}'
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
DECL|function|get_engine
name|'def'
name|'get_engine'
op|'('
name|'database'
op|'='
string|"'main'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'database'
op|'=='
string|"'main'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db_session'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'database'
op|'=='
string|"'api'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db_session'
op|'.'
name|'get_api_engine'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_sync
dedent|''
dedent|''
name|'def'
name|'db_sync'
op|'('
name|'version'
op|'='
name|'None'
op|','
name|'database'
op|'='
string|"'main'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'version'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'int'
op|'('
name|'version'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"version should be an integer"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'current_version'
op|'='
name|'db_version'
op|'('
name|'database'
op|')'
newline|'\n'
name|'repository'
op|'='
name|'_find_migrate_repo'
op|'('
name|'database'
op|')'
newline|'\n'
name|'if'
name|'version'
name|'is'
name|'None'
name|'or'
name|'version'
op|'>'
name|'current_version'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versioning_api'
op|'.'
name|'upgrade'
op|'('
name|'get_engine'
op|'('
name|'database'
op|')'
op|','
name|'repository'
op|','
nl|'\n'
name|'version'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versioning_api'
op|'.'
name|'downgrade'
op|'('
name|'get_engine'
op|'('
name|'database'
op|')'
op|','
name|'repository'
op|','
nl|'\n'
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_version
dedent|''
dedent|''
name|'def'
name|'db_version'
op|'('
name|'database'
op|'='
string|"'main'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'repository'
op|'='
name|'_find_migrate_repo'
op|'('
name|'database'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versioning_api'
op|'.'
name|'db_version'
op|'('
name|'get_engine'
op|'('
name|'database'
op|')'
op|','
name|'repository'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'versioning_exceptions'
op|'.'
name|'DatabaseNotControlledError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'meta'
op|'='
name|'sqlalchemy'
op|'.'
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'engine'
op|'='
name|'get_engine'
op|'('
name|'database'
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'reflect'
op|'('
name|'bind'
op|'='
name|'engine'
op|')'
newline|'\n'
name|'tables'
op|'='
name|'meta'
op|'.'
name|'tables'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'tables'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'db_version_control'
op|'('
name|'INIT_VERSION'
op|'['
name|'database'
op|']'
op|','
name|'database'
op|')'
newline|'\n'
name|'return'
name|'versioning_api'
op|'.'
name|'db_version'
op|'('
name|'get_engine'
op|'('
name|'database'
op|')'
op|','
name|'repository'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
comment|"# Some pre-Essex DB's may not be version controlled."
nl|'\n'
comment|'# Require them to upgrade using Essex first.'
nl|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Upgrade DB using Essex release first."'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_initial_version
dedent|''
dedent|''
dedent|''
name|'def'
name|'db_initial_version'
op|'('
name|'database'
op|'='
string|"'main'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'INIT_VERSION'
op|'['
name|'database'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_process_null_records
dedent|''
name|'def'
name|'_process_null_records'
op|'('
name|'table'
op|','
name|'col_name'
op|','
name|'check_fkeys'
op|','
name|'delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Queries the database and optionally deletes the NULL records.\n\n    :param table: sqlalchemy.Table object.\n    :param col_name: The name of the column to check in the table.\n    :param check_fkeys: If True, check the table for foreign keys back to the\n        instances table and if not found, return.\n    :param delete: If true, run a delete operation on the table, else just\n        query for number of records that match the NULL column.\n    :returns: The number of records processed for the table and column.\n    """'
newline|'\n'
name|'records'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'col_name'
name|'in'
name|'table'
op|'.'
name|'columns'
op|':'
newline|'\n'
comment|"# NOTE(mriedem): filter out tables that don't have a foreign key back"
nl|'\n'
comment|'# to the instances table since they could have stale data even if'
nl|'\n'
comment|"# instances.uuid wasn't NULL."
nl|'\n'
indent|'        '
name|'if'
name|'check_fkeys'
op|':'
newline|'\n'
indent|'            '
name|'fkey_found'
op|'='
name|'False'
newline|'\n'
name|'fkeys'
op|'='
name|'table'
op|'.'
name|'c'
op|'['
name|'col_name'
op|']'
op|'.'
name|'foreign_keys'
name|'or'
op|'['
op|']'
newline|'\n'
name|'for'
name|'fkey'
name|'in'
name|'fkeys'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'fkey'
op|'.'
name|'column'
op|'.'
name|'table'
op|'.'
name|'name'
op|'=='
string|"'instances'"
op|':'
newline|'\n'
indent|'                    '
name|'fkey_found'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'fkey_found'
op|':'
newline|'\n'
indent|'                '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'delete'
op|':'
newline|'\n'
indent|'            '
name|'records'
op|'='
name|'table'
op|'.'
name|'delete'
op|'('
op|')'
op|'.'
name|'where'
op|'('
nl|'\n'
name|'table'
op|'.'
name|'c'
op|'['
name|'col_name'
op|']'
op|'=='
name|'null'
op|'('
op|')'
nl|'\n'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|'.'
name|'rowcount'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'records'
op|'='
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'table'
op|'.'
name|'select'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'table'
op|'.'
name|'c'
op|'['
name|'col_name'
op|']'
op|'=='
name|'null'
op|'('
op|')'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
nl|'\n'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'records'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_null_instance_uuid_scan
dedent|''
name|'def'
name|'db_null_instance_uuid_scan'
op|'('
name|'delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Scans the database for NULL instance_uuid records.\n\n    :param delete: If true, delete NULL instance_uuid records found, else\n                   just query to see if they exist for reporting.\n    :returns: dict of table name to number of hits for NULL instance_uuid rows.\n    """'
newline|'\n'
name|'engine'
op|'='
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'='
name|'sqlalchemy'
op|'.'
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'engine'
op|')'
newline|'\n'
comment|"# NOTE(mriedem): We're going to load up all of the tables so we can find"
nl|'\n'
comment|'# any with an instance_uuid column since those may be foreign keys back'
nl|'\n'
comment|'# to the instances table and we want to cleanup those records first. We'
nl|'\n'
comment|"# have to do this explicitly because the foreign keys in nova aren't"
nl|'\n'
comment|'# defined with cascading deletes.'
nl|'\n'
name|'meta'
op|'.'
name|'reflect'
op|'('
name|'engine'
op|')'
newline|'\n'
comment|'# Keep track of all of the tables that had hits in the query.'
nl|'\n'
name|'processed'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'table'
name|'in'
name|'reversed'
op|'('
name|'meta'
op|'.'
name|'sorted_tables'
op|')'
op|':'
newline|'\n'
comment|'# Ignore the fixed_ips table by design.'
nl|'\n'
indent|'        '
name|'if'
name|'table'
op|'.'
name|'name'
name|'not'
name|'in'
op|'('
string|"'fixed_ips'"
op|','
string|"'shadow_fixed_ips'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'processed'
op|'['
name|'table'
op|'.'
name|'name'
op|']'
op|'='
name|'_process_null_records'
op|'('
nl|'\n'
name|'table'
op|','
string|"'instance_uuid'"
op|','
name|'check_fkeys'
op|'='
name|'True'
op|','
name|'delete'
op|'='
name|'delete'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now process the *instances tables.'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'table_name'
name|'in'
op|'('
string|"'instances'"
op|','
string|"'shadow_instances'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
name|'processed'
op|'['
name|'table'
op|'.'
name|'name'
op|']'
op|'='
name|'_process_null_records'
op|'('
nl|'\n'
name|'table'
op|','
string|"'uuid'"
op|','
name|'check_fkeys'
op|'='
name|'False'
op|','
name|'delete'
op|'='
name|'delete'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'processed'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_version_control
dedent|''
name|'def'
name|'db_version_control'
op|'('
name|'version'
op|'='
name|'None'
op|','
name|'database'
op|'='
string|"'main'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'repository'
op|'='
name|'_find_migrate_repo'
op|'('
name|'database'
op|')'
newline|'\n'
name|'versioning_api'
op|'.'
name|'version_control'
op|'('
name|'get_engine'
op|'('
name|'database'
op|')'
op|','
name|'repository'
op|','
name|'version'
op|')'
newline|'\n'
name|'return'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_find_migrate_repo
dedent|''
name|'def'
name|'_find_migrate_repo'
op|'('
name|'database'
op|'='
string|"'main'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the path for the migrate repository."""'
newline|'\n'
name|'global'
name|'_REPOSITORY'
newline|'\n'
name|'rel_path'
op|'='
string|"'migrate_repo'"
newline|'\n'
name|'if'
name|'database'
op|'=='
string|"'api'"
op|':'
newline|'\n'
indent|'        '
name|'rel_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'api_migrations'"
op|','
string|"'migrate_repo'"
op|')'
newline|'\n'
dedent|''
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|')'
op|','
nl|'\n'
name|'rel_path'
op|')'
newline|'\n'
name|'assert'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
newline|'\n'
name|'if'
name|'_REPOSITORY'
op|'.'
name|'get'
op|'('
name|'database'
op|')'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_REPOSITORY'
op|'['
name|'database'
op|']'
op|'='
name|'Repository'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_REPOSITORY'
op|'['
name|'database'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
