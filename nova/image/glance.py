begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""Implementation of an image service that uses Glance as the backend"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'absolute_import'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'iso8601'
newline|'\n'
nl|'\n'
name|'from'
name|'glance'
op|'.'
name|'common'
name|'import'
name|'exception'
name|'as'
name|'glance_exception'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'service'
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
string|"'nova.image.glance'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|GlanceClient
name|'GlanceClient'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
string|"'glance.client.Client'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceImageService
name|'class'
name|'GlanceImageService'
op|'('
name|'service'
op|'.'
name|'BaseImageService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provides storage and retrieval of disk image objects within Glance."""'
newline|'\n'
nl|'\n'
DECL|variable|GLANCE_ONLY_ATTRS
name|'GLANCE_ONLY_ATTRS'
op|'='
op|'['
string|'"size"'
op|','
string|'"location"'
op|','
string|'"disk_format"'
op|','
nl|'\n'
string|'"container_format"'
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): Overriding to use _translate_to_service provided by'
nl|'\n'
comment|'# BaseImageService'
nl|'\n'
name|'SERVICE_IMAGE_ATTRS'
op|'='
name|'service'
op|'.'
name|'BaseImageService'
op|'.'
name|'BASE_IMAGE_ATTRS'
op|'+'
DECL|variable|SERVICE_IMAGE_ATTRS
name|'GLANCE_ONLY_ATTRS'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'client'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# FIXME(sirp): can we avoid dependency-injection here by using'
nl|'\n'
comment|'# stubbing out a fake?'
nl|'\n'
indent|'        '
name|'if'
name|'client'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'GlanceClient'
op|'('
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
name|'FLAGS'
op|'.'
name|'glance_port'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'client'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
indent|'        '
string|'"""\n        Calls out to Glance for a list of images available\n        """'
newline|'\n'
comment|'# NOTE(sirp): We need to use `get_images_detailed` and not'
nl|'\n'
comment|'# `get_images` here because we need `is_public` and `properties`'
nl|'\n'
comment|'# included so we can filter by user'
nl|'\n'
name|'filtered'
op|'='
op|'['
op|']'
newline|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'get_images_detailed'
op|'('
op|')'
newline|'\n'
name|'for'
name|'image_meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_is_image_available'
op|'('
name|'context'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'meta_subset'
op|'='
name|'utils'
op|'.'
name|'subset_dict'
op|'('
name|'image_meta'
op|','
op|'('
string|"'id'"
op|','
string|"'name'"
op|')'
op|')'
newline|'\n'
name|'filtered'
op|'.'
name|'append'
op|'('
name|'meta_subset'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'filtered'
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
indent|'        '
string|'"""\n        Calls out to Glance for a list of detailed image information\n        """'
newline|'\n'
name|'filtered'
op|'='
op|'['
op|']'
newline|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'get_images_detailed'
op|'('
op|')'
newline|'\n'
name|'for'
name|'image_meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_is_image_available'
op|'('
name|'context'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_base'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'filtered'
op|'.'
name|'append'
op|'('
name|'base_image_meta'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'filtered'
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
string|'"""\n        Returns a dict containing image data for the given opaque image id.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'get_image_meta'
op|'('
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glance_exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_is_image_available'
op|'('
name|'context'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_base'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
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
string|'"""\n        Returns a dict containing image data for the given name.\n        """'
newline|'\n'
comment|'# TODO(vish): replace this with more efficient call when glance'
nl|'\n'
comment|'#             supports it.'
nl|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'detail'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'image_meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
name|'image_meta'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'image_meta'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
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
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Calls out to Glance for metadata and data and writes data.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|','
name|'image_chunks'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'get_image'
op|'('
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glance_exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'chunk'
name|'in'
name|'image_chunks'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'.'
name|'write'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_base'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
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
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Store the image data and return the new image id.\n\n        :raises AlreadyExists if the image already exist.\n        """'
newline|'\n'
comment|'# Translate Base -> Service'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Creating image in Glance. Metadata passed in %s"'
op|')'
op|','
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
name|'sent_service_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_service'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Metadata after formatting for Glance %s"'
op|')'
op|','
nl|'\n'
name|'sent_service_image_meta'
op|')'
newline|'\n'
nl|'\n'
name|'recv_service_image_meta'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'add_image'
op|'('
nl|'\n'
name|'sent_service_image_meta'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
comment|'# Translate Service -> Base'
nl|'\n'
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_base'
op|'('
name|'recv_service_image_meta'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Metadata returned from Glance formatted for Base %s"'
op|')'
op|','
nl|'\n'
name|'base_image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
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
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the contents of the given image with the new data.\n\n        :raises NotFound if the image does not exist.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'update_image'
op|'('
name|'image_id'
op|','
name|'image_meta'
op|','
name|'data'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glance_exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'base_image_meta'
op|'='
name|'self'
op|'.'
name|'_translate_to_base'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'base_image_meta'
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
string|'"""\n        Delete the given image.\n\n        :raises NotFound if the image does not exist.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'delete_image'
op|'('
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'glance_exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|delete_all
dedent|''
name|'def'
name|'delete_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Clears out all images\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_translate_to_base
name|'def'
name|'_translate_to_base'
op|'('
name|'cls'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Overriding the base translation to handle conversion to datetime\n        objects\n        """'
newline|'\n'
name|'image_meta'
op|'='
name|'service'
op|'.'
name|'BaseImageService'
op|'.'
name|'_translate_to_base'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'_convert_timestamps_to_datetimes'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_is_image_available
name|'def'
name|'_is_image_available'
op|'('
name|'context'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Images are always available if they are public or if the user is an\n        admin.\n\n        Otherwise, we filter by project_id (if present) and then fall-back to\n        images owned by user.\n        """'
newline|'\n'
comment|'# FIXME(sirp): We should be filtering by user_id on the Glance side'
nl|'\n'
comment|"# for security; however, we can't do that until we get authn/authz"
nl|'\n'
comment|'# sorted out. Until then, filtering in Nova.'
nl|'\n'
name|'if'
name|'image_meta'
op|'['
string|"'is_public'"
op|']'
name|'or'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'properties'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'context'
op|'.'
name|'project_id'
name|'and'
op|'('
string|"'project_id'"
name|'in'
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'properties'
op|'['
string|"'project_id'"
op|']'
op|')'
op|'=='
name|'str'
op|'('
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'user_id'
op|'='
name|'properties'
op|'['
string|"'user_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'str'
op|'('
name|'user_id'
op|')'
op|'=='
name|'str'
op|'('
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# utility functions'
nl|'\n'
DECL|function|_convert_timestamps_to_datetimes
dedent|''
dedent|''
name|'def'
name|'_convert_timestamps_to_datetimes'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Returns image with known timestamp fields converted to datetime objects\n    """'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'deleted_at'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'image_meta'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'['
name|'attr'
op|']'
op|'='
name|'_parse_glance_iso8601_timestamp'
op|'('
nl|'\n'
name|'image_meta'
op|'['
name|'attr'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_glance_iso8601_timestamp
dedent|''
name|'def'
name|'_parse_glance_iso8601_timestamp'
op|'('
name|'timestamp'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Parse a subset of iso8601 timestamps into datetime objects\n    """'
newline|'\n'
name|'return'
name|'iso8601'
op|'.'
name|'parse_date'
op|'('
name|'timestamp'
op|')'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
