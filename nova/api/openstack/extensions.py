begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'imp'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
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
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
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
string|"'extensions'"
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
DECL|class|ExtensionDescriptor
name|'class'
name|'ExtensionDescriptor'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class that defines the contract for extensions.\n\n    Note that you don\'t have to derive from this class to have a valid\n    extension; it is purely a convenience.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|get_name
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The name of the extension.\n\n        e.g. \'Fox In Socks\'\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The alias for the extension.\n\n        e.g. \'FOXNSOX\'\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Friendly description for the extension.\n\n        e.g. \'The Fox In Socks Extension\'\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The XML namespace for the extension.\n\n        e.g. \'http://www.fox.in.socks/api/ext/pie/v1.0\'\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The timestamp when the extension was last updated.\n\n        e.g. \'2011-01-22T13:25:27-06:00\'\n\n        """'
newline|'\n'
comment|'# NOTE(justinsb): Not sure of the purpose of this is, vs the XML NS'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List of extensions.ResourceExtension extension objects.\n\n        Resources define new nouns, and are accessible through URLs.\n\n        """'
newline|'\n'
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List of extensions.ActionExtension extension objects.\n\n        Actions are verbs callable from the API.\n\n        """'
newline|'\n'
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'actions'
newline|'\n'
nl|'\n'
DECL|member|get_response_extensions
dedent|''
name|'def'
name|'get_response_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List of extensions.ResponseExtension extension objects.\n\n        Response extensions are used to insert information into existing\n        response data.\n\n        """'
newline|'\n'
name|'response_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'response_exts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ActionExtensionController
dedent|''
dedent|''
name|'class'
name|'ActionExtensionController'
op|'('
name|'common'
op|'.'
name|'OpenstackController'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
name|'self'
op|'.'
name|'action_handlers'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|add_action
dedent|''
name|'def'
name|'add_action'
op|'('
name|'self'
op|','
name|'action_name'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'action_handlers'
op|'['
name|'action_name'
op|']'
op|'='
name|'handler'
newline|'\n'
nl|'\n'
DECL|member|action
dedent|''
name|'def'
name|'action'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'input_dict'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'action_name'
op|','
name|'handler'
name|'in'
name|'self'
op|'.'
name|'action_handlers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'action_name'
name|'in'
name|'input_dict'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'handler'
op|'('
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
newline|'\n'
comment|'# no action handler found (bump to downstream application)'
nl|'\n'
dedent|''
dedent|''
name|'res'
op|'='
name|'self'
op|'.'
name|'application'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResponseExtensionController
dedent|''
dedent|''
name|'class'
name|'ResponseExtensionController'
op|'('
name|'common'
op|'.'
name|'OpenstackController'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
name|'self'
op|'.'
name|'handlers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|add_handler
dedent|''
name|'def'
name|'add_handler'
op|'('
name|'self'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'handlers'
op|'.'
name|'append'
op|'('
name|'handler'
op|')'
newline|'\n'
nl|'\n'
DECL|member|process
dedent|''
name|'def'
name|'process'
op|'('
name|'self'
op|','
name|'req'
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
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
name|'content_type'
op|'='
name|'req'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
comment|'# currently response handlers are un-ordered'
nl|'\n'
name|'for'
name|'handler'
name|'in'
name|'self'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'handler'
op|'('
name|'res'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'body'
op|'='
name|'res'
op|'.'
name|'body'
newline|'\n'
name|'headers'
op|'='
name|'res'
op|'.'
name|'headers'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'                '
name|'body'
op|'='
name|'self'
op|'.'
name|'_serialize'
op|'('
name|'res'
op|','
name|'content_type'
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
string|'"Content-Type"'
op|':'
name|'content_type'
op|'}'
newline|'\n'
dedent|''
name|'res'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'res'
op|'.'
name|'body'
op|'='
name|'body'
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'='
name|'headers'
newline|'\n'
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionController
dedent|''
dedent|''
name|'class'
name|'ExtensionController'
op|'('
name|'common'
op|'.'
name|'OpenstackController'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'extension_manager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extension_manager'
op|'='
name|'extension_manager'
newline|'\n'
nl|'\n'
DECL|member|_translate
dedent|''
name|'def'
name|'_translate'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'ext_data'
op|'['
string|"'name'"
op|']'
op|'='
name|'ext'
op|'.'
name|'get_name'
op|'('
op|')'
newline|'\n'
name|'ext_data'
op|'['
string|"'alias'"
op|']'
op|'='
name|'ext'
op|'.'
name|'get_alias'
op|'('
op|')'
newline|'\n'
name|'ext_data'
op|'['
string|"'description'"
op|']'
op|'='
name|'ext'
op|'.'
name|'get_description'
op|'('
op|')'
newline|'\n'
name|'ext_data'
op|'['
string|"'namespace'"
op|']'
op|'='
name|'ext'
op|'.'
name|'get_namespace'
op|'('
op|')'
newline|'\n'
name|'ext_data'
op|'['
string|"'updated'"
op|']'
op|'='
name|'ext'
op|'.'
name|'get_updated'
op|'('
op|')'
newline|'\n'
name|'ext_data'
op|'['
string|"'links'"
op|']'
op|'='
op|'['
op|']'
comment|'# TODO(dprince): implement extension links'
newline|'\n'
name|'return'
name|'ext_data'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'extensions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'_alias'
op|','
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extension_manager'
op|'.'
name|'extensions'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'extensions'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'extensions'
op|'='
name|'extensions'
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
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(dprince): the extensions alias is used as the 'id' for show"
nl|'\n'
indent|'        '
name|'ext'
op|'='
name|'self'
op|'.'
name|'extension_manager'
op|'.'
name|'extensions'
op|'['
name|'id'
op|']'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
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
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
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
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionMiddleware
dedent|''
dedent|''
name|'class'
name|'ExtensionMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extensions middleware for WSGI."""'
newline|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Paste factory."""'
newline|'\n'
DECL|function|_factory
name|'def'
name|'_factory'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'('
name|'app'
op|','
op|'**'
name|'local_config'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_factory'
newline|'\n'
nl|'\n'
DECL|member|_action_ext_controllers
dedent|''
name|'def'
name|'_action_ext_controllers'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'ext_mgr'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dict of ActionExtensionController-s by collection."""'
newline|'\n'
name|'action_controllers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'action'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_actions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'action'
op|'.'
name|'collection'
name|'in'
name|'action_controllers'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'controller'
op|'='
name|'ActionExtensionController'
op|'('
name|'application'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/%s/:(id)/action.:(format)"'
op|'%'
nl|'\n'
name|'action'
op|'.'
name|'collection'
op|','
nl|'\n'
name|'action'
op|'='
string|"'action'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
op|'['
string|"'POST'"
op|']'
op|')'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/%s/:(id)/action"'
op|'%'
name|'action'
op|'.'
name|'collection'
op|','
nl|'\n'
name|'action'
op|'='
string|"'action'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
op|'['
string|"'POST'"
op|']'
op|')'
op|')'
newline|'\n'
name|'action_controllers'
op|'['
name|'action'
op|'.'
name|'collection'
op|']'
op|'='
name|'controller'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'action_controllers'
newline|'\n'
nl|'\n'
DECL|member|_response_ext_controllers
dedent|''
name|'def'
name|'_response_ext_controllers'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'ext_mgr'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dict of ResponseExtensionController-s by collection."""'
newline|'\n'
name|'response_ext_controllers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'resp_ext'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_response_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'resp_ext'
op|'.'
name|'key'
name|'in'
name|'response_ext_controllers'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'controller'
op|'='
name|'ResponseExtensionController'
op|'('
name|'application'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
name|'resp_ext'
op|'.'
name|'url_route'
op|'+'
string|"'.:(format)'"
op|','
nl|'\n'
name|'action'
op|'='
string|"'process'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'resp_ext'
op|'.'
name|'conditions'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
name|'resp_ext'
op|'.'
name|'url_route'
op|','
nl|'\n'
name|'action'
op|'='
string|"'process'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'resp_ext'
op|'.'
name|'conditions'
op|')'
newline|'\n'
name|'response_ext_controllers'
op|'['
name|'resp_ext'
op|'.'
name|'key'
op|']'
op|'='
name|'controller'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'response_ext_controllers'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'ext_mgr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'ext_mgr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'ext_mgr'
op|'='
name|'ExtensionManager'
op|'('
name|'FLAGS'
op|'.'
name|'osapi_extensions_path'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
newline|'\n'
nl|'\n'
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# extended resources'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_resources'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extended resource: %s'"
op|')'
op|','
nl|'\n'
name|'resource'
op|'.'
name|'collection'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
name|'resource'
op|'.'
name|'collection'
op|','
name|'resource'
op|'.'
name|'collection'
op|','
nl|'\n'
name|'controller'
op|'='
name|'resource'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'collection'
op|'='
name|'resource'
op|'.'
name|'collection_actions'
op|','
nl|'\n'
name|'member'
op|'='
name|'resource'
op|'.'
name|'member_actions'
op|','
nl|'\n'
name|'parent_resource'
op|'='
name|'resource'
op|'.'
name|'parent'
op|')'
newline|'\n'
nl|'\n'
comment|'# extended actions'
nl|'\n'
dedent|''
name|'action_controllers'
op|'='
name|'self'
op|'.'
name|'_action_ext_controllers'
op|'('
name|'application'
op|','
name|'ext_mgr'
op|','
nl|'\n'
name|'mapper'
op|')'
newline|'\n'
name|'for'
name|'action'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_actions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extended action: %s'"
op|')'
op|','
name|'action'
op|'.'
name|'action_name'
op|')'
newline|'\n'
name|'controller'
op|'='
name|'action_controllers'
op|'['
name|'action'
op|'.'
name|'collection'
op|']'
newline|'\n'
name|'controller'
op|'.'
name|'add_action'
op|'('
name|'action'
op|'.'
name|'action_name'
op|','
name|'action'
op|'.'
name|'handler'
op|')'
newline|'\n'
nl|'\n'
comment|'# extended responses'
nl|'\n'
dedent|''
name|'resp_controllers'
op|'='
name|'self'
op|'.'
name|'_response_ext_controllers'
op|'('
name|'application'
op|','
name|'ext_mgr'
op|','
nl|'\n'
name|'mapper'
op|')'
newline|'\n'
name|'for'
name|'response_ext'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_response_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extended response: %s'"
op|')'
op|','
name|'response_ext'
op|'.'
name|'key'
op|')'
newline|'\n'
name|'controller'
op|'='
name|'resp_controllers'
op|'['
name|'response_ext'
op|'.'
name|'key'
op|']'
newline|'\n'
name|'controller'
op|'.'
name|'add_handler'
op|'('
name|'response_ext'
op|'.'
name|'handler'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_router'
op|'='
name|'routes'
op|'.'
name|'middleware'
op|'.'
name|'RoutesMiddleware'
op|'('
name|'self'
op|'.'
name|'_dispatch'
op|','
nl|'\n'
name|'mapper'
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'ExtensionMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
op|')'
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
string|'"""Route the incoming request with router."""'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'extended.app'"
op|']'
op|'='
name|'self'
op|'.'
name|'application'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_router'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|_dispatch
name|'def'
name|'_dispatch'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Dispatch the request.\n\n        Returns the routed WSGI app\'s response or defers to the extended\n        application.\n\n        """'
newline|'\n'
name|'match'
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
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'extended.app'"
op|']'
newline|'\n'
dedent|''
name|'app'
op|'='
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'return'
name|'app'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionManager
dedent|''
dedent|''
name|'class'
name|'ExtensionManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Load extensions from the configured extension path.\n\n    See nova/tests/api/openstack/extensions/foxinsocks/extension.py for an\n    example extension implementation.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Initializing extension manager.'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_load_all_extensions'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of ResourceExtension objects."""'
newline|'\n'
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'ResourceExtension'
op|'('
string|"'extensions'"
op|','
nl|'\n'
name|'ExtensionController'
op|'('
name|'self'
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'alias'
op|','
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'resources'
op|'.'
name|'extend'
op|'('
name|'ext'
op|'.'
name|'get_resources'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# NOTE(dprince): Extension aren't required to have resource"
nl|'\n'
comment|'# extensions'
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of ActionExtension objects."""'
newline|'\n'
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'alias'
op|','
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'actions'
op|'.'
name|'extend'
op|'('
name|'ext'
op|'.'
name|'get_actions'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# NOTE(dprince): Extension aren't required to have action"
nl|'\n'
comment|'# extensions'
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'actions'
newline|'\n'
nl|'\n'
DECL|member|get_response_extensions
dedent|''
name|'def'
name|'get_response_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of ResponseExtension objects."""'
newline|'\n'
name|'response_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'alias'
op|','
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'response_exts'
op|'.'
name|'extend'
op|'('
name|'ext'
op|'.'
name|'get_response_extensions'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# NOTE(dprince): Extension aren't required to have response"
nl|'\n'
comment|'# extensions'
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'response_exts'
newline|'\n'
nl|'\n'
DECL|member|_check_extension
dedent|''
name|'def'
name|'_check_extension'
op|'('
name|'self'
op|','
name|'extension'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks for required methods in extension objects."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ext name: %s'"
op|')'
op|','
name|'extension'
op|'.'
name|'get_name'
op|'('
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ext alias: %s'"
op|')'
op|','
name|'extension'
op|'.'
name|'get_alias'
op|'('
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ext description: %s'"
op|')'
op|','
name|'extension'
op|'.'
name|'get_description'
op|'('
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ext namespace: %s'"
op|')'
op|','
name|'extension'
op|'.'
name|'get_namespace'
op|'('
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ext updated: %s'"
op|')'
op|','
name|'extension'
op|'.'
name|'get_updated'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Exception loading extension: %s"'
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_all_extensions
dedent|''
dedent|''
name|'def'
name|'_load_all_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Load extensions from the configured path.\n\n        Load extensions from the configured path. The extension name is\n        constructed from the module_name. If your extension module was named\n        widgets.py the extension class within that module should be\n        \'Widgets\'.\n\n        In addition, extensions are loaded from the \'contrib\' directory.\n\n        See nova/tests/api/openstack/extensions/foxinsocks.py for an example\n        extension implementation.\n\n        """'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_load_all_extensions_from_path'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'contrib_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|'"contrib"'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'contrib_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_load_all_extensions_from_path'
op|'('
name|'contrib_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_all_extensions_from_path
dedent|''
dedent|''
name|'def'
name|'_load_all_extensions_from_path'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'f'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Loading extension file: %s'"
op|')'
op|','
name|'f'
op|')'
newline|'\n'
name|'mod_name'
op|','
name|'file_ext'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'splitext'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'f'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'ext_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'f'
op|')'
newline|'\n'
name|'if'
name|'file_ext'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'.py'"
name|'and'
name|'not'
name|'mod_name'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'mod'
op|'='
name|'imp'
op|'.'
name|'load_source'
op|'('
name|'mod_name'
op|','
name|'ext_path'
op|')'
newline|'\n'
name|'ext_name'
op|'='
name|'mod_name'
op|'['
number|'0'
op|']'
op|'.'
name|'upper'
op|'('
op|')'
op|'+'
name|'mod_name'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'new_ext_class'
op|'='
name|'getattr'
op|'('
name|'mod'
op|','
name|'ext_name'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'new_ext_class'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Did not find expected name '"
nl|'\n'
string|'\'"%(ext_name)s" in %(file)s\''
op|')'
op|','
nl|'\n'
op|'{'
string|"'ext_name'"
op|':'
name|'ext_name'
op|','
nl|'\n'
string|"'file'"
op|':'
name|'ext_path'
op|'}'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'new_ext'
op|'='
name|'new_ext_class'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_extension'
op|'('
name|'new_ext'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_extension'
op|'('
name|'new_ext'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_extension
dedent|''
dedent|''
dedent|''
name|'def'
name|'_add_extension'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'alias'
op|'='
name|'ext'
op|'.'
name|'get_alias'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Loaded extension: %s'"
op|')'
op|','
name|'alias'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_check_extension'
op|'('
name|'ext'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'alias'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Found duplicate extension: %s"'
op|'%'
name|'alias'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'extensions'
op|'['
name|'alias'
op|']'
op|'='
name|'ext'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResponseExtension
dedent|''
dedent|''
name|'class'
name|'ResponseExtension'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add data to responses from core nova OpenStack API controllers."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'url_route'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'url_route'
op|'='
name|'url_route'
newline|'\n'
name|'self'
op|'.'
name|'handler'
op|'='
name|'handler'
newline|'\n'
name|'self'
op|'.'
name|'conditions'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
op|'['
name|'method'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'key'
op|'='
string|'"%s-%s"'
op|'%'
op|'('
name|'method'
op|','
name|'url_route'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ActionExtension
dedent|''
dedent|''
name|'class'
name|'ActionExtension'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add custom actions to core nova OpenStack API controllers."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'collection'
op|','
name|'action_name'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'collection'
op|'='
name|'collection'
newline|'\n'
name|'self'
op|'.'
name|'action_name'
op|'='
name|'action_name'
newline|'\n'
name|'self'
op|'.'
name|'handler'
op|'='
name|'handler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourceExtension
dedent|''
dedent|''
name|'class'
name|'ResourceExtension'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add top level resources to the OpenStack API in nova."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'collection'
op|','
name|'controller'
op|','
name|'parent'
op|'='
name|'None'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
op|'}'
op|','
name|'member_actions'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'collection'
op|'='
name|'collection'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'controller'
newline|'\n'
name|'self'
op|'.'
name|'parent'
op|'='
name|'parent'
newline|'\n'
name|'self'
op|'.'
name|'collection_actions'
op|'='
name|'collection_actions'
newline|'\n'
name|'self'
op|'.'
name|'member_actions'
op|'='
name|'member_actions'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
