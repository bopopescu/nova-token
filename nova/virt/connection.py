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
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'libvirt_conn'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'xenapi'
newline|'\n'
nl|'\n'
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
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'read_only'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): maybe lazy load after initial check for permissions'
nl|'\n'
comment|'# TODO(termie): check whether we can be disconnected'
nl|'\n'
indent|'    '
name|'t'
op|'='
name|'FLAGS'
op|'.'
name|'connection_type'
newline|'\n'
name|'if'
name|'t'
op|'=='
string|"'fake'"
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'='
name|'fake'
op|'.'
name|'get_connection'
op|'('
name|'read_only'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'t'
op|'=='
string|"'libvirt'"
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'='
name|'libvirt_conn'
op|'.'
name|'get_connection'
op|'('
name|'read_only'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'t'
op|'=='
string|"'xenapi'"
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'='
name|'xenapi'
op|'.'
name|'get_connection'
op|'('
name|'read_only'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'\'Unknown connection type "%s"\''
op|'%'
name|'t'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'conn'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
string|"'Failed to open connection to the hypervisor'"
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'conn'
newline|'\n'
dedent|''
endmarker|''
end_unit
