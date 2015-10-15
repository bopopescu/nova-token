begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'import'
name|'availability_zones'
newline|'\n'
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
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
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
comment|'# NOTE(danms): This is the global service version counter'
nl|'\n'
DECL|variable|SERVICE_VERSION
name|'SERVICE_VERSION'
op|'='
number|'2'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(danms): This is our SERVICE_VERSION history. The idea is that any'
nl|'\n'
comment|'# time we bump the version, we will put an entry here to record the change,'
nl|'\n'
comment|'# along with any pertinent data. For things that we can programatically'
nl|'\n'
comment|'# detect that need a bump, we put something in _collect_things() below to'
nl|'\n'
comment|'# assemble a dict of things we can check. For example, we pretty much always'
nl|'\n'
comment|'# want to consider the compute RPC API version a thing that requires a service'
nl|'\n'
comment|'# bump so that we can drive version pins from it. We could include other'
nl|'\n'
comment|'# service RPC versions at some point, minimum object versions, etc.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The TestServiceVersion test will fail if the calculated set of'
nl|'\n'
comment|'# things differs from the value in the last item of the list below,'
nl|'\n'
comment|'# indicating that a version bump is needed.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Also note that there are other reasons we may want to bump this,'
nl|'\n'
comment|'# which will not be caught by the test. An example of this would be'
nl|'\n'
comment|'# triggering (or disabling) an online data migration once all services'
nl|'\n'
comment|'# in the cluster are at the same level.'
nl|'\n'
DECL|variable|SERVICE_VERSION_HISTORY
name|'SERVICE_VERSION_HISTORY'
op|'='
op|'('
nl|'\n'
comment|'# Version 0: Pre-history'
nl|'\n'
op|'{'
string|"'compute_rpc'"
op|':'
string|"'4.0'"
op|'}'
op|','
nl|'\n'
nl|'\n'
comment|'# Version 1: Introduction of SERVICE_VERSION'
nl|'\n'
op|'{'
string|"'compute_rpc'"
op|':'
string|"'4.4'"
op|'}'
op|','
nl|'\n'
comment|'# Version 2: Changes to rebuild_instance signature in the compute_rpc'
nl|'\n'
op|'{'
string|"'compute_rpc'"
op|':'
string|"'4.5'"
op|'}'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'Service'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|Service
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added compute_node nested object'
nl|'\n'
comment|'# Version 1.2: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.3: ComputeNode version 1.5'
nl|'\n'
comment|'# Version 1.4: Added use_slave to get_by_compute_host'
nl|'\n'
comment|'# Version 1.5: ComputeNode version 1.6'
nl|'\n'
comment|'# Version 1.6: ComputeNode version 1.7'
nl|'\n'
comment|'# Version 1.7: ComputeNode version 1.8'
nl|'\n'
comment|'# Version 1.8: ComputeNode version 1.9'
nl|'\n'
comment|'# Version 1.9: ComputeNode version 1.10'
nl|'\n'
comment|'# Version 1.10: Changes behaviour of loading compute_node'
nl|'\n'
comment|'# Version 1.11: Added get_by_host_and_binary'
nl|'\n'
comment|'# Version 1.12: ComputeNode version 1.11'
nl|'\n'
comment|'# Version 1.13: Added last_seen_up'
nl|'\n'
comment|'# Version 1.14: Added forced_down'
nl|'\n'
comment|'# Version 1.15: ComputeNode version 1.12'
nl|'\n'
comment|'# Version 1.16: Added version'
nl|'\n'
comment|'# Version 1.17: ComputeNode version 1.13'
nl|'\n'
comment|'# Version 1.18: ComputeNode version 1.14'
nl|'\n'
comment|'# Version 1.19: Added get_minimum_version()'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.19'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'report_count'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'compute_node'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'ComputeNode'"
op|')'
op|','
nl|'\n'
string|"'last_seen_up'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'forced_down'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'compute_node'"
op|':'
op|'['
op|'('
string|"'1.1'"
op|','
string|"'1.4'"
op|')'
op|','
op|'('
string|"'1.3'"
op|','
string|"'1.5'"
op|')'
op|','
op|'('
string|"'1.5'"
op|','
string|"'1.6'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.7'"
op|','
string|"'1.8'"
op|')'
op|','
op|'('
string|"'1.8'"
op|','
string|"'1.9'"
op|')'
op|','
op|'('
string|"'1.9'"
op|','
string|"'1.10'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.12'"
op|','
string|"'1.11'"
op|')'
op|','
op|'('
string|"'1.15'"
op|','
string|"'1.12'"
op|')'
op|','
op|'('
string|"'1.17'"
op|','
string|"'1.13'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.18'"
op|','
string|"'1.14'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(danms): We're going against the rules here and overriding"
nl|'\n'
comment|"# init. The reason is that we want to *ensure* that we're always"
nl|'\n'
comment|'# setting the current service version on our objects, overriding'
nl|'\n'
comment|'# whatever else might be set in the database, or otherwise (which'
nl|'\n'
comment|'# is the normal reason not to override init).'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# We also need to do this here so that it's set on the client side"
nl|'\n'
comment|'# all the time, such that create() and save() operations will'
nl|'\n'
comment|'# include the current service version.'
nl|'\n'
indent|'        '
name|'if'
string|"'version'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'init'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'Version field is immutable'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'Service'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'version'
op|'='
name|'SERVICE_VERSION'
newline|'\n'
nl|'\n'
DECL|member|obj_make_compatible
dedent|''
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Service'
op|','
name|'self'
op|')'
op|'.'
name|'obj_make_compatible'
op|'('
name|'primitive'
op|','
name|'target_version'
op|')'
newline|'\n'
name|'_target_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'_target_version'
op|'<'
op|'('
number|'1'
op|','
number|'16'
op|')'
name|'and'
string|"'version'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'version'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'_target_version'
op|'<'
op|'('
number|'1'
op|','
number|'14'
op|')'
name|'and'
string|"'forced_down'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'forced_down'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'_target_version'
op|'<'
op|'('
number|'1'
op|','
number|'13'
op|')'
name|'and'
string|"'last_seen_up'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'last_seen_up'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'_target_version'
op|'<'
op|'('
number|'1'
op|','
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'target_compute_version'
op|'='
name|'self'
op|'.'
name|'obj_calculate_child_version'
op|'('
nl|'\n'
name|'target_version'
op|','
string|"'compute_node'"
op|')'
newline|'\n'
comment|'# service.compute_node was not lazy-loaded, we need to provide it'
nl|'\n'
comment|'# when called'
nl|'\n'
name|'self'
op|'.'
name|'_do_compute_node'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'primitive'
op|','
nl|'\n'
name|'target_compute_version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_compute_node
dedent|''
dedent|''
name|'def'
name|'_do_compute_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): Some drivers (VMware, Ironic) can have multiple'
nl|'\n'
comment|'# nodes for the same service, but for keeping same behaviour,'
nl|'\n'
comment|'# returning only the first elem of the list'
nl|'\n'
indent|'            '
name|'compute'
op|'='
name|'objects'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_all_by_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'primitive'
op|'['
string|"'host'"
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'primitive'
op|'['
string|"'compute_node'"
op|']'
op|'='
name|'compute'
op|'.'
name|'obj_to_primitive'
op|'('
nl|'\n'
name|'target_version'
op|'='
name|'target_version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'db_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'allow_missing'
op|'='
op|'('
string|"'availability_zone'"
op|','
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'service'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'allow_missing'
name|'and'
name|'key'
name|'not'
name|'in'
name|'db_service'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'key'
op|'=='
string|"'compute_node'"
op|':'
newline|'\n'
comment|'#  NOTE(sbauza); We want to only lazy-load compute_node'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'key'
op|'=='
string|"'version'"
op|':'
newline|'\n'
comment|'# NOTE(danms): Special handling of the version field, since'
nl|'\n'
comment|'# it is read_only and set in our init.'
nl|'\n'
indent|'                '
name|'setattr'
op|'('
name|'service'
op|','
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'key'
op|')'
op|','
name|'db_service'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'['
name|'key'
op|']'
op|'='
name|'db_service'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'service'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'service'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'service'
newline|'\n'
nl|'\n'
DECL|member|obj_load_attr
dedent|''
name|'def'
name|'obj_load_attr'
op|'('
name|'self'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_context'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'OrphanedObjectError'
op|'('
name|'method'
op|'='
string|"'obj_load_attr'"
op|','
nl|'\n'
name|'objtype'
op|'='
name|'self'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Lazy-loading `%(attr)s\' on %(name)s id %(id)s"'
op|','
nl|'\n'
op|'{'
string|"'attr'"
op|':'
name|'attrname'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'obj_name'
op|'('
op|')'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'attrname'
op|'!='
string|"'compute_node'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'obj_load_attr'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'attribute %s not lazy-loadable'"
op|'%'
name|'attrname'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'binary'
op|'=='
string|"'nova-compute'"
op|':'
newline|'\n'
comment|'# Only n-cpu services have attached compute_node(s)'
nl|'\n'
indent|'            '
name|'compute_nodes'
op|'='
name|'objects'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_all_by_host'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(sbauza); Previous behaviour was raising a ServiceNotFound,'
nl|'\n'
comment|'# we keep it for backwards compatibility'
nl|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ServiceNotFound'
op|'('
name|'service_id'
op|'='
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
comment|'# NOTE(sbauza): Some drivers (VMware, Ironic) can have multiple nodes'
nl|'\n'
comment|'# for the same service, but for keeping same behaviour, returning only'
nl|'\n'
comment|'# the first elem of the list'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_node'
op|'='
name|'compute_nodes'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host_and_topic
name|'def'
name|'get_by_host_and_topic'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_host_and_topic'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host_and_binary
name|'def'
name|'get_by_host_and_binary'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_host_and_binary'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'HostBinaryNotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_compute_host
name|'def'
name|'get_by_compute_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(ndipanov): This is deprecated and should be removed on the next'
nl|'\n'
comment|'# major version bump'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_args
name|'def'
name|'get_by_args'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_host_and_binary'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_minimum_version
dedent|''
name|'def'
name|'_check_minimum_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Enforce that we are not older that the minimum version.\n\n        This is a loose check to avoid creating or updating our service\n        record if we would do so with a version that is older that the current\n        minimum of all services. This could happen if we were started with\n        older code by accident, either due to a rollback or an old and\n        un-updated node suddenly coming back onto the network.\n\n        There is technically a race here between the check and the update,\n        but since the minimum version should always roll forward and never\n        backwards, we don\'t need to worry about doing it atomically. Further,\n        the consequence for getting this wrong is minor, in that we\'ll just\n        fail to send messages that other services understand.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'version'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'binary'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'minver'
op|'='
name|'self'
op|'.'
name|'get_minimum_version'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'binary'
op|')'
newline|'\n'
name|'if'
name|'minver'
op|'>'
name|'self'
op|'.'
name|'version'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ServiceTooOld'
op|'('
name|'thisver'
op|'='
name|'self'
op|'.'
name|'version'
op|','
nl|'\n'
name|'minver'
op|'='
name|'minver'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_check_minimum_version'
op|'('
op|')'
newline|'\n'
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'list'
op|'('
name|'updates'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'=='
op|'['
string|"'version'"
op|']'
op|':'
newline|'\n'
comment|"# NOTE(danms): Since we set/dirty version in init, don't"
nl|'\n'
comment|"# do a save if that's all that has changed. This keeps the"
nl|'\n'
comment|'# "save is a no-op if nothing has changed" behavior.'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_check_minimum_version'
op|'('
op|')'
newline|'\n'
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_minimum_version
name|'def'
name|'get_minimum_version'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'binary'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'binary'
op|'.'
name|'startswith'
op|'('
string|"'nova-'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'get_minimum_version called with likely-incorrect '"
nl|'\n'
string|"'binary `%s\\''"
op|')'
op|','
name|'binary'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'get_minimum_version'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'Invalid binary prefix'"
op|')'
newline|'\n'
dedent|''
name|'version'
op|'='
name|'db'
op|'.'
name|'service_get_minimum_version'
op|'('
name|'context'
op|','
name|'binary'
op|','
nl|'\n'
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'if'
name|'version'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
comment|'# NOTE(danms): Since our return value is not controlled by object'
nl|'\n'
comment|'# schema, be explicit here.'
nl|'\n'
dedent|''
name|'return'
name|'int'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|ServiceList
name|'class'
name|'ServiceList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'#              Service <= version 1.2'
nl|'\n'
comment|'# Version 1.1  Service version 1.3'
nl|'\n'
comment|'# Version 1.2: Service version 1.4'
nl|'\n'
comment|'# Version 1.3: Service version 1.5'
nl|'\n'
comment|'# Version 1.4: Service version 1.6'
nl|'\n'
comment|'# Version 1.5: Service version 1.7'
nl|'\n'
comment|'# Version 1.6: Service version 1.8'
nl|'\n'
comment|'# Version 1.7: Service version 1.9'
nl|'\n'
comment|'# Version 1.8: Service version 1.10'
nl|'\n'
comment|'# Version 1.9: Added get_by_binary() and Service version 1.11'
nl|'\n'
comment|'# Version 1.10: Service version 1.12'
nl|'\n'
comment|'# Version 1.11: Service version 1.13'
nl|'\n'
comment|'# Version 1.12: Service version 1.14'
nl|'\n'
comment|'# Version 1.13: Service version 1.15'
nl|'\n'
comment|'# Version 1.14: Service version 1.16'
nl|'\n'
comment|'# Version 1.15: Service version 1.17'
nl|'\n'
comment|'# Version 1.16: Service version 1.18'
nl|'\n'
comment|'# Version 1.17: Service version 1.19'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.17'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'Service'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
comment|'# NOTE(danms): Service was at 1.2 before we added this'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.2'"
op|')'
op|','
op|'('
string|"'1.1'"
op|','
string|"'1.3'"
op|')'
op|','
op|'('
string|"'1.2'"
op|','
string|"'1.4'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.3'"
op|','
string|"'1.5'"
op|')'
op|','
op|'('
string|"'1.4'"
op|','
string|"'1.6'"
op|')'
op|','
op|'('
string|"'1.5'"
op|','
string|"'1.7'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.6'"
op|','
string|"'1.8'"
op|')'
op|','
op|'('
string|"'1.7'"
op|','
string|"'1.9'"
op|')'
op|','
op|'('
string|"'1.8'"
op|','
string|"'1.10'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.9'"
op|','
string|"'1.11'"
op|')'
op|','
op|'('
string|"'1.10'"
op|','
string|"'1.12'"
op|')'
op|','
op|'('
string|"'1.11'"
op|','
string|"'1.13'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.12'"
op|','
string|"'1.14'"
op|')'
op|','
op|'('
string|"'1.13'"
op|','
string|"'1.15'"
op|')'
op|','
op|'('
string|"'1.14'"
op|','
string|"'1.16'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.15'"
op|','
string|"'1.17'"
op|')'
op|','
op|'('
string|"'1.16'"
op|','
string|"'1.18'"
op|')'
op|','
op|'('
string|"'1.17'"
op|','
string|"'1.19'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_topic
name|'def'
name|'get_by_topic'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
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
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Service'
op|','
nl|'\n'
name|'db_services'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_binary
name|'def'
name|'get_by_binary'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_binary'
op|'('
name|'context'
op|','
name|'binary'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Service'
op|','
nl|'\n'
name|'db_services'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host
name|'def'
name|'get_by_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Service'
op|','
nl|'\n'
name|'db_services'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'disabled'
op|'='
name|'None'
op|','
name|'set_zones'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'disabled'
op|')'
newline|'\n'
name|'if'
name|'set_zones'
op|':'
newline|'\n'
indent|'            '
name|'db_services'
op|'='
name|'availability_zones'
op|'.'
name|'set_availability_zones'
op|'('
nl|'\n'
name|'context'
op|','
name|'db_services'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Service'
op|','
nl|'\n'
name|'db_services'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
