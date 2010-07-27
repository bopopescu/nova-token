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
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
op|'.'
name|'volume'
name|'import'
name|'service'
name|'as'
name|'volume_service'
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
DECL|class|VolumeTestCase
name|'class'
name|'VolumeTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
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
name|'VolumeTestCase'
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
name|'compute'
op|'='
name|'compute'
op|'.'
name|'service'
op|'.'
name|'ComputeService'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'fake_libvirt'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_storage'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'='
name|'volume_service'
op|'.'
name|'VolumeService'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_create_volume
dedent|''
name|'def'
name|'test_run_create_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol_size'
op|'='
string|"'0'"
newline|'\n'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'vol_size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
comment|'# TODO(termie): get_volume returns differently than create_volume'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'volume_service'
op|'.'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'volume_id'
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
name|'volume_service'
op|'.'
name|'get_volume'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_big_volume
dedent|''
name|'def'
name|'test_too_big_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol_size'
op|'='
string|"'1001'"
newline|'\n'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|','
nl|'\n'
name|'vol_size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_volumes
dedent|''
name|'def'
name|'test_too_many_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol_size'
op|'='
string|"'1'"
newline|'\n'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'num_shelves'
op|'='
name|'FLAGS'
op|'.'
name|'last_shelf_id'
op|'-'
name|'FLAGS'
op|'.'
name|'first_shelf_id'
op|'+'
number|'1'
newline|'\n'
name|'total_slots'
op|'='
name|'FLAGS'
op|'.'
name|'slots_per_shelf'
op|'*'
name|'num_shelves'
newline|'\n'
name|'vols'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'total_slots'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vid'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'vol_size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'vols'
op|'.'
name|'append'
op|'('
name|'vid'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'volume_service'
op|'.'
name|'NoMoreVolumes'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|','
nl|'\n'
name|'vol_size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'for'
name|'id'
name|'in'
name|'vols'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_attach_detach_volume
dedent|''
dedent|''
name|'def'
name|'test_run_attach_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Create one volume and one compute to test with'
nl|'\n'
indent|'        '
name|'instance_id'
op|'='
string|'"storage-test"'
newline|'\n'
name|'vol_size'
op|'='
string|'"5"'
newline|'\n'
name|'user_id'
op|'='
string|'"fake"'
newline|'\n'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'mountpoint'
op|'='
string|'"/dev/sdf"'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'vol_size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'volume_obj'
op|'='
name|'volume_service'
op|'.'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'volume_obj'
op|'.'
name|'start_attach'
op|'('
name|'instance_id'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'attach_volume'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_obj'
op|'['
string|"'status'"
op|']'
op|','
string|'"in-use"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_obj'
op|'['
string|"'attachStatus'"
op|']'
op|','
string|'"attached"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_obj'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_obj'
op|'['
string|"'mountpoint'"
op|']'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
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
name|'volume'
op|'.'
name|'delete_volume'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'detach_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'volume_obj'
op|'='
name|'volume_service'
op|'.'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_obj'
op|'['
string|"'status'"
op|']'
op|','
string|'"available"'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'volume_id'
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
name|'volume_service'
op|'.'
name|'get_volume'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multi_node
dedent|''
name|'def'
name|'test_multi_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): Figure out how to test with two nodes,'
nl|'\n'
comment|'# each of them having a different FLAG for storage_node'
nl|'\n'
comment|'# This will allow us to test cross-node interactions'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
