begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nTests For Compute\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'logging'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeTestCase
name|'class'
name|'ComputeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for compute"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ComputeTestCase'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'stub_network'
op|'='
name|'True'
op|','
nl|'\n'
name|'network_manager'
op|'='
string|"'nova.network.manager.FlatManager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute_api'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ComputeTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
string|"'ami-test'"
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
string|"'m1.tiny'"
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_defaults_display_name
dedent|''
name|'def'
name|'test_create_instance_defaults_display_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verify that an instance cannot be created without a display_name."""'
newline|'\n'
name|'cases'
op|'='
op|'['
name|'dict'
op|'('
op|')'
op|','
name|'dict'
op|'('
name|'display_name'
op|'='
name|'None'
op|')'
op|']'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'cases'
op|':'
newline|'\n'
indent|'            '
name|'ref'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'create_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_instance_type'
op|','
name|'None'
op|','
op|'**'
name|'instance'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'ref'
op|'['
number|'0'
op|']'
op|'.'
name|'display_name'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'ref'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_associates_security_groups
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_create_instance_associates_security_groups'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure create_instances associates security groups"""'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|'}'
newline|'\n'
name|'group'
op|'='
name|'db'
op|'.'
name|'security_group_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'ref'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'create_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_instance_type'
op|','
name|'None'
op|','
name|'security_group'
op|'='
op|'['
string|"'default'"
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ref'
op|'['
number|'0'
op|']'
op|'['
string|"'security_groups'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'security_group_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'group'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'ref'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_terminate
dedent|''
dedent|''
name|'def'
name|'test_run_terminate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure it is possible to  run and terminate instance"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Running instances: %s"'
op|')'
op|','
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"After terminating instances: %s"'
op|')'
op|','
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_terminate_timestamps
dedent|''
name|'def'
name|'test_run_terminate_timestamps'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure timestamps are set for launched and destroyed"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_ref'
op|'['
string|"'launched_at'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_ref'
op|'['
string|"'deleted_at'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'launch'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'instance_ref'
op|'['
string|"'launched_at'"
op|']'
op|'>'
name|'launch'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_ref'
op|'['
string|"'deleted_at'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'terminate'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
name|'True'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'instance_ref'
op|'['
string|"'launched_at'"
op|']'
op|'<'
name|'terminate'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'instance_ref'
op|'['
string|"'deleted_at'"
op|']'
op|'>'
name|'terminate'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause
dedent|''
name|'def'
name|'test_pause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure instance can be paused"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'pause_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'unpause_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_suspend
dedent|''
name|'def'
name|'test_suspend'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""ensure instance can be suspended"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'suspend_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'resume_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reboot
dedent|''
name|'def'
name|'test_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure instance can be rebooted"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'reboot_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_diagnostics
dedent|''
name|'def'
name|'test_diagnostics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure instance diagnostics are available"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'get_diagnostics'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot
dedent|''
name|'def'
name|'test_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure instance can be snapshotted"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'name'
op|'='
string|'"myfakesnapshot"'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'snapshot_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_output
dedent|''
name|'def'
name|'test_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure we can get console output from instance"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'console'
op|'='
name|'self'
op|'.'
name|'compute'
op|'.'
name|'get_console_output'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'console'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance_existing
dedent|''
name|'def'
name|'test_run_instance_existing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure failure when running an instance that already exists"""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
