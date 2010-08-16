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
string|'"""\nTake uploaded bucket contents and register them as disk images (AMIs).\nRequires decryption using keys in the manifest.\n"""'
newline|'\n'
nl|'\n'
comment|'# TODO(jesse): Got these from Euca2ools, will need to revisit them'
nl|'\n'
nl|'\n'
name|'import'
name|'binascii'
newline|'\n'
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tarfile'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'bucket'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'images_path'"
op|','
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'../images'"
op|')'
op|','
nl|'\n'
string|"'path to decrypted images'"
op|')'
newline|'\n'
nl|'\n'
DECL|class|Image
name|'class'
name|'Image'
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
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
name|'image_id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|')'
op|')'
name|'or'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'             '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|image_path
name|'def'
name|'image_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'path'
op|','
string|"'image'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'fn'
name|'in'
op|'['
string|"'info.json'"
op|','
string|"'image'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'path'
op|','
name|'fn'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'rmdir'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|is_authorized
dedent|''
dedent|''
name|'def'
name|'is_authorized'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'readonly'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(devcamcar): Public images can be read by anyone,'
nl|'\n'
comment|'#                  but only modified by admin or owner.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'self'
op|'.'
name|'metadata'
op|'['
string|"'isPublic'"
op|']'
name|'and'
name|'readonly'
op|')'
name|'or'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_admin'
op|'('
op|')'
name|'or'
name|'self'
op|'.'
name|'metadata'
op|'['
string|"'imageOwnerId'"
op|']'
op|'=='
name|'context'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|set_public
dedent|''
dedent|''
name|'def'
name|'set_public'
op|'('
name|'self'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'md'
op|'='
name|'self'
op|'.'
name|'metadata'
newline|'\n'
name|'md'
op|'['
string|"'isPublic'"
op|']'
op|'='
name|'state'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'path'
op|','
string|"'info.json'"
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'json'
op|'.'
name|'dump'
op|'('
name|'md'
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|all
name|'def'
name|'all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'fn'
name|'in'
name|'glob'
op|'.'
name|'glob'
op|'('
string|'"%s/*/info.json"'
op|'%'
name|'FLAGS'
op|'.'
name|'images_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'image_id'
op|'='
name|'fn'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'2'
op|']'
newline|'\n'
name|'images'
op|'.'
name|'append'
op|'('
name|'Image'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'images'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|owner_id
name|'def'
name|'owner_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'metadata'
op|'['
string|"'imageOwnerId'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|metadata
name|'def'
name|'metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'path'
op|','
string|"'info.json'"
op|')'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'json'
op|'.'
name|'load'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|add
name|'def'
name|'add'
op|'('
name|'src'
op|','
name|'description'
op|','
name|'kernel'
op|'='
name|'None'
op|','
name|'ramdisk'
op|'='
name|'None'
op|','
name|'public'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""adds an image to imagestore\n\n        @type src: str\n        @param src: location of the partition image on disk\n\n        @type description: str\n        @param description: string describing the image contents\n\n        @type kernel: bool or str\n        @param kernel: either TRUE meaning this partition is a kernel image or\n                       a string of the image id for the kernel\n\n        @type ramdisk: bool or str\n        @param ramdisk: either TRUE meaning this partition is a ramdisk image or\n                        a string of the image id for the ramdisk\n\n\n        @type public: bool\n        @param public: determine if this is a public image or private\n        \n        @rtype: str\n        @return: a string with the image id\n        """'
newline|'\n'
nl|'\n'
name|'image_type'
op|'='
string|"'machine'"
newline|'\n'
name|'image_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'ami'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'kernel'
name|'is'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'image_type'
op|'='
string|"'kernel'"
newline|'\n'
name|'image_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'aki'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'ramdisk'
name|'is'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'image_type'
op|'='
string|"'ramdisk'"
newline|'\n'
name|'image_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'ari'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'image_path'
op|')'
newline|'\n'
nl|'\n'
name|'shutil'
op|'.'
name|'copyfile'
op|'('
name|'src'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
string|"'image'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
nl|'\n'
string|"'imageId'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'imageLocation'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'imageOwnerId'"
op|':'
string|"'system'"
op|','
nl|'\n'
string|"'isPublic'"
op|':'
name|'public'
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86_64'"
op|','
nl|'\n'
string|"'imageType'"
op|':'
name|'image_type'
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'available'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'type'
op|'('
name|'kernel'
op|')'
name|'is'
name|'str'
name|'and'
name|'len'
op|'('
name|'kernel'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'['
string|"'kernelId'"
op|']'
op|'='
name|'kernel'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'type'
op|'('
name|'ramdisk'
op|')'
name|'is'
name|'str'
name|'and'
name|'len'
op|'('
name|'ramdisk'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'['
string|"'ramdiskId'"
op|']'
op|'='
name|'ramdisk'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
string|"'info.json'"
op|')'
op|','
string|'"w"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'json'
op|'.'
name|'dump'
op|'('
name|'info'
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'image_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|register_aws_image
name|'def'
name|'register_aws_image'
op|'('
name|'image_id'
op|','
name|'image_location'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'image_path'
op|')'
newline|'\n'
nl|'\n'
name|'bucket_name'
op|'='
name|'image_location'
op|'.'
name|'split'
op|'('
string|'"/"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'manifest_path'
op|'='
name|'image_location'
op|'['
name|'len'
op|'('
name|'bucket_name'
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
name|'manifest'
op|'='
name|'ElementTree'
op|'.'
name|'fromstring'
op|'('
name|'bucket_object'
op|'['
name|'manifest_path'
op|']'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'image_type'
op|'='
string|"'machine'"
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'kernel_id'
op|'='
name|'manifest'
op|'.'
name|'find'
op|'('
string|'"machine_configuration/kernel_id"'
op|')'
op|'.'
name|'text'
newline|'\n'
name|'if'
name|'kernel_id'
op|'=='
string|"'true'"
op|':'
newline|'\n'
indent|'                '
name|'image_type'
op|'='
string|"'kernel'"
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ramdisk_id'
op|'='
name|'manifest'
op|'.'
name|'find'
op|'('
string|'"machine_configuration/ramdisk_id"'
op|')'
op|'.'
name|'text'
newline|'\n'
name|'if'
name|'ramdisk_id'
op|'=='
string|"'true'"
op|':'
newline|'\n'
indent|'                '
name|'image_type'
op|'='
string|"'ramdisk'"
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'='
op|'{'
nl|'\n'
string|"'imageId'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'imageLocation'"
op|':'
name|'image_location'
op|','
nl|'\n'
string|"'imageOwnerId'"
op|':'
name|'context'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'isPublic'"
op|':'
name|'False'
op|','
comment|'# FIXME: grab public from manifest'
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86_64'"
op|','
comment|'# FIXME: grab architecture from manifest'
nl|'\n'
string|"'imageType'"
op|':'
name|'image_type'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|write_state
name|'def'
name|'write_state'
op|'('
name|'state'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'['
string|"'imageState'"
op|']'
op|'='
name|'state'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
string|"'info.json'"
op|')'
op|','
string|'"w"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'json'
op|'.'
name|'dump'
op|'('
name|'info'
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'write_state'
op|'('
string|"'pending'"
op|')'
newline|'\n'
nl|'\n'
name|'encrypted_filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
string|"'image.encrypted'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'encrypted_filename'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'filename'
name|'in'
name|'manifest'
op|'.'
name|'find'
op|'('
string|'"image"'
op|')'
op|'.'
name|'getiterator'
op|'('
string|'"filename"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'shutil'
op|'.'
name|'copyfileobj'
op|'('
name|'bucket_object'
op|'['
name|'filename'
op|'.'
name|'text'
op|']'
op|'.'
name|'file'
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'write_state'
op|'('
string|"'decrypting'"
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME: grab kernelId and ramdiskId from bundle manifest'
nl|'\n'
name|'encrypted_key'
op|'='
name|'binascii'
op|'.'
name|'a2b_hex'
op|'('
name|'manifest'
op|'.'
name|'find'
op|'('
string|'"image/ec2_encrypted_key"'
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'encrypted_iv'
op|'='
name|'binascii'
op|'.'
name|'a2b_hex'
op|'('
name|'manifest'
op|'.'
name|'find'
op|'('
string|'"image/ec2_encrypted_iv"'
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'cloud_private_key'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'ca_path'
op|','
string|'"private/cakey.pem"'
op|')'
newline|'\n'
nl|'\n'
name|'decrypted_filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
string|"'image.tar.gz'"
op|')'
newline|'\n'
name|'Image'
op|'.'
name|'decrypt_image'
op|'('
name|'encrypted_filename'
op|','
name|'encrypted_key'
op|','
name|'encrypted_iv'
op|','
name|'cloud_private_key'
op|','
name|'decrypted_filename'
op|')'
newline|'\n'
nl|'\n'
name|'write_state'
op|'('
string|"'untarring'"
op|')'
newline|'\n'
nl|'\n'
name|'image_file'
op|'='
name|'Image'
op|'.'
name|'untarzip_image'
op|'('
name|'image_path'
op|','
name|'decrypted_filename'
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'move'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
name|'image_file'
op|')'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
string|"'image'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'write_state'
op|'('
string|"'available'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'decrypted_filename'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'encrypted_filename'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|decrypt_image
name|'def'
name|'decrypt_image'
op|'('
name|'encrypted_filename'
op|','
name|'encrypted_key'
op|','
name|'encrypted_iv'
op|','
name|'cloud_private_key'
op|','
name|'decrypted_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl rsautl -decrypt -inkey %s'"
op|'%'
name|'cloud_private_key'
op|','
name|'encrypted_key'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Failed to decrypt private key: %s"'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'iv'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl rsautl -decrypt -inkey %s'"
op|'%'
name|'cloud_private_key'
op|','
name|'encrypted_iv'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Failed to decrypt initialization vector: %s"'
op|'%'
name|'err'
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
string|"'openssl enc -d -aes-128-cbc -in %s -K %s -iv %s -out %s'"
op|'%'
op|'('
name|'encrypted_filename'
op|','
name|'key'
op|','
name|'iv'
op|','
name|'decrypted_filename'
op|')'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Failed to decrypt image file %s : %s"'
op|'%'
op|'('
name|'encrypted_filename'
op|','
name|'err'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|untarzip_image
name|'def'
name|'untarzip_image'
op|'('
name|'path'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tar_file'
op|'='
name|'tarfile'
op|'.'
name|'open'
op|'('
name|'filename'
op|','
string|'"r|gz"'
op|')'
newline|'\n'
name|'tar_file'
op|'.'
name|'extractall'
op|'('
name|'path'
op|')'
newline|'\n'
name|'image_file'
op|'='
name|'tar_file'
op|'.'
name|'getnames'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'tar_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'image_file'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
