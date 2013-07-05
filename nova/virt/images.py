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
string|'"""\nHandling of VM disk images.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
DECL|variable|image_opts
name|'image_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'force_raw_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force backing images to raw format'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'image_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QemuImgInfo
name|'class'
name|'QemuImgInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|BACKING_FILE_RE
indent|'    '
name|'BACKING_FILE_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
op|'('
string|'r"^(.*?)\\s*\\(actual\\s+path\\s*:"'
nl|'\n'
string|'r"\\s+(.*?)\\)\\s*$"'
op|')'
op|','
name|'re'
op|'.'
name|'I'
op|')'
newline|'\n'
DECL|variable|TOP_LEVEL_RE
name|'TOP_LEVEL_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"^([\\w\\d\\s\\_\\-]+):(.*)$"'
op|')'
newline|'\n'
DECL|variable|SIZE_RE
name|'SIZE_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"\\(\\s*(\\d+)\\s+bytes\\s*\\)"'
op|','
name|'re'
op|'.'
name|'I'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cmd_output'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'details'
op|'='
name|'self'
op|'.'
name|'_parse'
op|'('
name|'cmd_output'
name|'or'
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'backing_file'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'backing_file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'file_format'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'file_format'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'virtual_size'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'virtual_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cluster_size'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'cluster_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk_size'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'disk_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'snapshots'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'snapshot_list'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'encryption'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'encryption'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lines'
op|'='
op|'['
nl|'\n'
string|"'image: %s'"
op|'%'
name|'self'
op|'.'
name|'image'
op|','
nl|'\n'
string|"'file_format: %s'"
op|'%'
name|'self'
op|'.'
name|'file_format'
op|','
nl|'\n'
string|"'virtual_size: %s'"
op|'%'
name|'self'
op|'.'
name|'virtual_size'
op|','
nl|'\n'
string|"'disk_size: %s'"
op|'%'
name|'self'
op|'.'
name|'disk_size'
op|','
nl|'\n'
string|"'cluster_size: %s'"
op|'%'
name|'self'
op|'.'
name|'cluster_size'
op|','
nl|'\n'
string|"'backing_file: %s'"
op|'%'
name|'self'
op|'.'
name|'backing_file'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'snapshots'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'.'
name|'append'
op|'('
string|'"snapshots: %s"'
op|'%'
name|'self'
op|'.'
name|'snapshots'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_canonicalize
dedent|''
name|'def'
name|'_canonicalize'
op|'('
name|'self'
op|','
name|'field'
op|')'
op|':'
newline|'\n'
comment|'# Standardize on underscores/lc/no dash and no spaces'
nl|'\n'
comment|'# since qemu seems to have mixed outputs here... and'
nl|'\n'
comment|'# this format allows for better integration with python'
nl|'\n'
comment|'# - ie for usage in kwargs and such...'
nl|'\n'
indent|'        '
name|'field'
op|'='
name|'field'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'for'
name|'c'
name|'in'
op|'('
string|'" "'
op|','
string|'"-"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'field'
op|'='
name|'field'
op|'.'
name|'replace'
op|'('
name|'c'
op|','
string|"'_'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'field'
newline|'\n'
nl|'\n'
DECL|member|_extract_bytes
dedent|''
name|'def'
name|'_extract_bytes'
op|'('
name|'self'
op|','
name|'details'
op|')'
op|':'
newline|'\n'
comment|'# Replace it with the byte amount'
nl|'\n'
indent|'        '
name|'real_size'
op|'='
name|'self'
op|'.'
name|'SIZE_RE'
op|'.'
name|'search'
op|'('
name|'details'
op|')'
newline|'\n'
name|'if'
name|'real_size'
op|':'
newline|'\n'
indent|'            '
name|'details'
op|'='
name|'real_size'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'details'
op|'='
name|'strutils'
op|'.'
name|'to_bytes'
op|'('
name|'details'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'details'
newline|'\n'
nl|'\n'
DECL|member|_extract_details
dedent|''
name|'def'
name|'_extract_details'
op|'('
name|'self'
op|','
name|'root_cmd'
op|','
name|'root_details'
op|','
name|'lines_after'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'real_details'
op|'='
name|'root_details'
newline|'\n'
name|'if'
name|'root_cmd'
op|'=='
string|"'backing_file'"
op|':'
newline|'\n'
comment|'# Replace it with the real backing file'
nl|'\n'
indent|'            '
name|'backing_match'
op|'='
name|'self'
op|'.'
name|'BACKING_FILE_RE'
op|'.'
name|'match'
op|'('
name|'root_details'
op|')'
newline|'\n'
name|'if'
name|'backing_match'
op|':'
newline|'\n'
indent|'                '
name|'real_details'
op|'='
name|'backing_match'
op|'.'
name|'group'
op|'('
number|'2'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'root_cmd'
name|'in'
op|'['
string|"'virtual_size'"
op|','
string|"'cluster_size'"
op|','
string|"'disk_size'"
op|']'
op|':'
newline|'\n'
comment|'# Replace it with the byte amount (if we can convert it)'
nl|'\n'
indent|'            '
name|'real_details'
op|'='
name|'self'
op|'.'
name|'_extract_bytes'
op|'('
name|'root_details'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'root_cmd'
op|'=='
string|"'file_format'"
op|':'
newline|'\n'
indent|'            '
name|'real_details'
op|'='
name|'real_details'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'root_cmd'
op|'=='
string|"'snapshot_list'"
op|':'
newline|'\n'
comment|"# Next line should be a header, starting with 'ID'"
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'lines_after'
name|'or'
name|'not'
name|'lines_after'
op|'['
number|'0'
op|']'
op|'.'
name|'startswith'
op|'('
string|'"ID"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Snapshot list encountered but no header found!"'
op|')'
newline|'\n'
name|'raise'
name|'ValueError'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'del'
name|'lines_after'
op|'['
number|'0'
op|']'
newline|'\n'
name|'real_details'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# This is the sprintf pattern we will try to match'
nl|'\n'
comment|'# "%-10s%-20s%7s%20s%15s"'
nl|'\n'
comment|'# ID TAG VM SIZE DATE VM CLOCK (current header)'
nl|'\n'
name|'while'
name|'lines_after'
op|':'
newline|'\n'
indent|'                '
name|'line'
op|'='
name|'lines_after'
op|'['
number|'0'
op|']'
newline|'\n'
name|'line_pieces'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'line_pieces'
op|')'
op|'!='
number|'6'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
comment|'# Check against this pattern in the final position'
nl|'\n'
comment|'# "%02d:%02d:%02d.%03d"'
nl|'\n'
dedent|''
name|'date_pieces'
op|'='
name|'line_pieces'
op|'['
number|'5'
op|']'
op|'.'
name|'split'
op|'('
string|'":"'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'date_pieces'
op|')'
op|'!='
number|'3'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
name|'real_details'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'line_pieces'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'tag'"
op|':'
name|'line_pieces'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'vm_size'"
op|':'
name|'line_pieces'
op|'['
number|'2'
op|']'
op|','
nl|'\n'
string|"'date'"
op|':'
name|'line_pieces'
op|'['
number|'3'
op|']'
op|','
nl|'\n'
string|"'vm_clock'"
op|':'
name|'line_pieces'
op|'['
number|'4'
op|']'
op|'+'
string|'" "'
op|'+'
name|'line_pieces'
op|'['
number|'5'
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'del'
name|'lines_after'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'real_details'
newline|'\n'
nl|'\n'
DECL|member|_parse
dedent|''
name|'def'
name|'_parse'
op|'('
name|'self'
op|','
name|'cmd_output'
op|')'
op|':'
newline|'\n'
comment|'# Analysis done of qemu-img.c to figure out what is going on here'
nl|'\n'
comment|"# Find all points start with some chars and then a ':' then a newline"
nl|'\n'
comment|"# and then handle the results of those 'top level' items in a separate"
nl|'\n'
comment|'# function.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# TODO(harlowja): newer versions might have a json output format'
nl|'\n'
comment|'#                 we should switch to that whenever possible.'
nl|'\n'
comment|'#                 see: http://bit.ly/XLJXDX'
nl|'\n'
indent|'        '
name|'contents'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'lines'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'cmd_output'
op|'.'
name|'splitlines'
op|'('
op|')'
name|'if'
name|'x'
op|'.'
name|'strip'
op|'('
op|')'
op|']'
newline|'\n'
name|'while'
name|'lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'lines'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'top_level'
op|'='
name|'self'
op|'.'
name|'TOP_LEVEL_RE'
op|'.'
name|'match'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
name|'top_level'
op|':'
newline|'\n'
indent|'                '
name|'root'
op|'='
name|'self'
op|'.'
name|'_canonicalize'
op|'('
name|'top_level'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'root'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'root_details'
op|'='
name|'top_level'
op|'.'
name|'group'
op|'('
number|'2'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'details'
op|'='
name|'self'
op|'.'
name|'_extract_details'
op|'('
name|'root'
op|','
name|'root_details'
op|','
name|'lines'
op|')'
newline|'\n'
name|'contents'
op|'['
name|'root'
op|']'
op|'='
name|'details'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'contents'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|qemu_img_info
dedent|''
dedent|''
name|'def'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return an object containing the parsed output from qemu-img info."""'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
name|'and'
name|'CONF'
op|'.'
name|'libvirt_images_type'
op|'!='
string|"'rbd'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'QemuImgInfo'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
newline|'\n'
name|'return'
name|'QemuImgInfo'
op|'('
name|'out'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_image
dedent|''
name|'def'
name|'convert_image'
op|'('
name|'source'
op|','
name|'dest'
op|','
name|'out_format'
op|','
name|'run_as_root'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert image to other format."""'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
string|"'convert'"
op|','
string|"'-O'"
op|','
name|'out_format'
op|','
name|'source'
op|','
name|'dest'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'run_as_root'
op|'='
name|'run_as_root'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch
dedent|''
name|'def'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path'
op|','
name|'_user_id'
op|','
name|'_project_id'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): Improve context handling and add owner and auth data'
nl|'\n'
comment|'#             when it is added to glance.  Right now there is no'
nl|'\n'
comment|'#             auth checking in glance, so we assume that access was'
nl|'\n'
comment|'#             checked before we got here.'
nl|'\n'
indent|'    '
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
nl|'\n'
name|'image_href'
op|')'
newline|'\n'
name|'with'
name|'fileutils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|'"wb"'
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'            '
name|'image_service'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_to_raw
dedent|''
dedent|''
dedent|''
name|'def'
name|'fetch_to_raw'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'path_tmp'
op|'='
string|'"%s.part"'
op|'%'
name|'path'
newline|'\n'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path_tmp'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'fileutils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'path_tmp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'qemu_img_info'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
nl|'\n'
name|'fmt'
op|'='
name|'data'
op|'.'
name|'file_format'
newline|'\n'
name|'if'
name|'fmt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"\'qemu-img info\' parsing failed."'
op|')'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_href'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'backing_file'
op|'='
name|'data'
op|'.'
name|'backing_file'
newline|'\n'
name|'if'
name|'backing_file'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_href'
op|','
nl|'\n'
name|'reason'
op|'='
op|'('
name|'_'
op|'('
string|'"fmt=%(fmt)s backed by: %(backing_file)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'fmt'"
op|':'
name|'fmt'
op|','
string|"'backing_file'"
op|':'
name|'backing_file'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'fmt'
op|'!='
string|'"raw"'
name|'and'
name|'CONF'
op|'.'
name|'force_raw_images'
op|':'
newline|'\n'
indent|'            '
name|'staged'
op|'='
string|'"%s.converted"'
op|'%'
name|'path'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%s was %s, converting to raw"'
op|'%'
op|'('
name|'image_href'
op|','
name|'fmt'
op|')'
op|')'
newline|'\n'
name|'with'
name|'fileutils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'staged'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'convert_image'
op|'('
name|'path_tmp'
op|','
name|'staged'
op|','
string|"'raw'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'qemu_img_info'
op|'('
name|'staged'
op|')'
newline|'\n'
name|'if'
name|'data'
op|'.'
name|'file_format'
op|'!='
string|'"raw"'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_href'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Converted to raw, but format is now %s"'
op|')'
op|'%'
nl|'\n'
name|'data'
op|'.'
name|'file_format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'rename'
op|'('
name|'staged'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'rename'
op|'('
name|'path_tmp'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
