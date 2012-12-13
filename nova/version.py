begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
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
DECL|variable|NOVA_VENDOR
name|'NOVA_VENDOR'
op|'='
string|'"OpenStack Foundation"'
newline|'\n'
DECL|variable|NOVA_PRODUCT
name|'NOVA_PRODUCT'
op|'='
string|'"OpenStack Nova"'
newline|'\n'
DECL|variable|NOVA_PACKAGE
name|'NOVA_PACKAGE'
op|'='
name|'None'
comment|'# OS distro package version suffix'
newline|'\n'
DECL|variable|NOVA_VERSION
name|'NOVA_VERSION'
op|'='
op|'['
string|"'2013'"
op|','
string|"'1'"
op|','
name|'None'
op|']'
newline|'\n'
name|'YEAR'
op|','
name|'COUNT'
op|','
name|'REVISION'
op|'='
name|'NOVA_VERSION'
newline|'\n'
DECL|variable|FINAL
name|'FINAL'
op|'='
name|'False'
comment|'# This becomes true at Release Candidate time'
newline|'\n'
nl|'\n'
DECL|variable|loaded
name|'loaded'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_load_config
name|'def'
name|'_load_config'
op|'('
op|')'
op|':'
newline|'\n'
comment|"# Don't load in global context, since we can't assume"
nl|'\n'
comment|'# these modules are accessible when distutils uses'
nl|'\n'
comment|'# this module'
nl|'\n'
indent|'    '
name|'import'
name|'ConfigParser'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'global'
name|'loaded'
op|','
name|'NOVA_VENDOR'
op|','
name|'NOVA_PRODUCT'
op|','
name|'NOVA_PACKAGE'
newline|'\n'
name|'if'
name|'loaded'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'loaded'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'cfgfile'
op|'='
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'find_file'
op|'('
string|'"release"'
op|')'
newline|'\n'
name|'if'
name|'cfgfile'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'cfg'
op|'='
name|'ConfigParser'
op|'.'
name|'RawConfigParser'
op|'('
op|')'
newline|'\n'
name|'cfg'
op|'.'
name|'read'
op|'('
name|'cfgfile'
op|')'
newline|'\n'
nl|'\n'
name|'NOVA_VENDOR'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"Nova"'
op|','
string|'"vendor"'
op|')'
newline|'\n'
name|'if'
name|'cfg'
op|'.'
name|'has_option'
op|'('
string|'"Nova"'
op|','
string|'"vendor"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'NOVA_VENDOR'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"Nova"'
op|','
string|'"vendor"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'NOVA_PRODUCT'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"Nova"'
op|','
string|'"product"'
op|')'
newline|'\n'
name|'if'
name|'cfg'
op|'.'
name|'has_option'
op|'('
string|'"Nova"'
op|','
string|'"product"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'NOVA_PRODUCT'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"Nova"'
op|','
string|'"product"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'NOVA_PACKAGE'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"Nova"'
op|','
string|'"package"'
op|')'
newline|'\n'
name|'if'
name|'cfg'
op|'.'
name|'has_option'
op|'('
string|'"Nova"'
op|','
string|'"package"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'NOVA_PACKAGE'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"Nova"'
op|','
string|'"package"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"Failed to load %(cfgfile)s: %(ex)s"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vendor_string
dedent|''
dedent|''
name|'def'
name|'vendor_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_load_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'NOVA_VENDOR'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|product_string
dedent|''
name|'def'
name|'product_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_load_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'NOVA_PRODUCT'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|package_string
dedent|''
name|'def'
name|'package_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_load_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'NOVA_PACKAGE'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|canonical_version_string
dedent|''
name|'def'
name|'canonical_version_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'.'"
op|'.'
name|'join'
op|'('
name|'filter'
op|'('
name|'None'
op|','
name|'NOVA_VERSION'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|version_string
dedent|''
name|'def'
name|'version_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FINAL'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'canonical_version_string'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'%s-dev'"
op|'%'
op|'('
name|'canonical_version_string'
op|'('
op|')'
op|','
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|version_string_with_package
dedent|''
dedent|''
name|'def'
name|'version_string_with_package'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'package_string'
op|'('
op|')'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'canonical_version_string'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s-%s"'
op|'%'
op|'('
name|'canonical_version_string'
op|'('
op|')'
op|','
name|'package_string'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
