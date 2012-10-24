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
name|'itertools'
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
name|'glanceclient'
newline|'\n'
name|'import'
name|'glanceclient'
op|'.'
name|'exc'
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
name|'use_ssl'
op|'='
op|'('
name|'o'
op|'.'
name|'scheme'
op|'=='
string|"'https'"
op|')'
newline|'\n'
name|'return'
op|'('
name|'image_id'
op|','
name|'host'
op|','
name|'port'
op|','
name|'use_ssl'
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
op|','
name|'use_ssl'
op|','
name|'version'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Instantiate a new glanceclient.Client object"""'
newline|'\n'
name|'if'
name|'use_ssl'
op|':'
newline|'\n'
indent|'        '
name|'scheme'
op|'='
string|"'https'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'scheme'
op|'='
string|"'http'"
newline|'\n'
dedent|''
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'params'
op|'['
string|"'insecure'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'glance_api_insecure'
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
string|"'token'"
op|']'
op|'='
name|'context'
op|'.'
name|'auth_token'
newline|'\n'
dedent|''
name|'endpoint'
op|'='
string|"'%s://%s:%s'"
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
name|'return'
name|'glanceclient'
op|'.'
name|'Client'
op|'('
name|'str'
op|'('
name|'version'
op|')'
op|','
name|'endpoint'
op|','
op|'**'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_api_servers
dedent|''
name|'def'
name|'get_api_servers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Shuffle a list of FLAGS.glance_api_servers and return an iterator\n    that will cycle through the list, looping around to the beginning\n    if necessary.\n    """'
newline|'\n'
name|'api_servers'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'api_server'
name|'in'
name|'FLAGS'
op|'.'
name|'glance_api_servers'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'//'"
name|'not'
name|'in'
name|'api_server'
op|':'
newline|'\n'
indent|'            '
name|'api_server'
op|'='
string|"'http://'"
op|'+'
name|'api_server'
newline|'\n'
dedent|''
name|'o'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'api_server'
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
name|'use_ssl'
op|'='
op|'('
name|'o'
op|'.'
name|'scheme'
op|'=='
string|"'https'"
op|')'
newline|'\n'
name|'api_servers'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'port'
op|','
name|'use_ssl'
op|')'
op|')'
newline|'\n'
dedent|''
name|'random'
op|'.'
name|'shuffle'
op|'('
name|'api_servers'
op|')'
newline|'\n'
name|'return'
name|'itertools'
op|'.'
name|'cycle'
op|'('
name|'api_servers'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceClientWrapper
dedent|''
name|'class'
name|'GlanceClientWrapper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Glance client wrapper class that implements retries."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'port'
op|'='
name|'None'
op|','
name|'use_ssl'
op|'='
name|'False'
op|','
nl|'\n'
name|'version'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'host'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'self'
op|'.'
name|'_create_static_client'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
name|'port'
op|','
nl|'\n'
name|'use_ssl'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'api_servers'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_create_static_client
dedent|''
name|'def'
name|'_create_static_client'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'port'
op|','
name|'use_ssl'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a client that we\'ll use for every call."""'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'port'
newline|'\n'
name|'self'
op|'.'
name|'use_ssl'
op|'='
name|'use_ssl'
newline|'\n'
name|'self'
op|'.'
name|'version'
op|'='
name|'version'
newline|'\n'
name|'return'
name|'_create_glance_client'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|','
nl|'\n'
name|'self'
op|'.'
name|'use_ssl'
op|','
name|'self'
op|'.'
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_onetime_client
dedent|''
name|'def'
name|'_create_onetime_client'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a client that will be used for one call."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'api_servers'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'api_servers'
op|'='
name|'get_api_servers'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|','
name|'self'
op|'.'
name|'use_ssl'
op|'='
name|'self'
op|'.'
name|'api_servers'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'return'
name|'_create_glance_client'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|','
nl|'\n'
name|'self'
op|'.'
name|'use_ssl'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call
dedent|''
name|'def'
name|'call'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'version'
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
string|'"""\n        Call a glance client method.  If we get a connection error,\n        retry the request according to FLAGS.glance_num_retries.\n        """'
newline|'\n'
name|'retry_excs'
op|'='
op|'('
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'ServiceUnavailable'
op|','
nl|'\n'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'InvalidEndpoint'
op|','
nl|'\n'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'CommunicationError'
op|')'
newline|'\n'
name|'num_attempts'
op|'='
number|'1'
op|'+'
name|'FLAGS'
op|'.'
name|'glance_num_retries'
newline|'\n'
nl|'\n'
name|'for'
name|'attempt'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'num_attempts'
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
name|'client'
name|'or'
name|'self'
op|'.'
name|'_create_onetime_client'
op|'('
name|'context'
op|','
nl|'\n'
name|'version'
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
op|'.'
name|'images'
op|','
name|'method'
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
name|'retry_excs'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'port'
newline|'\n'
name|'extra'
op|'='
string|'"retrying"'
newline|'\n'
name|'error_msg'
op|'='
name|'_'
op|'('
string|'"Error contacting glance server "'
nl|'\n'
string|'"\'%(host)s:%(port)s\' for \'%(method)s\', %(extra)s."'
op|')'
newline|'\n'
name|'if'
name|'attempt'
op|'=='
name|'num_attempts'
op|':'
newline|'\n'
indent|'                    '
name|'extra'
op|'='
string|"'done trying'"
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'error_msg'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'GlanceConnectionFailed'
op|'('
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'port'
op|'='
name|'port'
op|','
name|'reason'
op|'='
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'error_msg'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceImageService
dedent|''
dedent|''
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
name|'or'
name|'GlanceClientWrapper'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'images'
op|'='
name|'self'
op|'.'
name|'_client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'1'
op|','
string|"'list'"
op|','
op|'**'
name|'params'
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
name|'_images'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'image'
name|'in'
name|'images'
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
name|'image'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'_images'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'image'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'_images'
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
name|'params'
op|'.'
name|'get'
op|'('
name|'param'
op|')'
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
comment|'# ensure filters is a dict'
nl|'\n'
dedent|''
dedent|''
name|'params'
op|'.'
name|'setdefault'
op|'('
string|"'filters'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|"# NOTE(vish): don't filter out private images"
nl|'\n'
name|'params'
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
name|'return'
name|'_params'
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
string|'"""Returns a dict with image data for the given opaque image id."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'_client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'1'
op|','
string|"'get'"
op|','
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
name|'image'
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
name|'image'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
newline|'\n'
nl|'\n'
DECL|member|get_location
dedent|''
name|'def'
name|'get_location'
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
string|'"""Returns the direct url representing the backend storage location,\n        or None if this attribute is not shown by Glance."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'client'
op|'='
name|'GlanceClientWrapper'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'2'
op|','
string|"'get'"
op|','
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
name|'return'
name|'getattr'
op|'('
name|'image_meta'
op|','
string|"'direct_url'"
op|','
name|'None'
op|')'
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
name|'image_chunks'
op|'='
name|'self'
op|'.'
name|'_client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'1'
op|','
string|"'data'"
op|','
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
string|'"""Store the image data and return the new image object."""'
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
nl|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'sent_service_image_meta'
op|'['
string|"'data'"
op|']'
op|'='
name|'data'
newline|'\n'
nl|'\n'
dedent|''
name|'recv_service_image_meta'
op|'='
name|'self'
op|'.'
name|'_client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'1'
op|','
string|"'create'"
op|','
nl|'\n'
op|'**'
name|'sent_service_image_meta'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'recv_service_image_meta'
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
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|','
nl|'\n'
name|'purge_props'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Modify the given image with the new data."""'
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
name|'image_meta'
op|'['
string|"'purge_props'"
op|']'
op|'='
name|'purge_props'
newline|'\n'
comment|'#NOTE(bcwaldon): id is not an editable field, but it is likely to be'
nl|'\n'
comment|"# passed in by calling code. Let's be nice and ignore it."
nl|'\n'
name|'image_meta'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'['
string|"'data'"
op|']'
op|'='
name|'data'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'_client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'1'
op|','
string|"'update'"
op|','
nl|'\n'
name|'image_id'
op|','
op|'**'
name|'image_meta'
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_translate_from_glance'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_client'
op|'.'
name|'call'
op|'('
name|'context'
op|','
number|'1'
op|','
string|"'delete'"
op|','
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glanceclient'
op|'.'
name|'exc'
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
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_translate_to_glance
name|'def'
name|'_translate_to_glance'
op|'('
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
name|'staticmethod'
newline|'\n'
DECL|member|_translate_from_glance
name|'def'
name|'_translate_from_glance'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_meta'
op|'='
name|'_extract_attributes'
op|'('
name|'image'
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
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check image availability.\n\n        This check is needed in case Nova and Glance are deployed\n        without authentication turned on.\n        """'
newline|'\n'
comment|'# The presence of an auth token implies this is an authenticated'
nl|'\n'
comment|'# request and we need not handle the noauth use-case.'
nl|'\n'
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
name|'image'
op|'.'
name|'is_public'
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
name|'image'
op|'.'
name|'properties'
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
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
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
DECL|function|_extract_attributes
dedent|''
name|'def'
name|'_extract_attributes'
op|'('
name|'image'
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
name|'getattr'
op|'('
name|'image'
op|','
name|'attr'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'output'
op|'['
string|"'properties'"
op|']'
op|'='
name|'getattr'
op|'('
name|'image'
op|','
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
string|"'status'"
op|','
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
name|'exc_value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'isinstance'
op|'('
name|'exc_value'
op|','
op|'('
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'Forbidden'
op|','
nl|'\n'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'Unauthorized'
op|')'
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
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'NotFound'
op|')'
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
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'BadRequest'
op|')'
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
name|'exc_value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'isinstance'
op|'('
name|'exc_value'
op|','
op|'('
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'Forbidden'
op|','
nl|'\n'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'Unauthorized'
op|')'
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
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'NotFound'
op|')'
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
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'BadRequest'
op|')'
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
name|'return'
name|'image_service'
op|','
name|'image_href'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'image_id'
op|','
name|'glance_host'
op|','
name|'glance_port'
op|','
name|'use_ssl'
op|')'
op|'='
name|'_parse_image_ref'
op|'('
name|'image_href'
op|')'
newline|'\n'
name|'glance_client'
op|'='
name|'GlanceClientWrapper'
op|'('
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'host'
op|'='
name|'glance_host'
op|','
name|'port'
op|'='
name|'glance_port'
op|','
name|'use_ssl'
op|'='
name|'use_ssl'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
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
name|'image_service'
op|'='
name|'GlanceImageService'
op|'('
name|'client'
op|'='
name|'glance_client'
op|')'
newline|'\n'
name|'return'
name|'image_service'
op|','
name|'image_id'
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
