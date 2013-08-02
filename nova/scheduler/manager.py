begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nScheduler Service\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
name|'import'
name|'messaging'
newline|'\n'
nl|'\n'
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
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'api'
name|'as'
name|'conductor_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'tasks'
name|'import'
name|'live_migrate'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'import'
name|'periodic_task'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
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
nl|'\n'
DECL|variable|scheduler_driver_opt
name|'scheduler_driver_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.filter_scheduler.FilterScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default driver to use for the scheduler'"
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
name|'scheduler_driver_opt'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerManager
name|'class'
name|'SchedulerManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Chooses a host to run instances on."""'
newline|'\n'
nl|'\n'
DECL|variable|target
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'version'
op|'='
string|"'2.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'scheduler_driver'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'scheduler_driver'
op|':'
newline|'\n'
indent|'            '
name|'scheduler_driver'
op|'='
name|'CONF'
op|'.'
name|'scheduler_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'scheduler_driver'
op|')'
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
name|'super'
op|'('
name|'SchedulerManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'scheduler'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'snapshot_id'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'None'
op|','
name|'image_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'#function removed in RPC API 2.3'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'messaging'
op|'.'
name|'expected_exceptions'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'UnableToMigrateToSelf'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidLocalStorage'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidSharedStorage'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'MigrationPreCheckError'
op|')'
newline|'\n'
DECL|member|live_migration
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_schedule_live_migration'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'UnableToMigrateToSelf'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidLocalStorage'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidSharedStorage'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'MigrationPreCheckError'
op|')'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'request_spec'
op|'='
op|'{'
string|"'instance_properties'"
op|':'
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
string|"'live_migration'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|','
nl|'\n'
name|'expected_task_state'
op|'='
name|'task_states'
op|'.'
name|'MIGRATING'
op|','
op|')'
op|','
nl|'\n'
name|'context'
op|','
name|'ex'
op|','
name|'request_spec'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'request_spec'
op|'='
op|'{'
string|"'instance_properties'"
op|':'
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
string|"'live_migration'"
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|'}'
op|','
nl|'\n'
name|'context'
op|','
name|'ex'
op|','
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule_live_migration
dedent|''
dedent|''
dedent|''
name|'def'
name|'_schedule_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'task'
op|'='
name|'live_migrate'
op|'.'
name|'LiveMigrationTask'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'dest'
op|','
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
newline|'\n'
name|'return'
name|'task'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_instance
dedent|''
name|'def'
name|'run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'admin_password'
op|','
nl|'\n'
name|'injected_files'
op|','
name|'requested_networks'
op|','
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'legacy_bdm_in_spec'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tries to call schedule_run_instance on the driver.\n        Sets instance vm_state to ERROR on exceptions\n        """'
newline|'\n'
name|'instance_uuids'
op|'='
name|'request_spec'
op|'['
string|"'instance_uuids'"
op|']'
newline|'\n'
name|'with'
name|'compute_utils'
op|'.'
name|'EventReporter'
op|'('
name|'context'
op|','
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|'('
op|')'
op|','
nl|'\n'
string|"'schedule'"
op|','
op|'*'
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'schedule_run_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'admin_password'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|','
name|'is_first_time'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'legacy_bdm_in_spec'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoValidHost'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|"# don't re-raise"
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
string|"'run_instance'"
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
name|'context'
op|','
name|'ex'
op|','
name|'request_spec'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
string|"'run_instance'"
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
name|'context'
op|','
name|'ex'
op|','
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prep_resize
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'prep_resize'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'instance'
op|','
name|'instance_type'
op|','
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tries to call schedule_prep_resize on the driver.\n        Sets instance vm_state to ACTIVE on NoHostFound\n        Sets vm_state to ERROR on other exceptions\n        """'
newline|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'with'
name|'compute_utils'
op|'.'
name|'EventReporter'
op|'('
name|'context'
op|','
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|'('
op|')'
op|','
nl|'\n'
string|"'schedule'"
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'request_spec'
op|'['
string|"'num_instances'"
op|']'
op|'='
name|'len'
op|'('
nl|'\n'
name|'request_spec'
op|'['
string|"'instance_uuids'"
op|']'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
nl|'\n'
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'host_state'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'populate_filter_properties'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'host_state'
op|')'
newline|'\n'
comment|'# context is not serializable'
nl|'\n'
name|'filter_properties'
op|'.'
name|'pop'
op|'('
string|"'context'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'host'
op|','
name|'node'
op|')'
op|'='
op|'('
name|'host_state'
op|'['
string|"'host'"
op|']'
op|','
name|'host_state'
op|'['
string|"'nodename'"
op|']'
op|')'
newline|'\n'
name|'attrs'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|','
string|"'info_cache'"
op|','
nl|'\n'
string|"'security_groups'"
op|']'
newline|'\n'
name|'inst_obj'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_obj'
op|'.'
name|'Instance'
op|'('
op|')'
op|','
name|'instance'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'attrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'prep_resize'
op|'('
nl|'\n'
name|'context'
op|','
name|'image'
op|','
name|'inst_obj'
op|','
name|'instance_type'
op|','
name|'host'
op|','
nl|'\n'
name|'reservations'
op|','
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
name|'node'
op|'='
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoValidHost'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'vm_state'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'vm_state'"
op|','
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
string|"'prep_resize'"
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_state'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
name|'context'
op|','
name|'ex'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'if'
name|'reservations'
op|':'
newline|'\n'
indent|'                    '
name|'QUOTAS'
op|'.'
name|'rollback'
op|'('
name|'context'
op|','
name|'reservations'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
string|"'prep_resize'"
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
name|'context'
op|','
name|'ex'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'if'
name|'reservations'
op|':'
newline|'\n'
indent|'                        '
name|'QUOTAS'
op|'.'
name|'rollback'
op|'('
name|'context'
op|','
name|'reservations'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_vm_state_and_notify
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_set_vm_state_and_notify'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'updates'
op|','
name|'context'
op|','
name|'ex'
op|','
nl|'\n'
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler_utils'
op|'.'
name|'set_vm_state_and_notify'
op|'('
nl|'\n'
name|'context'
op|','
string|"'scheduler'"
op|','
name|'method'
op|','
name|'updates'
op|','
name|'ex'
op|','
name|'request_spec'
op|','
name|'self'
op|'.'
name|'db'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(hanlind): This method can be removed in v3.0 of the RPC API.'
nl|'\n'
DECL|member|show_host_resources
dedent|''
name|'def'
name|'show_host_resources'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shows the physical/usage resource given by hosts.\n\n        :param context: security context\n        :param host: hostname\n        :returns:\n            example format is below::\n\n                {\'resource\':D, \'usage\':{proj_id1:D, proj_id2:D}}\n                D: {\'vcpus\': 3, \'memory_mb\': 2048, \'local_gb\': 2048,\n                    \'vcpus_used\': 12, \'memory_mb_used\': 10240,\n                    \'local_gb_used\': 64}\n\n        """'
newline|'\n'
comment|'# Getting compute node info and related instances info'
nl|'\n'
name|'service_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'instance_refs'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'service_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting total available/used resource'
nl|'\n'
name|'compute_ref'
op|'='
name|'service_ref'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'resource'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'compute_ref'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'compute_ref'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'compute_ref'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
name|'compute_ref'
op|'['
string|"'vcpus_used'"
op|']'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'compute_ref'
op|'['
string|"'memory_mb_used'"
op|']'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'compute_ref'
op|'['
string|"'local_gb_used'"
op|']'
op|'}'
newline|'\n'
name|'usage'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_refs'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'usage'"
op|':'
name|'usage'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Getting usage resource per project'
nl|'\n'
dedent|''
name|'project_ids'
op|'='
op|'['
name|'i'
op|'['
string|"'project_id'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
op|']'
newline|'\n'
name|'project_ids'
op|'='
name|'list'
op|'('
name|'set'
op|'('
name|'project_ids'
op|')'
op|')'
newline|'\n'
name|'for'
name|'project_id'
name|'in'
name|'project_ids'
op|':'
newline|'\n'
indent|'            '
name|'vcpus'
op|'='
op|'['
name|'i'
op|'['
string|"'vcpus'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'mem'
op|'='
op|'['
name|'i'
op|'['
string|"'memory_mb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'root'
op|'='
op|'['
name|'i'
op|'['
string|"'root_gb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'ephemeral'
op|'='
op|'['
name|'i'
op|'['
string|"'ephemeral_gb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'usage'
op|'['
name|'project_id'
op|']'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'sum'
op|'('
name|'vcpus'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'sum'
op|'('
name|'mem'
op|')'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
name|'sum'
op|'('
name|'root'
op|')'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'sum'
op|'('
name|'ephemeral'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'usage'"
op|':'
name|'usage'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'periodic_task'
op|'.'
name|'periodic_task'
newline|'\n'
DECL|member|_expire_reservations
name|'def'
name|'_expire_reservations'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'QUOTAS'
op|'.'
name|'expire'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(russellb) This method can be removed in 3.0 of this API.  It is'
nl|'\n'
comment|'# deprecated in favor of the method in the base API.'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
name|'def'
name|'get_backdoor_port'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'backdoor_port'
newline|'\n'
nl|'\n'
comment|'# NOTE(hanlind): This method can be removed in v4.0 of the RPC API.'
nl|'\n'
dedent|''
op|'@'
name|'messaging'
op|'.'
name|'expected_exceptions'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|')'
newline|'\n'
DECL|member|select_hosts
name|'def'
name|'select_hosts'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns host(s) best suited for this request_spec\n        and filter_properties.\n        """'
newline|'\n'
name|'dests'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
name|'dest'
op|'['
string|"'host'"
op|']'
name|'for'
name|'dest'
name|'in'
name|'dests'
op|']'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'messaging'
op|'.'
name|'expected_exceptions'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|')'
newline|'\n'
DECL|member|select_destinations
name|'def'
name|'select_destinations'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns destinations(s) best suited for this request_spec and\n        filter_properties.\n\n        The result should be a list of dicts with \'host\', \'nodename\' and\n        \'limits\' as keys.\n        """'
newline|'\n'
name|'dests'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'dests'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
