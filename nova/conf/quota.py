begin_unit
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
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|quota_opts
name|'quota_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_instances'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of instances allowed per project'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_cores'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'20'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of instance cores allowed per project'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_ram'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'50'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Megabytes of instance RAM allowed per project'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_floating_ips'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of floating IPs allowed per project'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_fixed_ips'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of fixed IPs allowed per project (this should be '"
nl|'\n'
string|"'at least the number of instances allowed)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_metadata_items'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'128'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of metadata items allowed per instance'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_injected_files'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of injected files allowed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_injected_file_content_bytes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of bytes allowed per injected file'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_injected_file_path_length'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'255'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Length of injected file path'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_security_groups'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of security groups per project'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_security_group_rules'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'20'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of security rules per security group'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_key_pairs'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'100'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of key pairs per user'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_server_groups'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of server groups per project'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quota_server_group_members'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of servers per server group'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reservation_expire'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'86400'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds until a reservation expires'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'until_refresh'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Count of reservations until usage is refreshed. This '"
nl|'\n'
string|"'defaults to 0(off) to avoid additional load but it is '"
nl|'\n'
string|"'useful to turn on to help keep quota usage up to date '"
nl|'\n'
string|"'and reduce the impact of out of sync usage issues.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_age'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds between subsequent usage refreshes. '"
nl|'\n'
string|"'This defaults to 0(off) to avoid additional load but it '"
nl|'\n'
string|"'is useful to turn on to help keep quota usage up to date '"
nl|'\n'
string|"'and reduce the impact of out of sync usage issues. '"
nl|'\n'
string|"'Note that quotas are not updated on a periodic task, '"
nl|'\n'
string|"'they will update on a new reservation if max_age has '"
nl|'\n'
string|"'passed since the last reservation'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quota_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.quota.DbQuotaDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default driver to use for quota checks'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'quota_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'DEFAULT'"
op|':'
name|'quota_opts'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
