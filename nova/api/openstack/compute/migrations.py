begin_unit
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
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'api_version_request'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-migrations"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|authorize
name|'def'
name|'authorize'
op|'('
name|'context'
op|','
name|'action_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
op|'('
name|'context'
op|','
name|'action'
op|'='
name|'action_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsController
dedent|''
name|'class'
name|'MigrationsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Controller for accessing migrations in OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|variable|_view_builder_class
name|'_view_builder_class'
op|'='
name|'common'
op|'.'
name|'ViewBuilder'
newline|'\n'
DECL|variable|_collection_name
name|'_collection_name'
op|'='
string|'"servers/%s/migrations"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MigrationsController'
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
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_output
dedent|''
name|'def'
name|'_output'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'migrations_obj'
op|','
name|'add_link'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the desired output of the API from an object.\n\n        From a MigrationsList\'s object this method returns a list of\n        primitive objects with the only necessary fields.\n        """'
newline|'\n'
name|'detail_keys'
op|'='
op|'['
string|"'memory_total'"
op|','
string|"'memory_processed'"
op|','
string|"'memory_remaining'"
op|','
nl|'\n'
string|"'disk_total'"
op|','
string|"'disk_processed'"
op|','
string|"'disk_remaining'"
op|']'
newline|'\n'
nl|'\n'
comment|'# TODO(Shaohe Feng) we should share the in-progress list.'
nl|'\n'
name|'live_migration_in_progress'
op|'='
op|'['
string|"'queued'"
op|','
string|"'preparing'"
op|','
nl|'\n'
string|"'running'"
op|','
string|"'post-migrating'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Note(Shaohe Feng): We need to leverage the oslo.versionedobjects.'
nl|'\n'
comment|"# Then we can pass the target version to it's obj_to_primitive."
nl|'\n'
name|'objects'
op|'='
name|'obj_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'migrations_obj'
op|')'
newline|'\n'
name|'objects'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'objects'
name|'if'
name|'not'
name|'x'
op|'['
string|"'hidden'"
op|']'
op|']'
newline|'\n'
name|'for'
name|'obj'
name|'in'
name|'objects'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'obj'
op|'['
string|"'deleted'"
op|']'
newline|'\n'
name|'del'
name|'obj'
op|'['
string|"'deleted_at'"
op|']'
newline|'\n'
name|'del'
name|'obj'
op|'['
string|"'hidden'"
op|']'
newline|'\n'
name|'if'
string|"'memory_total'"
name|'in'
name|'obj'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'key'
name|'in'
name|'detail_keys'
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'obj'
op|'['
name|'key'
op|']'
newline|'\n'
comment|'# NOTE(Shaohe Feng) above version 2.23, add migration_type for all'
nl|'\n'
comment|'# kinds of migration, but we only add links just for in-progress'
nl|'\n'
comment|'# live-migration.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'add_link'
name|'and'
name|'obj'
op|'['
string|"'migration_type'"
op|']'
op|'=='
string|'"live-migration"'
name|'and'
op|'('
nl|'\n'
name|'obj'
op|'['
string|'"status"'
op|']'
name|'in'
name|'live_migration_in_progress'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'obj'
op|'['
string|'"links"'
op|']'
op|'='
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'_get_links'
op|'('
nl|'\n'
name|'req'
op|','
name|'obj'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|'%'
name|'obj'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'add_link'
name|'is'
name|'False'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'obj'
op|'['
string|"'migration_type'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'objects'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all migrations in progress."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|','
string|'"index"'
op|')'
newline|'\n'
name|'migrations'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_migrations'
op|'('
name|'context'
op|','
name|'req'
op|'.'
name|'GET'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.23'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'migrations'"
op|':'
name|'self'
op|'.'
name|'_output'
op|'('
name|'req'
op|','
name|'migrations'
op|','
name|'True'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'migrations'"
op|':'
name|'self'
op|'.'
name|'_output'
op|'('
name|'req'
op|','
name|'migrations'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Migrations
dedent|''
dedent|''
name|'class'
name|'Migrations'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provide data on migrations."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Migrations"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'MigrationsController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
