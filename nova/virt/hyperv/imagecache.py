begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
string|'"""\nImage caching and management.\n"""'
newline|'\n'
name|'import'
name|'os'
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
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
name|'import'
name|'unit'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'utilsfactory'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vhdutilsv2'
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
name|'import'
name|'images'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_cow_images'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCache
name|'class'
name|'ImageCache'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'_pathutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_pathutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vhdutils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_vhd_image
dedent|''
name|'def'
name|'_validate_vhd_image'
op|'('
name|'self'
op|','
name|'vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'validate_vhd'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|"'The image is not a valid VHD: %s'"
op|')'
nl|'\n'
op|'%'
name|'vhd_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_root_vhd_size_gb
dedent|''
dedent|''
name|'def'
name|'_get_root_vhd_size_gb'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|'# In case of resizes we need the old root disk size'
nl|'\n'
indent|'            '
name|'old_instance_type'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
nl|'\n'
name|'instance'
op|','
name|'prefix'
op|'='
string|"'old_'"
op|')'
newline|'\n'
name|'return'
name|'old_instance_type'
op|'['
string|"'root_gb'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instance'
op|'['
string|"'root_gb'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_resize_and_cache_vhd
dedent|''
dedent|''
name|'def'
name|'_resize_and_cache_vhd'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vhd_info'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_info'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
name|'vhd_size'
op|'='
name|'vhd_info'
op|'['
string|"'MaxInternalSize'"
op|']'
newline|'\n'
nl|'\n'
name|'root_vhd_size_gb'
op|'='
name|'self'
op|'.'
name|'_get_root_vhd_size_gb'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'root_vhd_size'
op|'='
name|'root_vhd_size_gb'
op|'*'
name|'unit'
op|'.'
name|'Gi'
newline|'\n'
nl|'\n'
comment|'# NOTE(lpetrut): Checking the namespace is needed as the following'
nl|'\n'
comment|'# method is not yet implemented in the vhdutilsv2 module.'
nl|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'_vhdutils'
op|','
name|'vhdutilsv2'
op|'.'
name|'VHDUtilsV2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_internal_size'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_internal_vhd_size_by_file_size'
op|'('
nl|'\n'
name|'vhd_path'
op|','
name|'root_vhd_size'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_internal_size'
op|'='
name|'root_vhd_size'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'root_vhd_internal_size'
op|'<'
name|'vhd_size'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Cannot resize the image to a size smaller than the VHD "'
nl|'\n'
string|'"max. internal size: %(vhd_size)s. Requested disk size: "'
nl|'\n'
string|'"%(root_vhd_size)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'vhd_size'"
op|':'
name|'vhd_size'
op|','
string|"'root_vhd_size'"
op|':'
name|'root_vhd_size'
op|'}'
nl|'\n'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'root_vhd_internal_size'
op|'>'
name|'vhd_size'
op|':'
newline|'\n'
indent|'            '
name|'path_parts'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'splitext'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
name|'resized_vhd_path'
op|'='
string|"'%s_%s%s'"
op|'%'
op|'('
name|'path_parts'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'root_vhd_size_gb'
op|','
nl|'\n'
name|'path_parts'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'resized_vhd_path'
op|')'
newline|'\n'
DECL|function|copy_and_resize_vhd
name|'def'
name|'copy_and_resize_vhd'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'resized_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'try'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Copying VHD %(vhd_path)s to "'
nl|'\n'
string|'"%(resized_vhd_path)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'vhd_path'"
op|':'
name|'vhd_path'
op|','
nl|'\n'
string|"'resized_vhd_path'"
op|':'
name|'resized_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'copyfile'
op|'('
name|'vhd_path'
op|','
name|'resized_vhd_path'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Resizing VHD %(resized_vhd_path)s to new "'
nl|'\n'
string|'"size %(root_vhd_size)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'resized_vhd_path'"
op|':'
name|'resized_vhd_path'
op|','
nl|'\n'
string|"'root_vhd_size'"
op|':'
name|'root_vhd_size'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'resize_vhd'
op|'('
name|'resized_vhd_path'
op|','
nl|'\n'
name|'root_vhd_size'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                        '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'resized_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'                                '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'remove'
op|'('
name|'resized_vhd_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'copy_and_resize_vhd'
op|'('
op|')'
newline|'\n'
name|'return'
name|'resized_vhd_path'
newline|'\n'
nl|'\n'
DECL|member|get_cached_image
dedent|''
dedent|''
name|'def'
name|'get_cached_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'instance'
op|'['
string|"'image_ref'"
op|']'
newline|'\n'
nl|'\n'
name|'base_vhd_dir'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_base_vhd_dir'
op|'('
op|')'
newline|'\n'
name|'base_vhd_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_vhd_dir'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'base_vhd_path'
op|')'
newline|'\n'
DECL|function|fetch_image_if_not_existing
name|'def'
name|'fetch_image_if_not_existing'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vhd_path'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'format_ext'
name|'in'
op|'['
string|"'vhd'"
op|','
string|"'vhdx'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'test_path'
op|'='
name|'base_vhd_path'
op|'+'
string|"'.'"
op|'+'
name|'format_ext'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'test_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'vhd_path'
op|'='
name|'test_path'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'vhd_path'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'images'
op|'.'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'base_vhd_path'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'format_ext'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_format'
op|'('
name|'base_vhd_path'
op|')'
newline|'\n'
name|'vhd_path'
op|'='
name|'base_vhd_path'
op|'+'
string|"'.'"
op|'+'
name|'format_ext'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rename'
op|'('
name|'base_vhd_path'
op|','
name|'vhd_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'base_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'remove'
op|'('
name|'base_vhd_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'vhd_path'
newline|'\n'
nl|'\n'
dedent|''
name|'vhd_path'
op|'='
name|'fetch_image_if_not_existing'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_cow_images'
name|'and'
name|'vhd_path'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'vhd'"
op|':'
newline|'\n'
comment|"# Resize the base VHD image as it's not possible to resize a"
nl|'\n'
comment|'# differencing VHD. This does not apply to VHDX images.'
nl|'\n'
indent|'            '
name|'resized_vhd_path'
op|'='
name|'self'
op|'.'
name|'_resize_and_cache_vhd'
op|'('
name|'instance'
op|','
name|'vhd_path'
op|')'
newline|'\n'
name|'if'
name|'resized_vhd_path'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'resized_vhd_path'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'vhd_path'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
