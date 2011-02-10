begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Openstack, LLC.'
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
string|'"""\nScheduler base class that all Schedulers should inherit from\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'service_down_time'"
op|','
number|'60'
op|','
nl|'\n'
string|"'maximum time since last checkin for up service'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoValidHost
name|'class'
name|'NoValidHost'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""There is no valid host for the command."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WillNotSchedule
dedent|''
name|'class'
name|'WillNotSchedule'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The specified host is not up or doesn\'t exist."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Scheduler
dedent|''
name|'class'
name|'Scheduler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The base class that all Scheduler clases should inherit from."""'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|service_is_up
name|'def'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check whether a service is up based on last heartbeat."""'
newline|'\n'
name|'last_heartbeat'
op|'='
name|'service'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'service'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
comment|'# Timestamps in DB are UTC.'
nl|'\n'
name|'elapsed'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'last_heartbeat'
newline|'\n'
name|'return'
name|'elapsed'
op|'<'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'FLAGS'
op|'.'
name|'service_down_time'
op|')'
newline|'\n'
nl|'\n'
DECL|member|hosts_up
dedent|''
name|'def'
name|'hosts_up'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the list of hosts that have a running service for topic."""'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
op|'['
name|'service'
op|'.'
name|'host'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override at least this method for scheduler to work."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|'"Must implement a fallback schedule"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_live_migration
dedent|''
name|'def'
name|'schedule_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""live migration method"""'
newline|'\n'
nl|'\n'
comment|'# Whether instance exists and running'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking instance.'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_src_check'
op|'('
name|'context'
op|','
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking destination host.'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_dest_check'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Common checking.'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_common_check'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Changing instance_state.'
nl|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
string|"'migrating'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Changing volume state'
nl|'\n'
name|'for'
name|'v'
name|'in'
name|'instance_ref'
op|'['
string|"'volumes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'v'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'migrating'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Return value is necessary to send request to src'
nl|'\n'
comment|'# Check _schedule() in detail.'
nl|'\n'
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'return'
name|'src'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_src_check
dedent|''
name|'def'
name|'_live_migration_src_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration check routine (for src host)"""'
newline|'\n'
nl|'\n'
comment|'# Checking instance is running.'
nl|'\n'
name|'if'
name|'power_state'
op|'.'
name|'RUNNING'
op|'!='
name|'instance_ref'
op|'['
string|"'state'"
op|']'
name|'or'
string|"'running'"
op|'!='
name|'instance_ref'
op|'['
string|"'state_description'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Instance(%s) is not running'"
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'instance_ref'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|'%'
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checing volume node is running when any volumes are mounted'
nl|'\n'
comment|'# to the instance.'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'instance_ref'
op|'['
string|"'volumes'"
op|']'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
string|"'volume'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'services'
op|')'
op|'<'
number|'1'
name|'or'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'volume node is not alive(time synchronize problem?)'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking src host is alive.'
nl|'\n'
dedent|''
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'services'
op|'='
op|'['
name|'service'
name|'for'
name|'service'
name|'in'
name|'services'
name|'if'
name|'service'
op|'.'
name|'host'
op|'=='
name|'src'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'services'
op|')'
op|'<'
number|'1'
name|'or'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s is not alive(time synchronize problem?)'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|'%'
name|'src'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_dest_check
dedent|''
dedent|''
name|'def'
name|'_live_migration_dest_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration check routine (for destination host)"""'
newline|'\n'
nl|'\n'
comment|'# Checking dest exists and compute node.'
nl|'\n'
name|'dservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'dservice_refs'
op|')'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s does not exists.'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|'%'
name|'dest'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dservice_ref'
op|'='
name|'dservice_refs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'dservice_ref'
op|'['
string|"'topic'"
op|']'
op|'!='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s must be compute node'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|'%'
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking dest host is alive.'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'dservice_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s is not alive(time synchronize problem?)'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|'%'
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking whether The host where instance is running'
nl|'\n'
comment|'# and dest is not same.'
nl|'\n'
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'dest'
op|'=='
name|'src'
op|':'
newline|'\n'
indent|'            '
name|'ec2_id'
op|'='
name|'instance_ref'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"""%(dest)s is where %(ec2_id)s is """'
nl|'\n'
string|'"""running now. choose other host."""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking dst host still has enough capacities.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'has_enough_resource'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_common_check
dedent|''
name|'def'
name|'_live_migration_common_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Live migration check routine.\n        Below pre-checkings are followed by\n        http://wiki.libvirt.org/page/TodoPreMigrationChecks\n\n        """'
newline|'\n'
comment|'# Checking shared storage connectivity'
nl|'\n'
name|'self'
op|'.'
name|'mounted_on_same_shared_storage'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking dest exists.'
nl|'\n'
name|'dservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'dservice_refs'
op|')'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|"'%s does not exists.'"
op|')'
op|'%'
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'dservice_ref'
op|'='
name|'dservice_refs'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Checking original host( where instance was launched at) exists.'
nl|'\n'
name|'oservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'launched_on'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'oservice_refs'
op|')'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s(where instance was launched at) does not exists.'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|'%'
name|'instance_ref'
op|'['
string|"'launched_on'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'oservice_ref'
op|'='
name|'oservice_refs'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Checking hypervisor is same.'
nl|'\n'
name|'o'
op|'='
name|'oservice_ref'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'d'
op|'='
name|'dservice_ref'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'if'
name|'o'
op|'!='
name|'d'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Different hypervisor type(%(o)s->%(d)s)'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checkng hypervisor version.'
nl|'\n'
dedent|''
name|'o'
op|'='
name|'oservice_ref'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'d'
op|'='
name|'dservice_ref'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'if'
name|'o'
op|'>'
name|'d'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Older hypervisor version(%(o)s->%(d)s)'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking cpuinfo.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'dest'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|"'compare_cpu'"
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|"'cpu_info'"
op|':'
name|'oservice_ref'
op|'['
string|"'cpu_info'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'ec2_id'
op|'='
name|'instance_ref'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
op|'('
string|'"""%(dest)s doesnt have compatibility to %(src)s"""'
nl|'\n'
string|'"""(where %(ec2_id)s was launched at)"""'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'exception'
op|'('
name|'msg'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
DECL|member|has_enough_resource
dedent|''
dedent|''
name|'def'
name|'has_enough_resource'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check if destination host has enough resource for live migration.\n        Currently, only memory checking has been done.\n        If storage migration(block migration, meaning live-migration\n        without any shared storage) will be available, local storage\n        checking is also necessary.\n        """'
newline|'\n'
nl|'\n'
comment|'# Getting instance information'
nl|'\n'
name|'ec2_id'
op|'='
name|'instance_ref'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'mem'
op|'='
name|'instance_ref'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Getting host information'
nl|'\n'
name|'service_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'service_refs'
op|')'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|"'%s does not exists.'"
op|')'
op|'%'
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'service_ref'
op|'='
name|'service_refs'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'mem_total'
op|'='
name|'int'
op|'('
name|'service_ref'
op|'['
string|"'memory_mb'"
op|']'
op|')'
newline|'\n'
name|'mem_used'
op|'='
name|'int'
op|'('
name|'service_ref'
op|'['
string|"'memory_mb_used'"
op|']'
op|')'
newline|'\n'
name|'mem_avail'
op|'='
name|'mem_total'
op|'-'
name|'mem_used'
newline|'\n'
name|'mem_inst'
op|'='
name|'instance_ref'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'if'
name|'mem_avail'
op|'<='
name|'mem_inst'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"""%(ec2_id)s is not capable to migrate %(dest)s"""'
nl|'\n'
string|'"""(host:%(mem_avail)s <= instance:%(mem_inst)s)"""'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotEmpty'
op|'('
name|'msg'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|mounted_on_same_shared_storage
dedent|''
dedent|''
name|'def'
name|'mounted_on_same_shared_storage'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check if /nova-inst-dir/insntances is mounted same storage at\n        live-migration src and dest host.\n        """'
newline|'\n'
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'dst_t'
op|'='
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'dest'
op|')'
newline|'\n'
name|'src_t'
op|'='
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'src'
op|')'
newline|'\n'
nl|'\n'
comment|'# create tmpfile at dest host'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'filename'
op|'='
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'dst_t'
op|','
op|'{'
string|'"method"'
op|':'
string|"'mktmpfile'"
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot create tmpfile at %s to confirm shared storage."'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'msg'
op|'%'
name|'FLAGS'
op|'.'
name|'instance_path'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
comment|'# make sure existence at src host.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'src_t'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|"'confirm_tmpfile'"
op|','
string|'"args"'
op|':'
op|'{'
string|"'path'"
op|':'
name|'filename'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
op|'('
name|'rpc'
op|'.'
name|'RemoteError'
op|','
name|'exception'
op|'.'
name|'NotFound'
op|')'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'ipath'
op|'='
name|'FLAGS'
op|'.'
name|'instance_path'
newline|'\n'
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"""Cannot comfirm %(ipath)s at %(dest)s to """'
nl|'\n'
string|'"""confirm shared storage."""'
nl|'\n'
string|'"""Check if %(ipath)s is same shared storage."""'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'msg'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
