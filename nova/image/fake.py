begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""Implementation of an fake image service"""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'random'
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
op|'.'
name|'image'
name|'import'
name|'service'
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
string|"'nova.image.fake'"
op|')'
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
nl|'\n'
nl|'\n'
DECL|class|_FakeImageService
name|'class'
name|'_FakeImageService'
op|'('
name|'service'
op|'.'
name|'BaseImageService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mock (fake) image service for unit testing."""'
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
name|'images'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|"# NOTE(justinsb): The OpenStack API can't upload an image?"
nl|'\n'
comment|"# So, make sure we've got one.."
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'01'
op|','
number|'01'
op|','
number|'01'
op|','
number|'02'
op|','
number|'03'
op|')'
newline|'\n'
name|'image'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'123456'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage123456'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'FLAGS'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'FLAGS'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86_64'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image'
op|')'
newline|'\n'
name|'super'
op|'('
name|'_FakeImageService'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
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
string|'"""Returns list of images."""'
newline|'\n'
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'images'
op|'.'
name|'values'
op|'('
op|')'
op|')'
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
string|'"""Return list of detailed image information."""'
newline|'\n'
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'images'
op|'.'
name|'values'
op|'('
op|')'
op|')'
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
string|'"""Get data about specified image.\n\n        Returns a dict containing image data for the given opaque image id.\n\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'int'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'images'
op|'.'
name|'get'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warn'
op|'('
string|"'Unable to find image id %s.  Have images: %s'"
op|','
nl|'\n'
name|'image_id'
op|','
name|'self'
op|'.'
name|'images'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
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
string|'"""Store the image data and return the new image id.\n\n        :raises: Duplicate if the image already exist.\n\n        """'
newline|'\n'
comment|"#image_id = int(metadata['id'])"
nl|'\n'
comment|"# metadata['id'] may not exists, and since image_id is"
nl|'\n'
comment|'#   randomly generated in local.py, let us do the same here'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_id'
op|'='
name|'int'
op|'('
name|'metadata'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'images'
op|'.'
name|'get'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
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
string|'"""Replace the contents of the given image with the new data.\n\n        :raises: ImageNotFound if the image does not exist.\n\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'int'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'images'
op|'.'
name|'get'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
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
string|'"""Delete the given image.\n\n        :raises: ImageNotFound if the image does not exist.\n\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'int'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'removed'
op|'='
name|'self'
op|'.'
name|'images'
op|'.'
name|'pop'
op|'('
name|'image_id'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'removed'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
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
string|'"""Clears out all images."""'
newline|'\n'
name|'self'
op|'.'
name|'images'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_fakeImageService
dedent|''
dedent|''
name|'_fakeImageService'
op|'='
name|'_FakeImageService'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|FakeImageService
name|'def'
name|'FakeImageService'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_fakeImageService'
newline|'\n'
dedent|''
endmarker|''
end_unit
