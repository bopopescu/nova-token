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
string|'"""\nTests For Scheduler\n"""'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
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
name|'as'
name|'auth_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
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
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'max_instances'"
op|','
string|"'nova.scheduler.simple'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerTestCase
name|'class'
name|'SchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for scheduler"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=C0103'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SchedulerTestCase'
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
name|'max_instances'
op|'='
number|'4'
op|','
nl|'\n'
name|'scheduler_driver'
op|'='
string|"'nova.scheduler.simple.SimpleScheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'='
name|'manager'
op|'.'
name|'SchedulerManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'auth_manager'
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
name|'None'
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
comment|'# pylint: disable-msg=C0103'
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
newline|'\n'
nl|'\n'
DECL|member|test_hosts_are_up
dedent|''
name|'def'
name|'test_hosts_are_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): constructing service without create method'
nl|'\n'
comment|'#             because we are going to use it without queue'
nl|'\n'
indent|'        '
name|'service1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'service2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'hosts'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'service1'
op|'.'
name|'report_state'
op|'('
op|')'
newline|'\n'
name|'service2'
op|'.'
name|'report_state'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'hosts'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_least_busy_host_gets_instance
dedent|''
name|'def'
name|'test_least_busy_host_gets_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'service2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'service1'
op|'.'
name|'report_state'
op|'('
op|')'
newline|'\n'
name|'service2'
op|'.'
name|'report_state'
op|'('
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'service1'
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
name|'host'
op|'='
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'pick_compute_host'
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
name|'assertEqual'
op|'('
name|'host'
op|','
string|"'host2'"
op|')'
newline|'\n'
name|'service1'
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
DECL|member|test_too_many_instances
dedent|''
name|'def'
name|'test_too_many_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'max_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'service1'
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
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
dedent|''
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
name|'assertRaises'
op|'('
name|'driver'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'pick_compute_host'
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
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'service1'
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
dedent|''
endmarker|''
end_unit
