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
name|'functools'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
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
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
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
DECL|variable|XML_NS_V11
name|'XML_NS_V11'
op|'='
string|"'http://docs.openstack.org/compute/api/v1.1'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_STATE_MAP
name|'_STATE_MAP'
op|'='
op|'{'
nl|'\n'
name|'vm_states'
op|'.'
name|'ACTIVE'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'ACTIVE'"
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'REBOOTING'
op|':'
string|"'REBOOT'"
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'REBOOTING_HARD'
op|':'
string|"'HARD_REBOOT'"
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'UPDATING_PASSWORD'
op|':'
string|"'PASSWORD'"
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_VERIFY'
op|':'
string|"'VERIFY_RESIZE'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'BUILD'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'REBUILDING'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'REBUILD'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'STOPPED'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'STOPPED'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'SHUTOFF'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'SHUTOFF'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'MIGRATING'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'MIGRATING'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'RESIZING'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'RESIZE'"
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_REVERTING'
op|':'
string|"'REVERT_RESIZE'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'PAUSED'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'PAUSED'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'SUSPENDED'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'SUSPENDED'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'RESCUED'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'RESCUE'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'ERROR'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'ERROR'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'DELETED'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'DELETED'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'SOFT_DELETE'
op|':'
op|'{'
nl|'\n'
string|"'default'"
op|':'
string|"'DELETED'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|status_from_state
name|'def'
name|'status_from_state'
op|'('
name|'vm_state'
op|','
name|'task_state'
op|'='
string|"'default'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Given vm_state and task_state, return a status string."""'
newline|'\n'
name|'task_map'
op|'='
name|'_STATE_MAP'
op|'.'
name|'get'
op|'('
name|'vm_state'
op|','
name|'dict'
op|'('
name|'default'
op|'='
string|"'UNKNOWN_STATE'"
op|')'
op|')'
newline|'\n'
name|'status'
op|'='
name|'task_map'
op|'.'
name|'get'
op|'('
name|'task_state'
op|','
name|'task_map'
op|'['
string|"'default'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Generated %(status)s from vm_state=%(vm_state)s "'
nl|'\n'
string|'"task_state=%(task_state)s."'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'status'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vm_state_from_status
dedent|''
name|'def'
name|'vm_state_from_status'
op|'('
name|'status'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Map the server status string to a vm state."""'
newline|'\n'
name|'for'
name|'state'
op|','
name|'task_map'
name|'in'
name|'_STATE_MAP'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'status_string'
op|'='
name|'task_map'
op|'.'
name|'get'
op|'('
string|'"default"'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
name|'status_string'
op|'.'
name|'lower'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'state'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pagination_params
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_pagination_params'
op|'('
name|'request'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return marker, limit tuple from request.\n\n    :param request: `wsgi.Request` possibly containing \'marker\' and \'limit\'\n                    GET variables. \'marker\' is the id of the last element\n                    the client has seen, and \'limit\' is the maximum number\n                    of items to return. If \'limit\' is not specified, 0, or\n                    > max_limit, we default to max_limit. Negative values\n                    for either marker or limit will cause\n                    exc.HTTPBadRequest() exceptions to be raised.\n\n    """'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'limit'"
name|'in'
name|'request'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'['
string|"'limit'"
op|']'
op|'='
name|'_get_limit_param'
op|'('
name|'request'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'marker'"
name|'in'
name|'request'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'['
string|"'marker'"
op|']'
op|'='
name|'_get_marker_param'
op|'('
name|'request'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'params'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_limit_param
dedent|''
name|'def'
name|'_get_limit_param'
op|'('
name|'request'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extract integer limit from request or fail"""'
newline|'\n'
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
op|'['
string|"'limit'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'limit param must be an integer'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'limit'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'limit param must be positive'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'limit'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_marker_param
dedent|''
name|'def'
name|'_get_marker_param'
op|'('
name|'request'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extract marker id from request or fail"""'
newline|'\n'
name|'return'
name|'request'
op|'.'
name|'GET'
op|'['
string|"'marker'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|limited
dedent|''
name|'def'
name|'limited'
op|'('
name|'items'
op|','
name|'request'
op|','
name|'max_limit'
op|'='
name|'FLAGS'
op|'.'
name|'osapi_max_limit'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a slice of items according to requested offset and limit.\n\n    :param items: A sliceable entity\n    :param request: ``wsgi.Request`` possibly containing \'offset\' and \'limit\'\n                    GET variables. \'offset\' is where to start in the list,\n                    and \'limit\' is the maximum number of items to return. If\n                    \'limit\' is not specified, 0, or > max_limit, we default\n                    to max_limit. Negative values for either offset or limit\n                    will cause exc.HTTPBadRequest() exceptions to be raised.\n    :kwarg max_limit: The maximum number of items to return from \'items\'\n    """'
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
name|'msg'
op|'='
name|'_'
op|'('
string|"'offset param must be an integer'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
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
name|'msg'
op|'='
name|'_'
op|'('
string|"'limit param must be an integer'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
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
name|'msg'
op|'='
name|'_'
op|'('
string|"'limit param must be positive'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
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
name|'msg'
op|'='
name|'_'
op|'('
string|"'offset param must be positive'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
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
DECL|function|limited_by_marker
dedent|''
name|'def'
name|'limited_by_marker'
op|'('
name|'items'
op|','
name|'request'
op|','
name|'max_limit'
op|'='
name|'FLAGS'
op|'.'
name|'osapi_max_limit'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a slice of items according to the requested marker and limit."""'
newline|'\n'
name|'params'
op|'='
name|'get_pagination_params'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
name|'limit'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|','
name|'max_limit'
op|')'
newline|'\n'
name|'marker'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'marker'"
op|')'
newline|'\n'
nl|'\n'
name|'limit'
op|'='
name|'min'
op|'('
name|'max_limit'
op|','
name|'limit'
op|')'
newline|'\n'
name|'start_index'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'marker'
op|':'
newline|'\n'
indent|'        '
name|'start_index'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'for'
name|'i'
op|','
name|'item'
name|'in'
name|'enumerate'
op|'('
name|'items'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'id'"
op|']'
op|'=='
name|'marker'
name|'or'
name|'item'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|'=='
name|'marker'
op|':'
newline|'\n'
indent|'                '
name|'start_index'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'start_index'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'marker [%s] not found'"
op|')'
op|'%'
name|'marker'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'range_end'
op|'='
name|'start_index'
op|'+'
name|'limit'
newline|'\n'
name|'return'
name|'items'
op|'['
name|'start_index'
op|':'
name|'range_end'
op|']'
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
string|'"""Return the id or uuid portion of a url.\n\n    Given: \'http://www.foo.com/bar/123?q=4\'\n    Returns: \'123\'\n\n    Given: \'http://www.foo.com/bar/abc123?q=4\'\n    Returns: \'abc123\'\n\n    """'
newline|'\n'
name|'return'
name|'urlparse'
op|'.'
name|'urlsplit'
op|'('
string|'"%s"'
op|'%'
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
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_version_from_href
dedent|''
name|'def'
name|'remove_version_from_href'
op|'('
name|'href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Removes the first api version from the href.\n\n    Given: \'http://www.nova.com/v1.1/123\'\n    Returns: \'http://www.nova.com/123\'\n\n    Given: \'http://www.nova.com/v1.1\'\n    Returns: \'http://www.nova.com\'\n\n    """'
newline|'\n'
name|'parsed_url'
op|'='
name|'urlparse'
op|'.'
name|'urlsplit'
op|'('
name|'href'
op|')'
newline|'\n'
name|'url_parts'
op|'='
name|'parsed_url'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE: this should match vX.X or vX'
nl|'\n'
name|'expression'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r'^v([0-9]+|[0-9]+\\.[0-9]+)(/.*|$)'"
op|')'
newline|'\n'
name|'if'
name|'expression'
op|'.'
name|'match'
op|'('
name|'url_parts'
op|'['
number|'1'
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'url_parts'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'new_path'
op|'='
string|"'/'"
op|'.'
name|'join'
op|'('
name|'url_parts'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'new_path'
op|'=='
name|'parsed_url'
op|'.'
name|'path'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'href %s does not contain version'"
op|')'
op|'%'
name|'href'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'ValueError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'parsed_url'
op|'='
name|'list'
op|'('
name|'parsed_url'
op|')'
newline|'\n'
name|'parsed_url'
op|'['
number|'2'
op|']'
op|'='
name|'new_path'
newline|'\n'
name|'return'
name|'urlparse'
op|'.'
name|'urlunsplit'
op|'('
name|'parsed_url'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_version_from_href
dedent|''
name|'def'
name|'get_version_from_href'
op|'('
name|'href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the api version in the href.\n\n    Returns the api version in the href.\n    If no version is found, \'2\' is returned\n\n    Given: \'http://www.nova.com/123\'\n    Returns: \'2\'\n\n    Given: \'http://www.nova.com/v1.1\'\n    Returns: \'1.1\'\n\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'expression'
op|'='
string|"r'/v([0-9]+|[0-9]+\\.[0-9]+)(/|$)'"
newline|'\n'
name|'return'
name|'re'
op|'.'
name|'findall'
op|'('
name|'expression'
op|','
name|'href'
op|')'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'2'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_img_metadata_quota_limit
dedent|''
dedent|''
name|'def'
name|'check_img_metadata_quota_limit'
op|'('
name|'context'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'metadata'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'num_metadata'
op|'='
name|'len'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'quota_metadata'
op|'='
name|'quota'
op|'.'
name|'allowed_metadata_items'
op|'('
name|'context'
op|','
name|'num_metadata'
op|')'
newline|'\n'
name|'if'
name|'quota_metadata'
op|'<'
name|'num_metadata'
op|':'
newline|'\n'
indent|'        '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Image metadata limit exceeded"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'explanation'
op|'='
name|'expl'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dict_to_query_str
dedent|''
dedent|''
name|'def'
name|'dict_to_query_str'
op|'('
name|'params'
op|')'
op|':'
newline|'\n'
comment|'# TODO(throughnothing): we should just use urllib.urlencode instead of this'
nl|'\n'
comment|"# But currently we don't work with urlencoded url's"
nl|'\n'
indent|'    '
name|'param_str'
op|'='
string|'""'
newline|'\n'
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'params'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param_str'
op|'='
name|'param_str'
op|'+'
string|"'='"
op|'.'
name|'join'
op|'('
op|'['
name|'str'
op|'('
name|'key'
op|')'
op|','
name|'str'
op|'('
name|'val'
op|')'
op|']'
op|')'
op|'+'
string|"'&'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'param_str'
op|'.'
name|'rstrip'
op|'('
string|"'&'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_networks_for_instance_from_nw_info
dedent|''
name|'def'
name|'get_networks_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'networks'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Converting nw_info: %s'"
op|')'
op|'%'
name|'nw_info'
op|')'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
name|'floaters'
op|'='
name|'vif'
op|'.'
name|'floating_ips'
op|'('
op|')'
newline|'\n'
name|'label'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
newline|'\n'
name|'if'
name|'label'
name|'not'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'networks'
op|'['
name|'label'
op|']'
op|'='
op|'{'
string|"'ips'"
op|':'
op|'['
op|']'
op|','
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'networks'
op|'['
name|'label'
op|']'
op|'['
string|"'ips'"
op|']'
op|'.'
name|'extend'
op|'('
name|'ips'
op|')'
newline|'\n'
name|'networks'
op|'['
name|'label'
op|']'
op|'['
string|"'floating_ips'"
op|']'
op|'.'
name|'extend'
op|'('
name|'floaters'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Converted networks: %s'"
op|')'
op|'%'
name|'networks'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'networks'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_nw_info_for_instance
dedent|''
name|'def'
name|'get_nw_info_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'info_cache'
op|'='
name|'instance'
op|'['
string|"'info_cache'"
op|']'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'cached_nwinfo'
op|'='
name|'info_cache'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
name|'or'
op|'['
op|']'
newline|'\n'
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'cached_nwinfo'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_networks_for_instance
dedent|''
name|'def'
name|'get_networks_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a prepared nw_info list for passing into the view builders\n\n    We end up with a data structure like::\n\n        {\'public\': {\'ips\': [{\'addr\': \'10.0.0.1\', \'version\': 4},\n                            {\'addr\': \'2001::1\', \'version\': 6}],\n                    \'floating_ips\': [{\'addr\': \'172.16.0.1\', \'version\': 4},\n                                     {\'addr\': \'172.16.2.1\', \'version\': 4}]},\n         ...}\n    """'
newline|'\n'
name|'nw_info'
op|'='
name|'get_nw_info_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'get_networks_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|raise_http_conflict_for_instance_invalid_state
dedent|''
name|'def'
name|'raise_http_conflict_for_instance_invalid_state'
op|'('
name|'exc'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a webob.exc.HTTPConflict instance containing a message\n    appropriate to return via the API based on the original\n    InstanceInvalidState exception.\n    """'
newline|'\n'
name|'attr'
op|'='
name|'exc'
op|'.'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'attr'"
op|')'
newline|'\n'
name|'state'
op|'='
name|'exc'
op|'.'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'state'"
op|')'
newline|'\n'
name|'if'
name|'attr'
name|'and'
name|'state'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot \'%(action)s\' while instance is in %(attr)s %(state)s"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# At least give some meaningful message'
nl|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance is in an invalid state for \'%(action)s\'"'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'msg'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataDeserializer
dedent|''
name|'class'
name|'MetadataDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
DECL|member|deserialize
indent|'    '
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'text'
op|')'
newline|'\n'
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'dom'
op|','
string|'"metadata"'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'metadata'"
op|':'
name|'metadata'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetaItemDeserializer
dedent|''
dedent|''
name|'class'
name|'MetaItemDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
DECL|member|deserialize
indent|'    '
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'text'
op|')'
newline|'\n'
name|'metadata_item'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'meta'"
op|':'
name|'metadata_item'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataXMLDeserializer
dedent|''
dedent|''
name|'class'
name|'MetadataXMLDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|extract_metadata
indent|'    '
name|'def'
name|'extract_metadata'
op|'('
name|'self'
op|','
name|'metadata_node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the metadata attribute of a parsed request"""'
newline|'\n'
name|'if'
name|'metadata_node'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'meta_node'
name|'in'
name|'self'
op|'.'
name|'find_children_named'
op|'('
name|'metadata_node'
op|','
string|'"meta"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'meta_node'
op|'.'
name|'getAttribute'
op|'('
string|'"key"'
op|')'
newline|'\n'
name|'metadata'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_text'
op|'('
name|'meta_node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
DECL|member|_extract_metadata_container
dedent|''
name|'def'
name|'_extract_metadata_container'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'datastring'
op|')'
newline|'\n'
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'dom'
op|','
string|'"metadata"'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'metadata'"
op|':'
name|'metadata'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_extract_metadata_container'
op|'('
name|'datastring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_all
dedent|''
name|'def'
name|'update_all'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_extract_metadata_container'
op|'('
name|'datastring'
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
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'datastring'
op|')'
newline|'\n'
name|'metadata_item'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'meta'"
op|':'
name|'metadata_item'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|metadata_nsmap
dedent|''
dedent|''
name|'metadata_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetaItemTemplate
name|'class'
name|'MetaItemTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sel'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
string|"'meta'"
op|','
name|'xmlutil'
op|'.'
name|'get_items'
op|','
number|'0'
op|')'
newline|'\n'
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'meta'"
op|','
name|'selector'
op|'='
name|'sel'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'key'"
op|','
number|'0'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'text'
op|'='
number|'1'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'metadata_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataTemplateElement
dedent|''
dedent|''
name|'class'
name|'MetadataTemplateElement'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|')'
op|':'
newline|'\n'
DECL|member|will_render
indent|'    '
name|'def'
name|'will_render'
op|'('
name|'self'
op|','
name|'datum'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataTemplate
dedent|''
dedent|''
name|'class'
name|'MetadataTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'MetadataTemplateElement'
op|'('
string|"'metadata'"
op|','
name|'selector'
op|'='
string|"'metadata'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'meta'"
op|','
nl|'\n'
name|'selector'
op|'='
name|'xmlutil'
op|'.'
name|'get_items'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'key'"
op|','
number|'0'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'text'
op|'='
number|'1'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'metadata_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_snapshots_enabled
dedent|''
dedent|''
name|'def'
name|'check_snapshots_enabled'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|inner
name|'def'
name|'inner'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'allow_instance_snapshots'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Rejecting snapshot request, snapshots currently'"
nl|'\n'
string|"' disabled'"
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance snapshots are not permitted at this time."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'inner'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
dedent|''
name|'class'
name|'ViewBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Model API responses as dictionaries."""'
newline|'\n'
nl|'\n'
DECL|variable|_collection_name
name|'_collection_name'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_links
name|'def'
name|'_get_links'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'identifier'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_href_link'
op|'('
name|'request'
op|','
name|'identifier'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_bookmark_link'
op|'('
name|'request'
op|','
name|'identifier'
op|')'
op|','
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_next_link
dedent|''
name|'def'
name|'_get_next_link'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'identifier'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return href string with proper limit and marker params."""'
newline|'\n'
name|'params'
op|'='
name|'request'
op|'.'
name|'params'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'params'
op|'['
string|'"marker"'
op|']'
op|'='
name|'identifier'
newline|'\n'
name|'prefix'
op|'='
name|'self'
op|'.'
name|'_update_link_prefix'
op|'('
name|'request'
op|'.'
name|'application_url'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'osapi_compute_link_prefix'
op|')'
newline|'\n'
name|'url'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'prefix'
op|','
nl|'\n'
name|'request'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
newline|'\n'
name|'return'
string|'"%s?%s"'
op|'%'
op|'('
name|'url'
op|','
name|'dict_to_query_str'
op|'('
name|'params'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_href_link
dedent|''
name|'def'
name|'_get_href_link'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'identifier'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return an href string pointing to this object."""'
newline|'\n'
name|'prefix'
op|'='
name|'self'
op|'.'
name|'_update_link_prefix'
op|'('
name|'request'
op|'.'
name|'application_url'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'osapi_compute_link_prefix'
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'prefix'
op|','
nl|'\n'
name|'request'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|','
nl|'\n'
name|'str'
op|'('
name|'identifier'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_bookmark_link
dedent|''
name|'def'
name|'_get_bookmark_link'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'identifier'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a URL that refers to a specific resource."""'
newline|'\n'
name|'base_url'
op|'='
name|'remove_version_from_href'
op|'('
name|'request'
op|'.'
name|'application_url'
op|')'
newline|'\n'
name|'base_url'
op|'='
name|'self'
op|'.'
name|'_update_link_prefix'
op|'('
name|'base_url'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'osapi_compute_link_prefix'
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_url'
op|','
nl|'\n'
name|'request'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|','
nl|'\n'
name|'str'
op|'('
name|'identifier'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_collection_links
dedent|''
name|'def'
name|'_get_collection_links'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'items'
op|','
name|'id_key'
op|'='
string|'"uuid"'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve \'next\' link, if applicable."""'
newline|'\n'
name|'links'
op|'='
op|'['
op|']'
newline|'\n'
name|'limit'
op|'='
name|'int'
op|'('
name|'request'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|'"limit"'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'if'
name|'limit'
name|'and'
name|'limit'
op|'=='
name|'len'
op|'('
name|'items'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'last_item'
op|'='
name|'items'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'if'
name|'id_key'
name|'in'
name|'last_item'
op|':'
newline|'\n'
indent|'                '
name|'last_item_id'
op|'='
name|'last_item'
op|'['
name|'id_key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'last_item_id'
op|'='
name|'last_item'
op|'['
string|'"id"'
op|']'
newline|'\n'
dedent|''
name|'links'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"next"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_next_link'
op|'('
name|'request'
op|','
name|'last_item_id'
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'links'
newline|'\n'
nl|'\n'
DECL|member|_update_link_prefix
dedent|''
name|'def'
name|'_update_link_prefix'
op|'('
name|'self'
op|','
name|'orig_url'
op|','
name|'prefix'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'prefix'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'orig_url'
newline|'\n'
dedent|''
name|'url_parts'
op|'='
name|'list'
op|'('
name|'urlparse'
op|'.'
name|'urlsplit'
op|'('
name|'orig_url'
op|')'
op|')'
newline|'\n'
name|'prefix_parts'
op|'='
name|'list'
op|'('
name|'urlparse'
op|'.'
name|'urlsplit'
op|'('
name|'prefix'
op|')'
op|')'
newline|'\n'
name|'url_parts'
op|'['
number|'0'
op|':'
number|'2'
op|']'
op|'='
name|'prefix_parts'
op|'['
number|'0'
op|':'
number|'2'
op|']'
newline|'\n'
name|'return'
name|'urlparse'
op|'.'
name|'urlunsplit'
op|'('
name|'url_parts'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
