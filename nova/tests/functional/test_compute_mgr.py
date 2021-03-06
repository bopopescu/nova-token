begin_unit
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'import'
name|'fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'cast_as_call'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_server_actions'
newline|'\n'
nl|'\n'
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
DECL|class|ComputeManagerTestCase
name|'class'
name|'ComputeManagerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'ComputeManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'cast_as_call'
op|'.'
name|'CastAsCall'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'conductor'"
op|','
nl|'\n'
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'scheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'fake_server_actions'
op|'.'
name|'stub_out_action_events'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fake_network'
op|'.'
name|'set_stub_network_methods'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_fault_message_no_traceback_with_retry
dedent|''
name|'def'
name|'test_instance_fault_message_no_traceback_with_retry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This test simulates a spawn failure on the last retry attempt.\n\n        If driver spawn raises an exception on the last retry attempt, the\n        instance fault message should not contain a traceback for the\n        last exception. The fault message field is limited in size and a long\n        message with a traceback displaces the original error message.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'3'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'name'
op|'='
string|"'flavor1'"
op|','
name|'memory_mb'
op|'='
number|'256'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'root_gb'
op|'='
number|'1'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'1'
op|','
name|'flavorid'
op|'='
string|"'1'"
op|','
name|'swap'
op|'='
number|'0'
op|','
name|'rxtx_factor'
op|'='
number|'1.0'
op|','
nl|'\n'
name|'vcpu_weight'
op|'='
number|'1'
op|','
name|'disabled'
op|'='
name|'False'
op|','
name|'is_public'
op|'='
name|'True'
op|','
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'projects'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'flavor'
op|'='
name|'flavor'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'256'
op|','
name|'root_gb'
op|'='
number|'0'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'manager'
op|'.'
name|'compute_task_mgr'
op|','
nl|'\n'
string|"'_cleanup_allocated_networks'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'network_api'
op|','
nl|'\n'
string|"'cleanup_instance_network_on_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.utils.notify_about_instance_usage'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'driver'
op|','
string|"'spawn'"
op|')'
newline|'\n'
DECL|function|_test
name|'def'
name|'_test'
op|'('
name|'mock_spawn'
op|','
name|'mock_notify'
op|','
name|'mock_cinoh'
op|','
name|'mock_can'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mock_spawn'
op|'.'
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
op|'('
string|"'Preserve this'"
op|')'
newline|'\n'
comment|"# Simulate that we're on the last retry attempt"
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'retry'"
op|':'
op|'{'
string|"'num_attempts'"
op|':'
number|'3'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'manager'
op|'.'
name|'build_and_run_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'block_device_mapping'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'_test'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'Preserve this'"
op|','
name|'instance'
op|'.'
name|'fault'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
