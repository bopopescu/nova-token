begin_unit
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
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'fileutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'imageutils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'image'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|IMAGE_API
name|'IMAGE_API'
op|'='
name|'image'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|qemu_img_info
name|'def'
name|'qemu_img_info'
op|'('
name|'path'
op|','
name|'format'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return an object containing the parsed output from qemu-img info."""'
newline|'\n'
comment|'# TODO(mikal): this code should not be referring to a libvirt specific'
nl|'\n'
comment|'# flag.'
nl|'\n'
comment|'# NOTE(sirp): The config option import must go here to avoid an import'
nl|'\n'
comment|'# cycle'
nl|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'images_type'"
op|','
string|"'nova.virt.libvirt.imagebackend'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'libvirt'"
op|')'
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
name|'libvirt'
op|'.'
name|'images_type'
op|'!='
string|"'rbd'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DiskNotFound'
op|'('
name|'location'
op|'='
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
newline|'\n'
name|'if'
name|'format'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
name|'cmd'
op|'+'
op|'('
string|"'-f'"
op|','
name|'format'
op|')'
newline|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"qemu-img failed to execute on %(path)s : %(exp)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'exp'"
op|':'
name|'exp'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidDiskInfo'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'out'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Failed to run qemu-img info on %(path)s : %(error)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'error'"
op|':'
name|'err'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidDiskInfo'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'imageutils'
op|'.'
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
name|'in_format'
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
name|'if'
name|'in_format'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
string|'"convert_image without input format is a security"'
nl|'\n'
string|'"risk"'
op|')'
newline|'\n'
dedent|''
name|'_convert_image'
op|'('
name|'source'
op|','
name|'dest'
op|','
name|'in_format'
op|','
name|'out_format'
op|','
name|'run_as_root'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_image_unsafe
dedent|''
name|'def'
name|'convert_image_unsafe'
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
string|'"""Convert image to other format, doing unsafe automatic input format\n    detection. Do not call this function.\n    """'
newline|'\n'
nl|'\n'
comment|'# NOTE: there is only 1 caller of this function:'
nl|'\n'
comment|'# imagebackend.Lvm.create_image. It is not easy to fix that without a'
nl|'\n'
comment|'# larger refactor, so for the moment it has been manually audited and'
nl|'\n'
comment|'# allowed to continue. Remove this function when Lvm.create_image has'
nl|'\n'
comment|'# been fixed.'
nl|'\n'
name|'_convert_image'
op|'('
name|'source'
op|','
name|'dest'
op|','
name|'None'
op|','
name|'out_format'
op|','
name|'run_as_root'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_convert_image
dedent|''
name|'def'
name|'_convert_image'
op|'('
name|'source'
op|','
name|'dest'
op|','
name|'in_format'
op|','
name|'out_format'
op|','
name|'run_as_root'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'if'
name|'in_format'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
name|'cmd'
op|'+'
op|'('
string|"'-f'"
op|','
name|'in_format'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
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
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Unable to convert image to %(format)s: %(exp)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'format'"
op|':'
name|'out_format'
op|','
string|"'exp'"
op|':'
name|'exp'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'source'
op|','
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch
dedent|''
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
op|','
name|'max_size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'IMAGE_API'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'dest_path'
op|'='
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_info
dedent|''
dedent|''
name|'def'
name|'get_info'
op|'('
name|'context'
op|','
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMAGE_API'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_href'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_to_raw
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
op|','
name|'max_size'
op|'='
number|'0'
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
op|','
nl|'\n'
name|'max_size'
op|'='
name|'max_size'
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
comment|"# We can't generally shrink incoming images, so disallow"
nl|'\n'
comment|"# images > size of the flavor we're booting.  Checking here avoids"
nl|'\n'
comment|'# an immediate DoS where we convert large qcow images to raw'
nl|'\n'
comment|'# (which may compress well but not be sparse).'
nl|'\n'
comment|'# TODO(p-draigbrady): loop through all flavor sizes, so that'
nl|'\n'
comment|'# we might continue here and not discard the download.'
nl|'\n'
comment|"# If we did that we'd have to do the higher level size checks"
nl|'\n'
comment|'# irrespective of whether the base image was prepared or not.'
nl|'\n'
dedent|''
name|'disk_size'
op|'='
name|'data'
op|'.'
name|'virtual_size'
newline|'\n'
name|'if'
name|'max_size'
name|'and'
name|'max_size'
op|'<'
name|'disk_size'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'%(base)s virtual size %(disk_size)s '"
nl|'\n'
string|"'larger than flavor root disk size %(size)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'base'"
op|':'
name|'path'
op|','
nl|'\n'
string|"'disk_size'"
op|':'
name|'disk_size'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'max_size'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'FlavorDiskSmallerThanImage'
op|'('
nl|'\n'
name|'flavor_size'
op|'='
name|'max_size'
op|','
name|'image_size'
op|'='
name|'disk_size'
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
op|','
name|'image_href'
op|','
name|'fmt'
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
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'convert_image'
op|'('
name|'path_tmp'
op|','
name|'staged'
op|','
name|'fmt'
op|','
string|"'raw'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageUnacceptable'
name|'as'
name|'exp'
op|':'
newline|'\n'
comment|'# re-raise to include image_href'
nl|'\n'
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
string|'"Unable to convert image to raw: %(exp)s"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'exp'"
op|':'
name|'exp'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
