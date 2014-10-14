begin_unit
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
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'importutils'
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
name|'import'
name|'objects'
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
DECL|variable|scheduler_driver_opts
name|'scheduler_driver_opts'
op|'='
op|'['
nl|'\n'
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
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_driver_task_period'"
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
string|"'How often (in seconds) to run periodic tasks in '"
nl|'\n'
string|"'the scheduler driver of your choice. '"
nl|'\n'
string|"'Please note this is likely to interact with the value '"
nl|'\n'
string|"'of service_down_time, but exactly how they interact '"
nl|'\n'
string|"'will depend on your choice of scheduler driver.'"
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
name|'scheduler_driver_opts'
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
string|"'3.0'"
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
comment|'# NOTE(alaski): Remove this method when the scheduler rpc interface is'
nl|'\n'
comment|'# bumped to 4.x as it is no longer used.'
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
comment|'# NOTE(sbauza): Remove this method when the scheduler rpc interface is'
nl|'\n'
comment|'# bumped to 4.x as it is no longer used.'
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
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
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
dedent|''
op|'@'
name|'periodic_task'
op|'.'
name|'periodic_task'
op|'('
name|'spacing'
op|'='
name|'CONF'
op|'.'
name|'scheduler_driver_task_period'
op|','
nl|'\n'
name|'run_immediately'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|_run_periodic_tasks
name|'def'
name|'_run_periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'run_periodic_tasks'
op|'('
name|'context'
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
