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
string|'"""Implementation of an fake image service"""'
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
DECL|class|MockImageService
name|'class'
name|'MockImageService'
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
name|'image'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'123456'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'machine'"
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
string|"'disk_format'"
op|':'
string|"'ami'"
op|'}'
nl|'\n'
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
name|'MockImageService'
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
name|'self'
op|'.'
name|'images'
op|'.'
name|'values'
op|'('
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
name|'self'
op|'.'
name|'images'
op|'.'
name|'values'
op|'('
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
string|'"""Get data about specified image.\n\n        Returns a dict containing image data for the given opaque image id."""'
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
name|'image'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warn'
op|'('
string|'"Unable to find image id %s.  Have images: %s"'
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
name|'NotFound'
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
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Store the image data and return the new image id.\n\n        :raises Duplicate if the image already exist.\n\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'int'
op|'('
name|'data'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|'='
name|'data'
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
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the contents of the given image with the new data.\n\n        :raises NotFound if the image does not exist.\n\n        """'
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
name|'NotFound'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|'='
name|'data'
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
string|'"""Delete the given image.\n\n        :raises NotFound if the image does not exist.\n\n        """'
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
dedent|''
dedent|''
endmarker|''
end_unit
