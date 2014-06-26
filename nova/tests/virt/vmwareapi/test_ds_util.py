begin_unit
comment|'# Copyright (c) 2014 VMware, Inc.'
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
name|'contextlib'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'ds_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_session
name|'class'
name|'fake_session'
op|'('
name|'object'
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
name|'ret'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ret'
op|'='
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|_get_vim
dedent|''
name|'def'
name|'_get_vim'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake'
op|'.'
name|'FakeVim'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_call_method
dedent|''
name|'def'
name|'_call_method'
op|'('
name|'self'
op|','
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|_wait_for_task
dedent|''
name|'def'
name|'_wait_for_task'
op|'('
name|'self'
op|','
name|'task_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'task_info'
op|'='
name|'self'
op|'.'
name|'_call_method'
op|'('
string|"'module'"
op|','
string|'"get_dynamic_property"'
op|','
nl|'\n'
name|'task_ref'
op|','
string|'"Task"'
op|','
string|'"info"'
op|')'
newline|'\n'
name|'if'
name|'task_info'
op|'.'
name|'state'
op|'=='
string|"'success'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'task_info'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'error_info'
op|'='
string|"'fake error'"
newline|'\n'
name|'error'
op|'='
name|'task_info'
op|'.'
name|'error'
newline|'\n'
name|'name'
op|'='
name|'error'
op|'.'
name|'fault'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'raise'
name|'error_util'
op|'.'
name|'get_fault_class'
op|'('
name|'name'
op|')'
op|'('
name|'error_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DsUtilTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'DsUtilTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
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
name|'DsUtilTestCase'
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
name|'session'
op|'='
name|'fake_session'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'api_retry_count'
op|'='
number|'1'
op|','
name|'group'
op|'='
string|"'vmware'"
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
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
indent|'        '
name|'super'
op|'('
name|'DsUtilTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_build_datastore_path
dedent|''
name|'def'
name|'test_build_datastore_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'ds_util'
op|'.'
name|'build_datastore_path'
op|'('
string|"'ds'"
op|','
string|"'folder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[ds] folder'"
op|','
name|'path'
op|')'
newline|'\n'
name|'path'
op|'='
name|'ds_util'
op|'.'
name|'build_datastore_path'
op|'('
string|"'ds'"
op|','
string|"'folder/file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[ds] folder/file'"
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_file_delete
dedent|''
name|'def'
name|'test_file_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'DeleteDatastoreFile_Task'"
op|','
name|'method'
op|')'
newline|'\n'
name|'name'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-datastore-path'"
op|','
name|'name'
op|')'
newline|'\n'
name|'datacenter'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'datacenter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-dc-ref'"
op|','
name|'datacenter'
op|')'
newline|'\n'
name|'return'
string|"'fake_delete_task'"
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_wait_for_task'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_wait_for_task'
op|','
name|'_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ds_util'
op|'.'
name|'file_delete'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake-datastore-path'"
op|','
string|"'fake-dc-ref'"
op|')'
newline|'\n'
name|'_wait_for_task'
op|'.'
name|'assert_has_calls'
op|'('
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'fake_delete_task'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_file_move
dedent|''
dedent|''
name|'def'
name|'test_file_move'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'MoveDatastoreFile_Task'"
op|','
name|'method'
op|')'
newline|'\n'
name|'sourceName'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'sourceName'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[ds] tmp/src'"
op|','
name|'sourceName'
op|')'
newline|'\n'
name|'destinationName'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'destinationName'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[ds] base/dst'"
op|','
name|'destinationName'
op|')'
newline|'\n'
name|'sourceDatacenter'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'sourceDatacenter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-dc-ref'"
op|','
name|'sourceDatacenter'
op|')'
newline|'\n'
name|'destinationDatacenter'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'destinationDatacenter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-dc-ref'"
op|','
name|'destinationDatacenter'
op|')'
newline|'\n'
name|'return'
string|"'fake_move_task'"
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_wait_for_task'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_wait_for_task'
op|','
name|'_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ds_util'
op|'.'
name|'file_move'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake-dc-ref'"
op|','
string|"'[ds] tmp/src'"
op|','
string|"'[ds] base/dst'"
op|')'
newline|'\n'
name|'_wait_for_task'
op|'.'
name|'assert_has_calls'
op|'('
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'fake_move_task'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mkdir
dedent|''
dedent|''
name|'def'
name|'test_mkdir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'MakeDirectory'"
op|','
name|'method'
op|')'
newline|'\n'
name|'name'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-path'"
op|','
name|'name'
op|')'
newline|'\n'
name|'datacenter'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'datacenter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-dc-ref'"
op|','
name|'datacenter'
op|')'
newline|'\n'
name|'createParentDirectories'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'createParentDirectories'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'createParentDirectories'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ds_util'
op|'.'
name|'mkdir'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fake-path'"
op|','
string|"'fake-dc-ref'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_file_exists
dedent|''
dedent|''
name|'def'
name|'test_file_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'SearchDatastore_Task'"
op|':'
newline|'\n'
indent|'                '
name|'ds_browser'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-browser'"
op|','
name|'ds_browser'
op|')'
newline|'\n'
name|'datastorePath'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'datastorePath'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-path'"
op|','
name|'datastorePath'
op|')'
newline|'\n'
name|'return'
string|"'fake_exists_task'"
newline|'\n'
dedent|''
name|'elif'
name|'method'
op|'=='
string|"'get_dynamic_property'"
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'info'
op|'.'
name|'name'
op|'='
string|"'search_task'"
newline|'\n'
name|'info'
op|'.'
name|'state'
op|'='
string|"'success'"
newline|'\n'
name|'result'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'result'
op|'.'
name|'path'
op|'='
string|"'fake-path'"
newline|'\n'
name|'matched'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'matched'
op|'.'
name|'path'
op|'='
string|"'fake-file'"
newline|'\n'
name|'result'
op|'.'
name|'file'
op|'='
op|'['
name|'matched'
op|']'
newline|'\n'
name|'info'
op|'.'
name|'result'
op|'='
name|'result'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
comment|'# Should never get here'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fail'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'file_exists'
op|'='
name|'ds_util'
op|'.'
name|'file_exists'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake-browser'"
op|','
string|"'fake-path'"
op|','
string|"'fake-file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'file_exists'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_file_exists_fails
dedent|''
dedent|''
name|'def'
name|'test_file_exists_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'SearchDatastore_Task'"
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'fake_exists_task'"
newline|'\n'
dedent|''
name|'elif'
name|'method'
op|'=='
string|"'get_dynamic_property'"
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'info'
op|'.'
name|'name'
op|'='
string|"'search_task'"
newline|'\n'
name|'info'
op|'.'
name|'state'
op|'='
string|"'error'"
newline|'\n'
name|'error'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'error'
op|'.'
name|'localizedMessage'
op|'='
string|'"Error message"'
newline|'\n'
name|'error'
op|'.'
name|'fault'
op|'='
name|'fake'
op|'.'
name|'FileNotFound'
op|'('
op|')'
newline|'\n'
name|'info'
op|'.'
name|'error'
op|'='
name|'error'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
comment|'# Should never get here'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fail'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'file_exists'
op|'='
name|'ds_util'
op|'.'
name|'file_exists'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake-browser'"
op|','
string|"'fake-path'"
op|','
string|"'fake-file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'file_exists'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DatastorePathTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'DatastorePathTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path
indent|'    '
name|'def'
name|'test_ds_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
string|"'dsname'"
op|','
string|"'a/b/c'"
op|','
string|"'file.iso'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[dsname] a/b/c/file.iso'"
op|','
name|'str'
op|'('
name|'p'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'a/b/c/file.iso'"
op|','
name|'p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'a/b/c'"
op|','
name|'p'
op|'.'
name|'parent'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[dsname] a/b/c'"
op|','
name|'str'
op|'('
name|'p'
op|'.'
name|'parent'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'dsname'"
op|','
name|'p'
op|'.'
name|'datastore'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'file.iso'"
op|','
name|'p'
op|'.'
name|'basename'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'a/b/c'"
op|','
name|'p'
op|'.'
name|'dirname'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_no_ds_name
dedent|''
name|'def'
name|'test_ds_path_no_ds_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_args'
op|'='
op|'['
nl|'\n'
op|'('
string|"''"
op|','
op|'['
string|"'a/b/c'"
op|','
string|"'file.iso'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
name|'None'
op|','
op|'['
string|"'a/b/c'"
op|','
string|"'file.iso'"
op|']'
op|')'
op|']'
newline|'\n'
name|'for'
name|'t'
name|'in'
name|'bad_args'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'ValueError'
op|','
name|'ds_util'
op|'.'
name|'DatastorePath'
op|','
nl|'\n'
name|'t'
op|'['
number|'0'
op|']'
op|','
op|'*'
name|'t'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_invalid_path_components
dedent|''
dedent|''
name|'def'
name|'test_ds_path_invalid_path_components'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_args'
op|'='
op|'['
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"''"
op|','
name|'None'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a'"
op|','
name|'None'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a'"
op|','
name|'None'
op|','
string|"'b'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
name|'None'
op|','
string|"''"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
name|'None'
op|','
string|"'b'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'t'
name|'in'
name|'bad_args'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'ValueError'
op|','
name|'ds_util'
op|'.'
name|'DatastorePath'
op|','
nl|'\n'
name|'t'
op|'['
number|'0'
op|']'
op|','
op|'*'
name|'t'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_no_subdir
dedent|''
dedent|''
name|'def'
name|'test_ds_path_no_subdir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"''"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'x.vmdk'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'canonical_p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
string|"'dsname'"
op|','
string|"'x.vmdk'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[dsname] x.vmdk'"
op|','
name|'str'
op|'('
name|'canonical_p'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'canonical_p'
op|'.'
name|'dirname'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'x.vmdk'"
op|','
name|'canonical_p'
op|'.'
name|'basename'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'x.vmdk'"
op|','
name|'canonical_p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
name|'for'
name|'t'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
name|'t'
op|'['
number|'0'
op|']'
op|','
op|'*'
name|'t'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'canonical_p'
op|')'
op|','
name|'str'
op|'('
name|'p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_ds_only
dedent|''
dedent|''
name|'def'
name|'test_ds_path_ds_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"''"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"''"
op|','
string|"''"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'canonical_p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
string|"'dsname'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[dsname]'"
op|','
name|'str'
op|'('
name|'canonical_p'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'canonical_p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'canonical_p'
op|'.'
name|'basename'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'canonical_p'
op|'.'
name|'dirname'
op|')'
newline|'\n'
name|'for'
name|'t'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
name|'t'
op|'['
number|'0'
op|']'
op|','
op|'*'
name|'t'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'canonical_p'
op|')'
op|','
name|'str'
op|'('
name|'p'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'canonical_p'
op|'.'
name|'rel_path'
op|','
name|'p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_equivalence
dedent|''
dedent|''
name|'def'
name|'test_ds_path_equivalence'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/b/c/'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/'"
op|','
string|"'b/c/'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a'"
op|','
string|"'b'"
op|','
string|"'c'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/b/c'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'canonical_p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
string|"'dsname'"
op|','
string|"'a/b/c'"
op|','
string|"'x.vmdk'"
op|')'
newline|'\n'
name|'for'
name|'t'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
name|'t'
op|'['
number|'0'
op|']'
op|','
op|'*'
name|'t'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'canonical_p'
op|')'
op|','
name|'str'
op|'('
name|'p'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'canonical_p'
op|'.'
name|'datastore'
op|','
name|'p'
op|'.'
name|'datastore'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'canonical_p'
op|'.'
name|'rel_path'
op|','
name|'p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'canonical_p'
op|'.'
name|'parent'
op|')'
op|','
name|'str'
op|'('
name|'p'
op|'.'
name|'parent'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_non_equivalence
dedent|''
dedent|''
name|'def'
name|'test_ds_path_non_equivalence'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
nl|'\n'
comment|'# leading slash'
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'/a'"
op|','
string|"'b'"
op|','
string|"'c'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'/a/b/c/'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/b/c'"
op|','
string|"'/x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
comment|'# leading space'
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/b/c/'"
op|','
string|"' x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/'"
op|','
string|"' b/c/'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"' a'"
op|','
string|"'b'"
op|','
string|"'c'"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|','
nl|'\n'
comment|'# trailing space'
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'/a/b/c/'"
op|','
string|"'x.vmdk '"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dsname'"
op|','
op|'['
string|"'a/b/c/ '"
op|','
string|"'x.vmdk'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'canonical_p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
string|"'dsname'"
op|','
string|"'a/b/c'"
op|','
string|"'x.vmdk'"
op|')'
newline|'\n'
name|'for'
name|'t'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'('
name|'t'
op|'['
number|'0'
op|']'
op|','
op|'*'
name|'t'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'str'
op|'('
name|'canonical_p'
op|')'
op|','
name|'str'
op|'('
name|'p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ds_path_parse
dedent|''
dedent|''
name|'def'
name|'test_ds_path_parse'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'.'
name|'parse'
op|'('
string|"'[dsname]'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'dsname'"
op|','
name|'p'
op|'.'
name|'datastore'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
nl|'\n'
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'.'
name|'parse'
op|'('
string|"'[dsname] folder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'dsname'"
op|','
name|'p'
op|'.'
name|'datastore'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'folder'"
op|','
name|'p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
nl|'\n'
name|'p'
op|'='
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'.'
name|'parse'
op|'('
string|"'[dsname] folder/file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'dsname'"
op|','
name|'p'
op|'.'
name|'datastore'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'folder/file'"
op|','
name|'p'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'p'
name|'in'
op|'['
name|'None'
op|','
string|"''"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'.'
name|'parse'
op|','
name|'p'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'p'
name|'in'
op|'['
string|"'bad path'"
op|','
string|"'/a/b/c'"
op|','
string|"'a/b/c'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'IndexError'
op|','
name|'ds_util'
op|'.'
name|'DatastorePath'
op|'.'
name|'parse'
op|','
name|'p'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
