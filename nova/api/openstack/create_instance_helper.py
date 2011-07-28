begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
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
string|"'nova.api.openstack.create_instance_helper'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateFault
name|'class'
name|'CreateFault'
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
string|'"Invalid parameters given to create_instance."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'fault'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fault'
op|'='
name|'fault'
newline|'\n'
name|'super'
op|'('
name|'CreateFault'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateInstanceHelper
dedent|''
dedent|''
name|'class'
name|'CreateInstanceHelper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This is the base class for OS API Controllers that\n    are capable of creating instances (currently Servers and Zones).\n\n    Once we stabilize the Zones portion of the API we may be able\n    to move this code back into servers.py\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We need the image service to create an instance."""'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'controller'
newline|'\n'
name|'self'
op|'.'
name|'_image_service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\n'
name|'super'
op|'('
name|'CreateInstanceHelper'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_instance
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|','
name|'create_method'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new server for the given user. The approach\n        used depends on the create_method. For example, the standard\n        POST /server call uses compute.api.create(), while\n        POST /zones/server uses compute.api.create_all_at_once().\n\n        The problem is, both approaches return different values (i.e.\n        [instance dicts] vs. reservation_id). So the handling of the\n        return type from this method is left to the caller.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
string|"'server'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'server_dict'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_server_admin_password'
op|'('
name|'server_dict'
op|')'
newline|'\n'
nl|'\n'
name|'key_name'
op|'='
name|'None'
newline|'\n'
name|'key_data'
op|'='
name|'None'
newline|'\n'
name|'key_pairs'
op|'='
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'.'
name|'get_key_pairs'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'key_pairs'
op|':'
newline|'\n'
indent|'            '
name|'key_pair'
op|'='
name|'key_pairs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'key_name'
op|'='
name|'key_pair'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'key_data'
op|'='
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'image_href'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_image_ref_from_req_data'
op|'('
name|'body'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_service'
op|','
name|'image_id'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'get_image_service'
op|'('
name|'image_href'
op|')'
newline|'\n'
name|'kernel_id'
op|','
name|'ramdisk_id'
op|'='
name|'self'
op|'.'
name|'_get_kernel_ramdisk_from_image'
op|'('
nl|'\n'
name|'req'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'images'
op|'='
name|'set'
op|'('
op|'['
name|'str'
op|'('
name|'x'
op|'['
string|"'id'"
op|']'
op|')'
name|'for'
name|'x'
name|'in'
name|'image_service'
op|'.'
name|'index'
op|'('
name|'context'
op|')'
op|']'
op|')'
newline|'\n'
name|'assert'
name|'str'
op|'('
name|'image_id'
op|')'
name|'in'
name|'images'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot find requested image %(image_href)s: %(e)s"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'personality'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'personality'"
op|')'
newline|'\n'
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'personality'
op|':'
newline|'\n'
indent|'            '
name|'injected_files'
op|'='
name|'self'
op|'.'
name|'_get_injected_files'
op|'('
name|'personality'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor_id'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_flavor_id_from_req_data'
op|'('
name|'body'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid flavorRef provided."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
string|"'name'"
name|'in'
name|'server_dict'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Server name is not defined"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'zone_blob'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|')'
newline|'\n'
name|'name'
op|'='
name|'server_dict'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_validate_server_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'name'
op|'='
name|'name'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'reservation_id'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'reservation_id'"
op|')'
newline|'\n'
name|'min_count'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'min_count'"
op|')'
newline|'\n'
name|'max_count'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'max_count'"
op|')'
newline|'\n'
comment|'# min_count and max_count are optional.  If they exist, they come'
nl|'\n'
comment|"# in as strings.  We want to default 'min_count' to 1, and default"
nl|'\n'
comment|"# 'max_count' to be 'min_count'."
nl|'\n'
name|'min_count'
op|'='
name|'int'
op|'('
name|'min_count'
op|')'
name|'if'
name|'min_count'
name|'else'
number|'1'
newline|'\n'
name|'max_count'
op|'='
name|'int'
op|'('
name|'max_count'
op|')'
name|'if'
name|'max_count'
name|'else'
name|'min_count'
newline|'\n'
name|'if'
name|'min_count'
op|'>'
name|'max_count'
op|':'
newline|'\n'
indent|'            '
name|'min_count'
op|'='
name|'max_count'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
newline|'\n'
name|'extra_values'
op|'='
op|'{'
nl|'\n'
string|"'instance_type'"
op|':'
name|'inst_type'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'password'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'extra_values'
op|','
nl|'\n'
name|'create_method'
op|'('
name|'context'
op|','
nl|'\n'
name|'inst_type'
op|','
nl|'\n'
name|'image_id'
op|','
nl|'\n'
name|'kernel_id'
op|'='
name|'kernel_id'
op|','
nl|'\n'
name|'ramdisk_id'
op|'='
name|'ramdisk_id'
op|','
nl|'\n'
name|'display_name'
op|'='
name|'name'
op|','
nl|'\n'
name|'display_description'
op|'='
name|'name'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'key_name'
op|','
nl|'\n'
name|'key_data'
op|'='
name|'key_data'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'password'
op|','
nl|'\n'
name|'zone_blob'
op|'='
name|'zone_blob'
op|','
nl|'\n'
name|'reservation_id'
op|'='
name|'reservation_id'
op|','
nl|'\n'
name|'min_count'
op|'='
name|'min_count'
op|','
nl|'\n'
name|'max_count'
op|'='
name|'max_count'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'quota'
op|'.'
name|'QuotaError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_handle_quota_error'
op|'('
name|'error'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotFound'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Can not find requested image"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid flavorRef provided."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
comment|'# Let the caller deal with unhandled exceptions.'
nl|'\n'
nl|'\n'
DECL|member|_handle_quota_error
dedent|''
dedent|''
name|'def'
name|'_handle_quota_error'
op|'('
name|'self'
op|','
name|'error'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Reraise quota errors as api-specific http exceptions\n        """'
newline|'\n'
name|'if'
name|'error'
op|'.'
name|'code'
op|'=='
string|'"OnsetFileLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Personality file limit exceeded"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'error'
op|'.'
name|'code'
op|'=='
string|'"OnsetFilePathLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Personality file path too long"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'error'
op|'.'
name|'code'
op|'=='
string|'"OnsetFileContentLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Personality file content too long"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
comment|'# if the original error is okay, just reraise it'
nl|'\n'
dedent|''
name|'raise'
name|'error'
newline|'\n'
nl|'\n'
DECL|member|_deserialize_create
dedent|''
name|'def'
name|'_deserialize_create'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Deserialize a create request\n\n        Overrides normal behavior in the case of xml content\n        """'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'content_type'
op|'=='
string|'"application/xml"'
op|':'
newline|'\n'
indent|'            '
name|'deserializer'
op|'='
name|'ServerXMLDeserializer'
op|'('
op|')'
newline|'\n'
name|'return'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'request'
op|'.'
name|'body'
op|','
name|'request'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_server_name
dedent|''
dedent|''
name|'def'
name|'_validate_server_name'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'value'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Server name is not a string or unicode"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'value'
op|'.'
name|'strip'
op|'('
op|')'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Server name is an empty string"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_kernel_ramdisk_from_image
dedent|''
dedent|''
name|'def'
name|'_get_kernel_ramdisk_from_image'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetch an image from the ImageService, then if present, return the\n        associated kernel and ramdisk image IDs.\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
comment|'# NOTE(sirp): extracted to a separate method to aid unit-testing, the'
nl|'\n'
comment|"# new method doesn't need a request obj or an ImageService stub"
nl|'\n'
name|'kernel_id'
op|','
name|'ramdisk_id'
op|'='
name|'self'
op|'.'
name|'_do_get_kernel_ramdisk_from_image'
op|'('
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'kernel_id'
op|','
name|'ramdisk_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_do_get_kernel_ramdisk_from_image
name|'def'
name|'_do_get_kernel_ramdisk_from_image'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Given an ImageService image_meta, return kernel and ramdisk image\n        ids if present.\n\n        This is only valid for `ami` style images.\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'image_meta'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'if'
name|'image_meta'
op|'['
string|"'status'"
op|']'
op|'!='
string|"'active'"
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
name|'image_id'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"status is not active"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'image_meta'
op|'.'
name|'get'
op|'('
string|"'container_format'"
op|')'
op|'!='
string|"'ami'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'kernel_id'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'kernel_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'KernelNotFoundForImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ramdisk_id'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'ramdisk_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'RamdiskNotFoundForImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'kernel_id'
op|','
name|'ramdisk_id'
newline|'\n'
nl|'\n'
DECL|member|_get_injected_files
dedent|''
name|'def'
name|'_get_injected_files'
op|'('
name|'self'
op|','
name|'personality'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a list of injected files from the personality attribute\n\n        At this time, injected_files must be formatted as a list of\n        (file_path, file_content) pairs for compatibility with the\n        underlying compute service.\n        """'
newline|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'personality'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'path'
op|'='
name|'item'
op|'['
string|"'path'"
op|']'
newline|'\n'
name|'contents'
op|'='
name|'item'
op|'['
string|"'contents'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
name|'as'
name|'key'
op|':'
newline|'\n'
indent|'                '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Bad personality format: missing %s'"
op|')'
op|'%'
name|'key'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Bad personality format'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'contents'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'contents'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Personality content for %s cannot be decoded'"
op|')'
op|'%'
name|'path'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'injected_files'
op|'.'
name|'append'
op|'('
op|'('
name|'path'
op|','
name|'contents'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'injected_files'
newline|'\n'
nl|'\n'
DECL|member|_get_server_admin_password_old_style
dedent|''
name|'def'
name|'_get_server_admin_password_old_style'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Determine the admin password for a server on creation """'
newline|'\n'
name|'return'
name|'utils'
op|'.'
name|'generate_password'
op|'('
number|'16'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_server_admin_password_new_style
dedent|''
name|'def'
name|'_get_server_admin_password_new_style'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Determine the admin password for a server on creation """'
newline|'\n'
name|'password'
op|'='
name|'server'
op|'.'
name|'get'
op|'('
string|"'adminPass'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'generate_password'
op|'('
number|'16'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'password'
op|','
name|'basestring'
op|')'
name|'or'
name|'password'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid adminPass"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'password'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerXMLDeserializer
dedent|''
dedent|''
name|'class'
name|'ServerXMLDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Deserializer to handle xml-formatted server create requests.\n\n    Handles standard server attributes as well as optional metadata\n    and personality attributes\n    """'
newline|'\n'
nl|'\n'
DECL|member|action
name|'def'
name|'action'
op|'('
name|'self'
op|','
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'string'
op|')'
newline|'\n'
name|'action_node'
op|'='
name|'dom'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
newline|'\n'
name|'action_name'
op|'='
name|'action_node'
op|'.'
name|'tagName'
newline|'\n'
nl|'\n'
name|'action_deserializer'
op|'='
op|'{'
nl|'\n'
string|"'createImage'"
op|':'
name|'self'
op|'.'
name|'_action_create_image'
op|','
nl|'\n'
string|"'createBackup'"
op|':'
name|'self'
op|'.'
name|'_action_create_image'
op|','
nl|'\n'
op|'}'
op|'.'
name|'get'
op|'('
name|'action_name'
op|','
name|'self'
op|'.'
name|'default'
op|')'
newline|'\n'
nl|'\n'
name|'action_data'
op|'='
name|'action_deserializer'
op|'('
name|'action_node'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
name|'action_name'
op|':'
name|'action_data'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_action_create_image
dedent|''
name|'def'
name|'_action_create_image'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'value'
op|'='
name|'node'
op|'.'
name|'getAttribute'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'if'
name|'value'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'name'"
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'node'
op|','
string|"'metadata'"
op|')'
newline|'\n'
name|'data'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|_action_create_image
dedent|''
name|'def'
name|'_action_create_image'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'attributes'
op|'='
op|'['
string|"'name'"
op|','
string|"'backup_type'"
op|','
string|"'rotation'"
op|']'
newline|'\n'
name|'for'
name|'attribute'
name|'in'
name|'attributes'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'node'
op|'.'
name|'getAttribute'
op|'('
name|'attribute'
op|')'
newline|'\n'
name|'if'
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'['
name|'attribute'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'node'
op|','
string|"'metadata'"
op|')'
newline|'\n'
name|'data'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deserialize an xml-formatted server create request"""'
newline|'\n'
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'string'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_extract_server'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_extract_server
dedent|''
name|'def'
name|'_extract_server'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the server attribute of a parsed request"""'
newline|'\n'
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'server_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'node'
op|','
string|"'server'"
op|')'
newline|'\n'
nl|'\n'
name|'attributes'
op|'='
op|'['
string|'"name"'
op|','
string|'"imageId"'
op|','
string|'"flavorId"'
op|','
string|'"imageRef"'
op|','
nl|'\n'
string|'"flavorRef"'
op|','
string|'"adminPass"'
op|']'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'attributes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'server_node'
op|'.'
name|'getAttribute'
op|'('
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'server'
op|'['
name|'attr'
op|']'
op|'='
name|'server_node'
op|'.'
name|'getAttribute'
op|'('
name|'attr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'server_node'
op|','
string|'"metadata"'
op|')'
newline|'\n'
name|'server'
op|'['
string|'"metadata"'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'['
string|'"personality"'
op|']'
op|'='
name|'self'
op|'.'
name|'_extract_personality'
op|'('
name|'server_node'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|_extract_personality
dedent|''
name|'def'
name|'_extract_personality'
op|'('
name|'self'
op|','
name|'server_node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the personality attribute of a parsed request"""'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'server_node'
op|','
string|'"personality"'
op|')'
newline|'\n'
name|'personality'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'file_node'
name|'in'
name|'self'
op|'.'
name|'find_children_named'
op|'('
name|'node'
op|','
string|'"file"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'file_node'
op|'.'
name|'hasAttribute'
op|'('
string|'"path"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'item'
op|'['
string|'"path"'
op|']'
op|'='
name|'file_node'
op|'.'
name|'getAttribute'
op|'('
string|'"path"'
op|')'
newline|'\n'
dedent|''
name|'item'
op|'['
string|'"contents"'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_text'
op|'('
name|'file_node'
op|')'
newline|'\n'
name|'personality'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'personality'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
