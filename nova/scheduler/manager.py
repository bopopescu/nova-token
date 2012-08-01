begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
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
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
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
string|"'nova.scheduler.multi.MultiScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default driver to use for the scheduler'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
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
DECL|variable|RPC_API_VERSION
name|'RPC_API_VERSION'
op|'='
string|"'1.5'"
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
name|'FLAGS'
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
name|'super'
op|'('
name|'SchedulerManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Converts all method calls to use the schedule method"""'
newline|'\n'
comment|'# NOTE(russellb) Because of what this is doing, we must be careful'
nl|'\n'
comment|'# when changing the API of the scheduler drivers, as that changes'
nl|'\n'
comment|'# the rpc API as well, and the version should be updated accordingly.'
nl|'\n'
name|'return'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'self'
op|'.'
name|'_schedule'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_list
dedent|''
name|'def'
name|'get_host_list'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of hosts from the HostManager.\n\n        Currently unused, but left for backwards compatibility.\n        """'
newline|'\n'
name|'raise'
name|'rpc_common'
op|'.'
name|'RPCException'
op|'('
name|'message'
op|'='
name|'_'
op|'('
string|"'Deprecated in version 1.0'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_service_capabilities
dedent|''
name|'def'
name|'get_service_capabilities'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the normalized set of capabilities for this zone.\n\n        Has been unused since pre-essex, but remains for rpc API 1.X\n        completeness.\n        """'
newline|'\n'
name|'raise'
name|'rpc_common'
op|'.'
name|'RPCException'
op|'('
name|'message'
op|'='
name|'_'
op|'('
string|"'Deprecated in version 1.0'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'service_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|','
name|'capabilities'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Process a capability update from a service node."""'
newline|'\n'
name|'if'
name|'capabilities'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'.'
name|'update_service_capabilities'
op|'('
name|'service_name'
op|','
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'context'
op|','
name|'topic'
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
string|'"""Tries to call schedule_* method on the driver to retrieve host.\n        Falls back to schedule(context, topic) if method doesn\'t exist.\n        """'
newline|'\n'
name|'driver_method_name'
op|'='
string|"'schedule_%s'"
op|'%'
name|'method'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'driver_method'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
name|'driver_method_name'
op|')'
newline|'\n'
name|'args'
op|'='
op|'('
name|'context'
op|','
op|')'
op|'+'
name|'args'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Driver Method %(driver_method_name)s missing: "'
nl|'\n'
string|'"%(e)s. Reverting to schedule()"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'driver_method'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'schedule'
newline|'\n'
name|'args'
op|'='
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'method'
op|')'
op|'+'
name|'args'
newline|'\n'
nl|'\n'
comment|'# Scheduler methods are responsible for casting.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'driver_method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'request_spec'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state_and_notify'
op|'('
name|'method'
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
DECL|member|run_instance
dedent|''
dedent|''
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
name|'reservations'
op|','
name|'topic'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tries to call schedule_run_instance on the driver.\n        Sets instance vm_state to ERROR on exceptions\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
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
name|'reservations'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoValidHost'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|"# don't reraise"
nl|'\n'
indent|'            '
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
indent|'                '
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
indent|'            '
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
string|"'run_instance'"
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
nl|'\n'
comment|"# FIXME(comstud): Remove 'update_db' in a future version.  It's only"
nl|'\n'
comment|'# here for rpcapi backwards compatibility.'
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
name|'update_db'
op|'='
name|'None'
op|','
name|'instance'
op|'='
name|'None'
op|','
name|'instance_uuid'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'None'
op|','
name|'instance_type_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'None'
op|','
name|'topic'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tries to call schedule_prep_resize on the driver.\n        Sets instance vm_state to ACTIVE on NoHostFound\n        Sets vm_state to ERROR on other exceptions\n        """'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'context'
op|','
name|'instance_type_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'='
op|'{'
nl|'\n'
string|"'context'"
op|':'
name|'context'
op|','
nl|'\n'
string|"'image'"
op|':'
name|'image'
op|','
nl|'\n'
string|"'request_spec'"
op|':'
name|'request_spec'
op|','
nl|'\n'
string|"'filter_properties'"
op|':'
name|'filter_properties'
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'instance'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'reservations'"
op|':'
name|'reservations'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'schedule_prep_resize'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoValidHost'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
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
name|'ACTIVE'
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
indent|'                '
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
indent|'            '
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
string|"'prep_resize'"
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
nl|'\n'
DECL|member|_set_vm_state_and_notify
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
string|'"""changes VM state and notifies"""'
newline|'\n'
comment|'# FIXME(comstud): Re-factor this somehow. Not sure this belongs in the'
nl|'\n'
comment|'# scheduler manager like this. We should make this easier.'
nl|'\n'
comment|'# run_instance only sends a request_spec, and an instance may or may'
nl|'\n'
comment|'# not have been created in the API (or scheduler) already. If it was'
nl|'\n'
comment|"# created, there's a 'uuid' set in the instance_properties of the"
nl|'\n'
comment|'# request_spec.'
nl|'\n'
comment|'# (littleidea): I refactored this a bit, and I agree'
nl|'\n'
comment|'# it should be easier :)'
nl|'\n'
comment|'# The refactoring could go further but trying to minimize changes'
nl|'\n'
comment|'# for essex timeframe'
nl|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Failed to schedule_%(method)s: %(ex)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vm_state'
op|'='
name|'updates'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'properties'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance_uuid'
op|'='
name|'properties'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'state'
op|'='
name|'vm_state'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Setting instance to %(state)s state.'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|'# update instance state and notify on the transition'
nl|'\n'
op|'('
name|'old_ref'
op|','
name|'new_ref'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|','
name|'updates'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_ref'
op|','
name|'new_ref'
op|','
nl|'\n'
name|'service'
op|'='
string|'"scheduler"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'payload'
op|'='
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'instance_properties'
op|'='
name|'properties'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'state'
op|'='
name|'vm_state'
op|','
nl|'\n'
name|'method'
op|'='
name|'method'
op|','
nl|'\n'
name|'reason'
op|'='
name|'ex'
op|')'
newline|'\n'
nl|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'notifier'
op|'.'
name|'publisher_id'
op|'('
string|'"scheduler"'
op|')'
op|','
nl|'\n'
string|"'scheduler.'"
op|'+'
name|'method'
op|','
name|'notifier'
op|'.'
name|'ERROR'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE (masumotok) : This method should be moved to nova.api.ec2.admin.'
nl|'\n'
comment|'# Based on bexar design summit discussion,'
nl|'\n'
comment|'# just put this here for bexar release.'
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
name|'compute_ref'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'compute_ref'
op|'='
name|'compute_ref'
op|'['
number|'0'
op|']'
newline|'\n'
name|'instance_refs'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'compute_ref'
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
name|'compute_ref'
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
name|'manager'
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
dedent|''
dedent|''
endmarker|''
end_unit
