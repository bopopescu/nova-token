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
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'client'
name|'as'
name|'scheduler_client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'utils'
name|'as'
name|'scheduler_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|migrate_opt
name|'migrate_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'migrate_max_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of times to retry live-migration before failing. '"
nl|'\n'
string|"'If == -1, try until out of hosts. '"
nl|'\n'
string|"'If == 0, only try once, no retries.'"
op|')'
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
name|'register_opt'
op|'('
name|'migrate_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LiveMigrationTask
name|'class'
name|'LiveMigrationTask'
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
op|','
name|'context'
op|','
name|'instance'
op|','
name|'destination'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
name|'migration'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'destination'
op|'='
name|'destination'
newline|'\n'
name|'self'
op|'.'
name|'block_migration'
op|'='
name|'block_migration'
newline|'\n'
name|'self'
op|'.'
name|'disk_over_commit'
op|'='
name|'disk_over_commit'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'='
name|'migration'
newline|'\n'
name|'self'
op|'.'
name|'source'
op|'='
name|'instance'
op|'.'
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'migrate_data'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'='
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler_client'
op|'='
name|'scheduler_client'
op|'.'
name|'SchedulerClient'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_api'
op|'='
name|'image'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|execute
dedent|''
name|'def'
name|'execute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_instance_is_active'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'source'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'destination'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'destination'
op|'='
name|'self'
op|'.'
name|'_find_destination'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'dest_compute'
op|'='
name|'self'
op|'.'
name|'destination'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_requested_destination'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(johngarbutt) need to move complexity out of compute manager'
nl|'\n'
comment|'# TODO(johngarbutt) disk_over_commit?'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'live_migration'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'source'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'dest'
op|'='
name|'self'
op|'.'
name|'destination'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'self'
op|'.'
name|'block_migration'
op|','
nl|'\n'
name|'migration'
op|'='
name|'self'
op|'.'
name|'migration'
op|','
nl|'\n'
name|'migrate_data'
op|'='
name|'self'
op|'.'
name|'migrate_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rollback
dedent|''
name|'def'
name|'rollback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(johngarbutt) need to implement the clean up operation'
nl|'\n'
comment|'# but this will make sense only once we pull in the compute'
nl|'\n'
comment|'# calls, since this class currently makes no state changes,'
nl|'\n'
comment|'# except to call the compute method, that has no matching'
nl|'\n'
comment|'# rollback call right now.'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_instance_is_active
dedent|''
name|'def'
name|'_check_instance_is_active'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'power_state'
name|'not'
name|'in'
op|'('
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'PAUSED'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'attr'
op|'='
string|"'power_state'"
op|','
nl|'\n'
name|'state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'power_state'
op|','
nl|'\n'
name|'method'
op|'='
string|"'live migrate'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_host_is_up
dedent|''
dedent|''
name|'def'
name|'_check_host_is_up'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'.'
name|'get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_requested_destination
dedent|''
dedent|''
name|'def'
name|'_check_requested_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_destination_is_not_source'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_destination_has_enough_memory'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_destination_is_not_source
dedent|''
name|'def'
name|'_check_destination_is_not_source'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'destination'
op|'=='
name|'self'
op|'.'
name|'source'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'UnableToMigrateToSelf'
op|'('
nl|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'uuid'
op|','
name|'host'
op|'='
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_destination_has_enough_memory
dedent|''
dedent|''
name|'def'
name|'_check_destination_has_enough_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'avail'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
op|'['
string|"'free_ram_mb'"
op|']'
newline|'\n'
name|'mem_inst'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'memory_mb'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'mem_inst'
name|'or'
name|'avail'
op|'<='
name|'mem_inst'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'uuid'
newline|'\n'
name|'dest'
op|'='
name|'self'
op|'.'
name|'destination'
newline|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Unable to migrate %(instance_uuid)s to %(dest)s: "'
nl|'\n'
string|'"Lack of memory(host:%(avail)s <= "'
nl|'\n'
string|'"instance:%(mem_inst)s)"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MigrationPreCheckError'
op|'('
name|'reason'
op|'='
name|'reason'
op|'%'
name|'dict'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
name|'dest'
op|'='
name|'dest'
op|','
name|'avail'
op|'='
name|'avail'
op|','
nl|'\n'
name|'mem_inst'
op|'='
name|'mem_inst'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_compute_info
dedent|''
dedent|''
name|'def'
name|'_get_compute_info'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'objects'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_first_node_by_host_for_old_compat'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_compatible_with_source_hypervisor
dedent|''
name|'def'
name|'_check_compatible_with_source_hypervisor'
op|'('
name|'self'
op|','
name|'destination'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'source_info'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'source'
op|')'
newline|'\n'
name|'destination_info'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'destination'
op|')'
newline|'\n'
nl|'\n'
name|'source_type'
op|'='
name|'source_info'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'destination_type'
op|'='
name|'destination_info'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'if'
name|'source_type'
op|'!='
name|'destination_type'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'source_version'
op|'='
name|'source_info'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'destination_version'
op|'='
name|'destination_info'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'if'
name|'source_version'
op|'>'
name|'destination_version'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_call_livem_checks_on_host
dedent|''
dedent|''
name|'def'
name|'_call_livem_checks_on_host'
op|'('
name|'self'
op|','
name|'destination'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'migrate_data'
op|'='
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'check_can_live_migrate_destination'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'destination'
op|','
name|'self'
op|'.'
name|'block_migration'
op|','
name|'self'
op|'.'
name|'disk_over_commit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_find_destination
dedent|''
name|'def'
name|'_find_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(johngarbutt) this retry loop should be shared'
nl|'\n'
indent|'        '
name|'attempted_hosts'
op|'='
op|'['
name|'self'
op|'.'
name|'source'
op|']'
newline|'\n'
name|'image'
op|'='
name|'utils'
op|'.'
name|'get_image_from_system_metadata'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'request_spec'
op|'='
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image'
op|','
nl|'\n'
op|'['
name|'self'
op|'.'
name|'instance'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'None'
newline|'\n'
name|'while'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_not_over_max_retries'
op|'('
name|'attempted_hosts'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'ignore_hosts'"
op|':'
name|'attempted_hosts'
op|'}'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'setup_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Invalid'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Skipping host: %(host)s because: %(e)s"'
op|','
nl|'\n'
op|'{'
string|'"host"'
op|':'
name|'host'
op|','
string|'"e"'
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'attempted_hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|')'
newline|'\n'
name|'host'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'host'
newline|'\n'
nl|'\n'
DECL|member|_check_not_over_max_retries
dedent|''
name|'def'
name|'_check_not_over_max_retries'
op|'('
name|'self'
op|','
name|'attempted_hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'migrate_max_retries'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'retries'
op|'='
name|'len'
op|'('
name|'attempted_hosts'
op|')'
op|'-'
number|'1'
newline|'\n'
name|'if'
name|'retries'
op|'>'
name|'CONF'
op|'.'
name|'migrate_max_retries'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'Exceeded max scheduling retries %(max_retries)d for '"
nl|'\n'
string|"'instance %(instance_uuid)s during live migration'"
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'max_retries'"
op|':'
name|'retries'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'uuid'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MaxRetriesExceeded'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
dedent|''
dedent|''
dedent|''
name|'def'
name|'execute'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'destination'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
name|'migration'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'task'
op|'='
name|'LiveMigrationTask'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'destination'
op|','
nl|'\n'
name|'block_migration'
op|','
nl|'\n'
name|'disk_over_commit'
op|','
nl|'\n'
name|'migration'
op|')'
newline|'\n'
comment|'# TODO(johngarbutt) create a superclass that contains a safe_execute call'
nl|'\n'
name|'return'
name|'task'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
