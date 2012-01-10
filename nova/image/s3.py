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
string|'"""Proxy AMI-related calls from cloud controller to objectstore service."""'
newline|'\n'
nl|'\n'
name|'import'
name|'binascii'
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
name|'import'
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
newline|'\n'
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
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
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.image.s3"'
op|')'
newline|'\n'
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
string|"'image_decryption_dir'"
op|','
string|"'/tmp'"
op|','
nl|'\n'
string|"'parent dir for tempdir used for image decryption'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'s3_access_key'"
op|','
string|"'notchecked'"
op|','
nl|'\n'
string|"'access key to use for s3 server for images'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'s3_secret_key'"
op|','
string|"'notchecked'"
op|','
nl|'\n'
string|"'secret key to use for s3 server for images'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|S3ImageService
name|'class'
name|'S3ImageService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps an existing image service to support s3 based register."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'service'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service'
op|'='
name|'service'
name|'or'
name|'image'
op|'.'
name|'get_default_image_service'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_image_uuid
dedent|''
name|'def'
name|'get_image_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|'.'
name|'s3_image_get'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_image_id
dedent|''
name|'def'
name|'get_image_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|'.'
name|'s3_image_get_by_uuid'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_image_id
dedent|''
name|'def'
name|'_create_image_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|'.'
name|'s3_image_create'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_translate_uuids_to_ids
dedent|''
name|'def'
name|'_translate_uuids_to_ids'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'images'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'_translate_uuid_to_id'
op|'('
name|'context'
op|','
name|'img'
op|')'
name|'for'
name|'img'
name|'in'
name|'images'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_translate_uuid_to_id
dedent|''
name|'def'
name|'_translate_uuid_to_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
DECL|function|_find_or_create
indent|'        '
name|'def'
name|'_find_or_create'
op|'('
name|'image_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image_uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'get_image_id'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_create_image_id'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'image_copy'
op|'='
name|'image'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_id'
op|'='
name|'image_copy'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'image_copy'
op|'['
string|"'id'"
op|']'
op|'='
name|'_find_or_create'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'prop'
name|'in'
op|'['
string|"'kernel_id'"
op|','
string|"'ramdisk_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'image_uuid'
op|'='
name|'image_copy'
op|'['
string|"'properties'"
op|']'
op|'['
name|'prop'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'image_copy'
op|'['
string|"'properties'"
op|']'
op|'['
name|'prop'
op|']'
op|'='
name|'_find_or_create'
op|'('
name|'image_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'image_copy'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an image.\n\n        metadata[\'properties\'] should contain image_location.\n\n        """'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_s3_create'
op|'('
name|'context'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'return'
name|'image'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
name|'self'
op|'.'
name|'get_image_uuid'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
name|'self'
op|'.'
name|'get_image_uuid'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate_uuid_to_id'
op|'('
name|'context'
op|','
name|'image'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
comment|'#NOTE(bcwaldon): sort asc to make sure we assign lower ids'
nl|'\n'
comment|'# to older images'
nl|'\n'
indent|'        '
name|'images'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'context'
op|','
name|'sort_dir'
op|'='
string|"'asc'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate_uuids_to_ids'
op|'('
name|'context'
op|','
name|'images'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
comment|'#NOTE(bcwaldon): sort asc to make sure we assign lower ids'
nl|'\n'
comment|'# to older images'
nl|'\n'
indent|'        '
name|'images'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'context'
op|','
name|'sort_dir'
op|'='
string|"'asc'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate_uuids_to_ids'
op|'('
name|'context'
op|','
name|'images'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
name|'self'
op|'.'
name|'get_image_uuid'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate_uuid_to_id'
op|'('
name|'context'
op|','
name|'image'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show_by_name
dedent|''
name|'def'
name|'show_by_name'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_translate_uuid_to_id'
op|'('
name|'context'
op|','
name|'image'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
name|'self'
op|'.'
name|'get_image_uuid'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_conn
name|'def'
name|'_conn'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): access and secret keys for s3 server are not'
nl|'\n'
comment|'#             checked in nova-objectstore'
nl|'\n'
indent|'        '
name|'access'
op|'='
name|'FLAGS'
op|'.'
name|'s3_access_key'
newline|'\n'
name|'secret'
op|'='
name|'FLAGS'
op|'.'
name|'s3_secret_key'
newline|'\n'
name|'calling'
op|'='
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'OrdinaryCallingFormat'
op|'('
op|')'
newline|'\n'
name|'return'
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'S3Connection'
op|'('
name|'aws_access_key_id'
op|'='
name|'access'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'secret'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'False'
op|','
nl|'\n'
name|'calling_format'
op|'='
name|'calling'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
nl|'\n'
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'s3_host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_download_file
name|'def'
name|'_download_file'
op|'('
name|'bucket'
op|','
name|'filename'
op|','
name|'local_dir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'bucket'
op|'.'
name|'get_key'
op|'('
name|'filename'
op|')'
newline|'\n'
name|'local_filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'local_dir'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'filename'
op|')'
op|')'
newline|'\n'
name|'key'
op|'.'
name|'get_contents_to_filename'
op|'('
name|'local_filename'
op|')'
newline|'\n'
name|'return'
name|'local_filename'
newline|'\n'
nl|'\n'
DECL|member|_s3_parse_manifest
dedent|''
name|'def'
name|'_s3_parse_manifest'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'metadata'
op|','
name|'manifest'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manifest'
op|'='
name|'ElementTree'
op|'.'
name|'fromstring'
op|'('
name|'manifest'
op|')'
newline|'\n'
name|'image_format'
op|'='
string|"'ami'"
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
string|"'machine_configuration/kernel_id'"
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
name|'image_format'
op|'='
string|"'aki'"
newline|'\n'
name|'image_type'
op|'='
string|"'kernel'"
newline|'\n'
name|'kernel_id'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'kernel_id'
op|'='
name|'None'
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
string|"'machine_configuration/ramdisk_id'"
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
name|'image_format'
op|'='
string|"'ari'"
newline|'\n'
name|'image_type'
op|'='
string|"'ramdisk'"
newline|'\n'
name|'ramdisk_id'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'ramdisk_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'arch'
op|'='
name|'manifest'
op|'.'
name|'find'
op|'('
string|"'machine_configuration/architecture'"
op|')'
op|'.'
name|'text'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'arch'
op|'='
string|"'x86_64'"
newline|'\n'
nl|'\n'
comment|'# NOTE(yamahata):'
nl|'\n'
comment|'# EC2 ec2-budlne-image --block-device-mapping accepts'
nl|'\n'
comment|'# <virtual name>=<device name> where'
nl|'\n'
comment|'# virtual name = {ami, root, swap, ephemeral<N>}'
nl|'\n'
comment|'#                where N is no negative integer'
nl|'\n'
comment|'# device name = the device name seen by guest kernel.'
nl|'\n'
comment|'# They are converted into'
nl|'\n'
comment|'# block_device_mapping/mapping/{virtual, device}'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# Do NOT confuse this with ec2-register's block device mapping"
nl|'\n'
comment|'# argument.'
nl|'\n'
dedent|''
name|'mappings'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'block_device_mapping'
op|'='
name|'manifest'
op|'.'
name|'findall'
op|'('
string|"'machine_configuration/'"
nl|'\n'
string|"'block_device_mapping/'"
nl|'\n'
string|"'mapping'"
op|')'
newline|'\n'
name|'for'
name|'bdm'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'                '
name|'mappings'
op|'.'
name|'append'
op|'('
op|'{'
string|"'virtual'"
op|':'
name|'bdm'
op|'.'
name|'find'
op|'('
string|"'virtual'"
op|')'
op|'.'
name|'text'
op|','
nl|'\n'
string|"'device'"
op|':'
name|'bdm'
op|'.'
name|'find'
op|'('
string|"'device'"
op|')'
op|'.'
name|'text'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'properties'
op|'='
name|'metadata'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'properties'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'properties'
op|'['
string|"'architecture'"
op|']'
op|'='
name|'arch'
newline|'\n'
nl|'\n'
DECL|function|_translate_dependent_image_id
name|'def'
name|'_translate_dependent_image_id'
op|'('
name|'image_key'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_id'
op|'='
name|'ec2utils'
op|'.'
name|'ec2_id_to_id'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'image_uuid'
op|'='
name|'self'
op|'.'
name|'get_image_uuid'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'properties'
op|'['
name|'image_key'
op|']'
op|'='
name|'image_uuid'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'_translate_dependent_image_id'
op|'('
string|"'kernel_id'"
op|','
name|'kernel_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ramdisk_id'
op|':'
newline|'\n'
indent|'            '
name|'_translate_dependent_image_id'
op|'('
string|"'ramdisk_id'"
op|','
name|'ramdisk_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'mappings'
op|':'
newline|'\n'
indent|'            '
name|'properties'
op|'['
string|"'mappings'"
op|']'
op|'='
name|'mappings'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'.'
name|'update'
op|'('
op|'{'
string|"'disk_format'"
op|':'
name|'image_format'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'image_format'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'queued'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'properties'"
op|':'
name|'properties'
op|'}'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'pending'"
newline|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): right now, this removes user-defined ids.'
nl|'\n'
comment|'# We need to re-enable this.'
nl|'\n'
name|'image_id'
op|'='
name|'metadata'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'context'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
comment|'# extract the new uuid and generate an int id to present back to user'
nl|'\n'
name|'image_uuid'
op|'='
name|'image'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image'
op|'['
string|"'id'"
op|']'
op|'='
name|'self'
op|'.'
name|'_create_image_id'
op|'('
name|'context'
op|','
name|'image_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|'# return image_uuid so the caller can still make use of image_service'
nl|'\n'
name|'return'
name|'manifest'
op|','
name|'image'
op|','
name|'image_uuid'
newline|'\n'
nl|'\n'
DECL|member|_s3_create
dedent|''
name|'def'
name|'_s3_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets a manifest from s3 and makes an image."""'
newline|'\n'
nl|'\n'
name|'image_path'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'dir'
op|'='
name|'FLAGS'
op|'.'
name|'image_decryption_dir'
op|')'
newline|'\n'
nl|'\n'
name|'image_location'
op|'='
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_location'"
op|']'
newline|'\n'
name|'bucket_name'
op|'='
name|'image_location'
op|'.'
name|'split'
op|'('
string|"'/'"
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
name|'bucket'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'('
name|'context'
op|')'
op|'.'
name|'get_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
name|'key'
op|'='
name|'bucket'
op|'.'
name|'get_key'
op|'('
name|'manifest_path'
op|')'
newline|'\n'
name|'manifest'
op|'='
name|'key'
op|'.'
name|'get_contents_as_string'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'manifest'
op|','
name|'image'
op|','
name|'image_uuid'
op|'='
name|'self'
op|'.'
name|'_s3_parse_manifest'
op|'('
name|'context'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'manifest'
op|')'
newline|'\n'
nl|'\n'
DECL|function|delayed_create
name|'def'
name|'delayed_create'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""This handles the fetching and decrypting of the part files."""'
newline|'\n'
name|'log_vars'
op|'='
op|'{'
string|"'image_location'"
op|':'
name|'image_location'
op|','
nl|'\n'
string|"'image_path'"
op|':'
name|'image_path'
op|'}'
newline|'\n'
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'downloading'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'parts'
op|'='
op|'['
op|']'
newline|'\n'
name|'elements'
op|'='
name|'manifest'
op|'.'
name|'find'
op|'('
string|"'image'"
op|')'
op|'.'
name|'getiterator'
op|'('
string|"'filename'"
op|')'
newline|'\n'
name|'for'
name|'fn_element'
name|'in'
name|'elements'
op|':'
newline|'\n'
indent|'                    '
name|'part'
op|'='
name|'self'
op|'.'
name|'_download_file'
op|'('
name|'bucket'
op|','
nl|'\n'
name|'fn_element'
op|'.'
name|'text'
op|','
nl|'\n'
name|'image_path'
op|')'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
name|'part'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): this may be suboptimal, should we use cat?'
nl|'\n'
dedent|''
name|'enc_filename'
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
name|'enc_filename'
op|','
string|"'w'"
op|')'
name|'as'
name|'combined'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'filename'
name|'in'
name|'parts'
op|':'
newline|'\n'
indent|'                        '
name|'with'
name|'open'
op|'('
name|'filename'
op|')'
name|'as'
name|'part'
op|':'
newline|'\n'
indent|'                            '
name|'shutil'
op|'.'
name|'copyfileobj'
op|'('
name|'part'
op|','
name|'combined'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to download %(image_location)s "'
nl|'\n'
string|'"to %(image_path)s"'
op|')'
op|','
name|'log_vars'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'failed_download'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'decrypting'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'hex_key'
op|'='
name|'manifest'
op|'.'
name|'find'
op|'('
string|"'image/ec2_encrypted_key'"
op|')'
op|'.'
name|'text'
newline|'\n'
name|'encrypted_key'
op|'='
name|'binascii'
op|'.'
name|'a2b_hex'
op|'('
name|'hex_key'
op|')'
newline|'\n'
name|'hex_iv'
op|'='
name|'manifest'
op|'.'
name|'find'
op|'('
string|"'image/ec2_encrypted_iv'"
op|')'
op|'.'
name|'text'
newline|'\n'
name|'encrypted_iv'
op|'='
name|'binascii'
op|'.'
name|'a2b_hex'
op|'('
name|'hex_iv'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME(vish): grab key from common service so this can run on'
nl|'\n'
comment|'#              any host.'
nl|'\n'
name|'cloud_pk'
op|'='
name|'crypto'
op|'.'
name|'key_path'
op|'('
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'dec_filename'
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
name|'self'
op|'.'
name|'_decrypt_image'
op|'('
name|'enc_filename'
op|','
name|'encrypted_key'
op|','
nl|'\n'
name|'encrypted_iv'
op|','
name|'cloud_pk'
op|','
nl|'\n'
name|'dec_filename'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to decrypt %(image_location)s "'
nl|'\n'
string|'"to %(image_path)s"'
op|')'
op|','
name|'log_vars'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'failed_decrypt'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'untarring'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'unz_filename'
op|'='
name|'self'
op|'.'
name|'_untarzip_image'
op|'('
name|'image_path'
op|','
name|'dec_filename'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to untar %(image_location)s "'
nl|'\n'
string|'"to %(image_path)s"'
op|')'
op|','
name|'log_vars'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'failed_untar'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'uploading'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'open'
op|'('
name|'unz_filename'
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
nl|'\n'
name|'metadata'
op|','
name|'image_file'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to upload %(image_location)s "'
nl|'\n'
string|'"to %(image_path)s"'
op|')'
op|','
name|'log_vars'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'failed_upload'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|'='
string|"'available'"
newline|'\n'
name|'metadata'
op|'['
string|"'status'"
op|']'
op|'='
string|"'active'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_uuid'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'image_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'eventlet'
op|'.'
name|'spawn_n'
op|'('
name|'delayed_create'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'image'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_decrypt_image
name|'def'
name|'_decrypt_image'
op|'('
name|'encrypted_filename'
op|','
name|'encrypted_key'
op|','
name|'encrypted_iv'
op|','
nl|'\n'
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
string|"'openssl'"
op|','
nl|'\n'
string|"'rsautl'"
op|','
nl|'\n'
string|"'-decrypt'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
string|"'%s'"
op|'%'
name|'cloud_private_key'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'encrypted_key'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
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
name|'_'
op|'('
string|"'Failed to decrypt private key: %s'"
op|')'
nl|'\n'
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
string|"'openssl'"
op|','
nl|'\n'
string|"'rsautl'"
op|','
nl|'\n'
string|"'-decrypt'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
string|"'%s'"
op|'%'
name|'cloud_private_key'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'encrypted_iv'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
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
name|'_'
op|'('
string|"'Failed to decrypt initialization '"
nl|'\n'
string|"'vector: %s'"
op|')'
op|'%'
name|'err'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'enc'"
op|','
nl|'\n'
string|"'-d'"
op|','
string|"'-aes-128-cbc'"
op|','
nl|'\n'
string|"'-in'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'encrypted_filename'
op|','
op|')'
op|','
nl|'\n'
string|"'-K'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'key'
op|','
op|')'
op|','
nl|'\n'
string|"'-iv'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'iv'
op|','
op|')'
op|','
nl|'\n'
string|"'-out'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'decrypted_filename'
op|','
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
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
name|'_'
op|'('
string|"'Failed to decrypt image file '"
nl|'\n'
string|"'%(image_file)s: %(err)s'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'image_file'"
op|':'
name|'encrypted_filename'
op|','
nl|'\n'
string|"'err'"
op|':'
name|'err'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_test_for_malicious_tarball
name|'def'
name|'_test_for_malicious_tarball'
op|'('
name|'path'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Raises exception if extracting tarball would escape extract path"""'
newline|'\n'
name|'tar_file'
op|'='
name|'tarfile'
op|'.'
name|'open'
op|'('
name|'filename'
op|','
string|"'r|gz'"
op|')'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'tar_file'
op|'.'
name|'getnames'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
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
name|'path'
op|','
name|'n'
op|')'
op|')'
op|'.'
name|'startswith'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'tar_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Unsafe filenames in image'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'tar_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_untarzip_image
name|'def'
name|'_untarzip_image'
op|'('
name|'path'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'S3ImageService'
op|'.'
name|'_test_for_malicious_tarball'
op|'('
name|'path'
op|','
name|'filename'
op|')'
newline|'\n'
name|'tar_file'
op|'='
name|'tarfile'
op|'.'
name|'open'
op|'('
name|'filename'
op|','
string|"'r|gz'"
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
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'image_file'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
