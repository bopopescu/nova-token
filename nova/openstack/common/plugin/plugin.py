begin_unit
comment|'# Copyright 2012 OpenStack Foundation.'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
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
nl|'\n'
nl|'\n'
DECL|class|Plugin
name|'class'
name|'Plugin'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Defines an interface for adding functionality to an OpenStack service.\n\n    A plugin interacts with a service via the following pathways:\n\n    - An optional set of notifiers, managed by calling add_notifier()\n      or by overriding _notifiers()\n\n    - A set of api extensions, managed via add_api_extension_descriptor()\n\n    - Direct calls to service functions.\n\n    - Whatever else the plugin wants to do on its own.\n\n    This is the reference implementation.\n    """'
newline|'\n'
nl|'\n'
comment|'# The following functions are provided as convenience methods'
nl|'\n'
comment|'# for subclasses.  Subclasses should call them but probably not'
nl|'\n'
comment|'# override them.'
nl|'\n'
DECL|member|_add_api_extension_descriptor
name|'def'
name|'_add_api_extension_descriptor'
op|'('
name|'self'
op|','
name|'descriptor'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Subclass convenience method which adds an extension descriptor.\n\n           Subclass constructors should call this method when\n           extending a project\'s REST interface.\n\n           Note that once the api service has loaded, the\n           API extension set is more-or-less fixed, so\n           this should mainly be called by subclass constructors.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_api_extension_descriptors'
op|'.'
name|'append'
op|'('
name|'descriptor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_notifier
dedent|''
name|'def'
name|'_add_notifier'
op|'('
name|'self'
op|','
name|'notifier'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Subclass convenience method which adds a notifier.\n\n           Notifier objects should implement the function notify(message).\n           Each notifier receives a notify() call whenever an openstack\n           service broadcasts a notification.\n\n           Best to call this during construction.  Notifiers are enumerated\n           and registered by the pluginmanager at plugin load time.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_notifiers'
op|'.'
name|'append'
op|'('
name|'notifier'
op|')'
newline|'\n'
nl|'\n'
comment|'# The following methods are called by OpenStack services to query'
nl|'\n'
comment|'#  plugin features.  Subclasses should probably not override these.'
nl|'\n'
DECL|member|_notifiers
dedent|''
name|'def'
name|'_notifiers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns list of notifiers for this plugin."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_notifiers'
newline|'\n'
nl|'\n'
DECL|variable|notifiers
dedent|''
name|'notifiers'
op|'='
name|'property'
op|'('
name|'_notifiers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_api_extension_descriptors
name|'def'
name|'_api_extension_descriptors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of API extension descriptors.\n\n           Called by a project API during its load sequence.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_api_extension_descriptors'
newline|'\n'
nl|'\n'
DECL|variable|api_extension_descriptors
dedent|''
name|'api_extension_descriptors'
op|'='
name|'property'
op|'('
name|'_api_extension_descriptors'
op|')'
newline|'\n'
nl|'\n'
comment|'# Most plugins will override this:'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'service_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_notifiers'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_api_extension_descriptors'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
