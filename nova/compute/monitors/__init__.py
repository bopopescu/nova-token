begin_unit
comment|'# Copyright 2013 Intel Corporation.'
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
string|'"""\nResource monitor API specification.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'stevedore'
name|'import'
name|'enabled'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
nl|'\n'
DECL|variable|compute_monitors_opts
name|'compute_monitors_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'compute_available_monitors'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Monitor classes available to the compute which may '"
nl|'\n'
string|"'be specified more than once. This option is '"
nl|'\n'
string|"'DEPRECATED and no longer used. Use setuptools entry '"
nl|'\n'
string|"'points to list available monitor plugins.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'compute_monitors'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of monitors that can be used for getting '"
nl|'\n'
string|"'compute metrics. You can use the alias/name from '"
nl|'\n'
string|"'the setuptools entry points for nova.compute.monitors.* '"
nl|'\n'
string|'\'namespaces. If no namespace is supplied, the "cpu." \''
nl|'\n'
string|"'namespace is assumed for backwards-compatibility. '"
nl|'\n'
string|"'An example value that would enable both the CPU and '"
nl|'\n'
string|"'NUMA memory bandwidth monitors that used the virt '"
nl|'\n'
string|"'driver variant: '"
nl|'\n'
string|'\'["cpu.virt_driver", "numa_mem_bw.virt_driver"]\''
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
name|'compute_monitors_opts'
op|')'
newline|'\n'
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
DECL|class|MonitorHandler
name|'class'
name|'MonitorHandler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|NAMESPACES
indent|'    '
name|'NAMESPACES'
op|'='
op|'['
nl|'\n'
string|"'nova.compute.monitors.cpu'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'resource_tracker'
op|')'
op|':'
newline|'\n'
comment|'# Dictionary keyed by the monitor type namespace. Value is the'
nl|'\n'
comment|'# first loaded monitor of that namespace or False.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'type_monitor_loaded'
op|'='
op|'{'
name|'ns'
op|':'
name|'False'
name|'for'
name|'ns'
name|'in'
name|'self'
op|'.'
name|'NAMESPACES'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'monitors'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ns'
name|'in'
name|'self'
op|'.'
name|'NAMESPACES'
op|':'
newline|'\n'
indent|'            '
name|'plugin_mgr'
op|'='
name|'enabled'
op|'.'
name|'EnabledExtensionManager'
op|'('
nl|'\n'
name|'namespace'
op|'='
name|'ns'
op|','
nl|'\n'
name|'invoke_on_load'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_func'
op|'='
name|'self'
op|'.'
name|'check_enabled_monitor'
op|','
nl|'\n'
name|'invoke_args'
op|'='
op|'('
name|'resource_tracker'
op|','
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monitors'
op|'+='
op|'['
name|'ext'
op|'.'
name|'obj'
name|'for'
name|'ext'
name|'in'
name|'plugin_mgr'
op|']'
newline|'\n'
nl|'\n'
DECL|member|check_enabled_monitor
dedent|''
dedent|''
name|'def'
name|'check_enabled_monitor'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that only one monitor is specified of any type."""'
newline|'\n'
comment|'# The extension does not have a namespace attribute, unfortunately,'
nl|'\n'
comment|'# but we can get the namespace by examining the first part of the'
nl|'\n'
comment|'# entry_point_target attribute, which looks like this:'
nl|'\n'
comment|"# 'nova.compute.monitors.cpu.virt_driver:Monitor'"
nl|'\n'
name|'ept'
op|'='
name|'ext'
op|'.'
name|'entry_point_target'
newline|'\n'
name|'ept_parts'
op|'='
name|'ept'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'namespace_parts'
op|'='
name|'ept_parts'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'namespace'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
name|'namespace_parts'
op|'['
number|'0'
op|':'
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'type_monitor_loaded'
op|'['
name|'namespace'
op|']'
name|'is'
name|'not'
name|'False'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Excluding %(namespace)s monitor "'
nl|'\n'
string|'"%(monitor_name)s. Already loaded "'
nl|'\n'
string|'"%(loaded_monitor)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'namespace'"
op|':'
name|'namespace'
op|','
nl|'\n'
string|"'monitor_name'"
op|':'
name|'ext'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'loaded_monitor'"
op|':'
name|'self'
op|'.'
name|'type_monitor_loaded'
op|'['
name|'namespace'
op|']'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# NOTE(jaypipes): We used to only have CPU monitors, so'
nl|'\n'
comment|'# CONF.compute_monitors could contain "virt_driver" without any monitor'
nl|'\n'
comment|'# type namespace. So, to maintain backwards-compatibility with that'
nl|'\n'
comment|'# older way of specifying monitors, we first loop through any values in'
nl|'\n'
comment|"# CONF.compute_monitors and put any non-namespace'd values into the"
nl|'\n'
comment|"# 'cpu' namespace."
nl|'\n'
dedent|''
name|'cfg_monitors'
op|'='
op|'['
string|"'cpu.'"
op|'+'
name|'cfg'
name|'if'
string|"'.'"
name|'not'
name|'in'
name|'cfg'
name|'else'
name|'cfg'
nl|'\n'
name|'for'
name|'cfg'
name|'in'
name|'CONF'
op|'.'
name|'compute_monitors'
op|']'
newline|'\n'
comment|"# NOTE(jaypipes): Append 'nova.compute.monitors.' to any monitor value"
nl|'\n'
comment|"# that doesn't have it to allow CONF.compute_monitors to use shortened"
nl|'\n'
comment|"# namespaces (like 'cpu.' instead of 'nova.compute.monitors.cpu.')"
nl|'\n'
name|'cfg_monitors'
op|'='
op|'['
string|"'nova.compute.monitors.'"
op|'+'
name|'cfg'
nl|'\n'
name|'if'
string|"'nova.compute.monitors.'"
name|'not'
name|'in'
name|'cfg'
name|'else'
name|'cfg'
nl|'\n'
name|'for'
name|'cfg'
name|'in'
name|'cfg_monitors'
op|']'
newline|'\n'
name|'if'
name|'namespace'
op|'+'
string|"'.'"
op|'+'
name|'ext'
op|'.'
name|'name'
name|'in'
name|'cfg_monitors'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'type_monitor_loaded'
op|'['
name|'namespace'
op|']'
op|'='
name|'ext'
op|'.'
name|'name'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Excluding %(namespace)s monitor %(monitor_name)s. "'
nl|'\n'
string|'"Not in the list of enabled monitors "'
nl|'\n'
string|'"(CONF.compute_monitors)."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'namespace'"
op|':'
name|'namespace'
op|','
string|"'monitor_name'"
op|':'
name|'ext'
op|'.'
name|'name'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
