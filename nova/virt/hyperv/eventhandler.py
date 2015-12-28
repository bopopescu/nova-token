begin_unit
comment|'# Copyright 2015 Cloudbase Solutions Srl'
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
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'wmi'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'os_win'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'os_win'
name|'import'
name|'exceptions'
name|'as'
name|'os_win_exc'
newline|'\n'
name|'from'
name|'os_win'
name|'import'
name|'utilsfactory'
newline|'\n'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
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
name|'import'
name|'event'
name|'as'
name|'virtevent'
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
DECL|variable|hyperv_opts
name|'hyperv_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'power_state_check_timeframe'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The timeframe to be checked for instance power '"
nl|'\n'
string|"'state changes.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'power_state_event_polling_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Instance power state change event polling frequency.'"
op|')'
op|','
nl|'\n'
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
name|'hyperv_opts'
op|','
string|"'hyperv'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceEventHandler
name|'class'
name|'InstanceEventHandler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
comment|'# The event listener timeout is set to 0 in order to return immediately'
nl|'\n'
comment|'# and avoid blocking the thread.'
nl|'\n'
DECL|variable|_WAIT_TIMEOUT
indent|'    '
name|'_WAIT_TIMEOUT'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|variable|_TRANSITION_MAP
name|'_TRANSITION_MAP'
op|'='
op|'{'
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|':'
name|'virtevent'
op|'.'
name|'EVENT_LIFECYCLE_STARTED'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_DISABLED'
op|':'
name|'virtevent'
op|'.'
name|'EVENT_LIFECYCLE_STOPPED'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_PAUSED'
op|':'
name|'virtevent'
op|'.'
name|'EVENT_LIFECYCLE_PAUSED'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_SUSPENDED'
op|':'
nl|'\n'
name|'virtevent'
op|'.'
name|'EVENT_LIFECYCLE_SUSPENDED'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'state_change_callback'
op|'='
name|'None'
op|','
nl|'\n'
name|'running_state_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_listener'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_power_state_change_listener'
op|'('
nl|'\n'
name|'timeframe'
op|'='
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'power_state_check_timeframe'
op|','
nl|'\n'
name|'filtered_states'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_TRANSITION_MAP'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_polling_interval'
op|'='
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'power_state_event_polling_interval'
newline|'\n'
name|'self'
op|'.'
name|'_state_change_callback'
op|'='
name|'state_change_callback'
newline|'\n'
name|'self'
op|'.'
name|'_running_state_callback'
op|'='
name|'running_state_callback'
newline|'\n'
nl|'\n'
DECL|member|start_listener
dedent|''
name|'def'
name|'start_listener'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_poll_events'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_poll_events
dedent|''
name|'def'
name|'_poll_events'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# Retrieve one by one all the events that occurred in'
nl|'\n'
comment|'# the checked interval.'
nl|'\n'
indent|'                '
name|'event'
op|'='
name|'self'
op|'.'
name|'_listener'
op|'('
name|'self'
op|'.'
name|'_WAIT_TIMEOUT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_dispatch_event'
op|'('
name|'event'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'except'
name|'wmi'
op|'.'
name|'x_wmi_timed_out'
op|':'
newline|'\n'
comment|'# If no events were triggered in the checked interval,'
nl|'\n'
comment|"# a timeout exception is raised. We'll just ignore it."
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'eventlet'
op|'.'
name|'sleep'
op|'('
name|'self'
op|'.'
name|'_polling_interval'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_dispatch_event
dedent|''
dedent|''
name|'def'
name|'_dispatch_event'
op|'('
name|'self'
op|','
name|'event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_state'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_power_state'
op|'('
name|'event'
op|'.'
name|'EnabledState'
op|')'
newline|'\n'
name|'instance_name'
op|'='
name|'event'
op|'.'
name|'ElementName'
newline|'\n'
nl|'\n'
comment|'# Instance uuid set by Nova. If this is missing, we assume that'
nl|'\n'
comment|'# the instance was not created by Nova and ignore the event.'
nl|'\n'
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_get_instance_uuid'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_emit_event'
op|'('
name|'instance_name'
op|','
name|'instance_uuid'
op|','
name|'instance_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_emit_event
dedent|''
dedent|''
name|'def'
name|'_emit_event'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'instance_uuid'
op|','
name|'instance_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'virt_event'
op|'='
name|'self'
op|'.'
name|'_get_virt_event'
op|'('
name|'instance_uuid'
op|','
nl|'\n'
name|'instance_state'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_state_change_callback'
op|','
name|'virt_event'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance_state'
op|'=='
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_running_state_callback'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_uuid
dedent|''
dedent|''
name|'def'
name|'_get_instance_uuid'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_instance_uuid'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"Instance uuid could not be retrieved for "'
nl|'\n'
string|'"instance %s. Instance state change event "'
nl|'\n'
string|'"will be ignored."'
op|')'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_uuid'
newline|'\n'
dedent|''
name|'except'
name|'os_win_exc'
op|'.'
name|'HyperVVMNotFoundException'
op|':'
newline|'\n'
comment|'# The instance has been deleted.'
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_get_virt_event
dedent|''
dedent|''
name|'def'
name|'_get_virt_event'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|','
name|'instance_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'transition'
op|'='
name|'self'
op|'.'
name|'_TRANSITION_MAP'
op|'['
name|'instance_state'
op|']'
newline|'\n'
name|'return'
name|'virtevent'
op|'.'
name|'LifecycleEvent'
op|'('
name|'uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'transition'
op|'='
name|'transition'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
