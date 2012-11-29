begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
string|'"""Client side of the conductor RPC API"""'
newline|'\n'
nl|'\n'
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
name|'jsonutils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorAPI
name|'class'
name|'ConductorAPI'
op|'('
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Client side of the conductor RPC API\n\n    API version history:\n\n    1.0 - Initial version.\n    1.1 - Added migration_update\n    1.2 - Added instance_get_by_uuid and instance_get_all_by_host\n    """'
newline|'\n'
nl|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConductorAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'instance_update'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|'='
name|'updates_p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_by_uuid
dedent|''
name|'def'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'msg'
op|','
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_host
dedent|''
name|'def'
name|'instance_get_all_by_host'
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
name|'msg'
op|'='
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'instance_get_all_by_host'"
op|','
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'msg'
op|','
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_update
dedent|''
name|'def'
name|'migration_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migration'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'migration_update'"
op|','
name|'migration'
op|'='
name|'migration_p'
op|','
nl|'\n'
name|'status'
op|'='
name|'status'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'msg'
op|','
name|'version'
op|'='
string|"'1.1'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
