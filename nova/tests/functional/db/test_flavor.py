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
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api_models'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'flavor'
name|'as'
name|'flavor_obj'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
newline|'\n'
nl|'\n'
DECL|variable|fake_api_flavor
name|'fake_api_flavor'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'m1.foo'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
string|"'m1.foo'"
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'extra_specs'"
op|':'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
nl|'\n'
string|"'projects'"
op|':'
op|'['
string|"'project1'"
op|','
string|"'project2'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ForcedFlavor
name|'class'
name|'ForcedFlavor'
op|'('
name|'objects'
op|'.'
name|'Flavor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Flavor object that lets us create with things still in the main DB.\n\n    This is required for us to be able to test mixed scenarios.\n    """'
newline|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_ensure_migrated
name|'def'
name|'_ensure_migrated'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorObjectTestCase
dedent|''
dedent|''
name|'class'
name|'FlavorObjectTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|USES_DB_SELF
indent|'    '
name|'USES_DB_SELF'
op|'='
name|'True'
newline|'\n'
nl|'\n'
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
name|'FlavorObjectTestCase'
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
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake-user'"
op|','
string|"'fake-project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_main_flavors
dedent|''
name|'def'
name|'_delete_main_flavors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavors'
op|'='
name|'db_api'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'for'
name|'flavor'
name|'in'
name|'flavors'
op|':'
newline|'\n'
indent|'            '
name|'db_api'
op|'.'
name|'flavor_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'id'"
op|','
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure we find this in the API database'
nl|'\n'
name|'flavor2'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'_flavor_get_from_db'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|'.'
name|'id'
op|','
name|'flavor2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# Make sure we don't find it in the main database"
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'FlavorNotFoundByName'
op|','
nl|'\n'
name|'db'
op|'.'
name|'flavor_get_by_name'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'flavor_get_by_flavor_id'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_with_no_projects
dedent|''
name|'def'
name|'test_get_with_no_projects'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'fields'
op|'='
name|'dict'
op|'('
name|'fake_api_flavor'
op|','
name|'projects'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fields'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'flavor'
op|'.'
name|'projects'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_with_projects_and_specs
dedent|''
name|'def'
name|'test_get_with_projects_and_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_api_flavor'
op|'['
string|"'projects'"
op|']'
op|','
name|'flavor'
op|'.'
name|'projects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_api_flavor'
op|'['
string|"'extra_specs'"
op|']'
op|','
name|'flavor'
op|'.'
name|'extra_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_query
dedent|''
name|'def'
name|'_test_query'
op|'('
name|'self'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor2'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|'.'
name|'id'
op|','
name|'flavor2'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'flavor2'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|'.'
name|'id'
op|','
name|'flavor2'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'flavor2'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|'.'
name|'id'
op|','
name|'flavor2'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_query_api
dedent|''
name|'def'
name|'test_query_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_query'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_query_main
dedent|''
name|'def'
name|'test_query_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_query'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_save
dedent|''
name|'def'
name|'_test_save'
op|'('
name|'self'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
string|"'marty'"
op|']'
op|'='
string|"'mcfly'"
newline|'\n'
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
string|"'foo'"
op|']'
op|'='
string|"'bart'"
newline|'\n'
name|'projects'
op|'='
name|'list'
op|'('
name|'flavor'
op|'.'
name|'projects'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'projects'
op|'.'
name|'append'
op|'('
string|"'project3'"
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'flavor2'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'marty'"
op|':'
string|"'mcfly'"
op|','
string|"'foo'"
op|':'
string|"'bart'"
op|'}'
op|','
nl|'\n'
name|'flavor2'
op|'.'
name|'extra_specs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'projects'
op|'+'
op|'['
string|"'project3'"
op|']'
op|')'
op|','
name|'set'
op|'('
name|'flavor'
op|'.'
name|'projects'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'del'
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
string|"'foo'"
op|']'
newline|'\n'
name|'del'
name|'flavor'
op|'.'
name|'projects'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'flavor2'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'marty'"
op|':'
string|"'mcfly'"
op|'}'
op|','
name|'flavor2'
op|'.'
name|'extra_specs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'projects'
op|')'
op|','
name|'set'
op|'('
name|'flavor2'
op|'.'
name|'projects'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_api
dedent|''
name|'def'
name|'test_save_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_save'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_main
dedent|''
name|'def'
name|'test_save_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_save'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'db_api'
op|'.'
name|'api_context_manager'
op|'.'
name|'reader'
newline|'\n'
DECL|member|_collect_flavor_residue_api
name|'def'
name|'_collect_flavor_residue_api'
op|'('
name|'context'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavors'
op|'='
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'Flavors'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'flavor'
op|'.'
name|'id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
name|'specs'
op|'='
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'FlavorExtraSpecs'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'flavor_id'
op|'='
name|'flavor'
op|'.'
name|'id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
name|'projects'
op|'='
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'FlavorProjects'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'flavor_id'
op|'='
name|'flavor'
op|'.'
name|'id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'len'
op|'('
name|'flavors'
op|')'
op|'+'
name|'len'
op|'('
name|'specs'
op|')'
op|'+'
name|'len'
op|'('
name|'projects'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_destroy
dedent|''
name|'def'
name|'_test_destroy'
op|'('
name|'self'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_name'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_api
dedent|''
name|'def'
name|'test_destroy_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_destroy'
op|'('
name|'flavor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
number|'0'
op|','
name|'self'
op|'.'
name|'_collect_flavor_residue_api'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_main
dedent|''
name|'def'
name|'test_destroy_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_destroy'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_missing_flavor_by_name
dedent|''
name|'def'
name|'test_destroy_missing_flavor_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
name|'name'
op|'='
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'FlavorNotFoundByName'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'destroy'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_missing_flavor_by_id
dedent|''
name|'def'
name|'test_destroy_missing_flavor_by_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
name|'name'
op|'='
string|"'foo'"
op|','
name|'id'
op|'='
number|'1234'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'flavor'
op|'.'
name|'destroy'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_get_all
dedent|''
name|'def'
name|'_test_get_all'
op|'('
name|'self'
op|','
name|'expect_len'
op|','
name|'marker'
op|'='
name|'None'
op|','
name|'limit'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavors'
op|'='
name|'objects'
op|'.'
name|'FlavorList'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'marker'
op|'='
name|'marker'
op|','
nl|'\n'
name|'limit'
op|'='
name|'limit'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expect_len'
op|','
name|'len'
op|'('
name|'flavors'
op|')'
op|')'
newline|'\n'
name|'return'
name|'flavors'
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
name|'expect_len'
op|'='
name|'len'
op|'('
name|'db_api'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_get_all'
op|'('
name|'expect_len'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_with_some_api_flavors
dedent|''
name|'def'
name|'test_get_all_with_some_api_flavors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expect_len'
op|'='
name|'len'
op|'('
name|'db_api'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_get_all'
op|'('
name|'expect_len'
op|'+'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_with_all_api_flavors
dedent|''
name|'def'
name|'test_get_all_with_all_api_flavors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavors'
op|'='
name|'db_api'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'for'
name|'flavor'
name|'in'
name|'db_flavors'
op|':'
newline|'\n'
indent|'            '
name|'db_api'
op|'.'
name|'flavor_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_get_all'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_with_marker_in_api
dedent|''
name|'def'
name|'test_get_all_with_marker_in_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavors'
op|'='
name|'db_api'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'db_flavor_ids'
op|'='
op|'['
name|'x'
op|'['
string|"'flavorid'"
op|']'
name|'for'
name|'x'
name|'in'
name|'db_flavors'
op|']'
newline|'\n'
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'fake_flavor2'
op|'='
name|'dict'
op|'('
name|'fake_api_flavor'
op|','
name|'name'
op|'='
string|"'m1.zoo'"
op|','
name|'flavorid'
op|'='
string|"'m1.zoo'"
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_flavor2'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_test_get_all'
op|'('
number|'3'
op|','
name|'marker'
op|'='
string|"'m1.foo'"
op|','
name|'limit'
op|'='
number|'3'
op|')'
newline|'\n'
name|'result_flavorids'
op|'='
op|'['
name|'x'
op|'.'
name|'flavorid'
name|'for'
name|'x'
name|'in'
name|'result'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'m1.zoo'"
op|']'
op|'+'
name|'db_flavor_ids'
op|'['
op|':'
number|'2'
op|']'
op|','
name|'result_flavorids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_with_marker_in_main
dedent|''
name|'def'
name|'test_get_all_with_marker_in_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavors'
op|'='
name|'db_api'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'db_flavor_ids'
op|'='
op|'['
name|'x'
op|'['
string|"'flavorid'"
op|']'
name|'for'
name|'x'
name|'in'
name|'db_flavors'
op|']'
newline|'\n'
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'fake_flavor2'
op|'='
name|'dict'
op|'('
name|'fake_api_flavor'
op|','
name|'name'
op|'='
string|"'m1.zoo'"
op|','
name|'flavorid'
op|'='
string|"'m1.zoo'"
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_flavor2'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_test_get_all'
op|'('
number|'2'
op|','
name|'marker'
op|'='
string|"'3'"
op|','
name|'limit'
op|'='
number|'3'
op|')'
newline|'\n'
name|'result_flavorids'
op|'='
op|'['
name|'x'
op|'.'
name|'flavorid'
name|'for'
name|'x'
name|'in'
name|'result'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_flavor_ids'
op|'['
number|'3'
op|':'
op|']'
op|','
name|'result_flavorids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_with_marker_in_neither
dedent|''
name|'def'
name|'test_get_all_with_marker_in_neither'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'fake_flavor2'
op|'='
name|'dict'
op|'('
name|'fake_api_flavor'
op|','
name|'name'
op|'='
string|"'m1.zoo'"
op|','
name|'flavorid'
op|'='
string|"'m1.zoo'"
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'ForcedFlavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_flavor2'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'MarkerNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_get_all'
op|','
number|'2'
op|','
name|'marker'
op|'='
string|"'noflavoratall'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_checks_main_flavors
dedent|''
name|'def'
name|'test_create_checks_main_flavors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'fake_api_flavor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'flavor'
op|'.'
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_delete_main_flavors'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorMigrationTestCase
dedent|''
dedent|''
name|'class'
name|'FlavorMigrationTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|USES_DB_SELF
indent|'    '
name|'USES_DB_SELF'
op|'='
name|'True'
newline|'\n'
nl|'\n'
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
name|'FlavorMigrationTestCase'
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
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
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
nl|'\n'
DECL|member|test_migration
dedent|''
name|'def'
name|'test_migration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'main_flavors'
op|'='
name|'len'
op|'('
name|'db'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'match'
op|','
name|'done'
op|'='
name|'flavor_obj'
op|'.'
name|'migrate_flavors'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'50'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'main_flavors'
op|','
name|'match'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'main_flavors'
op|','
name|'done'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'db'
op|'.'
name|'flavor_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'main_flavors'
op|','
nl|'\n'
name|'len'
op|'('
name|'objects'
op|'.'
name|'FlavorList'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_flavor_reset_autoincrement
dedent|''
name|'def'
name|'test_migrate_flavor_reset_autoincrement'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Not much we can do here other than just make'
nl|'\n'
comment|'# sure that the non-postgres case does not explode.'
nl|'\n'
indent|'        '
name|'match'
op|','
name|'done'
op|'='
name|'flavor_obj'
op|'.'
name|'migrate_flavor_reset_autoincrement'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'match'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'done'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
