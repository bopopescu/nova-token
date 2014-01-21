begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright 2013 Canonical Corp.'
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
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
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
name|'uuidutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'unit'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_session
name|'class'
name|'fake_session'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ret'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ret'
op|'='
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|_call_method
dedent|''
name|'def'
name|'_call_method'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|partialObject
dedent|''
dedent|''
name|'class'
name|'partialObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|'='
string|"'fake-path'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'path'
op|'='
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'fault'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareVMUtilTestCase
dedent|''
dedent|''
name|'class'
name|'VMwareVMUtilTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
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
name|'VMwareVMUtilTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VMwareVMUtilTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
number|'1'
op|']'
op|','
string|'"fake-ds"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
number|'2'
op|']'
op|','
name|'unit'
op|'.'
name|'Ti'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
number|'3'
op|']'
op|','
number|'500'
op|'*'
name|'unit'
op|'.'
name|'Gi'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name_with_regex
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name_with_regex'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test with a regex that matches with a datastore'
nl|'\n'
indent|'        '
name|'datastore_valid_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^openstack.*\\d$"'
op|')'
newline|'\n'
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"openstack-ds0"'
op|')'
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"fake-ds0"'
op|')'
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"fake-ds1"'
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
name|'None'
op|','
name|'None'
op|','
name|'datastore_valid_regex'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"openstack-ds0"'
op|','
name|'result'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name_with_list
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name_with_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test with a regex containing whitelist of datastores'
nl|'\n'
indent|'        '
name|'datastore_valid_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"(openstack-ds0|openstack-ds2)"'
op|')'
newline|'\n'
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"openstack-ds0"'
op|')'
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"openstack-ds1"'
op|')'
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"openstack-ds2"'
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
name|'None'
op|','
name|'None'
op|','
name|'datastore_valid_regex'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
string|'"openstack-ds1"'
op|','
name|'result'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name_with_regex_error
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name_with_regex_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test with a regex that has no match'
nl|'\n'
comment|'# Checks if code raises DatastoreNotFound with a specific message'
nl|'\n'
indent|'        '
name|'datastore_invalid_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"unknown-ds"'
op|')'
newline|'\n'
name|'exp_message'
op|'='
op|'('
name|'_'
op|'('
string|'"Datastore regex %s did not match any datastores"'
op|')'
nl|'\n'
op|'%'
name|'datastore_invalid_regex'
op|'.'
name|'pattern'
op|')'
newline|'\n'
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"fake-ds0"'
op|')'
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'Datastore'
op|'('
string|'"fake-ds1"'
op|')'
op|')'
newline|'\n'
comment|'# assertRaisesRegExp would have been a good choice instead of'
nl|'\n'
comment|"# try/catch block, but it's available only from Py 2.7."
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'datastore_invalid_regex'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DatastoreNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_message'
op|','
name|'e'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"DatastoreNotFound Exception was not raised with "'
nl|'\n'
string|'"message: %s"'
op|'%'
name|'exp_message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name_without_datastore
dedent|''
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name_without_datastore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|','
nl|'\n'
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|','
nl|'\n'
name|'fake_session'
op|'('
op|')'
op|','
name|'host'
op|'='
string|'"fake-host"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|','
nl|'\n'
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|','
nl|'\n'
name|'fake_session'
op|'('
op|')'
op|','
name|'cluster'
op|'='
string|'"fake-cluster"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_ref_from_id
dedent|''
name|'def'
name|'test_get_host_ref_from_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host_name'
op|'='
string|'"ha-host"'
newline|'\n'
name|'fake_host_sys'
op|'='
name|'fake'
op|'.'
name|'HostSystem'
op|'('
name|'fake_host_name'
op|')'
newline|'\n'
name|'fake_host_id'
op|'='
name|'fake_host_sys'
op|'.'
name|'obj'
op|'.'
name|'value'
newline|'\n'
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake_host_sys'
op|')'
newline|'\n'
name|'ref'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref_from_id'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
name|'fake_host_id'
op|','
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'ref'
op|','
name|'fake'
op|'.'
name|'HostSystem'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_host_id'
op|','
name|'ref'
op|'.'
name|'obj'
op|'.'
name|'value'
op|')'
newline|'\n'
nl|'\n'
name|'host_name'
op|'='
name|'vm_util'
op|'.'
name|'get_host_name_from_host_ref'
op|'('
name|'ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_host_name'
op|','
name|'host_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_ref_no_hosts_in_cluster
dedent|''
name|'def'
name|'test_get_host_ref_no_hosts_in_cluster'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'vm_util'
op|'.'
name|'get_host_ref'
op|','
nl|'\n'
name|'fake_session'
op|'('
string|'""'
op|')'
op|','
string|"'fake_cluster'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name_no_host_in_cluster
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name_no_host_in_cluster'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|','
nl|'\n'
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|','
nl|'\n'
name|'fake_session'
op|'('
string|'""'
op|')'
op|','
string|"'fake_cluster'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_name_for_vm
dedent|''
name|'def'
name|'test_get_host_name_for_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host'
op|'='
name|'fake'
op|'.'
name|'HostSystem'
op|'('
op|')'
newline|'\n'
name|'fake_host_id'
op|'='
name|'fake_host'
op|'.'
name|'obj'
op|'.'
name|'value'
newline|'\n'
name|'fake_vm'
op|'='
name|'fake'
op|'.'
name|'VirtualMachine'
op|'('
name|'name'
op|'='
string|"'vm-123'"
op|','
nl|'\n'
name|'runtime_host'
op|'='
name|'fake_host'
op|'.'
name|'obj'
op|')'
newline|'\n'
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake_vm'
op|')'
newline|'\n'
nl|'\n'
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref_from_name'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
string|"'vm-123'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'host_id'
op|'='
name|'vm_util'
op|'.'
name|'get_host_id_from_vm_ref'
op|'('
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_host_id'
op|','
name|'host_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_property_from_property_set
dedent|''
name|'def'
name|'test_property_from_property_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'ObjectContent'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ObjectContent'"
op|','
op|'['
string|"'propSet'"
op|']'
op|')'
newline|'\n'
name|'DynamicProperty'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Property'"
op|','
op|'['
string|"'name'"
op|','
string|"'val'"
op|']'
op|')'
newline|'\n'
name|'MoRef'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Val'"
op|','
op|'['
string|"'value'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'good_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'results_good'
op|'='
op|'['
nl|'\n'
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'name'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'vm-123'"
op|')'
op|')'
op|']'
op|')'
op|','
nl|'\n'
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'foo'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'bar1'"
op|')'
op|')'
op|','
nl|'\n'
name|'DynamicProperty'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'runtime.host'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'host-123'"
op|')'
op|')'
op|','
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'foo'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'bar2'"
op|')'
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'something'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'thing'"
op|')'
op|')'
op|']'
op|')'
op|','
op|']'
newline|'\n'
name|'for'
name|'result'
name|'in'
name|'results_good'
op|':'
newline|'\n'
indent|'            '
name|'good_objects'
op|'.'
name|'add_object'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bad_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'results_bad'
op|'='
op|'['
nl|'\n'
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'name'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'vm-123'"
op|')'
op|')'
op|']'
op|')'
op|','
nl|'\n'
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'foo'"
op|','
name|'val'
op|'='
string|"'bar1'"
op|')'
op|','
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'foo'"
op|','
name|'val'
op|'='
string|"'bar2'"
op|')'
op|','
op|']'
op|')'
op|','
nl|'\n'
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'something'"
op|','
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'thing'"
op|')'
op|')'
op|']'
op|')'
op|','
op|']'
newline|'\n'
name|'for'
name|'result'
name|'in'
name|'results_bad'
op|':'
newline|'\n'
indent|'            '
name|'bad_objects'
op|'.'
name|'add_object'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'prop'
op|'='
name|'vm_util'
op|'.'
name|'property_from_property_set'
op|'('
nl|'\n'
string|"'runtime.host'"
op|','
name|'good_objects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'prop'
op|')'
newline|'\n'
name|'value'
op|'='
name|'prop'
op|'.'
name|'val'
op|'.'
name|'value'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host-123'"
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
name|'prop2'
op|'='
name|'vm_util'
op|'.'
name|'property_from_property_set'
op|'('
nl|'\n'
string|"'runtime.host'"
op|','
name|'bad_objects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'prop2'
op|')'
newline|'\n'
nl|'\n'
name|'prop3'
op|'='
name|'vm_util'
op|'.'
name|'property_from_property_set'
op|'('
string|"'foo'"
op|','
name|'good_objects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'prop3'
op|')'
newline|'\n'
name|'val3'
op|'='
name|'prop3'
op|'.'
name|'val'
op|'.'
name|'value'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'bar1'"
op|','
name|'val3'
op|')'
newline|'\n'
nl|'\n'
name|'prop4'
op|'='
name|'vm_util'
op|'.'
name|'property_from_property_set'
op|'('
string|"'foo'"
op|','
name|'bad_objects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'prop4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'bar1'"
op|','
name|'prop4'
op|'.'
name|'val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datastore_ref_and_name_inaccessible_ds
dedent|''
name|'def'
name|'test_get_datastore_ref_and_name_inaccessible_ds'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data_store'
op|'='
name|'fake'
op|'.'
name|'Datastore'
op|'('
op|')'
newline|'\n'
name|'data_store'
op|'.'
name|'set'
op|'('
string|'"summary.accessible"'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'data_store'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|','
nl|'\n'
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|','
nl|'\n'
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_resize_spec
dedent|''
name|'def'
name|'test_get_resize_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_instance'
op|'='
op|'{'
string|"'id'"
op|':'
number|'7'
op|','
string|"'name'"
op|':'
string|"'fake!'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'bda5fb9e-b347-40e8-8256-42397848cb00'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
string|"'memory_mb'"
op|':'
number|'2048'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_resize_spec'
op|'('
name|'fake'
op|'.'
name|'FakeFactory'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_instance'
op|')'
newline|'\n'
name|'expected'
op|'='
string|'"""{\'memoryMB\': 2048,\n                       \'numCPUs\': 2,\n                       \'obj_name\': \'ns0:VirtualMachineConfigSpec\'}"""'
newline|'\n'
name|'expected'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'expected'
op|')'
newline|'\n'
name|'result'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'repr'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cdrom_attach_config_spec
dedent|''
name|'def'
name|'test_get_cdrom_attach_config_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_cdrom_attach_config_spec'
op|'('
name|'fake'
op|'.'
name|'FakeFactory'
op|'('
op|')'
op|','
nl|'\n'
name|'fake'
op|'.'
name|'Datastore'
op|'('
op|')'
op|','
nl|'\n'
string|'"/tmp/foo.iso"'
op|','
nl|'\n'
number|'0'
op|')'
newline|'\n'
name|'expected'
op|'='
string|'"""{\n    \'deviceChange\': [\n        {\n            \'device\': {\n                \'connectable\': {\n                    \'allowGuestControl\': False,\n                    \'startConnected\': True,\n                    \'connected\': True,\n                    \'obj_name\': \'ns0: VirtualDeviceConnectInfo\'\n                },\n                \'backing\': {\n                    \'datastore\': {\n                        "summary.type": "VMFS",\n                        "summary.accessible":true,\n                        "summary.name": "fake-ds",\n                        "summary.capacity": 1099511627776,\n                        "summary.freeSpace": 536870912000,\n                        "browser": ""\n                    },\n                    \'fileName\': \'/tmp/foo.iso\',\n                    \'obj_name\': \'ns0: VirtualCdromIsoBackingInfo\'\n                },\n                \'controllerKey\': 200,\n                \'unitNumber\': 0,\n                \'key\': -1,\n                \'obj_name\': \'ns0: VirtualCdrom\'\n            },\n            \'operation\': \'add\',\n            \'obj_name\': \'ns0: VirtualDeviceConfigSpec\'\n        }\n    ],\n    \'obj_name\': \'ns0: VirtualMachineConfigSpec\'\n}\n"""'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'expected'
op|')'
newline|'\n'
name|'result'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'repr'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lsilogic_controller_spec
dedent|''
name|'def'
name|'test_lsilogic_controller_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test controller spec returned for lsiLogic sas adapter type'
nl|'\n'
indent|'        '
name|'config_spec'
op|'='
name|'vm_util'
op|'.'
name|'create_controller_spec'
op|'('
name|'fake'
op|'.'
name|'FakeFactory'
op|'('
op|')'
op|','
op|'-'
number|'101'
op|','
nl|'\n'
name|'adapter_type'
op|'='
string|'"lsiLogicsas"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"ns0:VirtualLsiLogicSASController"'
op|','
nl|'\n'
name|'config_spec'
op|'.'
name|'device'
op|'.'
name|'obj_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vmdk_path_and_adapter_type
dedent|''
name|'def'
name|'test_get_vmdk_path_and_adapter_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test the adapter_type returned for a lsiLogic sas controller'
nl|'\n'
indent|'        '
name|'controller_key'
op|'='
number|'1000'
newline|'\n'
name|'filename'
op|'='
string|"'[test_datastore] test_file.vmdk'"
newline|'\n'
name|'disk'
op|'='
name|'fake'
op|'.'
name|'VirtualDisk'
op|'('
op|')'
newline|'\n'
name|'disk'
op|'.'
name|'controllerKey'
op|'='
name|'controller_key'
newline|'\n'
name|'disk_backing'
op|'='
name|'fake'
op|'.'
name|'VirtualDiskFlatVer2BackingInfo'
op|'('
op|')'
newline|'\n'
name|'disk_backing'
op|'.'
name|'fileName'
op|'='
name|'filename'
newline|'\n'
name|'disk'
op|'.'
name|'backing'
op|'='
name|'disk_backing'
newline|'\n'
name|'controller'
op|'='
name|'fake'
op|'.'
name|'VirtualLsiLogicSASController'
op|'('
op|')'
newline|'\n'
name|'controller'
op|'.'
name|'key'
op|'='
name|'controller_key'
newline|'\n'
name|'devices'
op|'='
op|'['
name|'disk'
op|','
name|'controller'
op|']'
newline|'\n'
name|'vmdk_info'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_path_and_adapter_type'
op|'('
name|'devices'
op|')'
newline|'\n'
name|'adapter_type'
op|'='
name|'vmdk_info'
op|'['
number|'2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'lsiLogicsas'"
op|','
name|'adapter_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vmdk_adapter_type
dedent|''
name|'def'
name|'test_get_vmdk_adapter_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test for the adapter_type to be used in vmdk descriptor'
nl|'\n'
comment|'# Adapter type in vmdk descriptor is same for LSI-SAS & LSILogic'
nl|'\n'
indent|'        '
name|'vmdk_adapter_type'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_adapter_type'
op|'('
string|'"lsiLogic"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"lsiLogic"'
op|','
name|'vmdk_adapter_type'
op|')'
newline|'\n'
name|'vmdk_adapter_type'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_adapter_type'
op|'('
string|'"lsiLogicsas"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"lsiLogic"'
op|','
name|'vmdk_adapter_type'
op|')'
newline|'\n'
name|'vmdk_adapter_type'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_adapter_type'
op|'('
string|'"dummyAdapter"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"dummyAdapter"'
op|','
name|'vmdk_adapter_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_get_vnc_config_spec
dedent|''
name|'def'
name|'_test_get_vnc_config_spec'
op|'('
name|'self'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_vnc_config_spec'
op|'('
name|'fake'
op|'.'
name|'FakeFactory'
op|'('
op|')'
op|','
nl|'\n'
name|'port'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|test_get_vnc_config_spec
dedent|''
name|'def'
name|'test_get_vnc_config_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'_test_get_vnc_config_spec'
op|'('
number|'7'
op|')'
newline|'\n'
name|'expected'
op|'='
string|'"""{\'extraConfig\': [\n                          {\'value\': \'true\',\n                           \'key\': \'RemoteDisplay.vnc.enabled\',\n                           \'obj_name\': \'ns0:OptionValue\'},\n                          {\'value\': 7,\n                           \'key\': \'RemoteDisplay.vnc.port\',\n                           \'obj_name\': \'ns0:OptionValue\'}],\n                       \'obj_name\': \'ns0:VirtualMachineConfigSpec\'}"""'
newline|'\n'
name|'expected'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'expected'
op|')'
newline|'\n'
name|'result'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'repr'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_cluster_refs_by_name_none
dedent|''
name|'def'
name|'test_get_all_cluster_refs_by_name_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'refs'
op|'='
name|'vm_util'
op|'.'
name|'get_all_cluster_refs_by_name'
op|'('
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
nl|'\n'
op|'['
string|"'fake_cluster'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'not'
name|'refs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_cluster_refs_by_name_exists
dedent|''
name|'def'
name|'test_get_all_cluster_refs_by_name_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'ClusterComputeResource'
op|'('
name|'name'
op|'='
string|"'cluster'"
op|')'
op|')'
newline|'\n'
name|'refs'
op|'='
name|'vm_util'
op|'.'
name|'get_all_cluster_refs_by_name'
op|'('
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
nl|'\n'
op|'['
string|"'cluster'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'refs'
op|')'
op|'=='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_cluster_refs_by_name_missing
dedent|''
name|'def'
name|'test_get_all_cluster_refs_by_name_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'partialObject'
op|'('
name|'path'
op|'='
string|"'cluster'"
op|')'
op|')'
newline|'\n'
name|'refs'
op|'='
name|'vm_util'
op|'.'
name|'get_all_cluster_refs_by_name'
op|'('
name|'fake_session'
op|'('
name|'fake_objects'
op|')'
op|','
nl|'\n'
op|'['
string|"'cluster'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'not'
name|'refs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_propset_dict_simple
dedent|''
name|'def'
name|'test_propset_dict_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ObjectContent'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ObjectContent'"
op|','
op|'['
string|"'propSet'"
op|']'
op|')'
newline|'\n'
name|'DynamicProperty'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Property'"
op|','
op|'['
string|"'name'"
op|','
string|"'val'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'object'
op|'='
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'foo'"
op|','
name|'val'
op|'='
string|'"bar"'
op|')'
op|']'
op|')'
newline|'\n'
name|'propdict'
op|'='
name|'vm_util'
op|'.'
name|'propset_dict'
op|'('
name|'object'
op|'.'
name|'propSet'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"bar"'
op|','
name|'propdict'
op|'['
string|"'foo'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_propset_dict_complex
dedent|''
name|'def'
name|'test_propset_dict_complex'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ObjectContent'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ObjectContent'"
op|','
op|'['
string|"'propSet'"
op|']'
op|')'
newline|'\n'
name|'DynamicProperty'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Property'"
op|','
op|'['
string|"'name'"
op|','
string|"'val'"
op|']'
op|')'
newline|'\n'
name|'MoRef'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Val'"
op|','
op|'['
string|"'value'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'object'
op|'='
name|'ObjectContent'
op|'('
name|'propSet'
op|'='
op|'['
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'foo'"
op|','
name|'val'
op|'='
string|'"bar"'
op|')'
op|','
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'some.thing'"
op|','
nl|'\n'
name|'val'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|"'else'"
op|')'
op|')'
op|','
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
string|"'another.thing'"
op|','
name|'val'
op|'='
string|"'value'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'propdict'
op|'='
name|'vm_util'
op|'.'
name|'propset_dict'
op|'('
name|'object'
op|'.'
name|'propSet'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"bar"'
op|','
name|'propdict'
op|'['
string|"'foo'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'propdict'
op|'['
string|"'some.thing'"
op|']'
op|','
string|"'value'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"else"'
op|','
name|'propdict'
op|'['
string|"'some.thing'"
op|']'
op|'.'
name|'value'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"value"'
op|','
name|'propdict'
op|'['
string|"'another.thing'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_detach_virtual_disk_spec
dedent|''
name|'def'
name|'_test_detach_virtual_disk_spec'
op|'('
name|'self'
op|','
name|'destroy_disk'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'virtual_device_config'
op|'='
name|'vm_util'
op|'.'
name|'detach_virtual_disk_spec'
op|'('
nl|'\n'
name|'fake'
op|'.'
name|'FakeFactory'
op|'('
op|')'
op|','
nl|'\n'
string|"'fake_device'"
op|','
nl|'\n'
name|'destroy_disk'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'remove'"
op|','
name|'virtual_device_config'
op|'.'
name|'operation'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake_device'"
op|','
name|'virtual_device_config'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|','
nl|'\n'
name|'virtual_device_config'
op|'.'
name|'obj_name'
op|')'
newline|'\n'
name|'if'
name|'destroy_disk'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'destroy'"
op|','
name|'virtual_device_config'
op|'.'
name|'fileOperation'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'hasattr'
op|'('
name|'virtual_device_config'
op|','
string|"'fileOperation'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_virtual_disk_spec
dedent|''
dedent|''
name|'def'
name|'test_detach_virtual_disk_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_detach_virtual_disk_spec'
op|'('
name|'destroy_disk'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_virtual_disk_destroy_spec
dedent|''
name|'def'
name|'test_detach_virtual_disk_destroy_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_detach_virtual_disk_spec'
op|'('
name|'destroy_disk'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vm_create_spec
dedent|''
name|'def'
name|'test_get_vm_create_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'fake_instance'
op|'='
op|'{'
string|"'id'"
op|':'
number|'7'
op|','
string|"'name'"
op|':'
string|"'fake!'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
string|"'memory_mb'"
op|':'
number|'2048'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_create_spec'
op|'('
name|'fake'
op|'.'
name|'FakeFactory'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_instance'
op|','
string|"'fake-name'"
op|','
nl|'\n'
string|"'fake-datastore'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'expected'
op|'='
string|'"""{\n            \'files\': {\'vmPathName\': \'[fake-datastore]\',\n            \'obj_name\': \'ns0:VirtualMachineFileInfo\'},\n            \'name\': \'fake-name\', \'deviceChange\': [],\n            \'extraConfig\': [{\'value\': \'%s\',\n                             \'key\': \'nvp.vm-uuid\',\n                             \'obj_name\': \'ns0:OptionValue\'}],\n            \'memoryMB\': 2048,\n            \'obj_name\': \'ns0:VirtualMachineConfigSpec\',\n            \'guestId\': \'otherGuest\',\n            \'tools\': {\'beforeGuestStandby\': True,\n                      \'beforeGuestReboot\': True,\n                      \'beforeGuestShutdown\': True,\n                      \'afterResume\': True,\n                      \'afterPowerOn\': True,\n            \'obj_name\': \'ns0:ToolsConfigInfo\'},\n            \'numCPUs\': 2}"""'
op|'%'
name|'instance_uuid'
newline|'\n'
name|'expected'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'expected'
op|')'
newline|'\n'
name|'result'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'\\s+'"
op|','
string|"''"
op|','
name|'repr'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
