begin_unit
comment|'# Copyright 2013 Canonical Ltd'
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
string|'"""Render Vendordata as stored in configured file."""'
newline|'\n'
nl|'\n'
name|'import'
name|'errno'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|file_opt
name|'file_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vendordata_jsonfile_path'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'File to load json formatted vendor data from'"
op|')'
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
name|'register_opt'
op|'('
name|'file_opt'
op|')'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JsonFileVendorData
name|'class'
name|'JsonFileVendorData'
op|'('
name|'base'
op|'.'
name|'VendorDataDriver'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
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
name|'super'
op|'('
name|'JsonFileVendorData'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fpath'
op|'='
name|'CONF'
op|'.'
name|'vendordata_jsonfile_path'
newline|'\n'
name|'logprefix'
op|'='
string|'"%s[%s]: "'
op|'%'
op|'('
name|'file_opt'
op|'.'
name|'name'
op|','
name|'fpath'
op|')'
newline|'\n'
name|'if'
name|'fpath'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'open'
op|'('
name|'fpath'
op|','
string|'"r"'
op|')'
name|'as'
name|'fp'
op|':'
newline|'\n'
indent|'                    '
name|'data'
op|'='
name|'jsonutils'
op|'.'
name|'load'
op|'('
name|'fp'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'IOError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'logprefix'
op|'+'
name|'_'
op|'('
string|'"file does not exist"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'logprefix'
op|'+'
name|'_'
op|'('
string|'"Unexpected IOError when reading"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'e'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'logprefix'
op|'+'
name|'_'
op|'('
string|'"failed to load json"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_data'
op|'='
name|'data'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
