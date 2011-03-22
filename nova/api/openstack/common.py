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
name|'re'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'urlparse'
name|'import'
name|'urlparse'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|limited
name|'def'
name|'limited'
op|'('
name|'items'
op|','
name|'request'
op|','
name|'max_limit'
op|'='
number|'1000'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Return a slice of items according to requested offset and limit.\n\n    @param items: A sliceable entity\n    @param request: `wsgi.Request` possibly containing \'offset\' and \'limit\'\n                    GET variables. \'offset\' is where to start in the list,\n                    and \'limit\' is the maximum number of items to return. If\n                    \'limit\' is not specified, 0, or > max_limit, we default\n                    to max_limit. Negative values for either offset or limit\n                    will cause exc.HTTPBadRequest() exceptions to be raised.\n    @kwarg max_limit: The maximum number of items to return from \'items\'\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'offset'
op|'='
name|'int'
op|'('
name|'request'
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
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|"'offset param must be an integer'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'limit'
op|'='
name|'int'
op|'('
name|'request'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|','
name|'max_limit'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|"'limit param must be an integer'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'limit'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|"'limit param must be positive'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'offset'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|"'offset param must be positive'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'limit'
op|'='
name|'min'
op|'('
name|'max_limit'
op|','
name|'limit'
name|'or'
name|'max_limit'
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
comment|'# from objectstore in order to find the match. ObjectStore'
nl|'\n'
comment|'# should have a numeric counterpart to the string ID.'
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
string|"'id'"
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
nl|'\n'
nl|'\n'
DECL|function|get_id_from_href
dedent|''
name|'def'
name|'get_id_from_href'
op|'('
name|'href'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'urlparse'
op|'('
name|'href'
op|')'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|"'could not parse id from href'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
