begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'v3'
name|'import'
name|'test_servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
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
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AssistedVolumeSnapshotsJsonTests
name|'class'
name|'AssistedVolumeSnapshotsJsonTests'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-assisted-volume-snapshots"'
newline|'\n'
comment|"# TODO(gmann): Overriding '_api_version' till all functional tests"
nl|'\n'
comment|'# are merged between v2 and v2.1. After that base class variable'
nl|'\n'
comment|"# itself can be changed to 'v2'"
nl|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'AssistedVolumeSnapshotsJsonTests'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'assisted_volume_snapshots.Assisted_volume_snapshots'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a volume snapshots."""'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'volume_snapshot_create'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_compute_volume_snapshot_create'
op|')'
newline|'\n'
nl|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
string|"'521752a6-acf6-4b2d-bc7a-119f9148cd8c'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'421752a6-acf6-4b2d-bc7a-119f9148cd8c'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'qcow2'"
op|','
nl|'\n'
string|"'new_file'"
op|':'
string|"'new_file_name'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|'"os-assisted-volume-snapshots"'
op|','
nl|'\n'
string|'"snapshot-create-assisted-req"'
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|'"snapshot-create-assisted-resp"'
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshots_delete_assisted
dedent|''
name|'def'
name|'test_snapshots_delete_assisted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'volume_snapshot_delete'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_compute_volume_snapshot_delete'
op|')'
newline|'\n'
nl|'\n'
name|'snapshot_id'
op|'='
string|"'100'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
nl|'\n'
string|"'os-assisted-volume-snapshots/%s?delete_info='"
nl|'\n'
string|'\'{"volume_id":"521752a6-acf6-4b2d-bc7a-119f9148cd8c"}\''
nl|'\n'
op|'%'
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'204'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
