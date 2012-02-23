begin_unit
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
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'Integer'
op|','
name|'MetaData'
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
comment|"# Upgrade operations go here. Don't create your own engine;"
nl|'\n'
comment|'# bind migrate_engine to your metadata'
nl|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'fixed_ips'
op|'='
name|'Table'
op|'('
string|"'fixed_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# New Columns'
nl|'\n'
comment|'#'
nl|'\n'
name|'fixed_ips_addressV6'
op|'='
name|'Column'
op|'('
nl|'\n'
string|'"addressV6"'
op|','
nl|'\n'
name|'String'
op|'('
nl|'\n'
name|'length'
op|'='
number|'255'
op|','
nl|'\n'
name|'convert_unicode'
op|'='
name|'False'
op|','
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ips_netmaskV6'
op|'='
name|'Column'
op|'('
nl|'\n'
string|'"netmaskV6"'
op|','
nl|'\n'
name|'String'
op|'('
nl|'\n'
name|'length'
op|'='
number|'3'
op|','
nl|'\n'
name|'convert_unicode'
op|'='
name|'False'
op|','
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ips_gatewayV6'
op|'='
name|'Column'
op|'('
nl|'\n'
string|'"gatewayV6"'
op|','
nl|'\n'
name|'String'
op|'('
nl|'\n'
name|'length'
op|'='
number|'255'
op|','
nl|'\n'
name|'convert_unicode'
op|'='
name|'False'
op|','
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
comment|'# Add columns to existing tables'
nl|'\n'
name|'fixed_ips'
op|'.'
name|'create_column'
op|'('
name|'fixed_ips_addressV6'
op|')'
newline|'\n'
name|'fixed_ips'
op|'.'
name|'create_column'
op|'('
name|'fixed_ips_netmaskV6'
op|')'
newline|'\n'
name|'fixed_ips'
op|'.'
name|'create_column'
op|'('
name|'fixed_ips_gatewayV6'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'fixed_ips'
op|'='
name|'Table'
op|'('
string|"'fixed_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ips'
op|'.'
name|'drop_column'
op|'('
string|"'addressV6'"
op|')'
newline|'\n'
name|'fixed_ips'
op|'.'
name|'drop_column'
op|'('
string|"'netmaskV6'"
op|')'
newline|'\n'
name|'fixed_ips'
op|'.'
name|'drop_column'
op|'('
string|"'gatewayV6'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
