begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
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
string|'"""Implementation of SQLAlchemy backend."""'
newline|'\n'
nl|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
op|'.'
name|'expression'
name|'import'
name|'asc'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
op|'.'
name|'expression'
name|'import'
name|'literal_column'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
name|'import'
name|'null'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'sqlalchemy_api'
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
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'uuidutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'session'
name|'as'
name|'db_session'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|model_query
name|'def'
name|'model_query'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Query helper that accounts for context\'s `read_deleted` field.\n\n    :param context: context to query under\n    :param session: if present, the session to use\n    :param read_deleted: if present, overrides context\'s read_deleted field.\n    :param project_only: if present and context is user-type, then restrict\n            query to match the context\'s project_id.\n    """'
newline|'\n'
name|'session'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'session'"
op|')'
name|'or'
name|'db_session'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'read_deleted'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'read_deleted'"
op|')'
name|'or'
name|'context'
op|'.'
name|'read_deleted'
newline|'\n'
name|'project_only'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'project_only'"
op|')'
newline|'\n'
nl|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'read_deleted'
op|'=='
string|"'no'"
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'read_deleted'
op|'=='
string|"'yes'"
op|':'
newline|'\n'
indent|'        '
name|'pass'
comment|'# omit the filter to include deleted and active'
newline|'\n'
dedent|''
name|'elif'
name|'read_deleted'
op|'=='
string|"'only'"
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unrecognized read_deleted value \'%s\'"'
op|')'
op|'%'
name|'read_deleted'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'project_only'
name|'and'
name|'nova'
op|'.'
name|'context'
op|'.'
name|'is_user_context'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'query'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_save
dedent|''
name|'def'
name|'_save'
op|'('
name|'ref'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'db_session'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
comment|'# We must not call ref.save() with session=None, otherwise NovaBase'
nl|'\n'
comment|"# uses nova-db's session, which cannot access bm-db."
nl|'\n'
dedent|''
name|'ref'
op|'.'
name|'save'
op|'('
name|'session'
op|'='
name|'session'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_node_order_by
dedent|''
name|'def'
name|'_build_node_order_by'
op|'('
name|'query'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'query'
op|'='
name|'query'
op|'.'
name|'order_by'
op|'('
name|'asc'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'memory_mb'
op|')'
op|')'
newline|'\n'
name|'query'
op|'='
name|'query'
op|'.'
name|'order_by'
op|'('
name|'asc'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'cpus'
op|')'
op|')'
newline|'\n'
name|'query'
op|'='
name|'query'
op|'.'
name|'order_by'
op|'('
name|'asc'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'local_gb'
op|')'
op|')'
newline|'\n'
name|'return'
name|'query'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_get_all
name|'def'
name|'bm_node_get_all'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'query'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
newline|'\n'
name|'if'
name|'service_host'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'query'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_get_associated
name|'def'
name|'bm_node_get_associated'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'query'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'instance_uuid'
op|'!='
name|'null'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'service_host'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'query'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_get_unassociated
name|'def'
name|'bm_node_get_unassociated'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'query'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'instance_uuid'
op|'=='
name|'null'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'service_host'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'query'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_find_free
name|'def'
name|'bm_node_find_free'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|','
nl|'\n'
name|'cpus'
op|'='
name|'None'
op|','
name|'memory_mb'
op|'='
name|'None'
op|','
name|'local_gb'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'query'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
newline|'\n'
name|'query'
op|'='
name|'query'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'instance_uuid'
op|'=='
name|'null'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'service_host'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cpus'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'cpus'
op|'>='
name|'cpus'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'memory_mb'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'memory_mb'
op|'>='
name|'memory_mb'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'local_gb'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'query'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'BareMetalNode'
op|'.'
name|'local_gb'
op|'>='
name|'local_gb'
op|')'
newline|'\n'
dedent|''
name|'query'
op|'='
name|'_build_node_order_by'
op|'('
name|'query'
op|')'
newline|'\n'
name|'return'
name|'query'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_get
name|'def'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
comment|'# bm_node_id may be passed as a string. Convert to INT to improve DB perf.'
nl|'\n'
indent|'    '
name|'bm_node_id'
op|'='
name|'int'
op|'('
name|'bm_node_id'
op|')'
newline|'\n'
name|'result'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'bm_node_id'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NodeNotFound'
op|'('
name|'node_id'
op|'='
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_get_by_instance_uuid
name|'def'
name|'bm_node_get_by_instance_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_get_by_node_uuid
name|'def'
name|'bm_node_get_by_node_uuid'
op|'('
name|'context'
op|','
name|'bm_node_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'uuid'
op|'='
name|'bm_node_uuid'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NodeNotFoundByUUID'
op|'('
name|'node_uuid'
op|'='
name|'bm_node_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_create
name|'def'
name|'bm_node_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'values'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'bm_node_ref'
op|'='
name|'models'
op|'.'
name|'BareMetalNode'
op|'('
op|')'
newline|'\n'
name|'bm_node_ref'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'_save'
op|'('
name|'bm_node_ref'
op|')'
newline|'\n'
name|'return'
name|'bm_node_ref'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_update
name|'def'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rows'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'bm_node_id'
op|')'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'rows'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NodeNotFound'
op|'('
name|'node_id'
op|'='
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_associate_and_update
name|'def'
name|'bm_node_associate_and_update'
op|'('
name|'context'
op|','
name|'node_uuid'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Associate an instance to a node safely\n\n    Associate an instance to a node only if that node is not yet associated.\n    Allow the caller to set any other fields they require in the same\n    operation. For example, this is used to set the node\'s task_state to\n    BUILDING at the beginning of driver.spawn().\n\n    """'
newline|'\n'
name|'if'
string|"'instance_uuid'"
name|'not'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"instance_uuid must be supplied to bm_node_associate_and_update"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'session'
op|'='
name|'db_session'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'query'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
nl|'\n'
name|'session'
op|'='
name|'session'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'uuid'
op|'='
name|'node_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'count'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|'.'
name|'update'
op|'('
name|'values'
op|','
name|'synchronize_session'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'count'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"Failed to associate instance %(i_uuid)s to baremetal node "'
nl|'\n'
string|'"%(n_uuid)s."'
op|')'
op|'%'
op|'{'
string|"'i_uuid'"
op|':'
name|'values'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
string|"'n_uuid'"
op|':'
name|'node_uuid'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'ref'
op|'='
name|'query'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ref'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_node_destroy
name|'def'
name|'bm_node_destroy'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
comment|'# First, delete all interfaces belonging to the node.'
nl|'\n'
comment|'# Delete physically since these have unique columns.'
nl|'\n'
indent|'    '
name|'session'
op|'='
name|'db_session'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'bm_node_id'
op|'='
name|'bm_node_id'
op|')'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
name|'rows'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalNode'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'bm_node_id'
op|')'
op|'.'
name|'update'
op|'('
op|'{'
string|"'deleted'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'literal_column'
op|'('
string|"'updated_at'"
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'rows'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NodeNotFound'
op|'('
name|'node_id'
op|'='
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_get
name|'def'
name|'bm_interface_get'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
nl|'\n'
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'if_id'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Baremetal interface %s "'
nl|'\n'
string|'"not found"'
op|')'
op|'%'
name|'if_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_get_all
name|'def'
name|'bm_interface_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'query'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
nl|'\n'
name|'read_deleted'
op|'='
string|'"no"'
op|')'
newline|'\n'
name|'return'
name|'query'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_destroy
name|'def'
name|'bm_interface_destroy'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
op|':'
newline|'\n'
comment|'# Delete physically since it has unique columns'
nl|'\n'
indent|'    '
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'if_id'
op|')'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_create
name|'def'
name|'bm_interface_create'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|','
name|'address'
op|','
name|'datapath_id'
op|','
name|'port_no'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ref'
op|'='
name|'models'
op|'.'
name|'BareMetalInterface'
op|'('
op|')'
newline|'\n'
name|'ref'
op|'.'
name|'bm_node_id'
op|'='
name|'bm_node_id'
newline|'\n'
name|'ref'
op|'.'
name|'address'
op|'='
name|'address'
newline|'\n'
name|'ref'
op|'.'
name|'datapath_id'
op|'='
name|'datapath_id'
newline|'\n'
name|'ref'
op|'.'
name|'port_no'
op|'='
name|'port_no'
newline|'\n'
name|'_save'
op|'('
name|'ref'
op|')'
newline|'\n'
name|'return'
name|'ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_set_vif_uuid
name|'def'
name|'bm_interface_set_vif_uuid'
op|'('
name|'context'
op|','
name|'if_id'
op|','
name|'vif_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'db_session'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bm_interface'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
nl|'\n'
name|'read_deleted'
op|'='
string|'"no"'
op|','
name|'session'
op|'='
name|'session'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'if_id'
op|')'
op|'.'
name|'with_lockmode'
op|'('
string|"'update'"
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'bm_interface'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Baremetal interface %s "'
nl|'\n'
string|'"not found"'
op|')'
op|'%'
name|'if_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bm_interface'
op|'.'
name|'vif_uuid'
op|'='
name|'vif_uuid'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'add'
op|'('
name|'bm_interface'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'db_exc'
op|'.'
name|'DBError'
name|'as'
name|'e'
op|':'
newline|'\n'
comment|'# TODO(deva): clean up when db layer raises DuplicateKeyError'
nl|'\n'
indent|'            '
name|'if'
name|'str'
op|'('
name|'e'
op|')'
op|'.'
name|'find'
op|'('
string|"'IntegrityError'"
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Baremetal interface %s "'
nl|'\n'
string|'"already in use"'
op|')'
op|'%'
name|'vif_uuid'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_get_by_vif_uuid
name|'def'
name|'bm_interface_get_by_vif_uuid'
op|'('
name|'context'
op|','
name|'vif_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
nl|'\n'
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'vif_uuid'
op|'='
name|'vif_uuid'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Baremetal virtual interface %s "'
nl|'\n'
string|'"not found"'
op|')'
op|'%'
name|'vif_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sqlalchemy_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|bm_interface_get_all_by_bm_node_id
name|'def'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'model_query'
op|'('
name|'context'
op|','
name|'models'
op|'.'
name|'BareMetalInterface'
op|','
nl|'\n'
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'bm_node_id'
op|'='
name|'bm_node_id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NodeNotFound'
op|'('
name|'node_id'
op|'='
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
endmarker|''
end_unit
