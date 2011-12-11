begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Citrix Systems'
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
comment|'#    @author: Tyler Smith, Cisco Systems'
nl|'\n'
nl|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# FIXME(danwent): All content in this file should be removed once the'
nl|'\n'
comment|'# packaging work for the quantum client libraries is complete.'
nl|'\n'
comment|'# At that point, we will be able to just install the libraries as a'
nl|'\n'
comment|'# dependency and import from quantum.client.* and quantum.common.*'
nl|'\n'
comment|'# Until then, we have simplified versions of these classes in this file.'
nl|'\n'
nl|'\n'
DECL|class|JSONSerializer
name|'class'
name|'JSONSerializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This is a simple json-only serializer to use until we can just grab\n    the standard serializer from the quantum library.\n    """'
newline|'\n'
DECL|member|serialize
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'content_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'utils'
op|'.'
name|'to_primitive'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize
dedent|''
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'content_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# The full client lib will expose more'
nl|'\n'
comment|'# granular exceptions, for now, just try to distinguish'
nl|'\n'
comment|'# between the cases we care about.'
nl|'\n'
DECL|class|QuantumNotFoundException
dedent|''
dedent|''
name|'class'
name|'QuantumNotFoundException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Indicates that Quantum Server returned 404"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumServerException
dedent|''
name|'class'
name|'QuantumServerException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Indicates any non-404 error from Quantum Server"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumIOException
dedent|''
name|'class'
name|'QuantumIOException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Indicates network IO trouble reaching Quantum Server"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|api_call
dedent|''
name|'class'
name|'api_call'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Decorator to add support for format and tenant overriding"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'func'
op|'='
name|'func'
newline|'\n'
nl|'\n'
DECL|member|__get__
dedent|''
name|'def'
name|'__get__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'owner'
op|')'
op|':'
newline|'\n'
DECL|function|with_params
indent|'        '
name|'def'
name|'with_params'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Temporarily set format and tenant for this request"""'
newline|'\n'
op|'('
name|'format'
op|','
name|'tenant'
op|')'
op|'='
op|'('
name|'instance'
op|'.'
name|'format'
op|','
name|'instance'
op|'.'
name|'tenant'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'format'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'format'
op|'='
name|'kwargs'
op|'['
string|"'format'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'tenant'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'tenant'
op|'='
name|'kwargs'
op|'['
string|"'tenant'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ret'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'='
name|'self'
op|'.'
name|'func'
op|'('
name|'instance'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'                '
op|'('
name|'instance'
op|'.'
name|'format'
op|','
name|'instance'
op|'.'
name|'tenant'
op|')'
op|'='
op|'('
name|'format'
op|','
name|'tenant'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
dedent|''
name|'return'
name|'with_params'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Client
dedent|''
dedent|''
name|'class'
name|'Client'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A base client class - derived from Glance.BaseClient"""'
newline|'\n'
nl|'\n'
DECL|variable|action_prefix
name|'action_prefix'
op|'='
string|"'/v1.0/tenants/{tenant_id}'"
newline|'\n'
nl|'\n'
string|'"""Action query strings"""'
newline|'\n'
DECL|variable|networks_path
name|'networks_path'
op|'='
string|'"/networks"'
newline|'\n'
DECL|variable|network_path
name|'network_path'
op|'='
string|'"/networks/%s"'
newline|'\n'
DECL|variable|ports_path
name|'ports_path'
op|'='
string|'"/networks/%s/ports"'
newline|'\n'
DECL|variable|port_path
name|'port_path'
op|'='
string|'"/networks/%s/ports/%s"'
newline|'\n'
DECL|variable|attachment_path
name|'attachment_path'
op|'='
string|'"/networks/%s/ports/%s/attachment"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'9696'
op|','
name|'use_ssl'
op|'='
name|'False'
op|','
name|'tenant'
op|'='
name|'None'
op|','
nl|'\n'
name|'format'
op|'='
string|'"xml"'
op|','
name|'testing_stub'
op|'='
name|'None'
op|','
name|'key_file'
op|'='
name|'None'
op|','
nl|'\n'
name|'cert_file'
op|'='
name|'None'
op|','
name|'logger'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new client to some service.\n\n        :param host: The host where service resides\n        :param port: The port where service resides\n        :param use_ssl: True to use SSL, False to use HTTP\n        :param tenant: The tenant ID to make requests with\n        :param format: The format to query the server with\n        :param testing_stub: A class that stubs basic server methods for tests\n        :param key_file: The SSL key file to use if use_ssl is true\n        :param cert_file: The SSL cert file to use if use_ssl is true\n        """'
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
name|'tenant'
op|'='
name|'tenant'
newline|'\n'
name|'self'
op|'.'
name|'format'
op|'='
name|'format'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'testing_stub'
op|'='
name|'testing_stub'
newline|'\n'
name|'self'
op|'.'
name|'key_file'
op|'='
name|'key_file'
newline|'\n'
name|'self'
op|'.'
name|'cert_file'
op|'='
name|'cert_file'
newline|'\n'
name|'self'
op|'.'
name|'logger'
op|'='
name|'logger'
newline|'\n'
nl|'\n'
DECL|member|get_connection_type
dedent|''
name|'def'
name|'get_connection_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the proper connection type"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'testing_stub'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'testing_stub'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'use_ssl'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'httplib'
op|'.'
name|'HTTPSConnection'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'httplib'
op|'.'
name|'HTTPConnection'
newline|'\n'
nl|'\n'
DECL|member|do_request
dedent|''
dedent|''
name|'def'
name|'do_request'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'action'
op|','
name|'body'
op|'='
name|'None'
op|','
nl|'\n'
name|'headers'
op|'='
name|'None'
op|','
name|'params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Connects to the server and issues a request.\n        Returns the result data, or raises an appropriate exception if\n        HTTP status code is not 2xx\n\n        :param method: HTTP method ("GET", "POST", "PUT", etc...)\n        :param body: string of data to send, or None (default)\n        :param headers: mapping of key/value pairs to add as headers\n        :param params: dictionary of key/value pairs to add to append\n                             to action\n        """'
newline|'\n'
nl|'\n'
comment|'# Ensure we have a tenant id'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'tenant'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Tenant ID not set"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add format and tenant_id'
nl|'\n'
dedent|''
name|'action'
op|'+='
string|'".%s"'
op|'%'
name|'self'
op|'.'
name|'format'
newline|'\n'
name|'action'
op|'='
name|'Client'
op|'.'
name|'action_prefix'
op|'+'
name|'action'
newline|'\n'
name|'action'
op|'='
name|'action'
op|'.'
name|'replace'
op|'('
string|"'{tenant_id}'"
op|','
name|'self'
op|'.'
name|'tenant'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'type'
op|'('
name|'params'
op|')'
name|'is'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'+='
string|"'?'"
op|'+'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'connection_type'
op|'='
name|'self'
op|'.'
name|'get_connection_type'
op|'('
op|')'
newline|'\n'
name|'headers'
op|'='
name|'headers'
name|'or'
op|'{'
string|'"Content-Type"'
op|':'
nl|'\n'
string|'"application/%s"'
op|'%'
name|'self'
op|'.'
name|'format'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Open connection and send request, handling SSL certs'
nl|'\n'
name|'certs'
op|'='
op|'{'
string|"'key_file'"
op|':'
name|'self'
op|'.'
name|'key_file'
op|','
string|"'cert_file'"
op|':'
name|'self'
op|'.'
name|'cert_file'
op|'}'
newline|'\n'
name|'certs'
op|'='
name|'dict'
op|'('
op|'('
name|'x'
op|','
name|'certs'
op|'['
name|'x'
op|']'
op|')'
name|'for'
name|'x'
name|'in'
name|'certs'
name|'if'
name|'certs'
op|'['
name|'x'
op|']'
op|'!='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'use_ssl'
name|'and'
name|'len'
op|'('
name|'certs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'='
name|'connection_type'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|','
op|'**'
name|'certs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'='
name|'connection_type'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'logger'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'logger'
op|'.'
name|'debug'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Quantum Client Request:\\n%(method)s %(action)s\\n"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'logger'
op|'.'
name|'debug'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'c'
op|'.'
name|'request'
op|'('
name|'method'
op|','
name|'action'
op|','
name|'body'
op|','
name|'headers'
op|')'
newline|'\n'
name|'res'
op|'='
name|'c'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
name|'status_code'
op|'='
name|'self'
op|'.'
name|'get_status_code'
op|'('
name|'res'
op|')'
newline|'\n'
name|'data'
op|'='
name|'res'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'logger'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'logger'
op|'.'
name|'debug'
op|'('
string|'"Quantum Client Reply (code = %s) :\\n %s"'
op|'%'
op|'('
name|'str'
op|'('
name|'status_code'
op|')'
op|','
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'status_code'
op|'=='
name|'httplib'
op|'.'
name|'NOT_FOUND'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'QuantumNotFoundException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Quantum entity not found: %s"'
op|'%'
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'status_code'
name|'in'
op|'('
name|'httplib'
op|'.'
name|'OK'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'CREATED'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'ACCEPTED'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'NO_CONTENT'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'data'
name|'is'
name|'not'
name|'None'
name|'and'
name|'len'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'self'
op|'.'
name|'deserialize'
op|'('
name|'data'
op|','
name|'status_code'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'QuantumServerException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Server %(status_code)s error: %(data)s"'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'socket'
op|'.'
name|'error'
op|','
name|'IOError'
op|')'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'QuantumIOException'
op|'('
name|'_'
op|'('
string|'"Unable to connect to "'
nl|'\n'
string|'"server. Got error: %s"'
op|'%'
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_status_code
dedent|''
dedent|''
name|'def'
name|'get_status_code'
op|'('
name|'self'
op|','
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the integer status code from the response, which\n        can be either a Webob.Response (used in testing) or httplib.Response\n        """'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'response'
op|','
string|"'status_int'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
op|'.'
name|'status'
newline|'\n'
nl|'\n'
DECL|member|serialize
dedent|''
dedent|''
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'type'
op|'('
name|'data'
op|')'
name|'is'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'JSONSerializer'
op|'('
op|')'
op|'.'
name|'serialize'
op|'('
name|'data'
op|','
name|'self'
op|'.'
name|'content_type'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"unable to deserialize object of type = \'%s\'"'
op|'%'
nl|'\n'
name|'type'
op|'('
name|'data'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize
dedent|''
dedent|''
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'status_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'JSONSerializer'
op|'('
op|')'
op|'.'
name|'deserialize'
op|'('
name|'data'
op|','
name|'self'
op|'.'
name|'content_type'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|content_type
dedent|''
name|'def'
name|'content_type'
op|'('
name|'self'
op|','
name|'format'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'format'
op|':'
newline|'\n'
indent|'            '
name|'format'
op|'='
name|'self'
op|'.'
name|'format'
newline|'\n'
dedent|''
name|'return'
string|'"application/%s"'
op|'%'
op|'('
name|'format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|list_networks
name|'def'
name|'list_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetches a list of all networks for a tenant"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'self'
op|'.'
name|'networks_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|show_network_details
name|'def'
name|'show_network_details'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetches the details of a certain network"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'self'
op|'.'
name|'network_path'
op|'%'
op|'('
name|'network'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|create_network
name|'def'
name|'create_network'
op|'('
name|'self'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new network"""'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'serialize'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"POST"'
op|','
name|'self'
op|'.'
name|'networks_path'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|update_network
name|'def'
name|'update_network'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates a network"""'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'serialize'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"PUT"'
op|','
name|'self'
op|'.'
name|'network_path'
op|'%'
op|'('
name|'network'
op|')'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|delete_network
name|'def'
name|'delete_network'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the specified network"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"DELETE"'
op|','
name|'self'
op|'.'
name|'network_path'
op|'%'
op|'('
name|'network'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|list_ports
name|'def'
name|'list_ports'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetches a list of ports on a given network"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'self'
op|'.'
name|'ports_path'
op|'%'
op|'('
name|'network'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|show_port_details
name|'def'
name|'show_port_details'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetches the details of a certain port"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'self'
op|'.'
name|'port_path'
op|'%'
op|'('
name|'network'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|create_port
name|'def'
name|'create_port'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new port on a given network"""'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'serialize'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"POST"'
op|','
name|'self'
op|'.'
name|'ports_path'
op|'%'
op|'('
name|'network'
op|')'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|delete_port
name|'def'
name|'delete_port'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the specified port from a network"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"DELETE"'
op|','
name|'self'
op|'.'
name|'port_path'
op|'%'
op|'('
name|'network'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|set_port_state
name|'def'
name|'set_port_state'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'port'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the state of the specified port"""'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'serialize'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"PUT"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'port_path'
op|'%'
op|'('
name|'network'
op|','
name|'port'
op|')'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|show_port_attachment
name|'def'
name|'show_port_attachment'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetches the attachment-id associated with the specified port"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'self'
op|'.'
name|'attachment_path'
op|'%'
op|'('
name|'network'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|attach_resource
name|'def'
name|'attach_resource'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'port'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the attachment-id of the specified port"""'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'serialize'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"PUT"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'attachment_path'
op|'%'
op|'('
name|'network'
op|','
name|'port'
op|')'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'api_call'
newline|'\n'
DECL|member|detach_resource
name|'def'
name|'detach_resource'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes the attachment-id of the specified port"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"DELETE"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'attachment_path'
op|'%'
op|'('
name|'network'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
