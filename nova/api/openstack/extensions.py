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
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'as'
name|'base_wsgi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
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
DECL|member|get_request_extensions
dedent|''
name|'def'
name|'get_request_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List of extensions.RequestException extension objects.\n\n        Request extensions are used to handle custom request data.\n\n        """'
newline|'\n'
name|'request_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'request_exts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ActionExtensionController
dedent|''
dedent|''
name|'class'
name|'ActionExtensionController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
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
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'body'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'handler'
op|'('
name|'body'
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
DECL|class|ActionExtensionResource
dedent|''
dedent|''
name|'class'
name|'ActionExtensionResource'
op|'('
name|'wsgi'
op|'.'
name|'Resource'
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
name|'controller'
op|'='
name|'ActionExtensionController'
op|'('
name|'application'
op|')'
newline|'\n'
name|'wsgi'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|')'
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
name|'controller'
op|'.'
name|'add_action'
op|'('
name|'action_name'
op|','
name|'handler'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestExtensionController
dedent|''
dedent|''
name|'class'
name|'RequestExtensionController'
op|'('
name|'object'
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
comment|'# currently request handlers are un-ordered'
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
name|'req'
op|','
name|'res'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestExtensionResource
dedent|''
dedent|''
name|'class'
name|'RequestExtensionResource'
op|'('
name|'wsgi'
op|'.'
name|'Resource'
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
name|'controller'
op|'='
name|'RequestExtensionController'
op|'('
name|'application'
op|')'
newline|'\n'
name|'wsgi'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|')'
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
name|'controller'
op|'.'
name|'add_handler'
op|'('
name|'handler'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionsResource
dedent|''
dedent|''
name|'class'
name|'ExtensionsResource'
op|'('
name|'wsgi'
op|'.'
name|'Resource'
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
name|'dict'
op|'('
name|'extension'
op|'='
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
op|')'
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
name|'base_wsgi'
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
DECL|member|_action_ext_resources
dedent|''
name|'def'
name|'_action_ext_resources'
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
string|'"""Return a dict of ActionExtensionResource-s by collection."""'
newline|'\n'
name|'action_resources'
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
name|'action_resources'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'resource'
op|'='
name|'ActionExtensionResource'
op|'('
name|'application'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/:(tenant_id)/%s/:(id)/action.:(format)"'
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
name|'resource'
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
string|'"/:(tenant_id)/%s/:(id)/action"'
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
name|'resource'
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
name|'action_resources'
op|'['
name|'action'
op|'.'
name|'collection'
op|']'
op|'='
name|'resource'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'action_resources'
newline|'\n'
nl|'\n'
DECL|member|_request_ext_resources
dedent|''
name|'def'
name|'_request_ext_resources'
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
string|'"""Returns a dict of RequestExtensionResource-s by collection."""'
newline|'\n'
name|'request_ext_resources'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'req_ext'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_request_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'req_ext'
op|'.'
name|'key'
name|'in'
name|'request_ext_resources'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'resource'
op|'='
name|'RequestExtensionResource'
op|'('
name|'application'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
name|'req_ext'
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
name|'resource'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'req_ext'
op|'.'
name|'conditions'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
name|'req_ext'
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
name|'resource'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'req_ext'
op|'.'
name|'conditions'
op|')'
newline|'\n'
name|'request_ext_resources'
op|'['
name|'req_ext'
op|'.'
name|'key'
op|']'
op|'='
name|'resource'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'request_ext_resources'
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
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'TenantMapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
nl|'\n'
op|'{'
string|"'application/xml'"
op|':'
name|'ExtensionsXMLSerializer'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
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
name|'kargs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'controller'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
nl|'\n'
name|'resource'
op|'.'
name|'controller'
op|','
name|'serializer'
op|'='
name|'serializer'
op|')'
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
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'resource'
op|'.'
name|'parent'
op|':'
newline|'\n'
indent|'                '
name|'kargs'
op|'['
string|"'parent_resource'"
op|']'
op|'='
name|'resource'
op|'.'
name|'parent'
newline|'\n'
nl|'\n'
dedent|''
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
op|'**'
name|'kargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# extended actions'
nl|'\n'
dedent|''
name|'action_resources'
op|'='
name|'self'
op|'.'
name|'_action_ext_resources'
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
name|'resource'
op|'='
name|'action_resources'
op|'['
name|'action'
op|'.'
name|'collection'
op|']'
newline|'\n'
name|'resource'
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
comment|'# extended requests'
nl|'\n'
dedent|''
name|'req_controllers'
op|'='
name|'self'
op|'.'
name|'_request_ext_resources'
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
name|'request_ext'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_request_extensions'
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
string|"'Extended request: %s'"
op|')'
op|','
name|'request_ext'
op|'.'
name|'key'
op|')'
newline|'\n'
name|'controller'
op|'='
name|'req_controllers'
op|'['
name|'request_ext'
op|'.'
name|'key'
op|']'
newline|'\n'
name|'controller'
op|'.'
name|'add_handler'
op|'('
name|'request_ext'
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
name|'ExtensionsResource'
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
DECL|member|get_request_extensions
dedent|''
name|'def'
name|'get_request_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of RequestExtension objects."""'
newline|'\n'
name|'request_exts'
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
name|'request_exts'
op|'.'
name|'extend'
op|'('
name|'ext'
op|'.'
name|'get_request_extensions'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# NOTE(dprince): Extension aren't required to have request"
nl|'\n'
comment|'# extensions'
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'request_exts'
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
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_load_all_extensions
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
name|'add_extension'
op|'('
name|'new_ext'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_extension
dedent|''
dedent|''
dedent|''
name|'def'
name|'add_extension'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
comment|"# Do nothing if the extension doesn't check out"
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_check_extension'
op|'('
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
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
DECL|class|RequestExtension
dedent|''
dedent|''
name|'class'
name|'RequestExtension'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extend requests and responses of core nova OpenStack API resources.\n\n    Provide a way to add data to responses and handle custom request data\n    that is sent to core nova OpenStack API controllers.\n\n    """'
newline|'\n'
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
string|'"""Add custom actions to core nova OpenStack API resources."""'
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
nl|'\n'
nl|'\n'
DECL|class|ExtensionsXMLSerializer
dedent|''
dedent|''
name|'class'
name|'ExtensionsXMLSerializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|NSMAP
indent|'    '
name|'NSMAP'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'ext_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'extension'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_populate_ext'
op|'('
name|'ext'
op|','
name|'ext_dict'
op|'['
string|"'extension'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_to_xml'
op|'('
name|'ext'
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
name|'exts_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exts'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'extensions'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'for'
name|'ext_dict'
name|'in'
name|'exts_dict'
op|'['
string|"'extensions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'ext'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'exts'
op|','
string|"'extension'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_populate_ext'
op|'('
name|'ext'
op|','
name|'ext_dict'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_to_xml'
op|'('
name|'exts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_populate_ext
dedent|''
name|'def'
name|'_populate_ext'
op|'('
name|'self'
op|','
name|'ext_elem'
op|','
name|'ext_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Populate an extension xml element from a dict."""'
newline|'\n'
nl|'\n'
name|'ext_elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|','
name|'ext_dict'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'ext_elem'
op|'.'
name|'set'
op|'('
string|"'namespace'"
op|','
name|'ext_dict'
op|'['
string|"'namespace'"
op|']'
op|')'
newline|'\n'
name|'ext_elem'
op|'.'
name|'set'
op|'('
string|"'alias'"
op|','
name|'ext_dict'
op|'['
string|"'alias'"
op|']'
op|')'
newline|'\n'
name|'ext_elem'
op|'.'
name|'set'
op|'('
string|"'updated'"
op|','
name|'ext_dict'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
name|'desc'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'description'"
op|')'
newline|'\n'
name|'desc'
op|'.'
name|'text'
op|'='
name|'ext_dict'
op|'['
string|"'description'"
op|']'
newline|'\n'
name|'ext_elem'
op|'.'
name|'append'
op|'('
name|'desc'
op|')'
newline|'\n'
name|'for'
name|'link'
name|'in'
name|'ext_dict'
op|'.'
name|'get'
op|'('
string|"'links'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'ext_elem'
op|','
string|"'{%s}link'"
op|'%'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'rel'"
op|','
name|'link'
op|'['
string|"'rel'"
op|']'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'href'"
op|','
name|'link'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
name|'link'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ext_elem'
newline|'\n'
nl|'\n'
DECL|member|_to_xml
dedent|''
name|'def'
name|'_to_xml'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert the xml object to an xml string."""'
newline|'\n'
nl|'\n'
name|'return'
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
op|','
name|'encoding'
op|'='
string|"'UTF-8'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
