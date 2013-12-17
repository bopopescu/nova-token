begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'contextlib'
newline|'\n'
name|'import'
name|'cPickle'
name|'as'
name|'pickle'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'xmlrpclib'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'queue'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'timeout'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
op|'.'
name|'objects'
name|'import'
name|'aggregate'
name|'as'
name|'aggregate_obj'
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
name|'versionutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'pool'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'pool_states'
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
DECL|variable|xenapi_session_opts
name|'xenapi_session_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'login_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'xenapi_login_timeout'"
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Timeout in seconds for XenAPI login.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'connection_concurrent'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'xenapi_connection_concurrent'"
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum number of concurrent XenAPI connections. '"
nl|'\n'
string|"'Used only if compute_driver=xenapi.XenAPIDriver'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'xenapi_session_opts'
op|','
string|"'xenserver'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPISession
name|'class'
name|'XenAPISession'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The session to invoke XenAPI SDK calls."""'
newline|'\n'
nl|'\n'
comment|'# This is not a config option as it should only ever be'
nl|'\n'
comment|'# changed in development environments.'
nl|'\n'
comment|'# MAJOR VERSION: Incompatible changes with the plugins'
nl|'\n'
comment|'# MINOR VERSION: Compatible changes, new plguins, etc'
nl|'\n'
DECL|variable|PLUGIN_REQUIRED_VERSION
name|'PLUGIN_REQUIRED_VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'import'
name|'XenAPI'
newline|'\n'
name|'self'
op|'.'
name|'XenAPI'
op|'='
name|'XenAPI'
newline|'\n'
name|'self'
op|'.'
name|'_sessions'
op|'='
name|'queue'
op|'.'
name|'Queue'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'is_slave'
op|'='
name|'False'
newline|'\n'
name|'exception'
op|'='
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'_'
op|'('
string|'"Unable to log in to XenAPI "'
nl|'\n'
string|'"(is the Dom0 disk full?)"'
op|')'
op|')'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_create_first_session'
op|'('
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|','
name|'exception'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_populate_session_pool'
op|'('
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|','
name|'exception'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_uuid'
op|'='
name|'self'
op|'.'
name|'_get_host_uuid'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_ref'
op|'='
name|'self'
op|'.'
name|'_get_host_ref'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'product_version'
op|','
name|'self'
op|'.'
name|'product_brand'
op|'='
name|'self'
op|'.'
name|'_get_product_version_and_brand'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_plugin_version'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_plugin_version
dedent|''
name|'def'
name|'_verify_plugin_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'requested_version'
op|'='
name|'self'
op|'.'
name|'PLUGIN_REQUIRED_VERSION'
newline|'\n'
name|'current_version'
op|'='
name|'self'
op|'.'
name|'call_plugin_serialized'
op|'('
nl|'\n'
string|"'nova_plugin_version'"
op|','
string|"'get_version'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'versionutils'
op|'.'
name|'is_compatible'
op|'('
name|'requested_version'
op|','
name|'current_version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Plugin version mismatch (Expected %(exp)s, got %(got)s)"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'exp'"
op|':'
name|'requested_version'
op|','
string|"'got'"
op|':'
name|'current_version'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_first_session
dedent|''
dedent|''
name|'def'
name|'_create_first_session'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'self'
op|'.'
name|'_create_session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'with'
name|'timeout'
op|'.'
name|'Timeout'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'login_timeout'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'session'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
comment|"# if user and pw of the master are different, we're doomed!"
nl|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'HOST_IS_SLAVE'"
op|':'
newline|'\n'
indent|'                '
name|'master'
op|'='
name|'e'
op|'.'
name|'details'
op|'['
number|'1'
op|']'
newline|'\n'
name|'url'
op|'='
name|'pool'
op|'.'
name|'swap_xapi_host'
op|'('
name|'url'
op|','
name|'master'
op|')'
newline|'\n'
name|'session'
op|'='
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'is_slave'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_sessions'
op|'.'
name|'put'
op|'('
name|'session'
op|')'
newline|'\n'
name|'return'
name|'url'
newline|'\n'
nl|'\n'
DECL|member|_populate_session_pool
dedent|''
name|'def'
name|'_populate_session_pool'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_concurrent'
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'self'
op|'.'
name|'_create_session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'with'
name|'timeout'
op|'.'
name|'Timeout'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'login_timeout'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'session'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_sessions'
op|'.'
name|'put'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_host_uuid
dedent|''
dedent|''
name|'def'
name|'_get_host_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'is_slave'
op|':'
newline|'\n'
indent|'            '
name|'aggr'
op|'='
name|'aggregate_obj'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_host'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'host'
op|','
name|'key'
op|'='
name|'pool_states'
op|'.'
name|'POOL_FLAG'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'aggr'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Host is member of a pool, but DB '"
nl|'\n'
string|"'says otherwise'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AggregateHostNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'aggr'
op|'.'
name|'metadetails'
op|'['
name|'CONF'
op|'.'
name|'host'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'self'
op|'.'
name|'_get_session'
op|'('
op|')'
name|'as'
name|'session'
op|':'
newline|'\n'
indent|'                '
name|'host_ref'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'session'
op|'.'
name|'get_this_host'
op|'('
name|'session'
op|'.'
name|'handle'
op|')'
newline|'\n'
name|'return'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'host'
op|'.'
name|'get_uuid'
op|'('
name|'host_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_product_version_and_brand
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_product_version_and_brand'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a tuple of (major, minor, rev) for the host version and\n        a string of the product brand.\n        """'
newline|'\n'
name|'software_version'
op|'='
name|'self'
op|'.'
name|'_get_software_version'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'product_version_str'
op|'='
name|'software_version'
op|'.'
name|'get'
op|'('
string|"'product_version'"
op|')'
newline|'\n'
comment|'# Product version is only set in some cases (e.g. XCP, XenServer) and'
nl|'\n'
comment|'# not in others (e.g. xenserver-core, XAPI-XCP).'
nl|'\n'
comment|'# In these cases, the platform version is the best number to use.'
nl|'\n'
name|'if'
name|'product_version_str'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'product_version_str'
op|'='
name|'software_version'
op|'.'
name|'get'
op|'('
string|"'platform_version'"
op|','
nl|'\n'
string|"'0.0.0'"
op|')'
newline|'\n'
dedent|''
name|'product_brand'
op|'='
name|'software_version'
op|'.'
name|'get'
op|'('
string|"'product_brand'"
op|')'
newline|'\n'
name|'product_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'product_version_str'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'product_version'
op|','
name|'product_brand'
newline|'\n'
nl|'\n'
DECL|member|_get_software_version
dedent|''
name|'def'
name|'_get_software_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call_xenapi'
op|'('
string|"'host.get_software_version'"
op|','
name|'self'
op|'.'
name|'host_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_session_id
dedent|''
name|'def'
name|'get_session_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a string session_id.  Used for vnc consoles."""'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'_get_session'
op|'('
op|')'
name|'as'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'session'
op|'.'
name|'_session'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|member|_get_session
name|'def'
name|'_get_session'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return exclusive session for scope of with statement."""'
newline|'\n'
name|'session'
op|'='
name|'self'
op|'.'
name|'_sessions'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'session'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_sessions'
op|'.'
name|'put'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_host_ref
dedent|''
dedent|''
name|'def'
name|'_get_host_ref'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the xenapi host on which nova-compute runs on."""'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'_get_session'
op|'('
op|')'
name|'as'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'host'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'host_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_xenapi
dedent|''
dedent|''
name|'def'
name|'call_xenapi'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the specified XenAPI method on a background thread."""'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'_get_session'
op|'('
op|')'
name|'as'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'xenapi_request'
op|'('
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_plugin
dedent|''
dedent|''
name|'def'
name|'call_plugin'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call host.call_plugin on a background thread."""'
newline|'\n'
comment|'# NOTE(armando): pass the host uuid along with the args so that'
nl|'\n'
comment|'# the plugin gets executed on the right host when using XS pools'
nl|'\n'
name|'args'
op|'['
string|"'host_uuid'"
op|']'
op|'='
name|'self'
op|'.'
name|'host_uuid'
newline|'\n'
nl|'\n'
name|'with'
name|'self'
op|'.'
name|'_get_session'
op|'('
op|')'
name|'as'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_unwrap_plugin_exceptions'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'host'
op|'.'
name|'call_plugin'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host_ref'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_plugin_serialized
dedent|''
dedent|''
name|'def'
name|'call_plugin_serialized'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
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
name|'params'
op|'='
op|'{'
string|"'params'"
op|':'
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'dict'
op|'('
name|'args'
op|'='
name|'args'
op|','
name|'kwargs'
op|'='
name|'kwargs'
op|')'
op|')'
op|'}'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'call_plugin'
op|'('
name|'plugin'
op|','
name|'fn'
op|','
name|'params'
op|')'
newline|'\n'
name|'return'
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'rv'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_plugin_serialized_with_retry
dedent|''
name|'def'
name|'call_plugin_serialized_with_retry'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'num_retries'
op|','
nl|'\n'
name|'callback'
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
string|'"""Allows a plugin to raise RetryableError so we can try again."""'
newline|'\n'
name|'attempts'
op|'='
name|'num_retries'
op|'+'
number|'1'
newline|'\n'
name|'sleep_time'
op|'='
number|'0.5'
newline|'\n'
name|'for'
name|'attempt'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'attempts'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'%(plugin)s.%(fn)s attempt %(attempt)d/%(attempts)d'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'plugin'"
op|':'
name|'plugin'
op|','
string|"'fn'"
op|':'
name|'fn'
op|','
string|"'attempt'"
op|':'
name|'attempt'
op|','
nl|'\n'
string|"'attempts'"
op|':'
name|'attempts'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'attempt'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'time'
op|'.'
name|'sleep'
op|'('
name|'sleep_time'
op|')'
newline|'\n'
name|'sleep_time'
op|'='
name|'min'
op|'('
number|'2'
op|'*'
name|'sleep_time'
op|','
number|'15'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'callback'
op|':'
newline|'\n'
indent|'                    '
name|'callback'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'call_plugin_serialized'
op|'('
name|'plugin'
op|','
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'.'
name|'_is_retryable_exception'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'%(plugin)s.%(fn)s failed. Retrying call.'"
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'plugin'"
op|':'
name|'plugin'
op|','
string|"'fn'"
op|':'
name|'fn'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'PluginRetriesExceeded'
op|'('
name|'num_retries'
op|'='
name|'num_retries'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_is_retryable_exception
dedent|''
name|'def'
name|'_is_retryable_exception'
op|'('
name|'self'
op|','
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_type'
op|','
name|'method'
op|','
name|'error'
op|'='
name|'exc'
op|'.'
name|'details'
op|'['
op|':'
number|'3'
op|']'
newline|'\n'
name|'if'
name|'error'
op|'=='
string|"'RetryableError'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"RetryableError, so retrying upload_vhd"'
op|')'
op|','
nl|'\n'
name|'exc_info'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
string|'"signal"'
name|'in'
name|'method'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Error due to a signal, retrying upload_vhd"'
op|')'
op|','
nl|'\n'
name|'exc_info'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_create_session
dedent|''
dedent|''
name|'def'
name|'_create_session'
op|'('
name|'self'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stubout point. This can be replaced with a mock session."""'
newline|'\n'
name|'self'
op|'.'
name|'is_local_connection'
op|'='
name|'url'
op|'=='
string|'"unix://local"'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'is_local_connection'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'xapi_local'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_unwrap_plugin_exceptions
dedent|''
name|'def'
name|'_unwrap_plugin_exceptions'
op|'('
name|'self'
op|','
name|'func'
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
string|'"""Parse exception details."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'func'
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
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got exception: %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'exc'
op|'.'
name|'details'
op|')'
op|'=='
number|'4'
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'XENAPI_PLUGIN_EXCEPTION'"
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'2'
op|']'
op|'=='
string|"'Failure'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# FIXME(comstud): eval is evil.'
nl|'\n'
indent|'                    '
name|'params'
op|'='
name|'eval'
op|'('
name|'exc'
op|'.'
name|'details'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exc'
newline|'\n'
dedent|''
name|'raise'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'xmlrpclib'
op|'.'
name|'ProtocolError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got exception: %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|get_rec
dedent|''
dedent|''
name|'def'
name|'get_rec'
op|'('
name|'self'
op|','
name|'record_type'
op|','
name|'ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'call_xenapi'
op|'('
string|"'%s.get_record'"
op|'%'
name|'record_type'
op|','
name|'ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'HANDLE_INVALID'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_all_refs_and_recs
dedent|''
name|'def'
name|'get_all_refs_and_recs'
op|'('
name|'self'
op|','
name|'record_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve all refs and recs for a Xen record type.\n\n        Handles race-conditions where the record may be deleted between\n        the `get_all` call and the `get_record` call.\n        """'
newline|'\n'
nl|'\n'
name|'for'
name|'ref'
name|'in'
name|'self'
op|'.'
name|'call_xenapi'
op|'('
string|"'%s.get_all'"
op|'%'
name|'record_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rec'
op|'='
name|'self'
op|'.'
name|'get_rec'
op|'('
name|'record_type'
op|','
name|'ref'
op|')'
newline|'\n'
comment|'# Check to make sure the record still exists. It may have'
nl|'\n'
comment|'# been deleted between the get_all call and get_record call'
nl|'\n'
name|'if'
name|'rec'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'ref'
op|','
name|'rec'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
