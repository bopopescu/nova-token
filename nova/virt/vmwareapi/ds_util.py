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
string|'"""\nDatastore utility functions\n"""'
newline|'\n'
name|'import'
name|'posixpath'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
name|'vm_util'
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
DECL|class|DatastorePath
name|'class'
name|'DatastorePath'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for representing a directory or file path in a vSphere datatore.\n\n    This provides various helper methods to access components and useful\n    variants of the datastore path.\n\n    Example usage:\n\n    DatastorePath("datastore1", "_base/foo", "foo.vmdk") creates an\n    object that describes the "[datastore1] _base/foo/foo.vmdk" datastore\n    file path to a virtual disk.\n\n    Note:\n    - Datastore path representations always uses forward slash as separator\n      (hence the use of the posixpath module).\n    - Datastore names are enclosed in square brackets.\n    - Path part of datastore path is relative to the root directory\n      of the datastore, and is always separated from the [ds_name] part with\n      a single space.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|VMDK_EXTENSION
name|'VMDK_EXTENSION'
op|'='
string|'"vmdk"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'datastore_name'
op|','
op|'*'
name|'paths'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'datastore_name'
name|'is'
name|'None'
name|'or'
name|'datastore_name'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"datastore name empty"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_datastore_name'
op|'='
name|'datastore_name'
newline|'\n'
name|'self'
op|'.'
name|'_rel_path'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'paths'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'None'
name|'in'
name|'paths'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"path component cannot be None"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_rel_path'
op|'='
name|'posixpath'
op|'.'
name|'join'
op|'('
op|'*'
name|'paths'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Full datastore path to the file or directory."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_rel_path'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"[%s] %s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_datastore_name'
op|','
name|'self'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"[%s]"'
op|'%'
name|'self'
op|'.'
name|'_datastore_name'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|datastore
name|'def'
name|'datastore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_datastore_name'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|parent
name|'def'
name|'parent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'DatastorePath'
op|'('
name|'self'
op|'.'
name|'datastore'
op|','
name|'posixpath'
op|'.'
name|'dirname'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|basename
name|'def'
name|'basename'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'posixpath'
op|'.'
name|'basename'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|dirname
name|'def'
name|'dirname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'posixpath'
op|'.'
name|'dirname'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|rel_path
name|'def'
name|'rel_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_rel_path'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|parse
name|'def'
name|'parse'
op|'('
name|'cls'
op|','
name|'datastore_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs a DatastorePath object given a datastore path string."""'
newline|'\n'
name|'if'
name|'not'
name|'datastore_path'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"datastore path empty"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'spl'
op|'='
name|'datastore_path'
op|'.'
name|'split'
op|'('
string|"'['"
op|','
number|'1'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'split'
op|'('
string|"']'"
op|','
number|'1'
op|')'
newline|'\n'
name|'path'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'spl'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'datastore_name'
op|'='
name|'spl'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'datastore_name'
op|','
name|'path'
op|'='
name|'spl'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'('
name|'datastore_name'
op|','
name|'path'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_datastore_path
dedent|''
dedent|''
name|'def'
name|'build_datastore_path'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build the datastore compliant path."""'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'DatastorePath'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_delete
dedent|''
name|'def'
name|'file_delete'
op|'('
name|'session'
op|','
name|'datastore_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Deleting the datastore file %s"'
op|','
name|'datastore_path'
op|')'
newline|'\n'
name|'vim'
op|'='
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
newline|'\n'
name|'file_delete_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"DeleteDatastoreFile_Task"'
op|','
nl|'\n'
name|'vim'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'fileManager'
op|','
nl|'\n'
name|'name'
op|'='
name|'datastore_path'
op|','
nl|'\n'
name|'datacenter'
op|'='
name|'dc_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'file_delete_task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Deleted the datastore file"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_move
dedent|''
name|'def'
name|'file_move'
op|'('
name|'session'
op|','
name|'dc_ref'
op|','
name|'src_file'
op|','
name|'dst_file'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Moves the source file or folder to the destination.\n\n    The list of possible faults that the server can return on error\n    include:\n    - CannotAccessFile: Thrown if the source file or folder cannot be\n                        moved because of insufficient permissions.\n    - FileAlreadyExists: Thrown if a file with the given name already\n                         exists at the destination.\n    - FileFault: Thrown if there is a generic file error\n    - FileLocked: Thrown if the source file or folder is currently\n                  locked or in use.\n    - FileNotFound: Thrown if the file or folder specified by sourceName\n                    is not found.\n    - InvalidDatastore: Thrown if the operation cannot be performed on\n                        the source or destination datastores.\n    - NoDiskSpace: Thrown if there is not enough space available on the\n                   destination datastore.\n    - RuntimeFault: Thrown if any type of runtime fault is thrown that\n                    is not covered by the other faults; for example,\n                    a communication error.\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Moving file from %(src)s to %(dst)s."'
op|','
nl|'\n'
op|'{'
string|"'src'"
op|':'
name|'src_file'
op|','
string|"'dst'"
op|':'
name|'dst_file'
op|'}'
op|')'
newline|'\n'
name|'vim'
op|'='
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
newline|'\n'
name|'move_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"MoveDatastoreFile_Task"'
op|','
nl|'\n'
name|'vim'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'fileManager'
op|','
nl|'\n'
name|'sourceName'
op|'='
name|'src_file'
op|','
nl|'\n'
name|'sourceDatacenter'
op|'='
name|'dc_ref'
op|','
nl|'\n'
name|'destinationName'
op|'='
name|'dst_file'
op|','
nl|'\n'
name|'destinationDatacenter'
op|'='
name|'dc_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'move_task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"File moved"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_exists
dedent|''
name|'def'
name|'file_exists'
op|'('
name|'session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|','
name|'file_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if the file exists on the datastore."""'
newline|'\n'
name|'client_factory'
op|'='
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'search_spec'
op|'='
name|'vm_util'
op|'.'
name|'search_datastore_spec'
op|'('
name|'client_factory'
op|','
name|'file_name'
op|')'
newline|'\n'
name|'search_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"SearchDatastore_Task"'
op|','
nl|'\n'
name|'ds_browser'
op|','
nl|'\n'
name|'datastorePath'
op|'='
name|'ds_path'
op|','
nl|'\n'
name|'searchSpec'
op|'='
name|'search_spec'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'task_info'
op|'='
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'search_task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'FileNotFoundException'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'file_exists'
op|'='
op|'('
name|'getattr'
op|'('
name|'task_info'
op|'.'
name|'result'
op|','
string|"'file'"
op|','
name|'False'
op|')'
name|'and'
nl|'\n'
name|'task_info'
op|'.'
name|'result'
op|'.'
name|'file'
op|'['
number|'0'
op|']'
op|'.'
name|'path'
op|'=='
name|'file_name'
op|')'
newline|'\n'
name|'return'
name|'file_exists'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkdir
dedent|''
name|'def'
name|'mkdir'
op|'('
name|'session'
op|','
name|'ds_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a directory at the path specified. If it is just "NAME",\n    then a directory with this name is created at the topmost level of the\n    DataStore.\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating directory with path %s"'
op|','
name|'ds_path'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
string|'"MakeDirectory"'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'fileManager'
op|','
nl|'\n'
name|'name'
op|'='
name|'ds_path'
op|','
name|'datacenter'
op|'='
name|'dc_ref'
op|','
nl|'\n'
name|'createParentDirectories'
op|'='
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Created directory with path %s"'
op|','
name|'ds_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_sub_folders
dedent|''
name|'def'
name|'get_sub_folders'
op|'('
name|'session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a set of subfolders for a path on a datastore.\n\n    If the path does not exist then an empty set is returned.\n    """'
newline|'\n'
name|'search_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"SearchDatastore_Task"'
op|','
nl|'\n'
name|'ds_browser'
op|','
nl|'\n'
name|'datastorePath'
op|'='
name|'ds_path'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'task_info'
op|'='
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'search_task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'FileNotFoundException'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'set'
op|'('
op|')'
newline|'\n'
comment|'# populate the folder entries'
nl|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'task_info'
op|'.'
name|'result'
op|','
string|"'file'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'set'
op|'('
op|'['
name|'file'
op|'.'
name|'path'
name|'for'
name|'file'
name|'in'
name|'task_info'
op|'.'
name|'result'
op|'.'
name|'file'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'set'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
