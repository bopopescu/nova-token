begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'abc'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
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
name|'import'
name|'nova'
op|'.'
name|'policy'
newline|'\n'
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
comment|"# The name of the extension, e.g., 'Fox In Socks'"
nl|'\n'
DECL|variable|name
name|'name'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|"# The alias for the extension, e.g., 'FOXNSOX'"
nl|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# Description comes from the docstring for the class'
nl|'\n'
nl|'\n'
comment|'# The XML namespace for the extension, e.g.,'
nl|'\n'
comment|"# 'http://www.fox.in.socks/api/ext/pie/v1.0'"
nl|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# The timestamp when the extension was last updated, e.g.,'
nl|'\n'
comment|"# '2011-01-22T19:25:27Z'"
nl|'\n'
DECL|variable|updated
name|'updated'
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
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Register extension with the extension manager."""'
newline|'\n'
nl|'\n'
name|'ext_mgr'
op|'.'
name|'register'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
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
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List of extensions.ControllerExtension extension objects.\n\n        Controller extensions are used to extend existing controllers.\n        """'
newline|'\n'
name|'controller_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'controller_exts'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|nsmap
name|'def'
name|'nsmap'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Synthesize a namespace map from extension."""'
newline|'\n'
nl|'\n'
comment|'# Start with a base nsmap'
nl|'\n'
name|'nsmap'
op|'='
name|'ext_nsmap'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Add the namespace for the extension'
nl|'\n'
name|'nsmap'
op|'['
name|'cls'
op|'.'
name|'alias'
op|']'
op|'='
name|'cls'
op|'.'
name|'namespace'
newline|'\n'
nl|'\n'
name|'return'
name|'nsmap'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|xmlname
name|'def'
name|'xmlname'
op|'('
name|'cls'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Synthesize element and attribute names."""'
newline|'\n'
nl|'\n'
name|'return'
string|"'{%s}%s'"
op|'%'
op|'('
name|'cls'
op|'.'
name|'namespace'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_ext
dedent|''
dedent|''
name|'def'
name|'make_ext'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'namespace'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'alias'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'updated'"
op|')'
newline|'\n'
nl|'\n'
name|'desc'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'description'"
op|')'
newline|'\n'
name|'desc'
op|'.'
name|'text'
op|'='
string|"'description'"
newline|'\n'
nl|'\n'
name|'xmlutil'
op|'.'
name|'make_links'
op|'('
name|'elem'
op|','
string|"'links'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ext_nsmap
dedent|''
name|'ext_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_COMMON_V10'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionTemplate
name|'class'
name|'ExtensionTemplate'
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
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'extension'"
op|','
name|'selector'
op|'='
string|"'extension'"
op|')'
newline|'\n'
name|'make_ext'
op|'('
name|'root'
op|')'
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
name|'ext_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionsTemplate
dedent|''
dedent|''
name|'class'
name|'ExtensionsTemplate'
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
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'extensions'"
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
string|"'extension'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'extensions'"
op|')'
newline|'\n'
name|'make_ext'
op|'('
name|'elem'
op|')'
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
name|'ext_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionsController
dedent|''
dedent|''
name|'class'
name|'ExtensionsController'
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
name|'super'
op|'('
name|'ExtensionsController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'None'
op|')'
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
name|'name'
newline|'\n'
name|'ext_data'
op|'['
string|"'alias'"
op|']'
op|'='
name|'ext'
op|'.'
name|'alias'
newline|'\n'
name|'ext_data'
op|'['
string|"'description'"
op|']'
op|'='
name|'ext'
op|'.'
name|'__doc__'
newline|'\n'
name|'ext_data'
op|'['
string|"'namespace'"
op|']'
op|'='
name|'ext'
op|'.'
name|'namespace'
newline|'\n'
name|'ext_data'
op|'['
string|"'updated'"
op|']'
op|'='
name|'ext'
op|'.'
name|'updated'
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
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ExtensionsTemplate'
op|')'
newline|'\n'
DECL|member|index
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
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extension_manager'
op|'.'
name|'sorted_extensions'
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
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ExtensionTemplate'
op|')'
newline|'\n'
DECL|member|show
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
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|"# NOTE(dprince): the extensions alias is used as the 'id' for show"
nl|'\n'
indent|'            '
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
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
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
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
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
string|'"""Load extensions from the configured extension path.\n\n    See nova/tests/api/openstack/compute/extensions/foxinsocks.py or an\n    example extension implementation.\n\n    """'
newline|'\n'
DECL|member|sorted_extensions
name|'def'
name|'sorted_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'sorted_ext_list'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sorted_ext_list'
op|'='
name|'sorted'
op|'('
name|'self'
op|'.'
name|'extensions'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'_alias'
op|','
name|'ext'
name|'in'
name|'self'
op|'.'
name|'sorted_ext_list'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'ext'
newline|'\n'
nl|'\n'
DECL|member|is_loaded
dedent|''
dedent|''
name|'def'
name|'is_loaded'
op|'('
name|'self'
op|','
name|'alias'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'alias'
name|'in'
name|'self'
op|'.'
name|'extensions'
newline|'\n'
nl|'\n'
DECL|member|register
dedent|''
name|'def'
name|'register'
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
name|'alias'
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
name|'NovaException'
op|'('
string|'"Found duplicate extension: %s"'
nl|'\n'
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
name|'self'
op|'.'
name|'sorted_ext_list'
op|'='
name|'None'
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
nl|'\n'
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
name|'ExtensionsController'
op|'('
name|'self'
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'ext'
name|'in'
name|'self'
op|'.'
name|'sorted_extensions'
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
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of ControllerExtension objects."""'
newline|'\n'
name|'controller_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ext'
name|'in'
name|'self'
op|'.'
name|'sorted_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'get_ext_method'
op|'='
name|'ext'
op|'.'
name|'get_controller_extensions'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# NOTE(Vek): Extensions aren't required to have"
nl|'\n'
comment|'# controller extensions'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'controller_exts'
op|'.'
name|'extend'
op|'('
name|'get_ext_method'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'controller_exts'
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
string|"'Ext name: %s'"
op|','
name|'extension'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext alias: %s'"
op|','
name|'extension'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext description: %s'"
op|','
nl|'\n'
string|"' '"
op|'.'
name|'join'
op|'('
name|'extension'
op|'.'
name|'__doc__'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext namespace: %s'"
op|','
name|'extension'
op|'.'
name|'namespace'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext updated: %s'"
op|','
name|'extension'
op|'.'
name|'updated'
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
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|load_extension
dedent|''
name|'def'
name|'load_extension'
op|'('
name|'self'
op|','
name|'ext_factory'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Execute an extension factory.\n\n        Loads an extension.  The \'ext_factory\' is the name of a\n        callable that will be imported and called with one\n        argument--the extension manager.  The factory callable is\n        expected to call the register() method at least once.\n        """'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Loading extension %s"'
op|','
name|'ext_factory'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'ext_factory'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
comment|'# Load the factory'
nl|'\n'
indent|'            '
name|'factory'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'ext_factory'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'factory'
op|'='
name|'ext_factory'
newline|'\n'
nl|'\n'
comment|'# Call it'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Calling extension factory %s"'
op|','
name|'ext_factory'
op|')'
newline|'\n'
name|'factory'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_extensions
dedent|''
name|'def'
name|'_load_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Load extensions specified on the command line."""'
newline|'\n'
nl|'\n'
name|'extensions'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'cls_list'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'ext_factory'
name|'in'
name|'extensions'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'load_extension'
op|'('
name|'ext_factory'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Failed to load extension %(ext_factory)s: '"
nl|'\n'
string|"'%(exc)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'ext_factory'"
op|':'
name|'ext_factory'
op|','
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerExtension
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'ControllerExtension'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extend core controllers of nova OpenStack API.\n\n    Provide a way to extend existing nova OpenStack API core\n    controllers.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'extension'
op|','
name|'collection'
op|','
name|'controller'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extension'
op|'='
name|'extension'
newline|'\n'
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
op|'='
name|'None'
op|','
name|'parent'
op|'='
name|'None'
op|','
nl|'\n'
name|'collection_actions'
op|'='
name|'None'
op|','
name|'member_actions'
op|'='
name|'None'
op|','
nl|'\n'
name|'custom_routes_fn'
op|'='
name|'None'
op|','
name|'inherits'
op|'='
name|'None'
op|','
name|'member_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'collection_actions'
op|':'
newline|'\n'
indent|'            '
name|'collection_actions'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'member_actions'
op|':'
newline|'\n'
indent|'            '
name|'member_actions'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
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
name|'self'
op|'.'
name|'custom_routes_fn'
op|'='
name|'custom_routes_fn'
newline|'\n'
name|'self'
op|'.'
name|'inherits'
op|'='
name|'inherits'
newline|'\n'
name|'self'
op|'.'
name|'member_name'
op|'='
name|'member_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_standard_extensions
dedent|''
dedent|''
name|'def'
name|'load_standard_extensions'
op|'('
name|'ext_mgr'
op|','
name|'logger'
op|','
name|'path'
op|','
name|'package'
op|','
name|'ext_list'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Registers all standard API extensions."""'
newline|'\n'
nl|'\n'
comment|'# Walk through all the modules in our directory...'
nl|'\n'
name|'our_dir'
op|'='
name|'path'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'dirpath'
op|','
name|'dirnames'
op|','
name|'filenames'
name|'in'
name|'os'
op|'.'
name|'walk'
op|'('
name|'our_dir'
op|')'
op|':'
newline|'\n'
comment|'# Compute the relative package name from the dirpath'
nl|'\n'
indent|'        '
name|'relpath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'relpath'
op|'('
name|'dirpath'
op|','
name|'our_dir'
op|')'
newline|'\n'
name|'if'
name|'relpath'
op|'=='
string|"'.'"
op|':'
newline|'\n'
indent|'            '
name|'relpkg'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'relpkg'
op|'='
string|"'.%s'"
op|'%'
string|"'.'"
op|'.'
name|'join'
op|'('
name|'relpath'
op|'.'
name|'split'
op|'('
name|'os'
op|'.'
name|'sep'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now, consider each file in turn, only considering .py files'
nl|'\n'
dedent|''
name|'for'
name|'fname'
name|'in'
name|'filenames'
op|':'
newline|'\n'
indent|'            '
name|'root'
op|','
name|'ext'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'splitext'
op|'('
name|'fname'
op|')'
newline|'\n'
nl|'\n'
comment|"# Skip __init__ and anything that's not .py"
nl|'\n'
name|'if'
name|'ext'
op|'!='
string|"'.py'"
name|'or'
name|'root'
op|'=='
string|"'__init__'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Try loading it'
nl|'\n'
dedent|''
name|'classname'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'root'
op|'['
number|'0'
op|']'
op|'.'
name|'upper'
op|'('
op|')'
op|','
name|'root'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
name|'classpath'
op|'='
op|'('
string|'"%s%s.%s.%s"'
op|'%'
nl|'\n'
op|'('
name|'package'
op|','
name|'relpkg'
op|','
name|'root'
op|','
name|'classname'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'ext_list'
name|'is'
name|'not'
name|'None'
name|'and'
name|'classname'
name|'not'
name|'in'
name|'ext_list'
op|':'
newline|'\n'
indent|'                '
name|'logger'
op|'.'
name|'debug'
op|'('
string|'"Skipping extension: %s"'
op|'%'
name|'classpath'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'ext_mgr'
op|'.'
name|'load_extension'
op|'('
name|'classpath'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'logger'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Failed to load extension %(classpath)s: '"
nl|'\n'
string|"'%(exc)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'classpath'"
op|':'
name|'classpath'
op|','
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|"# Now, let's consider any subdirectories we may have..."
nl|'\n'
dedent|''
dedent|''
name|'subdirs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'dname'
name|'in'
name|'dirnames'
op|':'
newline|'\n'
comment|'# Skip it if it does not have __init__.py'
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'dirpath'
op|','
name|'dname'
op|','
string|"'__init__.py'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# If it has extension(), delegate...'
nl|'\n'
dedent|''
name|'ext_name'
op|'='
string|'"%s%s.%s.extension"'
op|'%'
op|'('
name|'package'
op|','
name|'relpkg'
op|','
name|'dname'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'ext'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'ext_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
comment|"# extension() doesn't exist on it, so we'll explore"
nl|'\n'
comment|'# the directory for ourselves'
nl|'\n'
indent|'                '
name|'subdirs'
op|'.'
name|'append'
op|'('
name|'dname'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'ext'
op|'('
name|'ext_mgr'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'logger'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Failed to load extension %(ext_name)s:'"
nl|'\n'
string|"'%(exc)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'ext_name'"
op|':'
name|'ext_name'
op|','
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|"# Update the list of directories we'll explore..."
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'dirnames'
op|'['
op|':'
op|']'
op|'='
name|'subdirs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|core_authorizer
dedent|''
dedent|''
name|'def'
name|'core_authorizer'
op|'('
name|'api_name'
op|','
name|'extension_name'
op|')'
op|':'
newline|'\n'
DECL|function|authorize
indent|'    '
name|'def'
name|'authorize'
op|'('
name|'context'
op|','
name|'target'
op|'='
name|'None'
op|','
name|'action'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'target'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'action'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'act'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'api_name'
op|','
name|'extension_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'act'
op|'='
string|"'%s:%s:%s'"
op|'%'
op|'('
name|'api_name'
op|','
name|'extension_name'
op|','
name|'action'
op|')'
newline|'\n'
dedent|''
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'context'
op|','
name|'act'
op|','
name|'target'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'authorize'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extension_authorizer
dedent|''
name|'def'
name|'extension_authorizer'
op|'('
name|'api_name'
op|','
name|'extension_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'core_authorizer'
op|'('
string|"'%s_extension'"
op|'%'
name|'api_name'
op|','
name|'extension_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|soft_extension_authorizer
dedent|''
name|'def'
name|'soft_extension_authorizer'
op|'('
name|'api_name'
op|','
name|'extension_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'hard_authorize'
op|'='
name|'extension_authorizer'
op|'('
name|'api_name'
op|','
name|'extension_name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|authorize
name|'def'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'hard_authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
name|'action'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Forbidden'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'authorize'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_compute_policy
dedent|''
name|'def'
name|'check_compute_policy'
op|'('
name|'context'
op|','
name|'action'
op|','
name|'target'
op|','
name|'scope'
op|'='
string|"'compute'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_action'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'scope'
op|','
name|'action'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'context'
op|','
name|'_action'
op|','
name|'target'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'six'
op|'.'
name|'add_metaclass'
op|'('
name|'abc'
op|'.'
name|'ABCMeta'
op|')'
newline|'\n'
DECL|class|V3APIExtensionBase
name|'class'
name|'V3APIExtensionBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstract base class for all V3 API extensions.\n\n    All V3 API extensions must derive from this class and implement\n    the abstract methods get_resources and get_controller_extensions\n    even if they just return an empty list. The extensions must also\n    define the abstract properties.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'extension_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extension_info'
op|'='
name|'extension_info'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of resources extensions.\n\n        The extensions should return a list of ResourceExtension\n        objects. This list may be empty.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of controller extensions.\n\n        The extensions should return a list of ControllerExtension\n        objects. This list may be empty.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractproperty'
newline|'\n'
DECL|member|name
name|'def'
name|'name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Name of the extension."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractproperty'
newline|'\n'
DECL|member|alias
name|'def'
name|'alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Alias for the extension."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractproperty'
newline|'\n'
DECL|member|version
name|'def'
name|'version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Version of the extension."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|expected_errors
dedent|''
dedent|''
name|'def'
name|'expected_errors'
op|'('
name|'errors'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator for v3 API methods which specifies expected exceptions.\n\n    Specify which exceptions may occur when an API method is called. If an\n    unexpected exception occurs then return a 500 instead and ask the user\n    of the API to file a bug report.\n    """'
newline|'\n'
DECL|function|decorator
name|'def'
name|'decorator'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|wrapped
name|'def'
name|'wrapped'
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
name|'try'
op|':'
newline|'\n'
indent|'                '
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
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'isinstance'
op|'('
name|'exc'
op|','
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'WSGIHTTPException'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'isinstance'
op|'('
name|'errors'
op|','
name|'int'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'t_errors'
op|'='
op|'('
name|'errors'
op|','
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'t_errors'
op|'='
name|'errors'
newline|'\n'
dedent|''
name|'if'
name|'exc'
op|'.'
name|'code'
name|'in'
name|'t_errors'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'exc'
op|','
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|')'
op|':'
newline|'\n'
comment|'# Note(cyeoh): Special case to handle'
nl|'\n'
comment|'# PolicyNotAuthorized exceptions so every'
nl|'\n'
comment|'# extension method does not need to wrap authorize'
nl|'\n'
comment|'# calls. ResourceExceptionHandler silently'
nl|'\n'
comment|'# converts NotAuthorized to HTTPForbidden'
nl|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'exc'
op|','
name|'exception'
op|'.'
name|'ValidationError'
op|')'
op|':'
newline|'\n'
comment|'# Note(oomichi): Handle a validation error, which'
nl|'\n'
comment|'# happens due to invalid API parameters, as an'
nl|'\n'
comment|'# expected error.'
nl|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Unexpected exception in API method"'
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'Unexpected API Error. Please report this at '"
nl|'\n'
string|"'http://bugs.launchpad.net/nova/ and attach the Nova '"
nl|'\n'
string|"'API log if possible.\\n%s'"
op|')'
op|'%'
name|'type'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'decorator'
newline|'\n'
dedent|''
endmarker|''
end_unit
