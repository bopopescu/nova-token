begin_unit
comment|'# Copyright (c) 2012 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""\nManagement class for Pool-related functions (join, eject, etc).\n"""'
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
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
op|'.'
name|'parse'
name|'as'
name|'urlparse'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'pool_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
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
DECL|variable|xenapi_pool_opts
name|'xenapi_pool_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_join_force'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'To use for hosts with different CPUs'"
op|')'
op|','
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
name|'xenapi_pool_opts'
op|','
string|"'xenserver'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourcePool
name|'class'
name|'ResourcePool'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements resource pool operations."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_rec'
op|'='
name|'session'
op|'.'
name|'host'
op|'.'
name|'get_record'
op|'('
name|'session'
op|'.'
name|'host_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host_rec'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_host_addr'
op|'='
name|'host_rec'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_host_uuid'
op|'='
name|'host_rec'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'_virtapi'
op|'='
name|'virtapi'
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
nl|'\n'
DECL|member|undo_aggregate_operation
dedent|''
name|'def'
name|'undo_aggregate_operation'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'op'
op|','
name|'aggregate'
op|','
nl|'\n'
name|'host'
op|','
name|'set_error'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Undo aggregate operation when pool error raised."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'set_error'
op|':'
newline|'\n'
indent|'                '
name|'metadata'
op|'='
op|'{'
name|'pool_states'
op|'.'
name|'KEY'
op|':'
name|'pool_states'
op|'.'
name|'ERROR'
op|'}'
newline|'\n'
name|'aggregate'
op|'.'
name|'update_metadata'
op|'('
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'op'
op|'('
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Aggregate %(aggregate_id)s: unrecoverable '"
nl|'\n'
string|"'state during operation on %(host)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'aggregate_id'"
op|':'
name|'aggregate'
op|'.'
name|'id'
op|','
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_to_aggregate
dedent|''
dedent|''
name|'def'
name|'add_to_aggregate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|','
name|'slave_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a compute host to an aggregate."""'
newline|'\n'
name|'if'
name|'not'
name|'pool_states'
op|'.'
name|'is_hv_pool'
op|'('
name|'aggregate'
op|'.'
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'invalid'
op|'='
op|'{'
name|'pool_states'
op|'.'
name|'CHANGING'
op|':'
name|'_'
op|'('
string|"'setup in progress'"
op|')'
op|','
nl|'\n'
name|'pool_states'
op|'.'
name|'DISMISSED'
op|':'
name|'_'
op|'('
string|"'aggregate deleted'"
op|')'
op|','
nl|'\n'
name|'pool_states'
op|'.'
name|'ERROR'
op|':'
name|'_'
op|'('
string|"'aggregate in error'"
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'aggregate'
op|'.'
name|'metadata'
op|'['
name|'pool_states'
op|'.'
name|'KEY'
op|']'
name|'in'
name|'invalid'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidAggregateActionAdd'
op|'('
nl|'\n'
name|'aggregate_id'
op|'='
name|'aggregate'
op|'.'
name|'id'
op|','
nl|'\n'
name|'reason'
op|'='
name|'invalid'
op|'['
name|'aggregate'
op|'.'
name|'metadata'
op|'['
name|'pool_states'
op|'.'
name|'KEY'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'aggregate'
op|'.'
name|'metadata'
op|'['
name|'pool_states'
op|'.'
name|'KEY'
op|']'
op|'=='
name|'pool_states'
op|'.'
name|'CREATED'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'.'
name|'update_metadata'
op|'('
op|'{'
name|'pool_states'
op|'.'
name|'KEY'
op|':'
name|'pool_states'
op|'.'
name|'CHANGING'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'aggregate'
op|'.'
name|'hosts'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
comment|'# this is the first host of the pool -> make it master'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_init_pool'
op|'('
name|'aggregate'
op|'.'
name|'id'
op|','
name|'aggregate'
op|'.'
name|'name'
op|')'
newline|'\n'
comment|'# save metadata so that we can find the master again'
nl|'\n'
name|'metadata'
op|'='
op|'{'
string|"'master_compute'"
op|':'
name|'host'
op|','
nl|'\n'
name|'host'
op|':'
name|'self'
op|'.'
name|'_host_uuid'
op|','
nl|'\n'
name|'pool_states'
op|'.'
name|'KEY'
op|':'
name|'pool_states'
op|'.'
name|'ACTIVE'
op|'}'
newline|'\n'
name|'aggregate'
op|'.'
name|'update_metadata'
op|'('
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# the pool is already up and running, we need to figure out'
nl|'\n'
comment|'# whether we can serve the request from this host or not.'
nl|'\n'
indent|'            '
name|'master_compute'
op|'='
name|'aggregate'
op|'.'
name|'metadata'
op|'['
string|"'master_compute'"
op|']'
newline|'\n'
name|'if'
name|'master_compute'
op|'=='
name|'CONF'
op|'.'
name|'host'
name|'and'
name|'master_compute'
op|'!='
name|'host'
op|':'
newline|'\n'
comment|'# this is the master ->  do a pool-join'
nl|'\n'
comment|'# To this aim, nova compute on the slave has to go down.'
nl|'\n'
comment|'# NOTE: it is assumed that ONLY nova compute is running now'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'_join_slave'
op|'('
name|'aggregate'
op|'.'
name|'id'
op|','
name|'host'
op|','
nl|'\n'
name|'slave_info'
op|'.'
name|'get'
op|'('
string|"'compute_uuid'"
op|')'
op|','
nl|'\n'
name|'slave_info'
op|'.'
name|'get'
op|'('
string|"'url'"
op|')'
op|','
name|'slave_info'
op|'.'
name|'get'
op|'('
string|"'user'"
op|')'
op|','
nl|'\n'
name|'slave_info'
op|'.'
name|'get'
op|'('
string|"'passwd'"
op|')'
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
name|'host'
op|':'
name|'slave_info'
op|'.'
name|'get'
op|'('
string|"'xenhost_uuid'"
op|')'
op|','
op|'}'
newline|'\n'
name|'aggregate'
op|'.'
name|'update_metadata'
op|'('
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'master_compute'
name|'and'
name|'master_compute'
op|'!='
name|'host'
op|':'
newline|'\n'
comment|'# send rpc cast to master, asking to add the following'
nl|'\n'
comment|'# host with specified credentials.'
nl|'\n'
indent|'                '
name|'slave_info'
op|'='
name|'self'
op|'.'
name|'_create_slave_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'add_aggregate_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|','
name|'master_compute'
op|','
name|'slave_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_from_aggregate
dedent|''
dedent|''
dedent|''
name|'def'
name|'remove_from_aggregate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|','
name|'slave_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a compute host from an aggregate."""'
newline|'\n'
name|'slave_info'
op|'='
name|'slave_info'
name|'or'
name|'dict'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pool_states'
op|'.'
name|'is_hv_pool'
op|'('
name|'aggregate'
op|'.'
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'invalid'
op|'='
op|'{'
name|'pool_states'
op|'.'
name|'CREATED'
op|':'
name|'_'
op|'('
string|"'no hosts to remove'"
op|')'
op|','
nl|'\n'
name|'pool_states'
op|'.'
name|'CHANGING'
op|':'
name|'_'
op|'('
string|"'setup in progress'"
op|')'
op|','
nl|'\n'
name|'pool_states'
op|'.'
name|'DISMISSED'
op|':'
name|'_'
op|'('
string|"'aggregate deleted'"
op|')'
op|'}'
newline|'\n'
name|'if'
name|'aggregate'
op|'.'
name|'metadata'
op|'['
name|'pool_states'
op|'.'
name|'KEY'
op|']'
name|'in'
name|'invalid'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidAggregateActionDelete'
op|'('
nl|'\n'
name|'aggregate_id'
op|'='
name|'aggregate'
op|'.'
name|'id'
op|','
nl|'\n'
name|'reason'
op|'='
name|'invalid'
op|'['
name|'aggregate'
op|'.'
name|'metadata'
op|'['
name|'pool_states'
op|'.'
name|'KEY'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'master_compute'
op|'='
name|'aggregate'
op|'.'
name|'metadata'
op|'['
string|"'master_compute'"
op|']'
newline|'\n'
name|'if'
name|'master_compute'
op|'=='
name|'CONF'
op|'.'
name|'host'
name|'and'
name|'master_compute'
op|'!='
name|'host'
op|':'
newline|'\n'
comment|'# this is the master -> instruct it to eject a host from the pool'
nl|'\n'
indent|'            '
name|'host_uuid'
op|'='
name|'aggregate'
op|'.'
name|'metadata'
op|'['
name|'host'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_eject_slave'
op|'('
name|'aggregate'
op|'.'
name|'id'
op|','
nl|'\n'
name|'slave_info'
op|'.'
name|'get'
op|'('
string|"'compute_uuid'"
op|')'
op|','
name|'host_uuid'
op|')'
newline|'\n'
name|'aggregate'
op|'.'
name|'update_metadata'
op|'('
op|'{'
name|'host'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'master_compute'
op|'=='
name|'host'
op|':'
newline|'\n'
comment|'# Remove master from its own pool -> destroy pool only if the'
nl|'\n'
comment|'# master is on its own, otherwise raise fault. Destroying a'
nl|'\n'
comment|'# pool made only by master is fictional'
nl|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'aggregate'
op|'.'
name|'hosts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
comment|'# NOTE: this could be avoided by doing a master'
nl|'\n'
comment|'# re-election, but this is simpler for now.'
nl|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidAggregateActionDelete'
op|'('
nl|'\n'
name|'aggregate_id'
op|'='
name|'aggregate'
op|'.'
name|'id'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to eject %s '"
nl|'\n'
string|"'from the pool; pool not empty'"
op|')'
nl|'\n'
op|'%'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_clear_pool'
op|'('
name|'aggregate'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'aggregate'
op|'.'
name|'update_metadata'
op|'('
op|'{'
string|"'master_compute'"
op|':'
name|'None'
op|','
name|'host'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'master_compute'
name|'and'
name|'master_compute'
op|'!='
name|'host'
op|':'
newline|'\n'
comment|'# A master exists -> forward pool-eject request to master'
nl|'\n'
indent|'            '
name|'slave_info'
op|'='
name|'self'
op|'.'
name|'_create_slave_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'remove_aggregate_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'aggregate'
op|'.'
name|'id'
op|','
name|'host'
op|','
name|'master_compute'
op|','
name|'slave_info'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# this shouldn't have happened"
nl|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'AggregateError'
op|'('
name|'aggregate_id'
op|'='
name|'aggregate'
op|'.'
name|'id'
op|','
nl|'\n'
name|'action'
op|'='
string|"'remove_from_aggregate'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to eject %s '"
nl|'\n'
string|"'from the pool; No master found'"
op|')'
nl|'\n'
op|'%'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_join_slave
dedent|''
dedent|''
name|'def'
name|'_join_slave'
op|'('
name|'self'
op|','
name|'aggregate_id'
op|','
name|'host'
op|','
name|'compute_uuid'
op|','
name|'url'
op|','
name|'user'
op|','
name|'passwd'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Joins a slave into a XenServer resource pool."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'='
op|'{'
string|"'compute_uuid'"
op|':'
name|'compute_uuid'
op|','
nl|'\n'
string|"'url'"
op|':'
name|'url'
op|','
nl|'\n'
string|"'user'"
op|':'
name|'user'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'passwd'
op|','
nl|'\n'
string|"'force'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'use_join_force'
op|')'
op|','
nl|'\n'
string|"'master_addr'"
op|':'
name|'self'
op|'.'
name|'_host_addr'
op|','
nl|'\n'
string|"'master_user'"
op|':'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_username'
op|','
nl|'\n'
string|"'master_pass'"
op|':'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_password'
op|','
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_plugin'
op|'('
string|"'xenhost'"
op|','
string|"'host_join'"
op|','
name|'args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Pool-Join failed: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AggregateError'
op|'('
name|'aggregate_id'
op|'='
name|'aggregate_id'
op|','
nl|'\n'
name|'action'
op|'='
string|"'add_to_aggregate'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to join %s '"
nl|'\n'
string|"'in the pool'"
op|')'
op|'%'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_eject_slave
dedent|''
dedent|''
name|'def'
name|'_eject_slave'
op|'('
name|'self'
op|','
name|'aggregate_id'
op|','
name|'compute_uuid'
op|','
name|'host_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Eject a slave from a XenServer resource pool."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# shutdown nova-compute; if there are other VMs running, e.g.'
nl|'\n'
comment|"# guest instances, the eject will fail. That's a precaution"
nl|'\n'
comment|'# to deal with the fact that the admin should evacuate the host'
nl|'\n'
comment|'# first. The eject wipes out the host completely.'
nl|'\n'
indent|'            '
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VM'
op|'.'
name|'get_by_uuid'
op|'('
name|'compute_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VM'
op|'.'
name|'clean_shutdown'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'host_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'host'
op|'.'
name|'get_by_uuid'
op|'('
name|'host_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'pool'
op|'.'
name|'eject'
op|'('
name|'host_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Pool-eject failed: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AggregateError'
op|'('
name|'aggregate_id'
op|'='
name|'aggregate_id'
op|','
nl|'\n'
name|'action'
op|'='
string|"'remove_from_aggregate'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_init_pool
dedent|''
dedent|''
name|'def'
name|'_init_pool'
op|'('
name|'self'
op|','
name|'aggregate_id'
op|','
name|'aggregate_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the name label of a XenServer pool."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pool_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'pool'
op|'.'
name|'get_all'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'pool'
op|'.'
name|'set_name_label'
op|'('
name|'pool_ref'
op|','
name|'aggregate_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Unable to set up pool: %s."'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AggregateError'
op|'('
name|'aggregate_id'
op|'='
name|'aggregate_id'
op|','
nl|'\n'
name|'action'
op|'='
string|"'add_to_aggregate'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_clear_pool
dedent|''
dedent|''
name|'def'
name|'_clear_pool'
op|'('
name|'self'
op|','
name|'aggregate_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Clear the name label of a XenServer pool."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pool_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'pool'
op|'.'
name|'get_all'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'pool'
op|'.'
name|'set_name_label'
op|'('
name|'pool_ref'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Pool-set_name_label failed: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AggregateError'
op|'('
name|'aggregate_id'
op|'='
name|'aggregate_id'
op|','
nl|'\n'
name|'action'
op|'='
string|"'remove_from_aggregate'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_slave_info
dedent|''
dedent|''
name|'def'
name|'_create_slave_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""XenServer specific info needed to join the hypervisor pool."""'
newline|'\n'
comment|'# replace the address from the xenapi connection url'
nl|'\n'
comment|'# because this might be 169.254.0.1, i.e. xenapi'
nl|'\n'
comment|"# NOTE: password in clear is not great, but it'll do for now"
nl|'\n'
name|'sender_url'
op|'='
name|'swap_xapi_host'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_url'
op|','
name|'self'
op|'.'
name|'_host_addr'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"url"'
op|':'
name|'sender_url'
op|','
nl|'\n'
string|'"user"'
op|':'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_username'
op|','
nl|'\n'
string|'"passwd"'
op|':'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_password'
op|','
nl|'\n'
string|'"compute_uuid"'
op|':'
name|'vm_utils'
op|'.'
name|'get_this_vm_uuid'
op|'('
name|'None'
op|')'
op|','
nl|'\n'
string|'"xenhost_uuid"'
op|':'
name|'self'
op|'.'
name|'_host_uuid'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|swap_xapi_host
dedent|''
dedent|''
name|'def'
name|'swap_xapi_host'
op|'('
name|'url'
op|','
name|'host_addr'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Replace the XenServer address present in \'url\' with \'host_addr\'."""'
newline|'\n'
name|'temp_url'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
newline|'\n'
name|'_netloc'
op|','
name|'sep'
op|','
name|'port'
op|'='
name|'temp_url'
op|'.'
name|'netloc'
op|'.'
name|'partition'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'return'
name|'url'
op|'.'
name|'replace'
op|'('
name|'temp_url'
op|'.'
name|'netloc'
op|','
string|"'%s%s%s'"
op|'%'
op|'('
name|'host_addr'
op|','
name|'sep'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
