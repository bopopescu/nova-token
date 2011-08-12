begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AllHostsFilter
name|'class'
name|'AllHostsFilter'
op|'('
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'host_filter'
op|'.'
name|'AbstractHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""NOP host filter. Returns all hosts in ZoneManager."""'
newline|'\n'
DECL|member|instance_type_to_filter
name|'def'
name|'instance_type_to_filter'
op|'('
name|'self'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return anything to prevent base-class from raising\n        exception.\n        """'
newline|'\n'
name|'return'
op|'('
name|'self'
op|'.'
name|'_full_name'
op|'('
op|')'
op|','
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'zone_manager'
op|','
name|'query'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts from ZoneManager list."""'
newline|'\n'
name|'return'
op|'['
op|'('
name|'host'
op|','
name|'services'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
