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
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_service'
name|'import'
name|'periodic_task'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
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
string|"'4.2'"
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
name|'self'
op|'.'
name|'additional_endpoints'
op|'.'
name|'append'
op|'('
name|'_SchedulerManagerV3Proxy'
op|'('
name|'self'
op|')'
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
nl|'\n'
DECL|member|update_aggregates
dedent|''
name|'def'
name|'update_aggregates'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'aggregates'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates HostManager internal aggregates information.\n\n        :param aggregates: Aggregate(s) to update\n        :type aggregates: :class:`nova.objects.Aggregate`\n                          or :class:`nova.objects.AggregateList`\n        """'
newline|'\n'
comment|"# NOTE(sbauza): We're dropping the user context now as we don't need it"
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'update_aggregates'
op|'('
name|'aggregates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_aggregate
dedent|''
name|'def'
name|'delete_aggregate'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'aggregate'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes HostManager internal information about a specific aggregate.\n\n        :param aggregate: Aggregate to delete\n        :type aggregate: :class:`nova.objects.Aggregate`\n        """'
newline|'\n'
comment|"# NOTE(sbauza): We're dropping the user context now as we don't need it"
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'delete_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_instance_info
dedent|''
name|'def'
name|'update_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'instance_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Receives information about changes to a host\'s instances, and\n        updates the driver\'s HostManager with that information.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'update_instance_info'
op|'('
name|'context'
op|','
name|'host_name'
op|','
nl|'\n'
name|'instance_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_instance_info
dedent|''
name|'def'
name|'delete_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Receives information about the deletion of one of a host\'s\n        instances, and updates the driver\'s HostManager with that information.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'delete_instance_info'
op|'('
name|'context'
op|','
name|'host_name'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|sync_instance_info
dedent|''
name|'def'
name|'sync_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Receives a sync request from a host, and passes it on to the\n        driver\'s HostManager.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'sync_instance_info'
op|'('
name|'context'
op|','
name|'host_name'
op|','
nl|'\n'
name|'instance_uuids'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_SchedulerManagerV3Proxy
dedent|''
dedent|''
name|'class'
name|'_SchedulerManagerV3Proxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|target
indent|'    '
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
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
newline|'\n'
nl|'\n'
comment|'# NOTE(sbauza): Previous run_instance() and prep_resize() methods were'
nl|'\n'
comment|'# removed from the Juno branch before Juno released, so we can safely'
nl|'\n'
comment|'# remove them even from the V3.1 proxy as there is no Juno RPC client'
nl|'\n'
comment|'# that can call them'
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
comment|'# TODO(melwitt): Remove this in version 4.0 of the RPC API'
nl|'\n'
name|'flavor'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'if'
name|'flavor'
name|'and'
name|'not'
name|'isinstance'
op|'('
name|'flavor'
op|','
name|'objects'
op|'.'
name|'Flavor'
op|')'
op|':'
newline|'\n'
comment|'# Code downstream may expect extra_specs to be populated since it'
nl|'\n'
comment|'# is receiving an object, so lookup the flavor to ensure this.'
nl|'\n'
indent|'            '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|','
name|'flavor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'filter_properties'
op|','
name|'instance_type'
op|'='
name|'flavor'
op|')'
newline|'\n'
dedent|''
name|'dests'
op|'='
name|'self'
op|'.'
name|'manager'
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
name|'dests'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
