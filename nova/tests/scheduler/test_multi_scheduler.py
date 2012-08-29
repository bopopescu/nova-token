begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC'
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
string|'"""\nTests For Multi Scheduler\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'multi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'scheduler'
name|'import'
name|'test_scheduler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeComputeScheduler
name|'class'
name|'FakeComputeScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
DECL|variable|is_fake_compute
indent|'    '
name|'is_fake_compute'
op|'='
name|'True'
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
name|'FakeComputeScheduler'
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
name|'is_update_caps_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|schedule_theoretical
dedent|''
name|'def'
name|'schedule_theoretical'
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
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeVolumeScheduler
dedent|''
dedent|''
name|'class'
name|'FakeVolumeScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
DECL|variable|is_fake_volume
indent|'    '
name|'is_fake_volume'
op|'='
name|'True'
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
name|'FakeVolumeScheduler'
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
name|'is_update_caps_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeDefaultScheduler
dedent|''
dedent|''
name|'class'
name|'FakeDefaultScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
DECL|variable|is_fake_default
indent|'    '
name|'is_fake_default'
op|'='
name|'True'
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
name|'FakeDefaultScheduler'
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
name|'is_update_caps_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MultiDriverTestCase
dedent|''
dedent|''
name|'class'
name|'MultiDriverTestCase'
op|'('
name|'test_scheduler'
op|'.'
name|'SchedulerTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for multi driver"""'
newline|'\n'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'multi'
op|'.'
name|'MultiScheduler'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'MultiDriverTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'base_name'
op|'='
string|"'nova.tests.scheduler.test_multi_scheduler.%s'"
newline|'\n'
name|'compute_cls_name'
op|'='
name|'base_name'
op|'%'
string|"'FakeComputeScheduler'"
newline|'\n'
name|'volume_cls_name'
op|'='
name|'base_name'
op|'%'
string|"'FakeVolumeScheduler'"
newline|'\n'
name|'default_cls_name'
op|'='
name|'base_name'
op|'%'
string|"'FakeDefaultScheduler'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'compute_scheduler_driver'
op|'='
name|'compute_cls_name'
op|','
nl|'\n'
name|'volume_scheduler_driver'
op|'='
name|'volume_cls_name'
op|','
nl|'\n'
name|'default_scheduler_driver'
op|'='
name|'default_cls_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_manager'
op|'='
name|'multi'
op|'.'
name|'MultiScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_drivers_inited
dedent|''
name|'def'
name|'test_drivers_inited'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mgr'
op|'='
name|'self'
op|'.'
name|'_manager'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'is_fake_compute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'volume'"
op|']'
op|'.'
name|'is_fake_volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'default'"
op|']'
op|'.'
name|'is_fake_default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_service_capabilities
dedent|''
name|'def'
name|'test_update_service_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_update_service_capabilities
indent|'        '
name|'def'
name|'fake_update_service_capabilities'
op|'('
name|'self'
op|','
name|'service'
op|','
name|'host'
op|','
name|'caps'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_update_caps_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'mgr'
op|'='
name|'self'
op|'.'
name|'_manager'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|','
nl|'\n'
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'fake_update_service_capabilities'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'volume'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
name|'mgr'
op|'.'
name|'update_service_capabilities'
op|'('
string|"'foo_svc'"
op|','
string|"'foo_host'"
op|','
string|"'foo_caps'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'volume'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleSchedulerTestCase
dedent|''
dedent|''
name|'class'
name|'SimpleSchedulerTestCase'
op|'('
name|'MultiDriverTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for simple driver."""'
newline|'\n'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'multi'
op|'.'
name|'MultiScheduler'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'SimpleSchedulerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'base_name'
op|'='
string|"'nova.tests.scheduler.test_multi_scheduler.%s'"
newline|'\n'
name|'compute_cls_name'
op|'='
name|'base_name'
op|'%'
string|"'FakeComputeScheduler'"
newline|'\n'
name|'volume_cls_name'
op|'='
string|"'nova.scheduler.simple.SimpleScheduler'"
newline|'\n'
name|'default_cls_name'
op|'='
name|'base_name'
op|'%'
string|"'FakeDefaultScheduler'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'compute_scheduler_driver'
op|'='
name|'compute_cls_name'
op|','
nl|'\n'
name|'volume_scheduler_driver'
op|'='
name|'volume_cls_name'
op|','
nl|'\n'
name|'default_scheduler_driver'
op|'='
name|'default_cls_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_manager'
op|'='
name|'multi'
op|'.'
name|'MultiScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_service_capabilities
dedent|''
name|'def'
name|'test_update_service_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_update_service_capabilities
indent|'        '
name|'def'
name|'fake_update_service_capabilities'
op|'('
name|'self'
op|','
name|'service'
op|','
name|'host'
op|','
name|'caps'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_update_caps_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'mgr'
op|'='
name|'self'
op|'.'
name|'_manager'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|','
nl|'\n'
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'fake_update_service_capabilities'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
name|'mgr'
op|'.'
name|'update_service_capabilities'
op|'('
string|"'foo_svc'"
op|','
string|"'foo_host'"
op|','
string|"'foo_caps'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'volume'"
op|']'
op|'.'
name|'is_update_caps_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_drivers_inited
dedent|''
name|'def'
name|'test_drivers_inited'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mgr'
op|'='
name|'self'
op|'.'
name|'_manager'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'is_fake_compute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'volume'"
op|']'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mgr'
op|'.'
name|'drivers'
op|'['
string|"'default'"
op|']'
op|'.'
name|'is_fake_default'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
