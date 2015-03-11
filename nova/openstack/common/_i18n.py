begin_unit
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
string|'"""oslo.i18n integration module.\n\nSee http://docs.openstack.org/developer/oslo.i18n/usage.html\n\n"""'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'oslo_i18n'
newline|'\n'
nl|'\n'
comment|'# NOTE(dhellmann): This reference to o-s-l-o will be replaced by the'
nl|'\n'
comment|'# application name when this module is synced into the separate'
nl|'\n'
comment|'# repository. It is OK to have more than one translation function'
nl|'\n'
comment|'# using the same domain, since there will still only be one message'
nl|'\n'
comment|'# catalog.'
nl|'\n'
DECL|variable|_translators
name|'_translators'
op|'='
name|'oslo_i18n'
op|'.'
name|'TranslatorFactory'
op|'('
name|'domain'
op|'='
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
comment|'# The primary translation function using the well-known name "_"'
nl|'\n'
DECL|variable|_
name|'_'
op|'='
name|'_translators'
op|'.'
name|'primary'
newline|'\n'
nl|'\n'
comment|'# Translators for log levels.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The abbreviated names are meant to reflect the usual use of a short'
nl|'\n'
comment|'# name like \'_\'. The "L" is for "log" and the other letter comes from'
nl|'\n'
comment|'# the level.'
nl|'\n'
DECL|variable|_LI
name|'_LI'
op|'='
name|'_translators'
op|'.'
name|'log_info'
newline|'\n'
DECL|variable|_LW
name|'_LW'
op|'='
name|'_translators'
op|'.'
name|'log_warning'
newline|'\n'
DECL|variable|_LE
name|'_LE'
op|'='
name|'_translators'
op|'.'
name|'log_error'
newline|'\n'
DECL|variable|_LC
name|'_LC'
op|'='
name|'_translators'
op|'.'
name|'log_critical'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
comment|'# NOTE(dims): Support for cases where a project wants to use'
nl|'\n'
comment|'# code from oslo-incubator, but is not ready to be internationalized'
nl|'\n'
comment|'# (like tempest)'
nl|'\n'
indent|'    '
name|'_'
op|'='
name|'_LI'
op|'='
name|'_LW'
op|'='
name|'_LE'
op|'='
name|'_LC'
op|'='
name|'lambda'
name|'x'
op|':'
name|'x'
newline|'\n'
dedent|''
endmarker|''
end_unit
