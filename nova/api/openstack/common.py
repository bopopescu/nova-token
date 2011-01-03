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
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|limited
name|'def'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a slice of items according to requested offset and limit.\n\n    items - a sliceable\n    req - wobob.Request possibly containing offset and limit GET variables.\n          offset is where to start in the list, and limit is the maximum number\n          of items to return.\n\n    If limit is not specified, 0, or > 1000, defaults to 1000.\n    """'
newline|'\n'
nl|'\n'
name|'offset'
op|'='
name|'int'
op|'('
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'offset'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'int'
op|'('
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'limit'
op|':'
newline|'\n'
indent|'        '
name|'limit'
op|'='
number|'1000'
newline|'\n'
dedent|''
name|'limit'
op|'='
name|'min'
op|'('
number|'1000'
op|','
name|'limit'
op|')'
newline|'\n'
name|'range_end'
op|'='
name|'offset'
op|'+'
name|'limit'
newline|'\n'
name|'return'
name|'items'
op|'['
name|'offset'
op|':'
name|'range_end'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_image_id_from_image_hash
dedent|''
name|'def'
name|'get_image_id_from_image_hash'
op|'('
name|'image_service'
op|','
name|'context'
op|','
name|'image_hash'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Given an Image ID Hash, return an objectstore Image ID.\n\n    image_service - reference to objectstore compatible image service.\n    context - security context for image service requests.\n    image_hash - hash of the image ID.\n    """'
newline|'\n'
nl|'\n'
comment|'# FIX(sandy): This is terribly inefficient. It pulls all images'
nl|'\n'
comment|'# from objectstore in order to find the match. ObjectStore '
nl|'\n'
comment|'# should have a numeric counterpart to the string ID. '
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'image_service'
op|'.'
name|'detail'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'image_service'
op|'.'
name|'index'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'image'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'image'
op|'['
string|"'imageId'"
op|']'
newline|'\n'
name|'if'
name|'abs'
op|'('
name|'hash'
op|'('
name|'image_id'
op|')'
op|')'
op|'=='
name|'int'
op|'('
name|'image_hash'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'image_id'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'image_hash'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
