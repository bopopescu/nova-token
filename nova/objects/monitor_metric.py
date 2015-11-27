begin_unit
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'versionutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(jwcroppe): Used to determine which fields whose value we need to adjust'
nl|'\n'
comment|'# (read: divide by 100.0) before sending information to the RPC notifier since'
nl|'\n'
comment|'# these values were expected to be within the range [0, 1].'
nl|'\n'
DECL|variable|FIELDS_REQUIRING_CONVERSION
name|'FIELDS_REQUIRING_CONVERSION'
op|'='
op|'['
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_USER_PERCENT'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_KERNEL_PERCENT'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_IDLE_PERCENT'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_IOWAIT_PERCENT'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_PERCENT'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|MonitorMetric
name|'class'
name|'MonitorMetric'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added NUMA support'
nl|'\n'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'fields'
op|'.'
name|'MonitorMetricTypeField'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'value'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'numa_membw_values'"
op|':'
name|'fields'
op|'.'
name|'DictOfIntegersField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
comment|'# This will be the stevedore extension full class name'
nl|'\n'
comment|'# for the plugin from which the metric originates.'
nl|'\n'
string|"'source'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|obj_make_compatible
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MonitorMetric'
op|','
name|'self'
op|')'
op|'.'
name|'obj_make_compatible'
op|'('
name|'primitive'
op|','
nl|'\n'
name|'target_version'
op|')'
newline|'\n'
name|'target_version'
op|'='
name|'versionutils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'1'
op|')'
name|'and'
string|"'numa_nodes_values'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'numa_membw_values'"
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(jaypipes): This method exists to convert the object to the'
nl|'\n'
comment|'# format expected by the RPC notifier for metrics events.'
nl|'\n'
DECL|member|to_dict
dedent|''
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dict_to_return'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
comment|'# NOTE(jaypipes): This is what jsonutils.dumps() does to'
nl|'\n'
comment|'# datetime.datetime objects, which is what timestamp is in'
nl|'\n'
comment|'# this object as well as the original simple dict metrics'
nl|'\n'
string|"'timestamp'"
op|':'
name|'utils'
op|'.'
name|'strtime'
op|'('
name|'self'
op|'.'
name|'timestamp'
op|')'
op|','
nl|'\n'
string|"'source'"
op|':'
name|'self'
op|'.'
name|'source'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'value'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'name'
name|'in'
name|'FIELDS_REQUIRING_CONVERSION'
op|':'
newline|'\n'
indent|'                '
name|'dict_to_return'
op|'['
string|"'value'"
op|']'
op|'='
name|'self'
op|'.'
name|'value'
op|'/'
number|'100.0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'dict_to_return'
op|'['
string|"'value'"
op|']'
op|'='
name|'self'
op|'.'
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'numa_membw_values'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'dict_to_return'
op|'['
string|"'numa_membw_values'"
op|']'
op|'='
name|'self'
op|'.'
name|'numa_membw_values'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict_to_return'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|MonitorMetricList
name|'class'
name|'MonitorMetricList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: MonitorMetric version 1.1'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'MonitorMetric'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_json
name|'def'
name|'from_json'
op|'('
name|'cls'
op|','
name|'metrics'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Converts a legacy json object into a list of MonitorMetric objs\n        and finally returns of MonitorMetricList\n\n        :param metrics: a string of json serialized objects\n        :returns: a MonitorMetricList Object.\n        """'
newline|'\n'
name|'metrics'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'metrics'
op|')'
name|'if'
name|'metrics'
name|'else'
op|'['
op|']'
newline|'\n'
name|'metric_list'
op|'='
op|'['
nl|'\n'
name|'MonitorMetric'
op|'('
op|'**'
name|'metric'
op|')'
name|'for'
name|'metric'
name|'in'
name|'metrics'
op|']'
newline|'\n'
name|'return'
name|'MonitorMetricList'
op|'('
name|'objects'
op|'='
name|'metric_list'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(jaypipes): This method exists to convert the object to the'
nl|'\n'
comment|'# format expected by the RPC notifier for metrics events.'
nl|'\n'
DECL|member|to_list
dedent|''
name|'def'
name|'to_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'m'
op|'.'
name|'to_dict'
op|'('
op|')'
name|'for'
name|'m'
name|'in'
name|'self'
op|'.'
name|'objects'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
