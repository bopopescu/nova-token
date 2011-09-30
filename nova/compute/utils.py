begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""Compute-related Utilities and helpers."""'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier_api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_usage_exists
name|'def'
name|'notify_usage_exists'
op|'('
name|'instance_ref'
op|','
name|'current_period'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Generates \'exists\' notification for an instance for usage auditing\n        purposes.\n\n        Generates usage for last completed period, unless \'current_period\'\n        is True."""'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'begin'
op|','
name|'end'
op|'='
name|'utils'
op|'.'
name|'current_audit_period'
op|'('
op|')'
newline|'\n'
name|'bw'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'current_period'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'end'
newline|'\n'
name|'audit_end'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'begin'
newline|'\n'
name|'audit_end'
op|'='
name|'end'
newline|'\n'
dedent|''
name|'for'
name|'b'
name|'in'
name|'db'
op|'.'
name|'bw_usage_get_by_instance'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'audit_start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bw'
op|'['
name|'b'
op|'.'
name|'network_label'
op|']'
op|'='
name|'dict'
op|'('
name|'bw_in'
op|'='
name|'b'
op|'.'
name|'bw_in'
op|','
name|'bw_out'
op|'='
name|'b'
op|'.'
name|'bw_out'
op|')'
newline|'\n'
dedent|''
name|'usage_info'
op|'='
name|'utils'
op|'.'
name|'usage_from_instance'
op|'('
name|'instance_ref'
op|','
nl|'\n'
name|'audit_period_begining'
op|'='
name|'str'
op|'('
name|'audit_start'
op|')'
op|','
nl|'\n'
name|'audit_period_ending'
op|'='
name|'str'
op|'('
name|'audit_end'
op|')'
op|','
nl|'\n'
name|'bandwidth'
op|'='
name|'bw'
op|')'
newline|'\n'
name|'notifier_api'
op|'.'
name|'notify'
op|'('
string|"'compute.%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'compute.instance.exists'"
op|','
nl|'\n'
name|'notifier_api'
op|'.'
name|'INFO'
op|','
nl|'\n'
name|'usage_info'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
