begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
name|'as'
name|'base_extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
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
op|'.'
name|'plugin'
name|'import'
name|'pluginmanager'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionManager
name|'class'
name|'ExtensionManager'
op|'('
name|'base_extensions'
op|'.'
name|'ExtensionManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'self'
op|'.'
name|'cls_list'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
newline|'\n'
name|'self'
op|'.'
name|'PluginManager'
op|'='
name|'pluginmanager'
op|'.'
name|'PluginManager'
op|'('
string|"'nova'"
op|','
nl|'\n'
string|"'compute-extensions'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'PluginManager'
op|'.'
name|'load_plugins'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cls_list'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'PluginManager'
op|'.'
name|'plugin_extension_factory'
op|')'
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
name|'sorted_ext_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_load_extensions'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
