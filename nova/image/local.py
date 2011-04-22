begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'json'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'images_path'"
op|','
string|"'$state_path/images'"
op|','
nl|'\n'
string|"'path to decrypted images'"
op|')'
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
string|"'nova.image.local'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalImageService
name|'class'
name|'LocalImageService'
op|'('
name|'service'
op|'.'
name|'BaseImageService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Image service storing images to local disk.\n\n    It assumes that image_ids are integers.\n\n    """'
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
name|'self'
op|'.'
name|'_path'
op|'='
name|'FLAGS'
op|'.'
name|'images_path'
newline|'\n'
nl|'\n'
DECL|member|_path_to
dedent|''
name|'def'
name|'_path_to'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'fname'
op|'='
string|"'info.json'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'fname'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_path'
op|','
string|"'%08x'"
op|'%'
name|'int'
op|'('
name|'image_id'
op|')'
op|','
name|'fname'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_path'
op|','
string|"'%08x'"
op|'%'
name|'int'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ids
dedent|''
name|'def'
name|'_ids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The list of all image ids."""'
newline|'\n'
name|'images'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'image_dir'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'unhexed_image_id'
op|'='
name|'int'
op|'('
name|'image_dir'
op|','
number|'16'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'%s is not in correct directory naming format'"
op|')'
nl|'\n'
op|'%'
name|'image_dir'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'images'
op|'.'
name|'append'
op|'('
name|'unhexed_image_id'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'images'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filtered'
op|'='
op|'['
op|']'
newline|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'detail'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'image_meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'meta'
op|'='
name|'utils'
op|'.'
name|'subset_dict'
op|'('
name|'image_meta'
op|','
op|'('
string|"'id'"
op|','
string|"'name'"
op|')'
op|')'
newline|'\n'
name|'filtered'
op|'.'
name|'append'
op|'('
name|'meta'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'filtered'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'image_id'
name|'in'
name|'self'
op|'.'
name|'_ids'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'image'
op|'='
name|'self'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'images'
op|'.'
name|'append'
op|'('
name|'image'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'images'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|')'
op|')'
name|'as'
name|'metadata_file'
op|':'
newline|'\n'
indent|'                '
name|'image_meta'
op|'='
name|'json'
op|'.'
name|'load'
op|'('
name|'metadata_file'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_is_image_available'
op|'('
name|'context'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
name|'return'
name|'image_meta'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|show_by_name
dedent|''
dedent|''
name|'def'
name|'show_by_name'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dict containing image data for the given name."""'
newline|'\n'
comment|'# NOTE(vish): Not very efficient, but the local image service'
nl|'\n'
comment|'#             is for testing so it should be fine.'
nl|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'detail'
op|'('
name|'context'
op|')'
newline|'\n'
name|'image'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'cantidate'
name|'in'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
name|'cantidate'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'image'
op|'='
name|'cantidate'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'image'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
name|'return'
name|'image'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get image and metadata."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|')'
op|')'
name|'as'
name|'metadata_file'
op|':'
newline|'\n'
indent|'                '
name|'metadata'
op|'='
name|'json'
op|'.'
name|'load'
op|'('
name|'metadata_file'
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|','
string|"'image'"
op|')'
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'                '
name|'shutil'
op|'.'
name|'copyfileobj'
op|'('
name|'image_file'
op|','
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Store the image data and return the new image."""'
newline|'\n'
name|'image_id'
op|'='
name|'random'
op|'.'
name|'randint'
op|'('
number|'0'
op|','
number|'2'
op|'**'
number|'31'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'image_path'
op|'='
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'image_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'image_path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_store'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the contents of the given image with the new data."""'
newline|'\n'
comment|'# NOTE(vish): show is to check if image is available'
nl|'\n'
name|'self'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_store'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_store
dedent|''
name|'def'
name|'_store'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'['
string|"'id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'location'
op|'='
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|','
string|"'image'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'location'
op|','
string|"'w'"
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'                    '
name|'shutil'
op|'.'
name|'copyfileobj'
op|'('
name|'data'
op|','
name|'image_file'
op|')'
newline|'\n'
comment|'# NOTE(vish): update metadata similarly to glance'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'status'"
op|']'
op|'='
string|"'active'"
newline|'\n'
name|'metadata'
op|'['
string|"'location'"
op|']'
op|'='
name|'location'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'metadata_file'
op|':'
newline|'\n'
indent|'                '
name|'json'
op|'.'
name|'dump'
op|'('
name|'metadata'
op|','
name|'metadata_file'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the given image.\n\n        :raises: NotFound if the image does not exist.\n\n        """'
newline|'\n'
comment|'# NOTE(vish): show is to check if image is available'
nl|'\n'
name|'self'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|delete_all
dedent|''
dedent|''
name|'def'
name|'delete_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Clears out all images in local directory."""'
newline|'\n'
name|'for'
name|'image_id'
name|'in'
name|'self'
op|'.'
name|'_ids'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
