begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Openstack LLC.'
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
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StubGlanceClient
name|'class'
name|'StubGlanceClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'images'
op|','
name|'add_response'
op|'='
name|'None'
op|','
name|'update_response'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'images'
op|'='
name|'images'
newline|'\n'
name|'self'
op|'.'
name|'add_response'
op|'='
name|'add_response'
newline|'\n'
name|'self'
op|'.'
name|'update_response'
op|'='
name|'update_response'
newline|'\n'
nl|'\n'
DECL|member|set_auth_token
dedent|''
name|'def'
name|'set_auth_token'
op|'('
name|'self'
op|','
name|'auth_tok'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_image_meta
dedent|''
name|'def'
name|'get_image_meta'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_images_detailed
dedent|''
name|'def'
name|'get_images_detailed'
op|'('
name|'self'
op|','
name|'filters'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|','
name|'limit'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'images'
op|'.'
name|'itervalues'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_image
dedent|''
name|'def'
name|'get_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|','
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|add_image
dedent|''
name|'def'
name|'add_image'
op|'('
name|'self'
op|','
name|'metadata'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'add_response'
newline|'\n'
nl|'\n'
DECL|member|update_image
dedent|''
name|'def'
name|'update_image'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'update_response'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NullWriter
dedent|''
dedent|''
name|'class'
name|'NullWriter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used to test ImageService.get which takes a writer object"""'
newline|'\n'
nl|'\n'
DECL|member|write
name|'def'
name|'write'
op|'('
name|'self'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseGlanceTest
dedent|''
dedent|''
name|'class'
name|'BaseGlanceTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|NOW_GLANCE_OLD_FORMAT
indent|'    '
name|'NOW_GLANCE_OLD_FORMAT'
op|'='
string|'"2010-10-11T10:30:22"'
newline|'\n'
DECL|variable|NOW_GLANCE_FORMAT
name|'NOW_GLANCE_FORMAT'
op|'='
string|'"2010-10-11T10:30:22.000000"'
newline|'\n'
DECL|variable|NOW_DATETIME
name|'NOW_DATETIME'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'11'
op|','
number|'10'
op|','
number|'30'
op|','
number|'22'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'='
name|'StubGlanceClient'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'glance'
op|'.'
name|'GlanceImageService'
op|'('
name|'client'
op|'='
name|'self'
op|'.'
name|'client'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertDateTimesFilled
dedent|''
name|'def'
name|'assertDateTimesFilled'
op|'('
name|'self'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'created_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'updated_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'deleted_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertDateTimesEmpty
dedent|''
name|'def'
name|'assertDateTimesEmpty'
op|'('
name|'self'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'updated_at'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'deleted_at'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertDateTimesBlank
dedent|''
name|'def'
name|'assertDateTimesBlank'
op|'('
name|'self'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'updated_at'"
op|']'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'deleted_at'"
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGlanceImageServiceProperties
dedent|''
dedent|''
name|'class'
name|'TestGlanceImageServiceProperties'
op|'('
name|'BaseGlanceTest'
op|')'
op|':'
newline|'\n'
DECL|member|test_show_passes_through_to_client
indent|'    '
name|'def'
name|'test_show_passes_through_to_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure attributes which aren\'t BASE_IMAGE_ATTRS are stored in the\n        properties dict\n        """'
newline|'\n'
name|'fixtures'
op|'='
op|'{'
string|"'image1'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'foo'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'prop1'"
op|':'
string|"'propvalue1'"
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'fixtures'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'prop1'"
op|':'
string|"'propvalue1'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_passes_through_to_client
dedent|''
name|'def'
name|'test_detail_passes_through_to_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'{'
string|"'image1'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'foo'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'prop1'"
op|':'
string|"'propvalue1'"
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'fixtures'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'prop1'"
op|':'
string|"'propvalue1'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGetterDateTimeNoneTests
dedent|''
dedent|''
name|'class'
name|'TestGetterDateTimeNoneTests'
op|'('
name|'BaseGlanceTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_show_handles_none_datetimes
indent|'    '
name|'def'
name|'test_show_handles_none_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_none_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesEmpty'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_handles_blank_datetimes
dedent|''
name|'def'
name|'test_show_handles_blank_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_blank_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesBlank'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_handles_none_datetimes
dedent|''
name|'def'
name|'test_detail_handles_none_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_none_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesEmpty'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_handles_blank_datetimes
dedent|''
name|'def'
name|'test_detail_handles_blank_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_blank_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesBlank'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_handles_none_datetimes
dedent|''
name|'def'
name|'test_get_handles_none_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_none_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'writer'
op|'='
name|'NullWriter'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|','
name|'writer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesEmpty'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_handles_blank_datetimes
dedent|''
name|'def'
name|'test_get_handles_blank_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_blank_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'writer'
op|'='
name|'NullWriter'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|','
name|'writer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesBlank'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_makes_datetimes
dedent|''
name|'def'
name|'test_show_makes_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_makes_datetimes
dedent|''
name|'def'
name|'test_detail_makes_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_makes_datetimes
dedent|''
name|'def'
name|'test_get_makes_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixtures'
op|'('
op|')'
newline|'\n'
name|'writer'
op|'='
name|'NullWriter'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|','
name|'writer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image2'"
op|','
name|'writer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_datetime_fixtures
dedent|''
name|'def'
name|'_make_datetime_fixtures'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'{'
nl|'\n'
string|"'image1'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'image1'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'image2'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'image2'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_OLD_FORMAT'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_OLD_FORMAT'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_OLD_FORMAT'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'fixtures'
newline|'\n'
nl|'\n'
DECL|member|_make_none_datetime_fixtures
dedent|''
name|'def'
name|'_make_none_datetime_fixtures'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'{'
string|"'image1'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
name|'return'
name|'fixtures'
newline|'\n'
nl|'\n'
DECL|member|_make_blank_datetime_fixtures
dedent|''
name|'def'
name|'_make_blank_datetime_fixtures'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'{'
string|"'image1'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'return'
name|'fixtures'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestMutatorDateTimeTests
dedent|''
dedent|''
name|'class'
name|'TestMutatorDateTimeTests'
op|'('
name|'BaseGlanceTest'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests create(), update()"""'
newline|'\n'
nl|'\n'
DECL|member|test_create_handles_datetimes
name|'def'
name|'test_create_handles_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'add_response'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_handles_none_datetimes
dedent|''
name|'def'
name|'test_create_handles_none_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'add_response'
op|'='
name|'self'
op|'.'
name|'_make_none_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'dummy_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'dummy_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesEmpty'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_handles_datetimes
dedent|''
name|'def'
name|'test_update_handles_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
op|'{'
string|"'image1'"
op|':'
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'update_response'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'dummy_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|','
name|'dummy_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesFilled'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_handles_none_datetimes
dedent|''
name|'def'
name|'test_update_handles_none_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'images'
op|'='
op|'{'
string|"'image1'"
op|':'
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'update_response'
op|'='
name|'self'
op|'.'
name|'_make_none_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'dummy_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'image1'"
op|','
name|'dummy_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDateTimesEmpty'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_datetime_fixture
dedent|''
name|'def'
name|'_make_datetime_fixture'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'image1'"
op|','
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|'}'
newline|'\n'
name|'return'
name|'fixture'
newline|'\n'
nl|'\n'
DECL|member|_make_none_datetime_fixture
dedent|''
name|'def'
name|'_make_none_datetime_fixture'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'image1'"
op|','
string|"'name'"
op|':'
string|"'image1'"
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'return'
name|'fixture'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
