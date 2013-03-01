begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMConnectionFailed
name|'class'
name|'PowerVMConnectionFailed'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|"'Connection to PowerVM manager failed'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMFileTransferFailed
dedent|''
name|'class'
name|'PowerVMFileTransferFailed'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"File \'%(file_path)s\' transfer to PowerVM manager failed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMFTPTransferFailed
dedent|''
name|'class'
name|'PowerVMFTPTransferFailed'
op|'('
name|'PowerVMFileTransferFailed'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"FTP %(ftp_cmd)s from %(source_path)s to %(dest_path)s failed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMLPARInstanceNotFound
dedent|''
name|'class'
name|'PowerVMLPARInstanceNotFound'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LPAR instance \'%(instance_name)s\' could not be found"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMLPARCreationFailed
dedent|''
name|'class'
name|'PowerVMLPARCreationFailed'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LPAR instance \'%(instance_name)s\' creation failed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMNoSpaceLeftOnVolumeGroup
dedent|''
name|'class'
name|'PowerVMNoSpaceLeftOnVolumeGroup'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"No space left on any volume group"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMLPARAttributeNotFound
dedent|''
name|'class'
name|'PowerVMLPARAttributeNotFound'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMLPAROperationTimeout
dedent|''
name|'class'
name|'PowerVMLPAROperationTimeout'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Operation \'%(operation)s\' on "'
nl|'\n'
string|'"LPAR \'%(instance_name)s\' timed out"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMImageCreationFailed
dedent|''
name|'class'
name|'PowerVMImageCreationFailed'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Image creation failed on PowerVM"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMInsufficientFreeMemory
dedent|''
name|'class'
name|'PowerVMInsufficientFreeMemory'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Insufficient free memory on PowerVM system to spawn instance "'
nl|'\n'
string|'"\'%(instance_name)s\'"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMInsufficientCPU
dedent|''
name|'class'
name|'PowerVMInsufficientCPU'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Insufficient available CPUs on PowerVM system to spawn "'
nl|'\n'
string|'"instance \'%(instance_name)s\'"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMLPARInstanceCleanupFailed
dedent|''
name|'class'
name|'PowerVMLPARInstanceCleanupFailed'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"PowerVM LPAR instance \'%(instance_name)s\' cleanup failed"'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
