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
string|'"""Implementation of an image service that uses Glance as the backend"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'absolute_import'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'import'
name|'glance'
op|'.'
name|'client'
newline|'\n'
name|'from'
name|'glance'
op|'.'
name|'common'
name|'import'
name|'exception'
name|'as'
name|'glance_exception'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'import'
name|'utils'
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
name|'__name__'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_image_ref
name|'def'
name|'_parse_image_ref'
op|'('
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse an image href into composite parts.\n\n    :param image_href: href of an image\n    :returns: a tuple of the form (image_id, host, port)\n    :raises ValueError\n\n    """'
newline|'\n'
name|'o'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'image_href'
op|')'
newline|'\n'
name|'port'
op|'='
name|'o'
op|'.'
name|'port'
name|'or'
number|'80'
newline|'\n'
name|'host'
op|'='
name|'o'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"':'"
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'image_id'
op|'='
name|'o'
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
newline|'\n'
name|'return'
op|'('
name|'image_id'
op|','
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_glance_client
dedent|''
name|'def'
name|'_create_glance_client'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'auth_strategy'
op|'=='
string|"'keystone'"
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'['
string|"'creds'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'strategy'"
op|':'
string|"'keystone'"
op|','
nl|'\n'
string|"'username'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'tenant'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'params'
op|'['
string|"'auth_tok'"
op|']'
op|'='
name|'context'
op|'.'
name|'auth_token'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'glance'
op|'.'
name|'client'
op|'.'
name|'Client'
op|'('
name|'host'
op|','
name|'port'
op|','
op|'**'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pick_glance_api_server
dedent|''
name|'def'
name|'pick_glance_api_server'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return which Glance API server to use for the request\n\n    This method provides a very primitive form of load-balancing suitable for\n    testing and sandbox environments. In production, it would be better to use\n    one IP and route that to a real load-balancer.\n\n        Returns (host, port)\n    """'
newline|'\n'
name|'host_port'
op|'='
name|'random'
op|'.'
name|'choice'
op|'('
name|'FLAGS'
op|'.'
name|'glance_api_servers'
op|')'
newline|'\n'
name|'host'
op|','
name|'port_str'
op|'='
name|'host_port'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'port'
op|'='
name|'int'
op|'('
name|'port_str'
op|')'
newline|'\n'
name|'return'
name|'host'
op|','
name|'port'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_glance_client
dedent|''
name|'def'
name|'_get_glance_client'
op|'('
name|'context'
op|','
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the correct glance client and id for the given image_href.\n\n    The image_href param can be an href of the form\n    http://myglanceserver:9292/images/42, or just an int such as 42. If the\n    image_href is an int, then flags are used to create the default\n    glance client.\n\n    NOTE: Do not use this or glance.client directly, all other code\n    should be using GlanceImageService.\n\n    :param image_href: image ref/id for an image\n    :returns: a tuple of the form (glance_client, image_id)\n\n    """'
newline|'\n'
name|'glance_host'
op|','
name|'glance_port'
op|'='
name|'pick_glance_api_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# check if this is an id'
nl|'\n'
name|'if'
string|"'/'"
name|'not'
name|'in'
name|'str'
op|'('
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'glance_client'
op|'='
name|'_create_glance_client'
op|'('
name|'context'
op|','
nl|'\n'
name|'glance_host'
op|','
nl|'\n'
name|'glance_port'
op|')'
newline|'\n'
name|'return'
op|'('
name|'glance_client'
op|','
name|'image_href'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'image_id'
op|','
name|'glance_host'
op|','
name|'glance_port'
op|')'
op|'='
name|'_parse_image_ref'
op|'('
name|'image_href'
op|')'
newline|'\n'
name|'glance_client'
op|'='
name|'_create_glance_client'
op|'('
name|'context'
op|','
nl|'\n'
name|'glance_host'
op|','
nl|'\n'
name|'glance_port'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidImageRef'
op|'('
name|'image_href'
op|'='
name|'image_href'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'glance_client'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceImageService
dedent|''
dedent|''
name|'class'
name|'GlanceImageService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provides storage and retrieval of disk image objects within Glance."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'client'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_client'
op|'='
name|'client'
newline|'\n'
nl|'\n'
DECL|member|_get_client
dedent|''
name|'def'
name|'_get_client'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sirp): we want to load balance each request across glance'
nl|'\n'
comment|'# servers. Since GlanceImageService is a long-lived object, `client`'
nl|'\n'
comment|'# is made to choose a new server each time via this property.'
nl|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_client'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_client'
newline|'\n'
dedent|''
name|'glance_host'
op|','
name|'glance_port'
op|'='
name|'pick_glance_api_server'
op|'('
op|')'
newline|'\n'
name|'return'
name|'_create_glance_client'
op|'('
name|'context'
op|','
name|'glance_host'
op|','
name|'glance_port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_call_retry
dedent|''
name|'def'
name|'_call_retry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
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
string|'"""Retry call to glance server if there is a connection error.\n        Suitable only for idempotent calls."""'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'glance_num_retries'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'client'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'getattr'
op|'('
name|'client'
op|','
name|'name'
op|')'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glance_exception'
op|'.'
name|'ClientConnectionError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Connection error contacting glance'"
nl|'\n'
string|"' server, retrying'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'GlanceConnectionFailed'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Maximum attempts reached'"
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
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Calls out to Glance for a list of detailed image information."""'
newline|'\n'
name|'params'
op|'='
name|'self'
op|'.'
name|'_extract_query_params'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'_get_images'
op|'('
name|'context'
op|','
op|'**'
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'images'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'image_meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'if'
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
indent|'                '
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'images'
op|'.'
name|'append'
op|'('
name|'base_image_meta'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'images'
newline|'\n'
nl|'\n'
DECL|member|_extract_query_params
dedent|''
name|'def'
name|'_extract_query_params'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'accepted_params'
op|'='
op|'('
string|"'filters'"
op|','
string|"'marker'"
op|','
string|"'limit'"
op|','
nl|'\n'
string|"'sort_key'"
op|','
string|"'sort_dir'"
op|')'
newline|'\n'
name|'for'
name|'param'
name|'in'
name|'accepted_params'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'param'
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'                '
name|'_params'
op|'['
name|'param'
op|']'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'_params'
newline|'\n'
nl|'\n'
DECL|member|_get_images
dedent|''
name|'def'
name|'_get_images'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get image entitites from images service"""'
newline|'\n'
nl|'\n'
comment|'# ensure filters is a dict'
nl|'\n'
name|'kwargs'
op|'['
string|"'filters'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'filters'"
op|')'
name|'or'
op|'{'
op|'}'
newline|'\n'
comment|"# NOTE(vish): don't filter out private images"
nl|'\n'
name|'kwargs'
op|'['
string|"'filters'"
op|']'
op|'.'
name|'setdefault'
op|'('
string|"'is_public'"
op|','
string|"'none'"
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_fetch_images'
op|'('
name|'client'
op|'.'
name|'get_images_detailed'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fetch_images
dedent|''
name|'def'
name|'_fetch_images'
op|'('
name|'self'
op|','
name|'fetch_func'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Paginate through results from glance server"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'images'
op|'='
name|'fetch_func'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'_reraise_translated_exception'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'images'
op|':'
newline|'\n'
comment|'# break out of recursive loop to end pagination'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image'
name|'in'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'image'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# attempt to advance the marker in order to fetch next page'
nl|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'marker'"
op|']'
op|'='
name|'images'
op|'['
op|'-'
number|'1'
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImagePaginationFailed'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'limit'"
op|']'
op|'='
name|'kwargs'
op|'['
string|"'limit'"
op|']'
op|'-'
name|'len'
op|'('
name|'images'
op|')'
newline|'\n'
comment|'# break if we have reached a provided limit'
nl|'\n'
name|'if'
name|'kwargs'
op|'['
string|"'limit'"
op|']'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|'# ignore missing limit, just proceed without it'
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'_fetch_images'
op|'('
name|'fetch_func'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'image'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
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
string|'"""Returns a dict with image data for the given opaque image id."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'_call_retry'
op|'('
name|'context'
op|','
string|"'get_image_meta'"
op|','
nl|'\n'
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'_reraise_translated_image_exception'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
dedent|''
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
newline|'\n'
nl|'\n'
DECL|member|download
dedent|''
name|'def'
name|'download'
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
string|'"""Calls out to Glance for metadata and data and writes data."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|','
name|'image_chunks'
op|'='
name|'self'
op|'.'
name|'_call_retry'
op|'('
name|'context'
op|','
string|"'get_image'"
op|','
nl|'\n'
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'_reraise_translated_image_exception'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'chunk'
name|'in'
name|'image_chunks'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'.'
name|'write'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Store the image data and return the new image id.\n\n        :raises: AlreadyExists if the image already exist.\n\n        """'
newline|'\n'
comment|'# Translate Base -> Service'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating image in Glance. Metadata passed in %s'"
op|')'
op|','
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
name|'sent_service_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_glance'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Metadata after formatting for Glance %s'"
op|')'
op|','
nl|'\n'
name|'sent_service_image_meta'
op|')'
newline|'\n'
nl|'\n'
name|'recv_service_image_meta'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'add_image'
op|'('
nl|'\n'
name|'sent_service_image_meta'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
comment|'# Translate Service -> Base'
nl|'\n'
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'recv_service_image_meta'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Metadata returned from Glance formatted for Base %s'"
op|')'
op|','
nl|'\n'
name|'base_image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
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
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|','
name|'features'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the contents of the given image with the new data.\n\n        :raises: ImageNotFound if the image does not exist.\n\n        """'
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
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_glance'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'client'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
name|'client'
op|'.'
name|'update_image'
op|'('
name|'image_id'
op|','
name|'image_meta'
op|','
name|'data'
op|','
nl|'\n'
name|'features'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'_reraise_translated_image_exception'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
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
string|'"""Delete the given image.\n\n        :raises: ImageNotFound if the image does not exist.\n        :raises: NotAuthorized if the user is not an owner.\n\n        """'
newline|'\n'
comment|'# NOTE(vish): show is to check if image is available'
nl|'\n'
name|'image_meta'
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
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'auth_strategy'
op|'=='
string|"'deprecated'"
op|':'
newline|'\n'
comment|'# NOTE(parthi): only allow image deletions if the user'
nl|'\n'
comment|'# is a member of the project owning the image, in case of'
nl|'\n'
comment|'# setup without keystone'
nl|'\n'
comment|'# TODO(parthi): Currently this access control breaks if'
nl|'\n'
comment|'# 1. Image is not owned by a project'
nl|'\n'
comment|'# 2. Deleting user is not bound a project'
nl|'\n'
indent|'            '
name|'properties'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'if'
op|'('
name|'context'
op|'.'
name|'project_id'
name|'and'
op|'('
string|"'project_id'"
name|'in'
name|'properties'
op|')'
nl|'\n'
name|'and'
op|'('
name|'context'
op|'.'
name|'project_id'
op|'!='
name|'properties'
op|'['
string|"'project_id'"
op|']'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
name|'_'
op|'('
string|'"Not the image owner"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'context'
op|'.'
name|'project_id'
name|'and'
op|'('
string|"'owner_id'"
name|'in'
name|'properties'
op|')'
nl|'\n'
name|'and'
op|'('
name|'context'
op|'.'
name|'project_id'
op|'!='
name|'properties'
op|'['
string|"'owner_id'"
op|']'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
name|'_'
op|'('
string|'"Not the image owner"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'delete_image'
op|'('
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glance_exception'
op|'.'
name|'NotFound'
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
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|delete_all
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_translate_to_glance
name|'def'
name|'_translate_to_glance'
op|'('
name|'cls'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_meta'
op|'='
name|'_convert_to_string'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'_remove_read_only'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_translate_from_glance
name|'def'
name|'_translate_from_glance'
op|'('
name|'cls'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_meta'
op|'='
name|'_limit_attributes'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'_convert_timestamps_to_datetimes'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'_convert_from_string'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_is_image_available
name|'def'
name|'_is_image_available'
op|'('
name|'context'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check image availability.\n\n        Under Glance, images are always available if the context has\n        an auth_token.\n\n        """'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'context'
op|','
string|"'auth_token'"
op|')'
name|'and'
name|'context'
op|'.'
name|'auth_token'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'image_meta'
op|'['
string|"'is_public'"
op|']'
name|'or'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'properties'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'context'
op|'.'
name|'project_id'
name|'and'
op|'('
string|"'owner_id'"
name|'in'
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'properties'
op|'['
string|"'owner_id'"
op|']'
op|')'
op|'=='
name|'str'
op|'('
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'context'
op|'.'
name|'project_id'
name|'and'
op|'('
string|"'project_id'"
name|'in'
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'properties'
op|'['
string|"'project_id'"
op|']'
op|')'
op|'=='
name|'str'
op|'('
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'user_id'
op|'='
name|'properties'
op|'['
string|"'user_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'str'
op|'('
name|'user_id'
op|')'
op|'=='
name|'str'
op|'('
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# utility functions'
nl|'\n'
DECL|function|_convert_timestamps_to_datetimes
dedent|''
dedent|''
name|'def'
name|'_convert_timestamps_to_datetimes'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns image with timestamp fields converted to datetime objects."""'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'deleted_at'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'image_meta'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'['
name|'attr'
op|']'
op|'='
name|'_parse_glance_iso8601_timestamp'
op|'('
nl|'\n'
name|'image_meta'
op|'['
name|'attr'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_glance_iso8601_timestamp
dedent|''
name|'def'
name|'_parse_glance_iso8601_timestamp'
op|'('
name|'timestamp'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse a subset of iso8601 timestamps into datetime objects."""'
newline|'\n'
name|'iso_formats'
op|'='
op|'['
string|"'%Y-%m-%dT%H:%M:%S.%f'"
op|','
string|"'%Y-%m-%dT%H:%M:%S'"
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'iso_format'
name|'in'
name|'iso_formats'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'timestamp'
op|','
name|'iso_format'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|"'%(timestamp)s does not follow any of the '"
nl|'\n'
string|"'signatures: %(iso_formats)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(bcwaldon): used to store non-string data in glance metadata'
nl|'\n'
DECL|function|_json_loads
dedent|''
name|'def'
name|'_json_loads'
op|'('
name|'properties'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'prop'
op|'='
name|'properties'
op|'['
name|'attr'
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'prop'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'['
name|'attr'
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'prop'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_json_dumps
dedent|''
dedent|''
name|'def'
name|'_json_dumps'
op|'('
name|'properties'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'prop'
op|'='
name|'properties'
op|'['
name|'attr'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'prop'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'['
name|'attr'
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'prop'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_CONVERT_PROPS
dedent|''
dedent|''
name|'_CONVERT_PROPS'
op|'='
op|'('
string|"'block_device_mapping'"
op|','
string|"'mappings'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_convert
name|'def'
name|'_convert'
op|'('
name|'method'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'metadata'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'properties'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'properties'"
op|')'
newline|'\n'
name|'if'
name|'properties'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'attr'
name|'in'
name|'_CONVERT_PROPS'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attr'
name|'in'
name|'properties'
op|':'
newline|'\n'
indent|'                '
name|'method'
op|'('
name|'properties'
op|','
name|'attr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_convert_from_string
dedent|''
name|'def'
name|'_convert_from_string'
op|'('
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_convert'
op|'('
name|'_json_loads'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_convert_to_string
dedent|''
name|'def'
name|'_convert_to_string'
op|'('
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_convert'
op|'('
name|'_json_dumps'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_limit_attributes
dedent|''
name|'def'
name|'_limit_attributes'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'IMAGE_ATTRIBUTES'
op|'='
op|'['
string|"'size'"
op|','
string|"'disk_format'"
op|','
string|"'owner'"
op|','
nl|'\n'
string|"'container_format'"
op|','
string|"'checksum'"
op|','
string|"'id'"
op|','
nl|'\n'
string|"'name'"
op|','
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
nl|'\n'
string|"'deleted_at'"
op|','
string|"'deleted'"
op|','
string|"'status'"
op|','
nl|'\n'
string|"'min_disk'"
op|','
string|"'min_ram'"
op|','
string|"'is_public'"
op|']'
newline|'\n'
name|'output'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'IMAGE_ATTRIBUTES'
op|':'
newline|'\n'
indent|'        '
name|'output'
op|'['
name|'attr'
op|']'
op|'='
name|'image_meta'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'output'
op|'['
string|"'properties'"
op|']'
op|'='
name|'image_meta'
op|'.'
name|'get'
op|'('
string|"'properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'output'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_remove_read_only
dedent|''
name|'def'
name|'_remove_read_only'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'IMAGE_ATTRIBUTES'
op|'='
op|'['
string|"'updated_at'"
op|','
string|"'created_at'"
op|','
string|"'deleted_at'"
op|']'
newline|'\n'
name|'output'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'IMAGE_ATTRIBUTES'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'attr'
name|'in'
name|'output'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'output'
op|'['
name|'attr'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'output'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_reraise_translated_image_exception
dedent|''
name|'def'
name|'_reraise_translated_image_exception'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Transform the exception for the image but keep its traceback intact."""'
newline|'\n'
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'exc_trace'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'new_exc'
op|'='
name|'_translate_image_exception'
op|'('
name|'image_id'
op|','
name|'exc_type'
op|','
name|'exc_value'
op|')'
newline|'\n'
name|'raise'
name|'new_exc'
op|','
name|'None'
op|','
name|'exc_trace'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_reraise_translated_exception
dedent|''
name|'def'
name|'_reraise_translated_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Transform the exception but keep its traceback intact."""'
newline|'\n'
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'exc_trace'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'new_exc'
op|'='
name|'_translate_plain_exception'
op|'('
name|'exc_type'
op|','
name|'exc_value'
op|')'
newline|'\n'
name|'raise'
name|'new_exc'
op|','
name|'None'
op|','
name|'exc_trace'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_image_exception
dedent|''
name|'def'
name|'_translate_image_exception'
op|'('
name|'image_id'
op|','
name|'exc_type'
op|','
name|'exc_value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'exc_type'
name|'in'
op|'('
name|'glance_exception'
op|'.'
name|'Forbidden'
op|','
nl|'\n'
name|'glance_exception'
op|'.'
name|'NotAuthenticated'
op|','
nl|'\n'
name|'glance_exception'
op|'.'
name|'MissingCredentialError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exc_type'
name|'is'
name|'glance_exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'return'
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
name|'if'
name|'exc_type'
name|'is'
name|'glance_exception'
op|'.'
name|'Invalid'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'exc_value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc_value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_plain_exception
dedent|''
name|'def'
name|'_translate_plain_exception'
op|'('
name|'exc_type'
op|','
name|'exc_value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'exc_type'
name|'in'
op|'('
name|'glance_exception'
op|'.'
name|'Forbidden'
op|','
nl|'\n'
name|'glance_exception'
op|'.'
name|'NotAuthenticated'
op|','
nl|'\n'
name|'glance_exception'
op|'.'
name|'MissingCredentialError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
name|'exc_value'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exc_type'
name|'is'
name|'glance_exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'exc_value'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exc_type'
name|'is'
name|'glance_exception'
op|'.'
name|'Invalid'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'exc_value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc_value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_remote_image_service
dedent|''
name|'def'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create an image_service and parse the id from the given image_href.\n\n    The image_href param can be an href of the form\n    \'http://example.com:9292/v1/images/b8b2c6f7-7345-4e2f-afa2-eedaba9cbbe3\',\n    or just an id such as \'b8b2c6f7-7345-4e2f-afa2-eedaba9cbbe3\'. If the\n    image_href is a standalone id, then the default image service is returned.\n\n    :param image_href: href that describes the location of an image\n    :returns: a tuple of the form (image_service, image_id)\n\n    """'
newline|'\n'
comment|"#NOTE(bcwaldon): If image_href doesn't look like a URI, assume its a"
nl|'\n'
comment|'# standalone image ID'
nl|'\n'
name|'if'
string|"'/'"
name|'not'
name|'in'
name|'str'
op|'('
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_service'
op|'='
name|'get_default_image_service'
op|'('
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'image_href'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'glance_client'
op|','
name|'image_id'
op|')'
op|'='
name|'_get_glance_client'
op|'('
name|'context'
op|','
name|'image_href'
op|')'
newline|'\n'
name|'image_service'
op|'='
name|'GlanceImageService'
op|'('
name|'glance_client'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_default_image_service
dedent|''
name|'def'
name|'get_default_image_service'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'GlanceImageService'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
