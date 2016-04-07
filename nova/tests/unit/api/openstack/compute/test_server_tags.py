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
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'extension_info'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'server_tags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'servers'
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
name|'import'
name|'exception'
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
name|'tag'
name|'as'
name|'tag_obj'
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
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
DECL|variable|UUID
name|'UUID'
op|'='
string|"'b48316c5-71e8-45e4-9884-6c78055b9b13'"
newline|'\n'
DECL|variable|TAG1
name|'TAG1'
op|'='
string|"'tag1'"
newline|'\n'
DECL|variable|TAG2
name|'TAG2'
op|'='
string|"'tag2'"
newline|'\n'
DECL|variable|TAG3
name|'TAG3'
op|'='
string|"'tag3'"
newline|'\n'
DECL|variable|TAGS
name|'TAGS'
op|'='
op|'['
name|'TAG1'
op|','
name|'TAG2'
op|','
name|'TAG3'
op|']'
newline|'\n'
DECL|variable|NON_EXISTING_UUID
name|'NON_EXISTING_UUID'
op|'='
string|"'123'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerTagsTest
name|'class'
name|'ServerTagsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|api_version
indent|'    '
name|'api_version'
op|'='
string|"'2.26'"
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
name|'ServerTagsTest'
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
name|'controller'
op|'='
name|'server_tags'
op|'.'
name|'ServerTagsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_tag
dedent|''
name|'def'
name|'_get_tag'
op|'('
name|'self'
op|','
name|'tag_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tag'
op|'='
name|'models'
op|'.'
name|'Tag'
op|'('
op|')'
newline|'\n'
name|'tag'
op|'.'
name|'tag'
op|'='
name|'tag_name'
newline|'\n'
name|'tag'
op|'.'
name|'resource_id'
op|'='
name|'UUID'
newline|'\n'
name|'return'
name|'tag'
newline|'\n'
nl|'\n'
DECL|member|_get_request
dedent|''
name|'def'
name|'_get_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'method'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
name|'version'
op|'='
name|'self'
op|'.'
name|'api_version'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
name|'method'
newline|'\n'
name|'return'
name|'request'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_exists'"
op|')'
newline|'\n'
DECL|member|test_show
name|'def'
name|'test_show'
op|'('
name|'self'
op|','
name|'mock_exists'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_exists'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG1'
op|')'
op|','
string|"'GET'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'UUID'
op|','
name|'TAG1'
op|')'
newline|'\n'
name|'mock_exists'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|','
name|'TAG1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_index
name|'def'
name|'test_index'
op|'('
name|'self'
op|','
name|'mock_db_get_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_tags'
op|'='
op|'['
name|'self'
op|'.'
name|'_get_tag'
op|'('
name|'tag'
op|')'
name|'for'
name|'tag'
name|'in'
name|'TAGS'
op|']'
newline|'\n'
name|'mock_db_get_inst_tags'
op|'.'
name|'return_value'
op|'='
name|'fake_tags'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'GET'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|','
name|'UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'TAGS'
op|','
name|'res'
op|'.'
name|'get'
op|'('
string|"'tags'"
op|')'
op|')'
newline|'\n'
name|'mock_db_get_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_set'"
op|')'
newline|'\n'
DECL|member|test_update_all
name|'def'
name|'test_update_all'
op|'('
name|'self'
op|','
name|'mock_db_set_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_tags'
op|'='
op|'['
name|'self'
op|'.'
name|'_get_tag'
op|'('
name|'tag'
op|')'
name|'for'
name|'tag'
name|'in'
name|'TAGS'
op|']'
newline|'\n'
name|'mock_db_set_inst_tags'
op|'.'
name|'return_value'
op|'='
name|'fake_tags'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|'('
name|'req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
op|'{'
string|"'tags'"
op|':'
name|'TAGS'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'TAGS'
op|','
name|'res'
op|'['
string|"'tags'"
op|']'
op|')'
newline|'\n'
name|'mock_db_set_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|','
name|'TAGS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_too_many_tags
dedent|''
name|'def'
name|'test_update_all_too_many_tags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_tags'
op|'='
op|'{'
string|"'tags'"
op|':'
op|'['
name|'str'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'MAX_TAG_COUNT'
op|'+'
number|'1'
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'fake_tags'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_forbidden_characters
dedent|''
name|'def'
name|'test_update_all_forbidden_characters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'for'
name|'tag'
name|'in'
op|'['
string|"'tag,1'"
op|','
string|"'tag/1'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
op|'{'
string|"'tags'"
op|':'
op|'['
name|'tag'
op|','
string|"'tag2'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_invalid_tag_type
dedent|''
dedent|''
name|'def'
name|'test_update_all_invalid_tag_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
op|'{'
string|"'tags'"
op|':'
op|'['
number|'1'
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_too_long_tag
dedent|''
name|'def'
name|'test_update_all_too_long_tag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'tag'
op|'='
string|'"a"'
op|'*'
op|'('
name|'tag_obj'
op|'.'
name|'MAX_TAG_LENGTH'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
op|'{'
string|"'tags'"
op|':'
op|'['
name|'tag'
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_invalid_tag_list_type
dedent|''
name|'def'
name|'test_update_all_invalid_tag_list_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'/v2/ake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
op|'{'
string|"'tags'"
op|':'
op|'{'
string|"'tag'"
op|':'
string|"'tag'"
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_exists'"
op|')'
newline|'\n'
DECL|member|test_show_non_existing_tag
name|'def'
name|'test_show_non_existing_tag'
op|'('
name|'self'
op|','
name|'mock_exists'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_exists'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG1'
op|')'
op|','
string|"'GET'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'TAG1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_add'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_update
name|'def'
name|'test_update'
op|'('
name|'self'
op|','
name|'mock_db_get_inst_tags'
op|','
name|'mock_db_add_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get_inst_tags'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'_get_tag'
op|'('
name|'TAG1'
op|')'
op|']'
newline|'\n'
name|'mock_db_add_inst_tags'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_get_tag'
op|'('
name|'TAG2'
op|')'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG2'
op|')'
newline|'\n'
name|'location'
op|'='
string|"'http://localhost'"
op|'+'
name|'url'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'url'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
name|'UUID'
op|','
name|'TAG2'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'201'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'location'
op|','
name|'res'
op|'.'
name|'headers'
op|'['
string|"'Location'"
op|']'
op|')'
newline|'\n'
name|'mock_db_add_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|','
name|'TAG2'
op|')'
newline|'\n'
name|'mock_db_get_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_update_existing_tag
name|'def'
name|'test_update_existing_tag'
op|'('
name|'self'
op|','
name|'mock_db_get_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get_inst_tags'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'_get_tag'
op|'('
name|'TAG1'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG1'
op|')'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
name|'UUID'
op|','
name|'TAG1'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'204'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'mock_db_get_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_update_tag_limit_exceed
name|'def'
name|'test_update_tag_limit_exceed'
op|'('
name|'self'
op|','
name|'mock_db_get_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_tags'
op|'='
op|'['
name|'self'
op|'.'
name|'_get_tag'
op|'('
name|'str'
op|'('
name|'i'
op|')'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'instance'
op|'.'
name|'MAX_TAG_COUNT'
op|')'
op|']'
newline|'\n'
name|'mock_db_get_inst_tags'
op|'.'
name|'return_value'
op|'='
name|'fake_tags'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG2'
op|')'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'TAG2'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_update_too_long_tag
name|'def'
name|'test_update_too_long_tag'
op|'('
name|'self'
op|','
name|'mock_db_get_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get_inst_tags'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'tag'
op|'='
string|'"a"'
op|'*'
op|'('
name|'tag_obj'
op|'.'
name|'MAX_TAG_LENGTH'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'tag'
op|')'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'tag'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_update_forbidden_characters
name|'def'
name|'test_update_forbidden_characters'
op|'('
name|'self'
op|','
name|'mock_db_get_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get_inst_tags'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'tag'
name|'in'
op|'['
string|"'tag,1'"
op|','
string|"'tag/1'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'tag'
op|')'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'tag'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_delete'"
op|')'
newline|'\n'
DECL|member|test_delete
name|'def'
name|'test_delete'
op|'('
name|'self'
op|','
name|'mock_db_delete_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG2'
op|')'
op|','
string|"'DELETE'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
name|'UUID'
op|','
name|'TAG2'
op|')'
newline|'\n'
name|'mock_db_delete_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|','
name|'TAG2'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_delete'"
op|')'
newline|'\n'
DECL|member|test_delete_non_existing_tag
name|'def'
name|'test_delete_non_existing_tag'
op|'('
name|'self'
op|','
name|'mock_db_delete_inst_tags'
op|')'
op|':'
newline|'\n'
DECL|function|fake_db_delete_tag
indent|'        '
name|'def'
name|'fake_db_delete_tag'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'tag'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'UUID'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'TAG1'
op|','
name|'tag'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceTagNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'tag'
op|'='
name|'tag'
op|')'
newline|'\n'
dedent|''
name|'mock_db_delete_inst_tags'
op|'.'
name|'side_effect'
op|'='
name|'fake_db_delete_tag'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'UUID'
op|','
name|'TAG1'
op|')'
op|','
string|"'DELETE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
name|'UUID'
op|','
name|'TAG1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_delete_all'"
op|')'
newline|'\n'
DECL|member|test_delete_all
name|'def'
name|'test_delete_all'
op|'('
name|'self'
op|','
name|'mock_db_delete_inst_tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'UUID'
op|','
string|"'DELETE'"
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete_all'
op|'('
name|'req'
op|','
name|'UUID'
op|')'
newline|'\n'
name|'mock_db_delete_inst_tags'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_non_existing_instance
dedent|''
name|'def'
name|'test_show_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'NON_EXISTING_UUID'
op|','
name|'TAG1'
op|')'
op|','
string|"'GET'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
nl|'\n'
name|'NON_EXISTING_UUID'
op|','
name|'TAG1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_with_details_information_non_existing_instance
dedent|''
name|'def'
name|'test_show_with_details_information_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s'"
op|'%'
name|'NON_EXISTING_UUID'
op|','
string|"'GET'"
op|')'
newline|'\n'
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'servers_controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'servers_controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
nl|'\n'
name|'NON_EXISTING_UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_non_existing_instance
dedent|''
name|'def'
name|'test_index_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'v2/fake/servers/%s/tags'"
op|'%'
name|'NON_EXISTING_UUID'
op|','
string|"'GET'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'req'
op|','
nl|'\n'
name|'NON_EXISTING_UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_non_existing_instance
dedent|''
name|'def'
name|'test_update_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'NON_EXISTING_UUID'
op|','
name|'TAG1'
op|')'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
nl|'\n'
name|'NON_EXISTING_UUID'
op|','
name|'TAG1'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_non_existing_instance
dedent|''
name|'def'
name|'test_update_all_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'NON_EXISTING_UUID'
op|','
string|"'PUT'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
name|'req'
op|','
nl|'\n'
name|'NON_EXISTING_UUID'
op|','
name|'body'
op|'='
op|'{'
string|"'tags'"
op|':'
name|'TAGS'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_non_existing_instance
dedent|''
name|'def'
name|'test_delete_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags/%s'"
op|'%'
op|'('
name|'NON_EXISTING_UUID'
op|','
name|'TAG1'
op|')'
op|','
nl|'\n'
string|"'DELETE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'req'
op|','
nl|'\n'
name|'NON_EXISTING_UUID'
op|','
name|'TAG1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_all_non_existing_instance
dedent|''
name|'def'
name|'test_delete_all_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
nl|'\n'
string|"'/v2/fake/servers/%s/tags'"
op|'%'
name|'NON_EXISTING_UUID'
op|','
string|"'DELETE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete_all'
op|','
nl|'\n'
name|'req'
op|','
name|'NON_EXISTING_UUID'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
