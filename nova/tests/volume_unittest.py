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
name|'exception'
newline|'\n'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
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
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_create_volume
dedent|''
name|'def'
name|'_create_volume'
op|'('
name|'self'
op|','
name|'size'
op|'='
string|"'0'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
string|"'0'"
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
string|'"creating"'
newline|'\n'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'None'
op|','
name|'vol'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_run_create_volume
name|'def'
name|'test_run_create_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_id'
op|','
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'None'
op|','
name|'volume_id'
op|')'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'volume_get'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_too_big_volume
name|'def'
name|'test_too_big_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# FIXME(vish): validation needs to move into the data layer in'
nl|'\n'
comment|'#              volume_create'
nl|'\n'
indent|'        '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'True'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
string|"'1001'"
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Should have thrown TypeError"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_too_many_volumes
name|'def'
name|'test_too_many_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vols'
op|'='
op|'['
op|']'
newline|'\n'
name|'total_slots'
op|'='
name|'FLAGS'
op|'.'
name|'num_shelves'
op|'*'
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
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
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'vols'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFailure'
op|'('
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'db'
op|'.'
name|'NoMoreBlades'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'None'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'vols'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_run_attach_detach_volume
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
name|'mountpoint'
op|'='
string|'"/dev/sdf"'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_attached'
op|'('
name|'None'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'attach_volume'
op|'('
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'None'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
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
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|','
string|'"attached"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
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
name|'vol'
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
name|'assertFailure'
op|'('
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'Error'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_detached'
op|'('
name|'None'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'detach_volume'
op|'('
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'None'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
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
name|'self'
op|'.'
name|'context'
op|','
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
name|'db'
op|'.'
name|'volume_get'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_concurrent_volumes_get_different_blades
name|'def'
name|'test_concurrent_volumes_get_different_blades'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'shelf_blades'
op|'='
op|'['
op|']'
newline|'\n'
name|'volume_ids'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_check
name|'def'
name|'_check'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_ids'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'db'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'None'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'shelf_blade'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'shelf_blade'
name|'not'
name|'in'
name|'shelf_blades'
op|')'
newline|'\n'
name|'shelf_blades'
op|'.'
name|'append'
op|'('
name|'shelf_blade'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"got %s"'
op|'%'
name|'shelf_blade'
op|')'
newline|'\n'
dedent|''
name|'deferreds'
op|'='
op|'['
op|']'
newline|'\n'
name|'total_slots'
op|'='
name|'FLAGS'
op|'.'
name|'num_shelves'
op|'*'
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'total_slots'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'_check'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'self'
op|'.'
name|'fail'
op|')'
newline|'\n'
name|'deferreds'
op|'.'
name|'append'
op|'('
name|'d'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'defer'
op|'.'
name|'DeferredList'
op|'('
name|'deferreds'
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multi_node
dedent|''
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
