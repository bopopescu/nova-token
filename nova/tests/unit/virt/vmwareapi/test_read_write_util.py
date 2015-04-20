begin_unit
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'requests'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'read_write_util'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
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
DECL|class|ReadWriteUtilTestCase
name|'class'
name|'ReadWriteUtilTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'requests'
op|'.'
name|'api'
op|','
string|"'request'"
op|')'
newline|'\n'
DECL|member|test_ipv6_host_read
name|'def'
name|'test_ipv6_host_read'
op|'('
name|'self'
op|','
name|'mock_request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ipv6_host'
op|'='
string|"'fd8c:215d:178e:c51e:200:c9ff:fed1:584c'"
newline|'\n'
name|'port'
op|'='
number|'7443'
newline|'\n'
name|'folder'
op|'='
string|"'tmp/fake.txt'"
newline|'\n'
name|'read_write_util'
op|'.'
name|'VMwareHTTPReadFile'
op|'('
name|'ipv6_host'
op|','
nl|'\n'
name|'port'
op|','
nl|'\n'
string|"'fake_dc'"
op|','
nl|'\n'
string|"'fake_ds'"
op|','
nl|'\n'
name|'dict'
op|'('
op|')'
op|','
nl|'\n'
name|'folder'
op|')'
newline|'\n'
name|'param_list'
op|'='
op|'{'
string|'"dcPath"'
op|':'
string|"'fake_dc'"
op|','
string|'"dsName"'
op|':'
string|"'fake_ds'"
op|'}'
newline|'\n'
name|'base_url'
op|'='
string|"'https://[%s]:%s/folder/%s'"
op|'%'
op|'('
name|'ipv6_host'
op|','
name|'port'
op|','
name|'folder'
op|')'
newline|'\n'
name|'base_url'
op|'+='
string|"'?'"
op|'+'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'param_list'
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
string|"'User-Agent'"
op|':'
string|"'OpenStack-ESX-Adapter'"
op|'}'
newline|'\n'
name|'mock_request'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'get'"
op|','
nl|'\n'
name|'base_url'
op|','
nl|'\n'
name|'headers'
op|'='
name|'headers'
op|','
nl|'\n'
name|'allow_redirects'
op|'='
name|'True'
op|','
nl|'\n'
name|'stream'
op|'='
name|'True'
op|','
nl|'\n'
name|'verify'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
