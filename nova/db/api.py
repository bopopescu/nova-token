begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nDefines interface for DB access\n"""'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'db_backend'"
op|','
string|"'sqlalchemy'"
op|','
nl|'\n'
string|"'The backend to use for db'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|IMPL
name|'IMPL'
op|'='
name|'utils'
op|'.'
name|'LazyPluggable'
op|'('
name|'FLAGS'
op|'['
string|"'db_backend'"
op|']'
op|','
nl|'\n'
DECL|variable|sqlalchemy
name|'sqlalchemy'
op|'='
string|"'nova.db.sqlalchemy.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoMoreAddresses
name|'class'
name|'NoMoreAddresses'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""No more available addresses"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoMoreBlades
dedent|''
name|'class'
name|'NoMoreBlades'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""No more available blades"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoMoreNetworks
dedent|''
name|'class'
name|'NoMoreNetworks'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""No more available networks"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|service_get
dedent|''
name|'def'
name|'service_get'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an service or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'service_get'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|service_get_by_args
dedent|''
name|'def'
name|'service_get_by_args'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the state of an service by node name and binary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'service_get_by_args'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|service_create
dedent|''
name|'def'
name|'service_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a service from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|service_update
dedent|''
name|'def'
name|'service_update'
op|'('
name|'context'
op|','
name|'service_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an service and update it.\n\n    Raises NotFound if service does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'service_update'
op|'('
name|'context'
op|','
name|'service_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_allocate_address
dedent|''
name|'def'
name|'floating_ip_allocate_address'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Allocate free floating ip and return the address.\n\n    Raises if one is not available.\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_allocate_address'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_create
dedent|''
name|'def'
name|'floating_ip_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a floating ip from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_count_by_project
dedent|''
name|'def'
name|'floating_ip_count_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Count floating ips used by project."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_count_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_deallocate
dedent|''
name|'def'
name|'floating_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deallocate an floating ip by address"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_destroy
dedent|''
name|'def'
name|'floating_ip_destroy'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the floating_ip or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_disassociate
dedent|''
name|'def'
name|'floating_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Disassociate an floating ip from a fixed ip by address.\n\n    Returns the address of the existing fixed ip.\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_fixed_ip_associate
dedent|''
name|'def'
name|'floating_ip_fixed_ip_associate'
op|'('
name|'context'
op|','
name|'floating_address'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Associate an floating ip to a fixed_ip by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_fixed_ip_associate'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_address'
op|','
nl|'\n'
name|'fixed_address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_get_all
dedent|''
name|'def'
name|'floating_ip_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all floating ips."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_get_all_by_host
dedent|''
name|'def'
name|'floating_ip_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all floating ips."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_get_by_address
dedent|''
name|'def'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a floating ip by address or raise if it doesn\'t exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_get_instance
dedent|''
name|'def'
name|'floating_ip_get_instance'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an instance for a floating ip by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'floating_ip_get_instance'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'####################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_allocate
dedent|''
name|'def'
name|'fixed_ip_allocate'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Allocate free fixed ip and return the address.\n\n    Raises if one is not available.\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_allocate'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_create
dedent|''
name|'def'
name|'fixed_ip_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a fixed ip from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_deallocate
dedent|''
name|'def'
name|'fixed_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deallocate a fixed ip by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_get_by_address
dedent|''
name|'def'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a fixed ip by address or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_get_instance
dedent|''
name|'def'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an instance for a fixed ip by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_get_network
dedent|''
name|'def'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a network for a fixed ip by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_instance_associate
dedent|''
name|'def'
name|'fixed_ip_instance_associate'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Associate a fixed ip to an instance by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_instance_associate'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_instance_disassociate
dedent|''
name|'def'
name|'fixed_ip_instance_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Disassociate a fixed ip from an instance by address."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_instance_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_update
dedent|''
name|'def'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a fixed ip from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'####################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_create
dedent|''
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create an instance from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_data_get_for_project
dedent|''
name|'def'
name|'instance_data_get_for_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get (instance_count, core_count) for project."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_data_get_for_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the instance or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an instance or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_all
dedent|''
name|'def'
name|'instance_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all instances."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_by_project
dedent|''
name|'def'
name|'instance_get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all instance belonging to a project."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_by_reservation
dedent|''
name|'def'
name|'instance_get_by_reservation'
op|'('
name|'context'
op|','
name|'reservation_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all instance belonging to a reservation."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get_by_reservation'
op|'('
name|'context'
op|','
name|'reservation_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_fixed_address
dedent|''
name|'def'
name|'instance_get_fixed_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the fixed ip address of an instance."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get_fixed_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_floating_address
dedent|''
name|'def'
name|'instance_get_floating_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the first floating ip address of an instance."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get_floating_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_by_str
dedent|''
name|'def'
name|'instance_get_by_str'
op|'('
name|'context'
op|','
name|'str_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an instance by string id."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_get_by_str'
op|'('
name|'context'
op|','
name|'str_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_is_vpn
dedent|''
name|'def'
name|'instance_is_vpn'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""True if instance is a vpn."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_is_vpn'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_set_state
dedent|''
name|'def'
name|'instance_set_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the state of an instance."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|','
name|'description'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an instance and update it.\n\n    Raises NotFound if instance does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'####################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_count
dedent|''
name|'def'
name|'network_count'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of networks."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_count'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_count_allocated_ips
dedent|''
name|'def'
name|'network_count_allocated_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of allocated non-reserved ips in the network."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_count_allocated_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_count_available_ips
dedent|''
name|'def'
name|'network_count_available_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of available ips in the network."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_count_available_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_count_reserved_ips
dedent|''
name|'def'
name|'network_count_reserved_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of reserved ips in the network."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_count_reserved_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_create
dedent|''
name|'def'
name|'network_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a network from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_create_fixed_ips
dedent|''
name|'def'
name|'network_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'num_vpn_clients'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create the ips for the network, reserving sepecified ips."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'num_vpn_clients'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_destroy
dedent|''
name|'def'
name|'network_destroy'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the network or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_destroy'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get
dedent|''
name|'def'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an network or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# pylint: disable-msg=C0103'
nl|'\n'
DECL|function|network_get_associated_fixed_ips
dedent|''
name|'def'
name|'network_get_associated_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all network\'s ips that have been associated."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get_by_bridge
dedent|''
name|'def'
name|'network_get_by_bridge'
op|'('
name|'context'
op|','
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an network or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_get_by_bridge'
op|'('
name|'context'
op|','
name|'bridge'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get_index
dedent|''
name|'def'
name|'network_get_index'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get non-conflicting index for network"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_get_index'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get_vpn_ip
dedent|''
name|'def'
name|'network_get_vpn_ip'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get non-conflicting index for network"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_get_vpn_ip'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_index_count
dedent|''
name|'def'
name|'network_index_count'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return count of network indexes"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_index_count'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_index_create
dedent|''
name|'def'
name|'network_index_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a network index from the values dict"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_index_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_set_cidr
dedent|''
name|'def'
name|'network_set_cidr'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the Classless Inner Domain Routing for the network"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_set_cidr'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_set_host
dedent|''
name|'def'
name|'network_set_host'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Safely set the host for network"""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_set_host'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_update
dedent|''
name|'def'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an network and update it.\n\n    Raises NotFound if network does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|project_get_network
dedent|''
name|'def'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the network associated with the project."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|queue_get_for
dedent|''
name|'def'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'physical_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a channel to send a message to a node with a topic."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'physical_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|export_device_count
dedent|''
name|'def'
name|'export_device_count'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return count of export devices."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'export_device_count'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|export_device_create
dedent|''
name|'def'
name|'export_device_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create an export_device from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'export_device_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_create
dedent|''
name|'def'
name|'quota_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a quota from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'quota_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_get
dedent|''
name|'def'
name|'quota_get'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve a quota or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'quota_get'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_update
dedent|''
name|'def'
name|'quota_update'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Update a quota from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'quota_update'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_destroy
dedent|''
name|'def'
name|'quota_destroy'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the quota or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'quota_destroy'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_allocate_shelf_and_blade
dedent|''
name|'def'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Atomically allocate a free shelf and blade from the pool."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_attached
dedent|''
name|'def'
name|'volume_attached'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that a volume is set as attached."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_attached'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_create
dedent|''
name|'def'
name|'volume_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a volume from the values dictionary."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_data_get_for_project
dedent|''
name|'def'
name|'volume_data_get_for_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get (volume_count, gigabytes) for project."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_data_get_for_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_destroy
dedent|''
name|'def'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the volume or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_detached
dedent|''
name|'def'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that a volume is set as detached."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get
dedent|''
name|'def'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a volume or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_all
dedent|''
name|'def'
name|'volume_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all volumes."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_instance
dedent|''
name|'def'
name|'volume_get_instance'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the instance that a volume is attached to."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_get_instance'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_by_project
dedent|''
name|'def'
name|'volume_get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all volumes belonging to a project."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_by_str
dedent|''
name|'def'
name|'volume_get_by_str'
op|'('
name|'context'
op|','
name|'str_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a volume by string id."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_get_by_str'
op|'('
name|'context'
op|','
name|'str_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_shelf_and_blade
dedent|''
name|'def'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the shelf and blade allocated to the volume."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_update
dedent|''
name|'def'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an volume and update it.\n\n    Raises NotFound if volume does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'values'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
