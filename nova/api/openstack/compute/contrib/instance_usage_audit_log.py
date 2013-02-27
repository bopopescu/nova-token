begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'import_opt'
op|'('
string|"'compute_topic'"
op|','
string|"'nova.compute.rpcapi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'instance_usage_audit_log'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceUsageAuditLogController
name|'class'
name|'InstanceUsageAuditLogController'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host_api'
op|'='
name|'compute'
op|'.'
name|'HostAPI'
op|'('
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
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'task_log'
op|'='
name|'self'
op|'.'
name|'_get_audit_task_logs'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'instance_usage_audit_logs'"
op|':'
name|'task_log'
op|'}'
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
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'.'"
name|'in'
name|'id'
op|':'
newline|'\n'
indent|'                '
name|'before_date'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'str'
op|'('
name|'id'
op|')'
op|','
nl|'\n'
string|'"%Y-%m-%d %H:%M:%S.%f"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'before_date'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'str'
op|'('
name|'id'
op|')'
op|','
nl|'\n'
string|'"%Y-%m-%d %H:%M:%S"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid timestamp for date %s"'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'task_log'
op|'='
name|'self'
op|'.'
name|'_get_audit_task_logs'
op|'('
name|'context'
op|','
nl|'\n'
name|'before'
op|'='
name|'before_date'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'instance_usage_audit_log'"
op|':'
name|'task_log'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_audit_task_logs
dedent|''
name|'def'
name|'_get_audit_task_logs'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|'='
name|'None'
op|','
name|'end'
op|'='
name|'None'
op|','
nl|'\n'
name|'before'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a full log for all instance usage audit tasks on all\n           computes.\n\n        :param begin: datetime beginning of audit period to get logs for,\n            Defaults to the beginning of the most recently completed\n            audit period prior to the \'before\' date.\n        :param end: datetime ending of audit period to get logs for,\n            Defaults to the ending of the most recently completed\n            audit period prior to the \'before\' date.\n        :param before: By default we look for the audit period most recently\n            completed before this datetime. Has no effect if both begin and end\n            are specified.\n        """'
newline|'\n'
name|'defbegin'
op|','
name|'defend'
op|'='
name|'utils'
op|'.'
name|'last_completed_audit_period'
op|'('
name|'before'
op|'='
name|'before'
op|')'
newline|'\n'
name|'if'
name|'begin'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'begin'
op|'='
name|'defbegin'
newline|'\n'
dedent|''
name|'if'
name|'end'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'end'
op|'='
name|'defend'
newline|'\n'
dedent|''
name|'task_logs'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'task_log_get_all'
op|'('
name|'context'
op|','
nl|'\n'
string|'"instance_usage_audit"'
op|','
nl|'\n'
name|'begin'
op|','
name|'end'
op|')'
newline|'\n'
comment|'# We do this this way to include disabled compute services,'
nl|'\n'
comment|'# which can have instances on them. (mdragon)'
nl|'\n'
name|'filters'
op|'='
op|'{'
string|"'topic'"
op|':'
name|'CONF'
op|'.'
name|'compute_topic'
op|'}'
newline|'\n'
name|'services'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'set'
op|'('
name|'serv'
op|'['
string|"'host'"
op|']'
name|'for'
name|'serv'
name|'in'
name|'services'
op|')'
newline|'\n'
name|'seen_hosts'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'done_hosts'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'running_hosts'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'total_errors'
op|'='
number|'0'
newline|'\n'
name|'total_items'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'tlog'
name|'in'
name|'task_logs'
op|':'
newline|'\n'
indent|'            '
name|'seen_hosts'
op|'.'
name|'add'
op|'('
name|'tlog'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'tlog'
op|'['
string|"'state'"
op|']'
op|'=='
string|'"DONE"'
op|':'
newline|'\n'
indent|'                '
name|'done_hosts'
op|'.'
name|'add'
op|'('
name|'tlog'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'tlog'
op|'['
string|"'state'"
op|']'
op|'=='
string|'"RUNNING"'
op|':'
newline|'\n'
indent|'                '
name|'running_hosts'
op|'.'
name|'add'
op|'('
name|'tlog'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'total_errors'
op|'+='
name|'tlog'
op|'['
string|"'errors'"
op|']'
newline|'\n'
name|'total_items'
op|'+='
name|'tlog'
op|'['
string|"'task_items'"
op|']'
newline|'\n'
dedent|''
name|'log'
op|'='
name|'dict'
op|'('
op|'('
name|'tl'
op|'['
string|"'host'"
op|']'
op|','
name|'dict'
op|'('
name|'state'
op|'='
name|'tl'
op|'['
string|"'state'"
op|']'
op|','
nl|'\n'
name|'instances'
op|'='
name|'tl'
op|'['
string|"'task_items'"
op|']'
op|','
nl|'\n'
name|'errors'
op|'='
name|'tl'
op|'['
string|"'errors'"
op|']'
op|','
nl|'\n'
name|'message'
op|'='
name|'tl'
op|'['
string|"'message'"
op|']'
op|')'
op|')'
nl|'\n'
name|'for'
name|'tl'
name|'in'
name|'task_logs'
op|')'
newline|'\n'
name|'missing_hosts'
op|'='
name|'hosts'
op|'-'
name|'seen_hosts'
newline|'\n'
name|'overall_status'
op|'='
string|'"%s hosts done. %s errors."'
op|'%'
op|'('
nl|'\n'
string|"'ALL'"
name|'if'
name|'len'
op|'('
name|'done_hosts'
op|')'
op|'=='
name|'len'
op|'('
name|'hosts'
op|')'
nl|'\n'
name|'else'
string|'"%s of %s"'
op|'%'
op|'('
name|'len'
op|'('
name|'done_hosts'
op|')'
op|','
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
op|','
nl|'\n'
name|'total_errors'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'period_beginning'
op|'='
name|'str'
op|'('
name|'begin'
op|')'
op|','
nl|'\n'
name|'period_ending'
op|'='
name|'str'
op|'('
name|'end'
op|')'
op|','
nl|'\n'
name|'num_hosts'
op|'='
name|'len'
op|'('
name|'hosts'
op|')'
op|','
nl|'\n'
name|'num_hosts_done'
op|'='
name|'len'
op|'('
name|'done_hosts'
op|')'
op|','
nl|'\n'
name|'num_hosts_running'
op|'='
name|'len'
op|'('
name|'running_hosts'
op|')'
op|','
nl|'\n'
name|'num_hosts_not_run'
op|'='
name|'len'
op|'('
name|'missing_hosts'
op|')'
op|','
nl|'\n'
name|'hosts_not_run'
op|'='
name|'list'
op|'('
name|'missing_hosts'
op|')'
op|','
nl|'\n'
name|'total_instances'
op|'='
name|'total_items'
op|','
nl|'\n'
name|'total_errors'
op|'='
name|'total_errors'
op|','
nl|'\n'
name|'overall_status'
op|'='
name|'overall_status'
op|','
nl|'\n'
name|'log'
op|'='
name|'log'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Instance_usage_audit_log
dedent|''
dedent|''
name|'class'
name|'Instance_usage_audit_log'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only Task Log Monitoring."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"OSInstanceUsageAuditLog"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-instance_usage_audit_log"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/ext/services/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-07-06T01:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-instance_usage_audit_log'"
op|','
nl|'\n'
name|'InstanceUsageAuditLogController'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ext'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
