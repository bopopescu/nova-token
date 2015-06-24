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
name|'import'
name|'abc'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
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
DECL|class|MonitorBase
name|'class'
name|'MonitorBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all resource monitor plugins."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'compute_manager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_manager'
op|'='
name|'compute_manager'
newline|'\n'
name|'self'
op|'.'
name|'source'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|get_metric
name|'def'
name|'get_metric'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a (value, timestamp) tuple for the supplied metric name.\n\n        :param name: The name/key for the metric to grab the value for.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'get_metric'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|get_metric_names
name|'def'
name|'get_metric_names'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get available metric names.\n\n        Get available metric names, which are represented by a set of keys\n        that can be used to check conflicts and duplications\n        :returns: set containing one or more values from\n                  nova.objects.fields.MonitorMetricType.ALL constants\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'get_metric_names'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_metrics_to_list
dedent|''
name|'def'
name|'add_metrics_to_list'
op|'('
name|'self'
op|','
name|'metrics_list'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds metric objects to a supplied list object.\n\n        :param metric_list: nova.objects.MonitorMetricList that the monitor\n                            plugin should append nova.objects.MonitorMetric\n                            objects to.\n        """'
newline|'\n'
name|'metric_names'
op|'='
name|'self'
op|'.'
name|'get_metric_names'
op|'('
op|')'
newline|'\n'
name|'metrics'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'metric_names'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|','
name|'timestamp'
op|'='
name|'self'
op|'.'
name|'get_metric'
op|'('
name|'name'
op|')'
newline|'\n'
name|'metric'
op|'='
name|'objects'
op|'.'
name|'MonitorMetric'
op|'('
name|'name'
op|'='
name|'name'
op|','
nl|'\n'
name|'value'
op|'='
name|'value'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'timestamp'
op|','
nl|'\n'
name|'source'
op|'='
name|'self'
op|'.'
name|'source'
op|')'
newline|'\n'
name|'metrics'
op|'.'
name|'append'
op|'('
name|'metric'
op|')'
newline|'\n'
dedent|''
name|'metrics_list'
op|'.'
name|'objects'
op|'.'
name|'extend'
op|'('
name|'metrics'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CPUMonitorBase
dedent|''
dedent|''
name|'class'
name|'CPUMonitorBase'
op|'('
name|'MonitorBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all monitors that return CPU-related metrics."""'
newline|'\n'
nl|'\n'
DECL|member|get_metric_names
name|'def'
name|'get_metric_names'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'set'
op|'('
op|'['
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_FREQUENCY'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_USER_TIME'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_KERNEL_TIME'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_IDLE_TIME'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'MonitorMetricType'
op|'.'
name|'CPU_IOWAIT_TIME'
op|','
nl|'\n'
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
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
