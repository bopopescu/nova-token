begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
name|'calendar'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'services'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'availability_zones'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'drivers'
name|'import'
name|'db'
name|'as'
name|'db_driver'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_services_list
name|'fake_services_list'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'test_service'
op|'.'
name|'fake_service'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|"'nova-scheduler'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host1'"
op|','
nl|'\n'
DECL|variable|id
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|"'scheduler'"
op|','
nl|'\n'
DECL|variable|updated_at
name|'updated_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
DECL|variable|created_at
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'2'
op|','
number|'46'
op|','
number|'27'
op|')'
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
string|"'test1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'test_service'
op|'.'
name|'fake_service'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|"'nova-compute'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host1'"
op|','
nl|'\n'
DECL|variable|id
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
DECL|variable|updated_at
name|'updated_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|','
nl|'\n'
DECL|variable|created_at
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'2'
op|','
number|'46'
op|','
number|'27'
op|')'
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
string|"'test2'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'test_service'
op|'.'
name|'fake_service'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|"'nova-scheduler'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host2'"
op|','
nl|'\n'
DECL|variable|id
name|'id'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|"'scheduler'"
op|','
nl|'\n'
DECL|variable|updated_at
name|'updated_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'19'
op|','
number|'6'
op|','
number|'55'
op|','
number|'34'
op|')'
op|','
nl|'\n'
DECL|variable|created_at
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'2'
op|','
number|'46'
op|','
number|'28'
op|')'
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
string|"''"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'test_service'
op|'.'
name|'fake_service'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|"'nova-compute'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host2'"
op|','
nl|'\n'
DECL|variable|id
name|'id'
op|'='
number|'4'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
DECL|variable|updated_at
name|'updated_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'8'
op|','
number|'3'
op|','
number|'38'
op|')'
op|','
nl|'\n'
DECL|variable|created_at
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'2'
op|','
number|'46'
op|','
number|'28'
op|')'
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
string|"'test4'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'        '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestWithService
dedent|''
name|'class'
name|'FakeRequestWithService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'        '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
string|'"binary"'
op|':'
string|'"nova-compute"'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestWithHost
dedent|''
name|'class'
name|'FakeRequestWithHost'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'        '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestWithHostService
dedent|''
name|'class'
name|'FakeRequestWithHostService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'        '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|','
string|'"binary"'
op|':'
string|'"nova-compute"'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_host_api_service_get_all
dedent|''
name|'def'
name|'fake_host_api_service_get_all'
op|'('
name|'context'
op|','
name|'filters'
op|'='
name|'None'
op|','
name|'set_zones'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'set_zones'
name|'or'
string|"'availability_zone'"
name|'in'
name|'filters'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'availability_zones'
op|'.'
name|'set_availability_zones'
op|'('
name|'context'
op|','
nl|'\n'
name|'fake_services_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_db_api_service_get_all
dedent|''
dedent|''
name|'def'
name|'fake_db_api_service_get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'fake_services_list'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_get_by_host_binary
dedent|''
name|'def'
name|'fake_service_get_by_host_binary'
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
name|'for'
name|'service'
name|'in'
name|'fake_services_list'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'service'
op|'['
string|"'host'"
op|']'
op|'=='
name|'host'
name|'and'
name|'service'
op|'['
string|"'binary'"
op|']'
op|'=='
name|'binary'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'service'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_get_by_id
dedent|''
name|'def'
name|'fake_service_get_by_id'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'service'
name|'in'
name|'fake_services_list'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'service'
op|'['
string|"'id'"
op|']'
op|'=='
name|'value'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'service'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_update
dedent|''
name|'def'
name|'fake_service_update'
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
name|'service'
op|'='
name|'fake_service_get_by_id'
op|'('
name|'service_id'
op|')'
newline|'\n'
name|'if'
name|'service'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ServiceNotFound'
op|'('
name|'service_id'
op|'='
name|'service_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_utcnow
dedent|''
name|'def'
name|'fake_utcnow'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'11'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_utcnow_ts
dedent|''
name|'def'
name|'fake_utcnow_ts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'d'
op|'='
name|'fake_utcnow'
op|'('
op|')'
newline|'\n'
name|'return'
name|'calendar'
op|'.'
name|'timegm'
op|'('
name|'d'
op|'.'
name|'utctimetuple'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServicesTest
dedent|''
name|'class'
name|'ServicesTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ServicesTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'extensions'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|'"service_get_all"'
op|','
nl|'\n'
name|'fake_host_api_service_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'timeutils'
op|','
string|'"utcnow"'
op|','
name|'fake_utcnow'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'timeutils'
op|','
string|'"utcnow_ts"'
op|','
name|'fake_utcnow_ts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"service_get_by_args"'
op|','
nl|'\n'
name|'fake_service_get_by_host_binary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"service_update"'
op|','
name|'fake_service_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_list
dedent|''
name|'def'
name|'test_services_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'enabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'down'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'19'
op|','
number|'6'
op|','
number|'55'
op|','
number|'34'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'down'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'8'
op|','
number|'3'
op|','
number|'38'
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_list_with_host
dedent|''
name|'def'
name|'test_services_list_with_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequestWithHost'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_list_with_service
dedent|''
name|'def'
name|'test_services_list_with_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequestWithService'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'down'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'8'
op|','
number|'3'
op|','
number|'38'
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_list_with_host_service
dedent|''
name|'def'
name|'test_services_list_with_host_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequestWithHostService'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_detail
dedent|''
name|'def'
name|'test_services_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'['
string|"'os-extended-services'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|'"service_get_all"'
op|','
nl|'\n'
name|'fake_host_api_service_get_all'
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test1'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'enabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'down'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'19'
op|','
number|'6'
op|','
number|'55'
op|','
number|'34'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"''"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'down'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'8'
op|','
number|'3'
op|','
number|'38'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test4'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_detail_with_host
dedent|''
name|'def'
name|'test_service_detail_with_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'['
string|"'os-extended-services'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|'"service_get_all"'
op|','
nl|'\n'
name|'fake_host_api_service_get_all'
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequestWithHost'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test1'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_detail_with_service
dedent|''
name|'def'
name|'test_service_detail_with_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'['
string|"'os-extended-services'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|'"service_get_all"'
op|','
nl|'\n'
name|'fake_host_api_service_get_all'
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequestWithService'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'down'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'9'
op|','
number|'18'
op|','
number|'8'
op|','
number|'3'
op|','
number|'38'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test4'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_detail_with_host_service
dedent|''
name|'def'
name|'test_service_detail_with_host_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'['
string|"'os-extended-services'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|'"service_get_all"'
op|','
nl|'\n'
name|'fake_host_api_service_get_all'
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequestWithHostService'
op|'('
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'services'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'5'
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_enable
dedent|''
name|'def'
name|'test_services_enable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_service_update
indent|'        '
name|'def'
name|'_service_update'
op|'('
name|'context'
op|','
name|'service_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'values'
op|'['
string|"'disabled_reason'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'test_service'
op|'.'
name|'fake_service'
op|','
op|'**'
name|'values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"service_update"'
op|','
name|'_service_update'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
string|"'binary'"
op|':'
string|"'nova-compute'"
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-services/enable'"
op|')'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|'"enable"'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'service'"
op|']'
op|'['
string|"'status'"
op|']'
op|','
string|"'enabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'disabled_reason'"
op|','
name|'res_dict'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# This test is just to verify that the servicegroup API gets used when'
nl|'\n'
comment|'# calling this API.'
nl|'\n'
DECL|member|test_services_with_exception
dedent|''
name|'def'
name|'test_services_with_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|dummy_is_up
indent|'        '
name|'def'
name|'dummy_is_up'
op|'('
name|'self'
op|','
name|'dummy'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'KeyError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db_driver'
op|'.'
name|'DbDriver'
op|','
string|"'is_up'"
op|','
name|'dummy_is_up'
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequestWithHostService'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyError'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_disable
dedent|''
name|'def'
name|'test_services_disable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-services/disable'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
string|"'binary'"
op|':'
string|"'nova-compute'"
op|'}'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|'"disable"'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'service'"
op|']'
op|'['
string|"'status'"
op|']'
op|','
string|"'disabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'disabled_reason'"
op|','
name|'res_dict'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_disable_log_reason
dedent|''
name|'def'
name|'test_services_disable_log_reason'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'['
string|"'os-extended-services'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'v2/fakes/os-services/disable-log-reason'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test-reason'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|'"disable-log-reason"'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'service'"
op|']'
op|'['
string|"'status'"
op|']'
op|','
string|"'disabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'service'"
op|']'
op|'['
string|"'disabled_reason'"
op|']'
op|','
string|"'test-reason'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mandatory_reason_field
dedent|''
name|'def'
name|'test_mandatory_reason_field'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'['
string|"'os-extended-services'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'services'
op|'.'
name|'ServiceController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'v2/fakes/os-services/disable-log-reason'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
string|'"disable-log-reason"'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_reason_field
dedent|''
name|'def'
name|'test_invalid_reason_field'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reason'
op|'='
string|"' '"
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_is_valid_as_reason'
op|'('
name|'reason'
op|')'
op|')'
newline|'\n'
name|'reason'
op|'='
string|"'a'"
op|'*'
number|'256'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_is_valid_as_reason'
op|'('
name|'reason'
op|')'
op|')'
newline|'\n'
name|'reason'
op|'='
string|"'it\\'s a valid reason.'"
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_is_valid_as_reason'
op|'('
name|'reason'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
