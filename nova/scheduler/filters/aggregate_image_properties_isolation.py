begin_unit
comment|'# Copyright (c) 2013 Cloudwatt'
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
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'aggregate_image_properties_isolation_namespace'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force the filter to consider only keys matching '"
nl|'\n'
string|"'the given namespace.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'aggregate_image_properties_isolation_separator'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"."'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The separator used between the namespace and keys'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
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
name|'opts'
op|')'
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
DECL|class|AggregateImagePropertiesIsolation
name|'class'
name|'AggregateImagePropertiesIsolation'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AggregateImagePropertiesIsolation works with image properties."""'
newline|'\n'
nl|'\n'
comment|'# Aggregate data and instance type does not change within a request'
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks a host in an aggregate that metadata key/value match\n        with image properties.\n        """'
newline|'\n'
name|'cfg_namespace'
op|'='
name|'CONF'
op|'.'
name|'aggregate_image_properties_isolation_namespace'
newline|'\n'
name|'cfg_separator'
op|'='
name|'CONF'
op|'.'
name|'aggregate_image_properties_isolation_separator'
newline|'\n'
nl|'\n'
name|'spec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'image_props'
op|'='
name|'spec'
op|'.'
name|'get'
op|'('
string|"'image'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'utils'
op|'.'
name|'aggregate_metadata_get_by_host'
op|'('
name|'host_state'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'options'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'cfg_namespace'
name|'and'
nl|'\n'
name|'not'
name|'key'
op|'.'
name|'startswith'
op|'('
name|'cfg_namespace'
op|'+'
name|'cfg_separator'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'prop'
op|'='
name|'image_props'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'prop'
name|'and'
name|'prop'
name|'not'
name|'in'
name|'options'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s fails image aggregate properties "'
nl|'\n'
string|'"requirements. Property %(prop)s does not "'
nl|'\n'
string|'"match %(options)s."'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'prop'"
op|':'
name|'prop'
op|','
nl|'\n'
string|"'options'"
op|':'
name|'options'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
