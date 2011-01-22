begin_unit
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
comment|'#'
nl|'\n'
comment|'# Helper functions for the Nova xapi plugins.  In time, this will merge'
nl|'\n'
comment|'# with the pluginlib.py shipped with xapi, but for now, that file is not'
nl|'\n'
comment|"# very stable, so it's easiest just to have a copy of all the functions"
nl|'\n'
comment|'# that we need.'
nl|'\n'
comment|'#'
nl|'\n'
nl|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'gettext'
op|'.'
name|'install'
op|'('
string|"'nova'"
op|','
name|'unicode'
op|'='
number|'1'
op|')'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'logging'
op|'.'
name|'handlers'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'##### Logging setup'
nl|'\n'
nl|'\n'
DECL|function|configure_logging
name|'def'
name|'configure_logging'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'sysh'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'('
string|"'/dev/log'"
op|')'
newline|'\n'
name|'sysh'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'formatter'
op|'='
name|'logging'
op|'.'
name|'Formatter'
op|'('
string|"'%s: %%(levelname)-8s %%(message)s'"
op|'%'
name|'name'
op|')'
newline|'\n'
name|'sysh'
op|'.'
name|'setFormatter'
op|'('
name|'formatter'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'addHandler'
op|'('
name|'sysh'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'##### Exceptions'
nl|'\n'
nl|'\n'
DECL|class|PluginError
dedent|''
name|'class'
name|'PluginError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Exception class for all plugin errors."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ArgumentError
dedent|''
dedent|''
name|'class'
name|'ArgumentError'
op|'('
name|'PluginError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Raised when required arguments are missing, argument values are invalid,\n    or incompatible arguments are given.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'PluginError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'##### Helpers'
nl|'\n'
nl|'\n'
DECL|function|ignore_failure
dedent|''
dedent|''
name|'def'
name|'ignore_failure'
op|'('
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
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
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
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Ignoring XenAPI.Failure %s'"
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'##### Argument validation'
nl|'\n'
nl|'\n'
DECL|variable|ARGUMENT_PATTERN
dedent|''
dedent|''
name|'ARGUMENT_PATTERN'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r'^[a-zA-Z0-9_:\\.\\-,]+$'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_exists
name|'def'
name|'validate_exists'
op|'('
name|'args'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates that a string argument to a RPC method call is given, and\n    matches the shell-safe regex, with an optional default value in case it\n    does not exist.\n\n    Returns the string.\n    """'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'args'
op|'['
name|'key'
op|']'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|"'Argument %(key)s value %(value)s is too '"
nl|'\n'
string|"'short.'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
nl|'\n'
string|"'value'"
op|':'
name|'args'
op|'['
name|'key'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'ARGUMENT_PATTERN'
op|'.'
name|'match'
op|'('
name|'args'
op|'['
name|'key'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|"'Argument %(key)s value %(value)s contains '"
nl|'\n'
string|"'invalid characters.'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
nl|'\n'
string|"'value'"
op|':'
name|'args'
op|'['
name|'key'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'args'
op|'['
name|'key'
op|']'
op|'['
number|'0'
op|']'
op|'=='
string|"'-'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|"'Argument %(key)s value %(value)s starts '"
nl|'\n'
string|"'with a hyphen.'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
nl|'\n'
string|"'value'"
op|':'
name|'args'
op|'['
name|'key'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'args'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'default'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'default'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|"'Argument %s is required.'"
op|')'
op|'%'
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_bool
dedent|''
dedent|''
name|'def'
name|'validate_bool'
op|'('
name|'args'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates that a string argument to a RPC method call is a boolean\n    string, with an optional default value in case it does not exist.\n\n    Returns the python boolean value.\n    """'
newline|'\n'
name|'value'
op|'='
name|'validate_exists'
op|'('
name|'args'
op|','
name|'key'
op|','
name|'default'
op|')'
newline|'\n'
name|'if'
name|'value'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'true'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'value'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'false'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|'"Argument %(key)s may not take value %(value)s. "'
nl|'\n'
string|'"Valid values are [\'true\', \'false\']."'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
nl|'\n'
string|"'value'"
op|':'
name|'value'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|exists
dedent|''
dedent|''
name|'def'
name|'exists'
op|'('
name|'args'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates that a freeform string argument to a RPC method call is given.\n    Returns the string.\n    """'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'args'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|"'Argument %s is required.'"
op|')'
op|'%'
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|optional
dedent|''
dedent|''
name|'def'
name|'optional'
op|'('
name|'args'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""If the given key is in args, return the corresponding value, otherwise\n    return None"""'
newline|'\n'
name|'return'
name|'key'
name|'in'
name|'args'
name|'and'
name|'args'
op|'['
name|'key'
op|']'
name|'or'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_this_host
dedent|''
name|'def'
name|'get_this_host'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
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
nl|'\n'
nl|'\n'
DECL|function|get_domain_0
dedent|''
name|'def'
name|'get_domain_0'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'this_host_ref'
op|'='
name|'get_this_host'
op|'('
name|'session'
op|')'
newline|'\n'
name|'expr'
op|'='
string|'\'field "is_control_domain" = "true" and field "resident_on" = "%s"\''
newline|'\n'
name|'expr'
op|'='
name|'expr'
op|'%'
name|'this_host_ref'
newline|'\n'
name|'return'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_all_records_where'
op|'('
name|'expr'
op|')'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_vdi
dedent|''
name|'def'
name|'create_vdi'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'name_label'
op|','
name|'virtual_size'
op|','
name|'read_only'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vdi_ref'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'create'
op|'('
nl|'\n'
op|'{'
string|"'name_label'"
op|':'
name|'name_label'
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'SR'"
op|':'
name|'sr_ref'
op|','
nl|'\n'
string|"'virtual_size'"
op|':'
name|'str'
op|'('
name|'virtual_size'
op|')'
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'User'"
op|','
nl|'\n'
string|"'sharable'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'read_only'"
op|':'
name|'read_only'
op|','
nl|'\n'
string|"'xenstore_data'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'sm_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'tags'"
op|':'
op|'['
op|']'
op|'}'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created VDI %(vdi_ref)s (%(label)s, %(size)s, '"
nl|'\n'
string|"'%(read_only)s) on %(sr_ref)s.'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'vdi_ref'"
op|':'
name|'vdi_ref'
op|','
nl|'\n'
string|"'label'"
op|':'
name|'name_label'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'virtual_size'
op|','
nl|'\n'
string|"'read_only'"
op|':'
name|'read_only'
op|','
nl|'\n'
string|"'sr_ref'"
op|':'
name|'sr_ref'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'vdi_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|with_vdi_in_dom0
dedent|''
name|'def'
name|'with_vdi_in_dom0'
op|'('
name|'session'
op|','
name|'vdi'
op|','
name|'read_only'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'dom0'
op|'='
name|'get_domain_0'
op|'('
name|'session'
op|')'
newline|'\n'
name|'vbd_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'dom0'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VDI'"
op|']'
op|'='
name|'vdi'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'userdevice'"
op|']'
op|'='
string|"'autodetect'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'bootable'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'mode'"
op|']'
op|'='
name|'read_only'
name|'and'
string|"'RO'"
name|'or'
string|"'RW'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'type'"
op|']'
op|'='
string|"'disk'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'unpluggable'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'empty'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_supported_algorithms'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VBD for VDI %s ... '"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
name|'vbd'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'create'
op|'('
name|'vbd_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VBD for VDI %s done.'"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Plugging VBD %s ... '"
op|')'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'plug'
op|'('
name|'vbd'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Plugging VBD %s done.'"
op|')'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'return'
name|'f'
op|'('
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'get_device'
op|'('
name|'vbd'
op|')'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Destroying VBD for VDI %s ... '"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
name|'vbd_unplug_with_retry'
op|'('
name|'session'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'ignore_failure'
op|'('
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'destroy'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Destroying VBD for VDI %s done.'"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vbd_unplug_with_retry
dedent|''
dedent|''
name|'def'
name|'vbd_unplug_with_retry'
op|'('
name|'session'
op|','
name|'vbd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Call VBD.unplug on the given VBD, with a retry if we get\n    DEVICE_DETACH_REJECTED.  For reasons which I don\'t understand, we\'re\n    seeing the device still in use, even when all processes using the device\n    should be dead."""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'unplug'
op|'('
name|'vbd'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VBD.unplug successful first time.'"
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'len'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|'>'
number|'0'
name|'and'
nl|'\n'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'DEVICE_DETACH_REJECTED'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VBD.unplug rejected: retrying...'"
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
dedent|''
name|'elif'
op|'('
name|'len'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|'>'
number|'0'
name|'and'
nl|'\n'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'DEVICE_ALREADY_DETACHED'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VBD.unplug successful eventually.'"
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Ignoring XenAPI.Failure in VBD.unplug: %s'"
op|')'
op|','
nl|'\n'
name|'e'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|with_http_connection
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'with_http_connection'
op|'('
name|'proto'
op|','
name|'netloc'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conn'
op|'='
op|'('
name|'proto'
op|'=='
string|"'https'"
name|'and'
nl|'\n'
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'netloc'
op|')'
name|'or'
nl|'\n'
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'netloc'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'f'
op|'('
name|'conn'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|with_file
dedent|''
dedent|''
name|'def'
name|'with_file'
op|'('
name|'dest_path'
op|','
name|'mode'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'dest'
op|'='
name|'open'
op|'('
name|'dest_path'
op|','
name|'mode'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'f'
op|'('
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'dest'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
