begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""Generic Node base class for all workers that run on hosts."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
name|'import'
name|'messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'baserpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'debugger'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
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
DECL|variable|service_opts
name|'service_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'report_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds between nodes reporting state to datastore'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'periodic_enable'"
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
string|"'Enable periodic tasks'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'periodic_fuzzy_delay'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Range of seconds to randomly delay when starting the'"
nl|'\n'
string|"' periodic task scheduler to reduce stampeding.'"
nl|'\n'
string|"' (Disable by setting to 0)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'enabled_apis'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'ec2'"
op|','
string|"'osapi_compute'"
op|','
string|"'metadata'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of APIs to enable by default'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'enabled_ssl_apis'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of APIs with enabled SSL'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ec2_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The IP address on which the EC2 API will listen.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ec2_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8773'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The port on which the EC2 API will listen.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ec2_workers'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of workers for EC2 API service. The default will '"
nl|'\n'
string|"'be equal to the number of CPUs available.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_compute_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The IP address on which the OpenStack API will listen.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'osapi_compute_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8774'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The port on which the OpenStack API will listen.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'osapi_compute_workers'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of workers for OpenStack API service. The default '"
nl|'\n'
string|"'will be the number of CPUs available.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'metadata_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.api.manager.MetadataManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'OpenStack metadata service manager'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'metadata_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The IP address on which the metadata API will listen.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'metadata_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8775'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The port on which the metadata API will listen.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'metadata_workers'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of workers for metadata service. The default will '"
nl|'\n'
string|"'be the number of CPUs available.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.compute.manager.ComputeManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Full class name for the Manager for compute'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.console.manager.ConsoleProxyManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Full class name for the Manager for console proxy'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'consoleauth_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.consoleauth.manager.ConsoleAuthManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Manager for console auth'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cert_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cert.manager.CertManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Full class name for the Manager for cert'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.manager.VlanManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Full class name for the Manager for network'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.manager.SchedulerManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Full class name for the Manager for scheduler'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'service_down_time'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum time since last check-in for up service'"
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
name|'service_opts'
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
DECL|class|Service
name|'class'
name|'Service'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Service object for binaries running on hosts.\n\n    A service takes a manager and enables rpc by listening to queues based\n    on topic. It also periodically runs tasks on the manager and reports\n    it state to the database services table.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'binary'
op|','
name|'topic'
op|','
name|'manager'
op|','
name|'report_interval'
op|'='
name|'None'
op|','
nl|'\n'
name|'periodic_enable'
op|'='
name|'None'
op|','
name|'periodic_fuzzy_delay'
op|'='
name|'None'
op|','
nl|'\n'
name|'periodic_interval_max'
op|'='
name|'None'
op|','
name|'db_allowed'
op|'='
name|'True'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'binary'
op|'='
name|'binary'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'manager_class_name'
op|'='
name|'manager'
newline|'\n'
comment|'# NOTE(russellb) We want to make sure to create the servicegroup API'
nl|'\n'
comment|'# instance early, before creating other things such as the manager,'
nl|'\n'
comment|'# that will also create a servicegroup API instance.  Internally, the'
nl|'\n'
comment|'# servicegroup only allocates a single instance of the driver API and'
nl|'\n'
comment|'# we want to make sure that our value of db_allowed is there when it'
nl|'\n'
comment|'# gets created.  For that to happen, this has to be the first instance'
nl|'\n'
comment|'# of the servicegroup API.'
nl|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
name|'db_allowed'
op|'='
name|'db_allowed'
op|')'
newline|'\n'
name|'manager_class'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'self'
op|'.'
name|'manager_class_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager_class'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rpcserver'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'report_interval'
op|'='
name|'report_interval'
newline|'\n'
name|'self'
op|'.'
name|'periodic_enable'
op|'='
name|'periodic_enable'
newline|'\n'
name|'self'
op|'.'
name|'periodic_fuzzy_delay'
op|'='
name|'periodic_fuzzy_delay'
newline|'\n'
name|'self'
op|'.'
name|'periodic_interval_max'
op|'='
name|'periodic_interval_max'
newline|'\n'
name|'self'
op|'.'
name|'saved_args'
op|','
name|'self'
op|'.'
name|'saved_kwargs'
op|'='
name|'args'
op|','
name|'kwargs'
newline|'\n'
name|'self'
op|'.'
name|'backdoor_port'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'conductor_api'
op|'='
name|'conductor'
op|'.'
name|'API'
op|'('
name|'use_local'
op|'='
name|'db_allowed'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'wait_until_ready'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'verstr'
op|'='
name|'version'
op|'.'
name|'version_string_with_package'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Starting %(topic)s node (version %(version)s)'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'topic'"
op|':'
name|'self'
op|'.'
name|'topic'
op|','
string|"'version'"
op|':'
name|'verstr'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'basic_config_check'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'model_disconnected'
op|'='
name|'False'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'service_ref'
op|'='
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_get_by_args'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'binary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service_id'
op|'='
name|'self'
op|'.'
name|'service_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'service_ref'
op|'='
name|'self'
op|'.'
name|'_create_service_ref'
op|'('
name|'ctxt'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'ServiceTopicExists'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'ServiceBinaryExists'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): If we race to create a record with a sibling'
nl|'\n'
comment|"# worker, don't fail here."
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'service_ref'
op|'='
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_get_by_args'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'binary'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'manager'
op|'.'
name|'pre_start_hook'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'backdoor_port'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'backdoor_port'
op|'='
name|'self'
op|'.'
name|'backdoor_port'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating RPC server for service %s"'
op|','
name|'self'
op|'.'
name|'topic'
op|')'
newline|'\n'
nl|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'self'
op|'.'
name|'topic'
op|','
name|'server'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'endpoints'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|','
nl|'\n'
name|'baserpc'
op|'.'
name|'BaseRPCAPI'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'service_name'
op|','
name|'self'
op|'.'
name|'backdoor_port'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'endpoints'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'additional_endpoints'
op|')'
newline|'\n'
nl|'\n'
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'rpcserver'
op|'='
name|'rpc'
op|'.'
name|'get_server'
op|'('
name|'target'
op|','
name|'endpoints'
op|','
name|'serializer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rpcserver'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'post_start_hook'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Join ServiceGroup membership for this service %s"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|')'
newline|'\n'
comment|'# Add service to the ServiceGroup membership group.'
nl|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'self'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'periodic_enable'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'periodic_fuzzy_delay'
op|':'
newline|'\n'
indent|'                '
name|'initial_delay'
op|'='
name|'random'
op|'.'
name|'randint'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'periodic_fuzzy_delay'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'initial_delay'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'tg'
op|'.'
name|'add_dynamic_timer'
op|'('
name|'self'
op|'.'
name|'periodic_tasks'
op|','
nl|'\n'
name|'initial_delay'
op|'='
name|'initial_delay'
op|','
nl|'\n'
name|'periodic_interval_max'
op|'='
nl|'\n'
name|'self'
op|'.'
name|'periodic_interval_max'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_service_ref
dedent|''
dedent|''
name|'def'
name|'_create_service_ref'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'svc_values'
op|'='
op|'{'
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
nl|'\n'
op|'}'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
name|'svc_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service_id'
op|'='
name|'service'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'return'
name|'service'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'get'
op|'('
string|"'manager'"
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'manager'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'binary'
op|'='
name|'None'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'manager'
op|'='
name|'None'
op|','
nl|'\n'
name|'report_interval'
op|'='
name|'None'
op|','
name|'periodic_enable'
op|'='
name|'None'
op|','
nl|'\n'
name|'periodic_fuzzy_delay'
op|'='
name|'None'
op|','
name|'periodic_interval_max'
op|'='
name|'None'
op|','
nl|'\n'
name|'db_allowed'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Instantiates class and passes back application object.\n\n        :param host: defaults to CONF.host\n        :param binary: defaults to basename of executable\n        :param topic: defaults to bin_name - \'nova-\' part\n        :param manager: defaults to CONF.<topic>_manager\n        :param report_interval: defaults to CONF.report_interval\n        :param periodic_enable: defaults to CONF.periodic_enable\n        :param periodic_fuzzy_delay: defaults to CONF.periodic_fuzzy_delay\n        :param periodic_interval_max: if set, the max time to wait between runs\n\n        """'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'CONF'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'binary'
op|':'
newline|'\n'
indent|'            '
name|'binary'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'topic'
op|':'
newline|'\n'
indent|'            '
name|'topic'
op|'='
name|'binary'
op|'.'
name|'rpartition'
op|'('
string|"'nova-'"
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'manager_cls'
op|'='
op|'('
string|"'%s_manager'"
op|'%'
nl|'\n'
name|'binary'
op|'.'
name|'rpartition'
op|'('
string|"'nova-'"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'get'
op|'('
name|'manager_cls'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'report_interval'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'report_interval'
op|'='
name|'CONF'
op|'.'
name|'report_interval'
newline|'\n'
dedent|''
name|'if'
name|'periodic_enable'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'periodic_enable'
op|'='
name|'CONF'
op|'.'
name|'periodic_enable'
newline|'\n'
dedent|''
name|'if'
name|'periodic_fuzzy_delay'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'periodic_fuzzy_delay'
op|'='
name|'CONF'
op|'.'
name|'periodic_fuzzy_delay'
newline|'\n'
nl|'\n'
dedent|''
name|'debugger'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'service_obj'
op|'='
name|'cls'
op|'('
name|'host'
op|','
name|'binary'
op|','
name|'topic'
op|','
name|'manager'
op|','
nl|'\n'
name|'report_interval'
op|'='
name|'report_interval'
op|','
nl|'\n'
name|'periodic_enable'
op|'='
name|'periodic_enable'
op|','
nl|'\n'
name|'periodic_fuzzy_delay'
op|'='
name|'periodic_fuzzy_delay'
op|','
nl|'\n'
name|'periodic_interval_max'
op|'='
name|'periodic_interval_max'
op|','
nl|'\n'
name|'db_allowed'
op|'='
name|'db_allowed'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'service_obj'
newline|'\n'
nl|'\n'
DECL|member|kill
dedent|''
name|'def'
name|'kill'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy the service object in the datastore."""'
newline|'\n'
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Service killed that has no database entry'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'rpcserver'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rpcserver'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'cleanup_host'
op|'('
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
name|'_'
op|'('
string|"'Service error occurred during cleanup_host'"
op|')'
op|')'
newline|'\n'
name|'pass'
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
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|periodic_tasks
dedent|''
name|'def'
name|'periodic_tasks'
op|'('
name|'self'
op|','
name|'raise_on_error'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'periodic_tasks'
op|'('
name|'ctxt'
op|','
name|'raise_on_error'
op|'='
name|'raise_on_error'
op|')'
newline|'\n'
nl|'\n'
DECL|member|basic_config_check
dedent|''
name|'def'
name|'basic_config_check'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform basic config checks before starting processing."""'
newline|'\n'
comment|'# Make sure the tempdir exists and is writable'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Temporary directory is invalid: %s'"
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WSGIService
dedent|''
dedent|''
dedent|''
name|'class'
name|'WSGIService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provides ability to launch API from a \'paste\' configuration."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'loader'
op|'='
name|'None'
op|','
name|'use_ssl'
op|'='
name|'False'
op|','
name|'max_url_len'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize, but do not start the WSGI server.\n\n        :param name: The name of the WSGI server given to the loader.\n        :param loader: Loads the WSGI application using the given name.\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'self'
op|'.'
name|'_get_manager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loader'
op|'='
name|'loader'
name|'or'
name|'wsgi'
op|'.'
name|'Loader'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'self'
op|'.'
name|'loader'
op|'.'
name|'load_app'
op|'('
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'getattr'
op|'('
name|'CONF'
op|','
string|"'%s_listen'"
op|'%'
name|'name'
op|','
string|'"0.0.0.0"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'getattr'
op|'('
name|'CONF'
op|','
string|"'%s_listen_port'"
op|'%'
name|'name'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'workers'
op|'='
op|'('
name|'getattr'
op|'('
name|'CONF'
op|','
string|"'%s_workers'"
op|'%'
name|'name'
op|','
name|'None'
op|')'
name|'or'
nl|'\n'
name|'processutils'
op|'.'
name|'get_worker_count'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'workers'
name|'and'
name|'self'
op|'.'
name|'workers'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'worker_name'
op|'='
string|"'%s_workers'"
op|'%'
name|'name'
newline|'\n'
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"%(worker_name)s value of %(workers)s is invalid, "'
nl|'\n'
string|'"must be greater than 0"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'worker_name'"
op|':'
name|'worker_name'
op|','
nl|'\n'
string|"'workers'"
op|':'
name|'str'
op|'('
name|'self'
op|'.'
name|'workers'
op|')'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'use_ssl'
op|'='
name|'use_ssl'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'='
name|'wsgi'
op|'.'
name|'Server'
op|'('
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'app'
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'port'
op|','
nl|'\n'
name|'use_ssl'
op|'='
name|'self'
op|'.'
name|'use_ssl'
op|','
nl|'\n'
name|'max_url_len'
op|'='
name|'max_url_len'
op|')'
newline|'\n'
comment|'# Pull back actual port used'
nl|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'self'
op|'.'
name|'server'
op|'.'
name|'port'
newline|'\n'
name|'self'
op|'.'
name|'backdoor_port'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_manager
dedent|''
name|'def'
name|'_get_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize a Manager object appropriate for this service.\n\n        Use the service name to look up a Manager subclass from the\n        configuration and initialize an instance. If no class name\n        is configured, just return None.\n\n        :returns: a Manager instance, or None.\n\n        """'
newline|'\n'
name|'fl'
op|'='
string|"'%s_manager'"
op|'%'
name|'self'
op|'.'
name|'name'
newline|'\n'
name|'if'
name|'fl'
name|'not'
name|'in'
name|'CONF'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'manager_class_name'
op|'='
name|'CONF'
op|'.'
name|'get'
op|'('
name|'fl'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'manager_class_name'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'manager_class'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'manager_class_name'
op|')'
newline|'\n'
name|'return'
name|'manager_class'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start serving this service using loaded configuration.\n\n        Also, retrieve updated port number in case \'0\' was passed in, which\n        indicates a random port should be used.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'pre_start_hook'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'backdoor_port'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'backdoor_port'
op|'='
name|'self'
op|'.'
name|'backdoor_port'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'post_start_hook'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop serving this API.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for the service to stop serving this API.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|process_launcher
dedent|''
dedent|''
name|'def'
name|'process_launcher'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'service'
op|'.'
name|'ProcessLauncher'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(vish): the global launcher is to maintain the existing'
nl|'\n'
comment|'#             functionality of calling service.serve +'
nl|'\n'
comment|'#             service.wait'
nl|'\n'
DECL|variable|_launcher
dedent|''
name|'_launcher'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve
name|'def'
name|'serve'
op|'('
name|'server'
op|','
name|'workers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_launcher'
newline|'\n'
name|'if'
name|'_launcher'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'serve() can only be called once'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_launcher'
op|'='
name|'service'
op|'.'
name|'launch'
op|'('
name|'server'
op|','
name|'workers'
op|'='
name|'workers'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wait
dedent|''
name|'def'
name|'wait'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_launcher'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
