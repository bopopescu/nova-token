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
string|'"""\nImage cache class\n\nImages that are stored in the cache folder will be stored in a folder whose\nname is the image ID. In the event that an image is discovered to be no longer\nused then a timestamp will be added to the image folder.\nThe timestamp will be a folder - this is due to the fact that we can use the\nVMware API\'s for creating and deleting of folders (it really simplifies\nthings). The timestamp will contain the time, on the compute node, when the\nimage was first seen to be unused.\nAt each aging iteration we check if the image can be aged.\nThis is done by comparing the current nova compute time to the time embedded\nin the timestamp. If the time exceeds the configured aging time then\nthe parent folder, that is the image ID folder, will be deleted.\nThat effectively ages the cached image.\nIf an image is used then the timestamps will be deleted.\n\nWhen accessing a timestamp we make use of locking. This ensure that aging\nwill not delete an image during the spawn operation. When spawning\nthe timestamp folder will be locked  and the timestamps will be purged.\nThis will ensure that a image is not deleted during the spawn.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'vmware'
name|'import'
name|'exceptions'
name|'as'
name|'vexc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
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
name|'lockutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'imagecache'
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
name|'vim_util'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'remove_unused_original_minimum_age_seconds'"
op|','
nl|'\n'
string|"'nova.virt.imagecache'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|TIMESTAMP_PREFIX
name|'TIMESTAMP_PREFIX'
op|'='
string|"'ts-'"
newline|'\n'
DECL|variable|TIMESTAMP_FORMAT
name|'TIMESTAMP_FORMAT'
op|'='
string|"'%Y-%m-%d-%H-%M-%S'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCacheManager
name|'class'
name|'ImageCacheManager'
op|'('
name|'imagecache'
op|'.'
name|'ImageCacheManager'
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
name|'session'
op|','
name|'base_folder'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ImageCacheManager'
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
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'_base_folder'
op|'='
name|'base_folder'
newline|'\n'
name|'self'
op|'.'
name|'_ds_browser'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_folder_delete
dedent|''
name|'def'
name|'_folder_delete'
op|'('
name|'self'
op|','
name|'ds_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ds_util'
op|'.'
name|'file_delete'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'ds_path'
op|','
name|'dc_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'vexc'
op|'.'
name|'CannotDeleteFileException'
op|','
nl|'\n'
name|'vexc'
op|'.'
name|'FileFaultException'
op|','
nl|'\n'
name|'vexc'
op|'.'
name|'FileLockedException'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
comment|'# There may be more than one process or thread that tries'
nl|'\n'
comment|'# to delete the file.'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Unable to delete %(file)s. Exception: %(ex)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'file'"
op|':'
name|'ds_path'
op|','
string|"'ex'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'vexc'
op|'.'
name|'FileNotFoundException'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"File not found: %s"'
op|','
name|'ds_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|enlist_image
dedent|''
dedent|''
name|'def'
name|'enlist_image'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'datastore'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ds_browser'
op|'='
name|'self'
op|'.'
name|'_get_ds_browser'
op|'('
name|'datastore'
op|'.'
name|'ref'
op|')'
newline|'\n'
name|'cache_root_folder'
op|'='
name|'datastore'
op|'.'
name|'build_path'
op|'('
name|'self'
op|'.'
name|'_base_folder'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if the timestamp file exists - if so then delete it. This'
nl|'\n'
comment|'# will ensure that the aging will not delete a cache image if it'
nl|'\n'
comment|'# is going to be used now.'
nl|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'timestamp_folder_get'
op|'('
name|'cache_root_folder'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Lock to ensure that the spawn will not try and access a image'
nl|'\n'
comment|'# that is currently being deleted on the datastore.'
nl|'\n'
name|'with'
name|'lockutils'
op|'.'
name|'lock'
op|'('
name|'str'
op|'('
name|'path'
op|')'
op|','
name|'lock_file_prefix'
op|'='
string|"'nova-vmware-ts'"
op|','
nl|'\n'
name|'external'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'timestamp_cleanup'
op|'('
name|'dc_ref'
op|','
name|'ds_browser'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|timestamp_folder_get
dedent|''
dedent|''
name|'def'
name|'timestamp_folder_get'
op|'('
name|'self'
op|','
name|'ds_path'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the timestamp folder."""'
newline|'\n'
name|'return'
name|'ds_path'
op|'.'
name|'join'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|timestamp_cleanup
dedent|''
name|'def'
name|'timestamp_cleanup'
op|'('
name|'self'
op|','
name|'dc_ref'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ts'
op|'='
name|'self'
op|'.'
name|'_get_timestamp'
op|'('
name|'ds_browser'
op|','
name|'ds_path'
op|')'
newline|'\n'
name|'if'
name|'ts'
op|':'
newline|'\n'
indent|'            '
name|'ts_path'
op|'='
name|'ds_path'
op|'.'
name|'join'
op|'('
name|'ts'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Timestamp path %s exists. Deleting!"'
op|','
name|'ts_path'
op|')'
newline|'\n'
comment|'# Image is used - no longer need timestamp folder'
nl|'\n'
name|'self'
op|'.'
name|'_folder_delete'
op|'('
name|'ts_path'
op|','
name|'dc_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_timestamp
dedent|''
dedent|''
name|'def'
name|'_get_timestamp'
op|'('
name|'self'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'files'
op|'='
name|'ds_util'
op|'.'
name|'get_sub_folders'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
newline|'\n'
name|'if'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'file'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'file'
op|'.'
name|'startswith'
op|'('
name|'TIMESTAMP_PREFIX'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'file'
newline|'\n'
nl|'\n'
DECL|member|_get_timestamp_filename
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_timestamp_filename'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'%s%s'"
op|'%'
op|'('
name|'TIMESTAMP_PREFIX'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'fmt'
op|'='
name|'TIMESTAMP_FORMAT'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_datetime_from_filename
dedent|''
name|'def'
name|'_get_datetime_from_filename'
op|'('
name|'self'
op|','
name|'timestamp_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ts'
op|'='
name|'timestamp_filename'
op|'.'
name|'lstrip'
op|'('
name|'TIMESTAMP_PREFIX'
op|')'
newline|'\n'
name|'return'
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'ts'
op|','
name|'fmt'
op|'='
name|'TIMESTAMP_FORMAT'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_ds_browser
dedent|''
name|'def'
name|'_get_ds_browser'
op|'('
name|'self'
op|','
name|'ds_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ds_browser'
op|'='
name|'self'
op|'.'
name|'_ds_browser'
op|'.'
name|'get'
op|'('
name|'ds_ref'
op|'.'
name|'value'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ds_browser'
op|':'
newline|'\n'
indent|'            '
name|'ds_browser'
op|'='
name|'vim_util'
op|'.'
name|'get_dynamic_property'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
name|'ds_ref'
op|','
nl|'\n'
string|'"Datastore"'
op|','
string|'"browser"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ds_browser'
op|'['
name|'ds_ref'
op|'.'
name|'value'
op|']'
op|'='
name|'ds_browser'
newline|'\n'
dedent|''
name|'return'
name|'ds_browser'
newline|'\n'
nl|'\n'
DECL|member|_list_datastore_images
dedent|''
name|'def'
name|'_list_datastore_images'
op|'('
name|'self'
op|','
name|'ds_path'
op|','
name|'datastore'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of the images present in _base.\n\n        This method returns a dictionary with the following keys:\n            - unexplained_images\n            - originals\n        """'
newline|'\n'
name|'ds_browser'
op|'='
name|'self'
op|'.'
name|'_get_ds_browser'
op|'('
name|'datastore'
op|'.'
name|'ref'
op|')'
newline|'\n'
name|'originals'
op|'='
name|'ds_util'
op|'.'
name|'get_sub_folders'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'ds_browser'
op|','
nl|'\n'
name|'ds_path'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'unexplained_images'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'originals'"
op|':'
name|'originals'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_age_cached_images
dedent|''
name|'def'
name|'_age_cached_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'datastore'
op|','
name|'dc_info'
op|','
nl|'\n'
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ages cached images."""'
newline|'\n'
name|'age_seconds'
op|'='
name|'CONF'
op|'.'
name|'remove_unused_original_minimum_age_seconds'
newline|'\n'
name|'unused_images'
op|'='
name|'self'
op|'.'
name|'originals'
op|'-'
name|'self'
op|'.'
name|'used_images'
newline|'\n'
name|'ds_browser'
op|'='
name|'self'
op|'.'
name|'_get_ds_browser'
op|'('
name|'datastore'
op|'.'
name|'ref'
op|')'
newline|'\n'
name|'for'
name|'image'
name|'in'
name|'unused_images'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'self'
op|'.'
name|'timestamp_folder_get'
op|'('
name|'ds_path'
op|','
name|'image'
op|')'
newline|'\n'
comment|'# Lock to ensure that the spawn will not try and access a image'
nl|'\n'
comment|'# that is currently being deleted on the datastore.'
nl|'\n'
name|'with'
name|'lockutils'
op|'.'
name|'lock'
op|'('
name|'str'
op|'('
name|'path'
op|')'
op|','
name|'lock_file_prefix'
op|'='
string|"'nova-vmware-ts'"
op|','
nl|'\n'
name|'external'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ts'
op|'='
name|'self'
op|'.'
name|'_get_timestamp'
op|'('
name|'ds_browser'
op|','
name|'path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ts'
op|':'
newline|'\n'
indent|'                    '
name|'ts_path'
op|'='
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_get_timestamp_filename'
op|'('
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                        '
name|'ds_util'
op|'.'
name|'mkdir'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'ts_path'
op|','
name|'dc_info'
op|'.'
name|'ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'vexc'
op|'.'
name|'FileAlreadyExistsException'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Timestamp already exists."'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Image %s is no longer used by this node. "'
nl|'\n'
string|'"Pending deletion!"'
op|')'
op|','
name|'image'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'dt'
op|'='
name|'self'
op|'.'
name|'_get_datetime_from_filename'
op|'('
name|'str'
op|'('
name|'ts'
op|')'
op|')'
newline|'\n'
name|'if'
name|'timeutils'
op|'.'
name|'is_older_than'
op|'('
name|'dt'
op|','
name|'age_seconds'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Image %s is no longer used. "'
nl|'\n'
string|'"Deleting!"'
op|')'
op|','
name|'path'
op|')'
newline|'\n'
comment|'# Image has aged - delete the image ID folder'
nl|'\n'
name|'self'
op|'.'
name|'_folder_delete'
op|'('
name|'path'
op|','
name|'dc_info'
op|'.'
name|'ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# If the image is used and the timestamp file exists then we delete'
nl|'\n'
comment|'# the timestamp.'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'used_images'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'self'
op|'.'
name|'timestamp_folder_get'
op|'('
name|'ds_path'
op|','
name|'image'
op|')'
newline|'\n'
name|'with'
name|'lockutils'
op|'.'
name|'lock'
op|'('
name|'str'
op|'('
name|'path'
op|')'
op|','
name|'lock_file_prefix'
op|'='
string|"'nova-vmware-ts'"
op|','
nl|'\n'
name|'external'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'timestamp_cleanup'
op|'('
name|'dc_info'
op|'.'
name|'ref'
op|','
name|'ds_browser'
op|','
nl|'\n'
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
dedent|''
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instances'
op|','
name|'datastores_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The cache manager entry point.\n\n        This will invoke the cache manager. This will update the cache\n        according to the defined cache management scheme. The information\n        populated in the cached stats will be used for the cache management.\n        """'
newline|'\n'
comment|'# read running instances data'
nl|'\n'
name|'running'
op|'='
name|'self'
op|'.'
name|'_list_running_instances'
op|'('
name|'context'
op|','
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'used_images'
op|'='
name|'set'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# perform the aging and image verification per datastore'
nl|'\n'
name|'for'
op|'('
name|'datastore'
op|','
name|'dc_info'
op|')'
name|'in'
name|'datastores_info'
op|':'
newline|'\n'
indent|'            '
name|'ds_path'
op|'='
name|'datastore'
op|'.'
name|'build_path'
op|'('
name|'self'
op|'.'
name|'_base_folder'
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_list_datastore_images'
op|'('
name|'ds_path'
op|','
name|'datastore'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'originals'
op|'='
name|'images'
op|'['
string|"'originals'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_age_cached_images'
op|'('
name|'context'
op|','
name|'datastore'
op|','
name|'dc_info'
op|','
name|'ds_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_image_cache_folder
dedent|''
dedent|''
name|'def'
name|'get_image_cache_folder'
op|'('
name|'self'
op|','
name|'datastore'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns datastore path of folder containing the image."""'
newline|'\n'
name|'return'
name|'datastore'
op|'.'
name|'build_path'
op|'('
name|'self'
op|'.'
name|'_base_folder'
op|','
name|'image_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
