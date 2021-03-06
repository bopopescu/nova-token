begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
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
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregatesSampleJsonTest
name|'class'
name|'AggregatesSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-aggregates"'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'AggregatesSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.aggregates.Aggregates'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_create
dedent|''
name|'def'
name|'test_aggregate_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|'"aggregate_id"'
op|':'
string|"'(?P<id>\\d+)'"
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates'"
op|','
string|"'aggregate-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregate-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_aggregates
dedent|''
name|'def'
name|'test_list_aggregates'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-aggregates'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-list-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_get
dedent|''
name|'def'
name|'test_aggregate_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-aggregates/%s'"
op|'%'
name|'agg_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_metadata
dedent|''
name|'def'
name|'test_add_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates/%s/action'"
op|'%'
name|'agg_id'
op|','
nl|'\n'
string|"'aggregate-metadata-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'set_metadata'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-metadata-post-resp'"
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_host
dedent|''
name|'def'
name|'test_add_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|'"host_name"'
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates/%s/action'"
op|'%'
name|'aggregate_id'
op|','
nl|'\n'
string|"'aggregate-add-host-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-add-host-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_host
dedent|''
name|'def'
name|'test_remove_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_add_host'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|'"host_name"'
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates/1/action'"
op|','
nl|'\n'
string|"'aggregate-remove-host-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-remove-host-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_aggregate
dedent|''
name|'def'
name|'test_update_aggregate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-aggregates/%s'"
op|'%'
name|'aggregate_id'
op|','
nl|'\n'
string|"'aggregate-update-post-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregate-update-post-resp'"
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
