begin_unit
comment|'# Copyright (c) 2011-2013 OpenStack Foundation'
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
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'utils'
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
nl|'\n'
DECL|class|AggregateMultiTenancyIsolation
name|'class'
name|'AggregateMultiTenancyIsolation'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Isolate tenants in specific aggregates."""'
newline|'\n'
nl|'\n'
comment|'# Aggregate data and tenant do not change within a request'
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
newline|'\n'
nl|'\n'
op|'@'
name|'filters'
op|'.'
name|'compat_legacy_props'
newline|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""If a host is in an aggregate that has the metadata key\n        "filter_tenant_id" it can only create instances from that tenant(s).\n        A host can be in different aggregates.\n\n        If a host doesn\'t belong to an aggregate with the metadata key\n        "filter_tenant_id" it can create instances from all tenants.\n        """'
newline|'\n'
name|'spec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'props'
op|'='
name|'spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'tenant_id'
op|'='
name|'props'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
name|'utils'
op|'.'
name|'aggregate_metadata_get_by_host'
op|'('
name|'host_state'
op|','
nl|'\n'
name|'key'
op|'='
string|'"filter_tenant_id"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'metadata'
op|'!='
op|'{'
op|'}'
op|':'
newline|'\n'
indent|'            '
name|'configured_tenant_ids'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|'"filter_tenant_id"'
op|')'
newline|'\n'
name|'if'
name|'configured_tenant_ids'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'tenant_id'
name|'not'
name|'in'
name|'configured_tenant_ids'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%s fails tenant id on aggregate"'
op|','
name|'host_state'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Host tenant id %s matched"'
op|','
name|'tenant_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"No tenant id\'s defined on host. Host passes."'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
