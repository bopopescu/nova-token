begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""Public HTTP interface that allows services to self-register.\n\nThe general flow of a request is:\n    - Request is parsed into WSGI bits.\n    - Some middleware checks authentication.\n    - Routing takes place based on the URL to find a controller.\n      (/controller/method)\n    - Parameters are parsed from the request and passed to a method on the\n      controller as keyword arguments.\n      - Optionally \'json\' is decoded to provide all the parameters.\n    - Actual work is done and a result is returned.\n    - That result is turned into json and returned.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Global storage for registering modules.'
nl|'\n'
DECL|variable|ROUTES
name|'ROUTES'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_service
name|'def'
name|'register_service'
op|'('
name|'path'
op|','
name|'handle'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Register a service handle at a given path.\n\n    Services registered in this way will be made available to any instances of\n    nova.api.direct.Router.\n\n    :param path: `routes` path, can be a basic string like "/path"\n    :param handle: an object whose methods will be made available via the api\n\n    """'
newline|'\n'
name|'ROUTES'
op|'['
name|'path'
op|']'
op|'='
name|'handle'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Router
dedent|''
name|'class'
name|'Router'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A simple WSGI router configured via `register_service`.\n\n    This is a quick way to attach multiple services to a given endpoint.\n    It will automatically load the routes registered in the `ROUTES` global.\n\n    TODO(termie): provide a paste-deploy version of this.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'mapper'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'mapper'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_load_registered_routes'
op|'('
name|'mapper'
op|')'
newline|'\n'
name|'super'
op|'('
name|'Router'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|'='
name|'mapper'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_registered_routes
dedent|''
name|'def'
name|'_load_registered_routes'
op|'('
name|'self'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'route'
name|'in'
name|'ROUTES'
op|':'
newline|'\n'
indent|'            '
name|'mapper'
op|'.'
name|'connect'
op|'('
string|"'/%s/{action}'"
op|'%'
name|'route'
op|','
nl|'\n'
name|'controller'
op|'='
name|'ServiceWrapper'
op|'('
name|'ROUTES'
op|'['
name|'route'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DelegatedAuthMiddleware
dedent|''
dedent|''
dedent|''
name|'class'
name|'DelegatedAuthMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A simple and naive authentication middleware.\n\n    Designed mostly to provide basic support for alternative authentication\n    schemes, this middleware only desires the identity of the user and will\n    generate the appropriate nova.context.RequestContext for the rest of the\n    application. This allows any middleware above it in the stack to\n    authenticate however it would like while only needing to conform to a\n    minimal interface.\n\n    Expects two headers to determine identity:\n     - X-OpenStack-User\n     - X-OpenStack-Project\n\n    This middleware is tied to identity management and will need to be kept\n    in sync with any changes to the way identity is dealt with internally.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|process_request
name|'def'
name|'process_request'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os_user'
op|'='
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X-OpenStack-User'"
op|']'
newline|'\n'
name|'os_project'
op|'='
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X-OpenStack-Project'"
op|']'
newline|'\n'
name|'context_ref'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|'='
name|'os_user'
op|','
name|'project'
op|'='
name|'os_project'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'context_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JsonParamsMiddleware
dedent|''
dedent|''
name|'class'
name|'JsonParamsMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Middleware to allow method arguments to be passed as serialized JSON.\n\n    Accepting arguments as JSON is useful for accepting data that may be more\n    complex than simple primitives.\n\n    In this case we accept it as urlencoded data under the key \'json\' as in\n    json=<urlencoded_json> but this could be extended to accept raw JSON\n    in the POST body.\n\n    Filters out the parameters `self`, `context` and anything beginning with\n    an underscore.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|process_request
name|'def'
name|'process_request'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'json'"
name|'not'
name|'in'
name|'request'
op|'.'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'params_json'
op|'='
name|'request'
op|'.'
name|'params'
op|'['
string|"'json'"
op|']'
newline|'\n'
name|'params_parsed'
op|'='
name|'utils'
op|'.'
name|'loads'
op|'('
name|'params_json'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'params_parsed'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
op|'('
string|"'self'"
op|','
string|"'context'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'k'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'params'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'.'
name|'environ'
op|'['
string|"'openstack.params'"
op|']'
op|'='
name|'params'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PostParamsMiddleware
dedent|''
dedent|''
name|'class'
name|'PostParamsMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Middleware to allow method arguments to be passed as POST parameters.\n\n    Filters out the parameters `self`, `context` and anything beginning with\n    an underscore.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|process_request
name|'def'
name|'process_request'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params_parsed'
op|'='
name|'request'
op|'.'
name|'params'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'params_parsed'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
op|'('
string|"'self'"
op|','
string|"'context'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'k'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'params'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'.'
name|'environ'
op|'['
string|"'openstack.params'"
op|']'
op|'='
name|'params'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Reflection
dedent|''
dedent|''
name|'class'
name|'Reflection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Reflection methods to list available methods.\n\n    This is an object that expects to be registered via register_service.\n    These methods allow the endpoint to be self-describing. They introspect\n    the exposed methods and provide call signatures and documentation for\n    them allowing quick experimentation.\n\n    """'
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
name|'_methods'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_controllers'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_gather_methods
dedent|''
name|'def'
name|'_gather_methods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Introspect available methods and generate documentation for them."""'
newline|'\n'
name|'methods'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'controllers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'route'
op|','
name|'handler'
name|'in'
name|'ROUTES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'controllers'
op|'['
name|'route'
op|']'
op|'='
name|'handler'
op|'.'
name|'__doc__'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'dir'
op|'('
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'k'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'f'
op|'='
name|'getattr'
op|'('
name|'handler'
op|','
name|'k'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'callable'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# bunch of ugly formatting stuff'
nl|'\n'
dedent|''
name|'argspec'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'f'
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'argspec'
op|'['
number|'0'
op|']'
nl|'\n'
name|'if'
name|'x'
op|'!='
string|"'self'"
name|'and'
name|'x'
op|'!='
string|"'context'"
op|']'
newline|'\n'
name|'defaults'
op|'='
name|'argspec'
op|'['
number|'3'
op|']'
name|'and'
name|'argspec'
op|'['
number|'3'
op|']'
name|'or'
op|'['
op|']'
newline|'\n'
name|'args_r'
op|'='
name|'list'
op|'('
name|'reversed'
op|'('
name|'args'
op|')'
op|')'
newline|'\n'
name|'defaults_r'
op|'='
name|'list'
op|'('
name|'reversed'
op|'('
name|'defaults'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'args_out'
op|'='
op|'['
op|']'
newline|'\n'
name|'while'
name|'args_r'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'defaults_r'
op|':'
newline|'\n'
indent|'                        '
name|'args_out'
op|'.'
name|'append'
op|'('
op|'('
name|'args_r'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
op|','
nl|'\n'
name|'repr'
op|'('
name|'defaults_r'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'args_out'
op|'.'
name|'append'
op|'('
op|'('
name|'str'
op|'('
name|'args_r'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
op|')'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# if the method accepts keywords'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'argspec'
op|'['
number|'2'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'args_out'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
op|'('
string|"'**%s'"
op|'%'
name|'argspec'
op|'['
number|'2'
op|']'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'f'
op|'.'
name|'__doc__'
op|':'
newline|'\n'
indent|'                    '
name|'short_doc'
op|'='
name|'f'
op|'.'
name|'__doc__'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'doc'
op|'='
name|'f'
op|'.'
name|'__doc__'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'short_doc'
op|'='
name|'doc'
op|'='
name|'_'
op|'('
string|"'not available'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'methods'
op|'['
string|"'/%s/%s'"
op|'%'
op|'('
name|'route'
op|','
name|'k'
op|')'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'short_doc'"
op|':'
name|'short_doc'
op|','
nl|'\n'
string|"'doc'"
op|':'
name|'doc'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'k'
op|','
nl|'\n'
string|"'args'"
op|':'
name|'list'
op|'('
name|'reversed'
op|'('
name|'args_out'
op|')'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_methods'
op|'='
name|'methods'
newline|'\n'
name|'self'
op|'.'
name|'_controllers'
op|'='
name|'controllers'
newline|'\n'
nl|'\n'
DECL|member|get_controllers
dedent|''
name|'def'
name|'get_controllers'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List available controllers."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_controllers'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_gather_methods'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_controllers'
newline|'\n'
nl|'\n'
DECL|member|get_methods
dedent|''
name|'def'
name|'get_methods'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List available methods."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_methods'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_gather_methods'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'method_list'
op|'='
name|'self'
op|'.'
name|'_methods'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'method_list'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'methods'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'method_list'
op|':'
newline|'\n'
indent|'            '
name|'methods'
op|'['
name|'k'
op|']'
op|'='
name|'self'
op|'.'
name|'_methods'
op|'['
name|'k'
op|']'
op|'['
string|"'short_doc'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'methods'
newline|'\n'
nl|'\n'
DECL|member|get_method_info
dedent|''
name|'def'
name|'get_method_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'method'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get detailed information about a method."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_methods'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_gather_methods'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_methods'
op|'['
name|'method'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceWrapper
dedent|''
dedent|''
name|'class'
name|'ServiceWrapper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper to dynamically povide a WSGI controller for arbitrary objects.\n\n    With lightweight introspection allows public methods on the object to\n    be accesed via simple WSGI routing and parameters and serializes the\n    return values.\n\n    Automatically used be nova.api.direct.Router to wrap registered instances.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'service_handle'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_handle'
op|'='
name|'service_handle'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'arg_dict'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'action'
op|'='
name|'arg_dict'
op|'['
string|"'action'"
op|']'
newline|'\n'
name|'del'
name|'arg_dict'
op|'['
string|"'action'"
op|']'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
newline|'\n'
comment|'# allow middleware up the stack to override the params'
nl|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'openstack.params'"
name|'in'
name|'req'
op|'.'
name|'environ'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.params'"
op|']'
newline|'\n'
nl|'\n'
comment|'# TODO(termie): do some basic normalization on methods'
nl|'\n'
dedent|''
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'service_handle'
op|','
name|'action'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): make sure we have no unicode keys for py2.6.'
nl|'\n'
name|'params'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'str'
op|'('
name|'k'
op|')'
op|','
name|'v'
op|')'
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'params'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'result'
op|'='
name|'method'
op|'('
name|'context'
op|','
op|'**'
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'result'
name|'is'
name|'None'
name|'or'
name|'type'
op|'('
name|'result'
op|')'
name|'is'
name|'str'
name|'or'
name|'type'
op|'('
name|'result'
op|')'
name|'is'
name|'unicode'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'content_type'
op|'='
name|'req'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'serializer'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'wsgi'
op|'.'
name|'XMLSerializer'
op|'('
op|')'
op|','
nl|'\n'
string|"'application/json'"
op|':'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'wsgi'
op|'.'
name|'JSONSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
op|'['
name|'content_type'
op|']'
newline|'\n'
name|'return'
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"returned non-serializable type: %s"'
nl|'\n'
op|'%'
name|'result'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Limited
dedent|''
dedent|''
dedent|''
name|'class'
name|'Limited'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'__notdoc'
op|'='
string|'"""Limit the available methods on a given object.\n\n    (Not a docstring so that the docstring can be conditionally overriden.)\n\n    Useful when defining a public API that only exposes a subset of an\n    internal API.\n\n    Expected usage of this class is to define a subclass that lists the allowed\n    methods in the \'allowed\' variable.\n\n    Additionally where appropriate methods can be added or overwritten, for\n    example to provide backwards compatibility.\n\n    The wrapping approach has been chosen so that the wrapped API can maintain\n    its own internal consistency, for example if it calls "self.create" it\n    should get its own create method rather than anything we do here.\n\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_allowed
name|'_allowed'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'proxy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_proxy'
op|'='
name|'proxy'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__doc__'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__doc__'
op|'='
name|'proxy'
op|'.'
name|'__doc__'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_allowed'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_allowed'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Only return methods that are named in self._allowed."""'
newline|'\n'
name|'if'
name|'key'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_allowed'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_proxy'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__dir__
dedent|''
name|'def'
name|'__dir__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Only return methods that are named in self._allowed."""'
newline|'\n'
name|'return'
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'dir'
op|'('
name|'self'
op|'.'
name|'_proxy'
op|')'
name|'if'
name|'x'
name|'in'
name|'self'
op|'.'
name|'_allowed'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Proxy
dedent|''
dedent|''
name|'class'
name|'Proxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pretend a Direct API endpoint is an object.\n\n    This is mostly useful in testing at the moment though it should be easily\n    extendable to provide a basic API library functionality.\n\n    In testing we use this to stub out internal objects to verify that results\n    from the API are serializable.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'app'
op|','
name|'prefix'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'app'
op|'='
name|'app'
newline|'\n'
name|'self'
op|'.'
name|'prefix'
op|'='
name|'prefix'
newline|'\n'
nl|'\n'
DECL|member|__do_request
dedent|''
name|'def'
name|'__do_request'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'path'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'urllib'
op|'.'
name|'urlencode'
op|'('
op|'{'
string|"'json'"
op|':'
name|'utils'
op|'.'
name|'dumps'
op|'('
name|'kwargs'
op|')'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'context'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'resp'
op|'.'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'prefix'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'__class__'
op|'('
name|'self'
op|'.'
name|'app'
op|','
name|'prefix'
op|'='
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_wrapper
dedent|''
name|'def'
name|'_wrapper'
op|'('
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'__do_request'
op|'('
string|"'/%s/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'prefix'
op|','
name|'key'
op|')'
op|','
nl|'\n'
name|'context'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'_wrapper'
op|'.'
name|'func_name'
op|'='
name|'key'
newline|'\n'
name|'return'
name|'_wrapper'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
