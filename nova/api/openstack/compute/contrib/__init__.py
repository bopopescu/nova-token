begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""Contrib contains extensions that are shipped with nova.\n\nIt can\'t be called \'extensions\' because that causes namespacing problems.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
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
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
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
DECL|function|standard_extensions
name|'def'
name|'standard_extensions'
op|'('
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'extensions'
op|'.'
name|'load_standard_extensions'
op|'('
name|'ext_mgr'
op|','
name|'LOG'
op|','
name|'__path__'
op|','
name|'__package__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|select_extensions
dedent|''
name|'def'
name|'select_extensions'
op|'('
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'extensions'
op|'.'
name|'load_standard_extensions'
op|'('
name|'ext_mgr'
op|','
name|'LOG'
op|','
name|'__path__'
op|','
name|'__package__'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'osapi_compute_ext_list'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
