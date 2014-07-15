begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
string|'"""\nUtility class for VHD related operations.\nBased on the "root/virtualization/v2" namespace available starting with\nHyper-V Server / Windows Server 2012.\n"""'
newline|'\n'
name|'import'
name|'struct'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'wmi'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'xml'
op|'.'
name|'etree'
name|'import'
name|'ElementTree'
newline|'\n'
nl|'\n'
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
name|'units'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vhdutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutilsv2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|VHDX_BAT_ENTRY_SIZE
name|'VHDX_BAT_ENTRY_SIZE'
op|'='
number|'8'
newline|'\n'
DECL|variable|VHDX_HEADER_OFFSETS
name|'VHDX_HEADER_OFFSETS'
op|'='
op|'['
number|'64'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|','
number|'128'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|']'
newline|'\n'
DECL|variable|VHDX_HEADER_SECTION_SIZE
name|'VHDX_HEADER_SECTION_SIZE'
op|'='
name|'units'
op|'.'
name|'Mi'
newline|'\n'
DECL|variable|VHDX_LOG_LENGTH_OFFSET
name|'VHDX_LOG_LENGTH_OFFSET'
op|'='
number|'68'
newline|'\n'
DECL|variable|VHDX_METADATA_SIZE_OFFSET
name|'VHDX_METADATA_SIZE_OFFSET'
op|'='
number|'64'
newline|'\n'
DECL|variable|VHDX_REGION_TABLE_OFFSET
name|'VHDX_REGION_TABLE_OFFSET'
op|'='
number|'192'
op|'*'
name|'units'
op|'.'
name|'Ki'
newline|'\n'
DECL|variable|VHDX_BS_METADATA_ENTRY_OFFSET
name|'VHDX_BS_METADATA_ENTRY_OFFSET'
op|'='
number|'48'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VHDUtilsV2
name|'class'
name|'VHDUtilsV2'
op|'('
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_VHD_TYPE_DYNAMIC
indent|'    '
name|'_VHD_TYPE_DYNAMIC'
op|'='
number|'3'
newline|'\n'
DECL|variable|_VHD_TYPE_DIFFERENCING
name|'_VHD_TYPE_DIFFERENCING'
op|'='
number|'4'
newline|'\n'
nl|'\n'
DECL|variable|_vhd_format_map
name|'_vhd_format_map'
op|'='
op|'{'
nl|'\n'
name|'constants'
op|'.'
name|'DISK_FORMAT_VHD'
op|':'
number|'2'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'DISK_FORMAT_VHDX'
op|':'
number|'3'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|'('
op|')'
newline|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conn'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
name|'moniker'
op|'='
string|"'//./root/virtualization/v2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_dynamic_vhd
dedent|''
dedent|''
name|'def'
name|'create_dynamic_vhd'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'max_internal_size'
op|','
name|'format'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vhd_format'
op|'='
name|'self'
op|'.'
name|'_vhd_format_map'
op|'.'
name|'get'
op|'('
name|'format'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'vhd_format'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Unsupported disk format: %s"'
op|')'
op|'%'
nl|'\n'
name|'format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_create_vhd'
op|'('
name|'self'
op|'.'
name|'_VHD_TYPE_DYNAMIC'
op|','
name|'vhd_format'
op|','
name|'path'
op|','
nl|'\n'
name|'max_internal_size'
op|'='
name|'max_internal_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_differencing_vhd
dedent|''
name|'def'
name|'create_differencing_vhd'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'parent_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parent_vhd_info'
op|'='
name|'self'
op|'.'
name|'get_vhd_info'
op|'('
name|'parent_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_vhd'
op|'('
name|'self'
op|'.'
name|'_VHD_TYPE_DIFFERENCING'
op|','
nl|'\n'
name|'parent_vhd_info'
op|'['
string|'"Format"'
op|']'
op|','
nl|'\n'
name|'path'
op|','
name|'parent_path'
op|'='
name|'parent_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_vhd
dedent|''
name|'def'
name|'_create_vhd'
op|'('
name|'self'
op|','
name|'vhd_type'
op|','
name|'format'
op|','
name|'path'
op|','
name|'max_internal_size'
op|'='
name|'None'
op|','
nl|'\n'
name|'parent_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vhd_info'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualHardDiskSettingData'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vhd_info'
op|'.'
name|'Type'
op|'='
name|'vhd_type'
newline|'\n'
name|'vhd_info'
op|'.'
name|'Format'
op|'='
name|'format'
newline|'\n'
name|'vhd_info'
op|'.'
name|'Path'
op|'='
name|'path'
newline|'\n'
name|'vhd_info'
op|'.'
name|'ParentPath'
op|'='
name|'parent_path'
newline|'\n'
nl|'\n'
name|'if'
name|'max_internal_size'
op|':'
newline|'\n'
indent|'            '
name|'vhd_info'
op|'.'
name|'MaxInternalSize'
op|'='
name|'max_internal_size'
newline|'\n'
nl|'\n'
dedent|''
name|'image_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ImageManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'image_man_svc'
op|'.'
name|'CreateVirtualHardDisk'
op|'('
nl|'\n'
name|'VirtualDiskSettingData'
op|'='
name|'vhd_info'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reconnect_parent_vhd
dedent|''
name|'def'
name|'reconnect_parent_vhd'
op|'('
name|'self'
op|','
name|'child_vhd_path'
op|','
name|'parent_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ImageManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vhd_info_xml'
op|'='
name|'self'
op|'.'
name|'_get_vhd_info_xml'
op|'('
name|'image_man_svc'
op|','
name|'child_vhd_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Can\'t use ".//PROPERTY[@NAME=\'ParentPath\']/VALUE" due to'
nl|'\n'
comment|'# compatibility requirements with Python 2.6'
nl|'\n'
name|'et'
op|'='
name|'ElementTree'
op|'.'
name|'fromstring'
op|'('
name|'vhd_info_xml'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'et'
op|'.'
name|'findall'
op|'('
string|'"PROPERTY"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'item'
op|'.'
name|'attrib'
op|'['
string|'"NAME"'
op|']'
newline|'\n'
name|'if'
name|'name'
op|'=='
string|"'ParentPath'"
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'.'
name|'find'
op|'('
string|'"VALUE"'
op|')'
op|'.'
name|'text'
op|'='
name|'parent_vhd_path'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'vhd_info_xml'
op|'='
name|'ElementTree'
op|'.'
name|'tostring'
op|'('
name|'et'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'image_man_svc'
op|'.'
name|'SetVirtualHardDiskSettingData'
op|'('
nl|'\n'
name|'VirtualDiskSettingData'
op|'='
name|'vhd_info_xml'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_resize_method
dedent|''
name|'def'
name|'_get_resize_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ImageManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'image_man_svc'
op|'.'
name|'ResizeVirtualHardDisk'
newline|'\n'
nl|'\n'
DECL|member|get_internal_vhd_size_by_file_size
dedent|''
name|'def'
name|'get_internal_vhd_size_by_file_size'
op|'('
name|'self'
op|','
name|'vhd_path'
op|','
nl|'\n'
name|'new_vhd_file_size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""VHDX Size = Header (1 MB)\n                        + Log\n                        + Metadata Region\n                        + BAT\n                        + Payload Blocks\n            Chunk size = maximum number of bytes described by a SB block\n                       = 2 ** 23 * LogicalSectorSize\n        """'
newline|'\n'
name|'vhd_format'
op|'='
name|'self'
op|'.'
name|'get_vhd_format'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
name|'if'
name|'vhd_format'
op|'=='
name|'constants'
op|'.'
name|'DISK_FORMAT_VHD'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'super'
op|'('
name|'VHDUtilsV2'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_internal_vhd_size_by_file_size'
op|'('
nl|'\n'
name|'vhd_path'
op|','
name|'new_vhd_file_size'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'vhd_info'
op|'='
name|'self'
op|'.'
name|'get_vhd_info'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
name|'vhd_type'
op|'='
name|'vhd_info'
op|'['
string|"'Type'"
op|']'
newline|'\n'
name|'if'
name|'vhd_type'
op|'=='
name|'self'
op|'.'
name|'_VHD_TYPE_DIFFERENCING'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Differencing VHDX images "'
nl|'\n'
string|'"are not supported"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'with'
name|'open'
op|'('
name|'vhd_path'
op|','
string|"'rb'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                        '
name|'hs'
op|'='
name|'VHDX_HEADER_SECTION_SIZE'
newline|'\n'
name|'bes'
op|'='
name|'VHDX_BAT_ENTRY_SIZE'
newline|'\n'
nl|'\n'
name|'lss'
op|'='
name|'vhd_info'
op|'['
string|"'LogicalSectorSize'"
op|']'
newline|'\n'
name|'bs'
op|'='
name|'self'
op|'.'
name|'_get_vhdx_block_size'
op|'('
name|'f'
op|')'
newline|'\n'
name|'ls'
op|'='
name|'self'
op|'.'
name|'_get_vhdx_log_size'
op|'('
name|'f'
op|')'
newline|'\n'
name|'ms'
op|'='
name|'self'
op|'.'
name|'_get_vhdx_metadata_size_and_offset'
op|'('
name|'f'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'chunk_ratio'
op|'='
op|'('
number|'1'
op|'<<'
number|'23'
op|')'
op|'*'
name|'lss'
op|'/'
name|'bs'
newline|'\n'
name|'size'
op|'='
name|'new_vhd_file_size'
newline|'\n'
nl|'\n'
name|'max_internal_size'
op|'='
op|'('
name|'bs'
op|'*'
name|'chunk_ratio'
op|'*'
op|'('
name|'size'
op|'-'
name|'hs'
op|'-'
nl|'\n'
name|'ls'
op|'-'
name|'ms'
op|'-'
name|'bes'
op|'-'
name|'bes'
op|'/'
name|'chunk_ratio'
op|')'
op|'/'
op|'('
name|'bs'
op|'*'
nl|'\n'
name|'chunk_ratio'
op|'+'
name|'bes'
op|'*'
name|'chunk_ratio'
op|'+'
name|'bes'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'max_internal_size'
op|'-'
op|'('
name|'max_internal_size'
op|'%'
name|'bs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'IOError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Unable to obtain "'
nl|'\n'
string|'"internal size from VHDX: "'
nl|'\n'
string|'"%(vhd_path)s. Exception: "'
nl|'\n'
string|'"%(ex)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|'"vhd_path"'
op|':'
name|'vhd_path'
op|','
nl|'\n'
string|'"ex"'
op|':'
name|'ex'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vhdx_current_header_offset
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_vhdx_current_header_offset'
op|'('
name|'self'
op|','
name|'vhdx_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sequence_numbers'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'offset'
name|'in'
name|'VHDX_HEADER_OFFSETS'
op|':'
newline|'\n'
indent|'            '
name|'vhdx_file'
op|'.'
name|'seek'
op|'('
name|'offset'
op|'+'
number|'8'
op|')'
newline|'\n'
name|'sequence_numbers'
op|'.'
name|'append'
op|'('
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'<Q'"
op|','
nl|'\n'
name|'vhdx_file'
op|'.'
name|'read'
op|'('
number|'8'
op|')'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'current_header'
op|'='
name|'sequence_numbers'
op|'.'
name|'index'
op|'('
name|'max'
op|'('
name|'sequence_numbers'
op|')'
op|')'
newline|'\n'
name|'return'
name|'VHDX_HEADER_OFFSETS'
op|'['
name|'current_header'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_vhdx_log_size
dedent|''
name|'def'
name|'_get_vhdx_log_size'
op|'('
name|'self'
op|','
name|'vhdx_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_header_offset'
op|'='
name|'self'
op|'.'
name|'_get_vhdx_current_header_offset'
op|'('
name|'vhdx_file'
op|')'
newline|'\n'
name|'offset'
op|'='
name|'current_header_offset'
op|'+'
name|'VHDX_LOG_LENGTH_OFFSET'
newline|'\n'
name|'vhdx_file'
op|'.'
name|'seek'
op|'('
name|'offset'
op|')'
newline|'\n'
name|'log_size'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'<I'"
op|','
name|'vhdx_file'
op|'.'
name|'read'
op|'('
number|'4'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'log_size'
newline|'\n'
nl|'\n'
DECL|member|_get_vhdx_metadata_size_and_offset
dedent|''
name|'def'
name|'_get_vhdx_metadata_size_and_offset'
op|'('
name|'self'
op|','
name|'vhdx_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'offset'
op|'='
name|'VHDX_METADATA_SIZE_OFFSET'
op|'+'
name|'VHDX_REGION_TABLE_OFFSET'
newline|'\n'
name|'vhdx_file'
op|'.'
name|'seek'
op|'('
name|'offset'
op|')'
newline|'\n'
name|'metadata_offset'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'<Q'"
op|','
name|'vhdx_file'
op|'.'
name|'read'
op|'('
number|'8'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'metadata_size'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'<I'"
op|','
name|'vhdx_file'
op|'.'
name|'read'
op|'('
number|'4'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'metadata_size'
op|','
name|'metadata_offset'
newline|'\n'
nl|'\n'
DECL|member|_get_vhdx_block_size
dedent|''
name|'def'
name|'_get_vhdx_block_size'
op|'('
name|'self'
op|','
name|'vhdx_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata_offset'
op|'='
name|'self'
op|'.'
name|'_get_vhdx_metadata_size_and_offset'
op|'('
name|'vhdx_file'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'offset'
op|'='
name|'metadata_offset'
op|'+'
name|'VHDX_BS_METADATA_ENTRY_OFFSET'
newline|'\n'
name|'vhdx_file'
op|'.'
name|'seek'
op|'('
name|'offset'
op|')'
newline|'\n'
name|'file_parameter_offset'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'<I'"
op|','
name|'vhdx_file'
op|'.'
name|'read'
op|'('
number|'4'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'vhdx_file'
op|'.'
name|'seek'
op|'('
name|'file_parameter_offset'
op|'+'
name|'metadata_offset'
op|')'
newline|'\n'
name|'block_size'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'<I'"
op|','
name|'vhdx_file'
op|'.'
name|'read'
op|'('
number|'4'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'block_size'
newline|'\n'
nl|'\n'
DECL|member|_get_vhd_info_xml
dedent|''
name|'def'
name|'_get_vhd_info_xml'
op|'('
name|'self'
op|','
name|'image_man_svc'
op|','
name|'vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'job_path'
op|','
nl|'\n'
name|'ret_val'
op|','
nl|'\n'
name|'vhd_info_xml'
op|')'
op|'='
name|'image_man_svc'
op|'.'
name|'GetVirtualHardDiskSettingData'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'vhd_info_xml'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|','
string|"'xmlcharrefreplace'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vhd_info
dedent|''
name|'def'
name|'get_vhd_info'
op|'('
name|'self'
op|','
name|'vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ImageManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vhd_info_xml'
op|'='
name|'self'
op|'.'
name|'_get_vhd_info_xml'
op|'('
name|'image_man_svc'
op|','
name|'vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'vhd_info_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'et'
op|'='
name|'ElementTree'
op|'.'
name|'fromstring'
op|'('
name|'vhd_info_xml'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'et'
op|'.'
name|'findall'
op|'('
string|'"PROPERTY"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'item'
op|'.'
name|'attrib'
op|'['
string|'"NAME"'
op|']'
newline|'\n'
name|'value_text'
op|'='
name|'item'
op|'.'
name|'find'
op|'('
string|'"VALUE"'
op|')'
op|'.'
name|'text'
newline|'\n'
name|'if'
name|'name'
name|'in'
op|'['
string|'"Path"'
op|','
string|'"ParentPath"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'vhd_info_dict'
op|'['
name|'name'
op|']'
op|'='
name|'value_text'
newline|'\n'
dedent|''
name|'elif'
name|'name'
name|'in'
op|'['
string|'"BlockSize"'
op|','
string|'"LogicalSectorSize"'
op|','
nl|'\n'
string|'"PhysicalSectorSize"'
op|','
string|'"MaxInternalSize"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'vhd_info_dict'
op|'['
name|'name'
op|']'
op|'='
name|'long'
op|'('
name|'value_text'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
name|'in'
op|'['
string|'"Type"'
op|','
string|'"Format"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'vhd_info_dict'
op|'['
name|'name'
op|']'
op|'='
name|'int'
op|'('
name|'value_text'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'vhd_info_dict'
newline|'\n'
nl|'\n'
DECL|member|get_best_supported_vhd_format
dedent|''
name|'def'
name|'get_best_supported_vhd_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'constants'
op|'.'
name|'DISK_FORMAT_VHDX'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
