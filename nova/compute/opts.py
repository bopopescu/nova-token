begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may not'
nl|'\n'
comment|'# use this file except in compliance with the License. You may obtain a copy'
nl|'\n'
comment|'# of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'flavors'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'monitors'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'resource_tracker'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'rpcapi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
op|'('
string|"'DEFAULT'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'api'
op|'.'
name|'compute_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'flavors'
op|'.'
name|'flavor_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'compute_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'instance_cleaning_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'interval_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'running_deleted_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'timeout_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'monitors'
op|'.'
name|'compute_monitors_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'resource_tracker'
op|'.'
name|'resource_tracker_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'ephemeral_storage_encryption'"
op|','
nl|'\n'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'api'
op|'.'
name|'ephemeral_storage_encryption_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'upgrade_levels'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
