begin_unit
comment|'# Copyright 2015 NEC Corporation.  All rights reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'paths'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiPasteV21Fixture
name|'class'
name|'ApiPasteV21Fixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_replace_line
indent|'    '
name|'def'
name|'_replace_line'
op|'('
name|'self'
op|','
name|'target_file'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
comment|'# TODO(johnthetubaguy) should really point the tests at /v2.1'
nl|'\n'
indent|'        '
name|'target_file'
op|'.'
name|'write'
op|'('
name|'line'
op|'.'
name|'replace'
op|'('
nl|'\n'
string|'"/v2: openstack_compute_api_v21_legacy_v2_compatible"'
op|','
nl|'\n'
string|'"/v2: openstack_compute_api_v21"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ApiPasteV21Fixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|"'api_paste_config'"
op|','
nl|'\n'
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'etc/nova/api-paste.ini'"
op|')'
op|','
nl|'\n'
name|'group'
op|'='
string|"'wsgi'"
op|')'
newline|'\n'
name|'tmp_api_paste_dir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
newline|'\n'
name|'tmp_api_paste_file_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmp_api_paste_dir'
op|'.'
name|'path'
op|','
nl|'\n'
string|"'fake_api_paste.ini'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'CONF'
op|'.'
name|'wsgi'
op|'.'
name|'api_paste_config'
op|','
string|"'r'"
op|')'
name|'as'
name|'orig_api_paste'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'tmp_api_paste_file_name'
op|','
string|"'w'"
op|')'
name|'as'
name|'tmp_file'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'line'
name|'in'
name|'orig_api_paste'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_replace_line'
op|'('
name|'tmp_file'
op|','
name|'line'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'api_paste_config'"
op|','
name|'tmp_api_paste_file_name'
op|','
nl|'\n'
name|'group'
op|'='
string|"'wsgi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiPasteLegacyV2Fixture
dedent|''
dedent|''
name|'class'
name|'ApiPasteLegacyV2Fixture'
op|'('
name|'ApiPasteV21Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_replace_line
indent|'    '
name|'def'
name|'_replace_line'
op|'('
name|'self'
op|','
name|'target_file'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(johnthetubaguy) this is hack so we test the legacy_v2 code'
nl|'\n'
comment|'# even though its disable by default in api-paste.ini'
nl|'\n'
indent|'        '
name|'line'
op|'='
name|'line'
op|'.'
name|'replace'
op|'('
nl|'\n'
string|'"/v2: openstack_compute_api_v21_legacy_v2_compatible"'
op|','
nl|'\n'
string|'"/v2: openstack_compute_api_legacy_v2"'
op|')'
newline|'\n'
name|'target_file'
op|'.'
name|'write'
op|'('
name|'line'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiPasteNoProjectId
dedent|''
dedent|''
name|'class'
name|'ApiPasteNoProjectId'
op|'('
name|'ApiPasteV21Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_replace_line
indent|'    '
name|'def'
name|'_replace_line'
op|'('
name|'self'
op|','
name|'target_file'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'line'
op|'='
name|'line'
op|'.'
name|'replace'
op|'('
nl|'\n'
string|'"paste.filter_factory = nova.api.openstack.auth:"'
nl|'\n'
string|'"NoAuthMiddleware.factory"'
op|','
nl|'\n'
string|'"paste.filter_factory = nova.api.openstack.auth:"'
nl|'\n'
string|'"NoAuthMiddlewareV2_18.factory"'
op|')'
newline|'\n'
name|'target_file'
op|'.'
name|'write'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
