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
nl|'\n'
string|'"""\nTest suites for \'common\' code used throughout the OpenStack HTTP API.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
name|'import'
name|'xml'
op|'.'
name|'dom'
op|'.'
name|'minidom'
name|'as'
name|'minidom'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'Request'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimiterTest
name|'class'
name|'LimiterTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Unit tests for the `nova.api.openstack.common.limited` method which takes\n    in a list of items and, depending on the \'offset\' and \'limit\' GET params,\n    returns a subset or complete set of the given items.\n    """'
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
string|'""" Run before each test. """'
newline|'\n'
name|'super'
op|'('
name|'LimiterTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tiny'
op|'='
name|'range'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'small'
op|'='
name|'range'
op|'('
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'medium'
op|'='
name|'range'
op|'('
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'large'
op|'='
name|'range'
op|'('
number|'10000'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_offset_zero
dedent|''
name|'def'
name|'test_limiter_offset_zero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test offset key works with 0. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'tiny'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'small'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'medium'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
op|':'
number|'1000'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_offset_medium
dedent|''
name|'def'
name|'test_limiter_offset_medium'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test offset key works with a medium sized number. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'small'
op|'['
number|'10'
op|':'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'medium'
op|'['
number|'10'
op|':'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
number|'10'
op|':'
number|'1010'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_offset_over_max
dedent|''
name|'def'
name|'test_limiter_offset_over_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test offset key works with a number over 1000 (max_limit). """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=1001'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
number|'1001'
op|':'
number|'2001'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_offset_blank
dedent|''
name|'def'
name|'test_limiter_offset_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test offset key works with a blank offset. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset='"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'common'
op|'.'
name|'limited'
op|','
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_offset_bad
dedent|''
name|'def'
name|'test_limiter_offset_bad'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test offset key works with a BAD offset. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"u'/?offset=\\u0020aa'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'common'
op|'.'
name|'limited'
op|','
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_nothing
dedent|''
name|'def'
name|'test_limiter_nothing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test request with no offset or limit """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'tiny'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'small'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'medium'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
op|':'
number|'1000'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_limit_zero
dedent|''
name|'def'
name|'test_limiter_limit_zero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test limit of zero. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'tiny'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'small'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'medium'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
op|':'
number|'1000'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_limit_medium
dedent|''
name|'def'
name|'test_limiter_limit_medium'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test limit of 10. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'tiny'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'small'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'medium'
op|'['
op|':'
number|'10'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
op|':'
number|'10'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_limit_over_max
dedent|''
name|'def'
name|'test_limiter_limit_over_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test limit of 3000. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=3000'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'tiny'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'small'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'small'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'medium'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'medium'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'self'
op|'.'
name|'large'
op|','
name|'req'
op|')'
op|','
name|'self'
op|'.'
name|'large'
op|'['
op|':'
number|'1000'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_limit_and_offset
dedent|''
name|'def'
name|'test_limiter_limit_and_offset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test request with both limit and offset. """'
newline|'\n'
name|'items'
op|'='
name|'range'
op|'('
number|'2000'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=1&limit=3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
op|','
name|'items'
op|'['
number|'1'
op|':'
number|'4'
op|']'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=3&limit=0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
op|','
name|'items'
op|'['
number|'3'
op|':'
number|'1003'
op|']'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=3&limit=1500'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
op|','
name|'items'
op|'['
number|'3'
op|':'
number|'1003'
op|']'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=3000&limit=10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_custom_max_limit
dedent|''
name|'def'
name|'test_limiter_custom_max_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test a max_limit other than 1000. """'
newline|'\n'
name|'items'
op|'='
name|'range'
op|'('
number|'2000'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=1&limit=3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|','
name|'max_limit'
op|'='
number|'2000'
op|')'
op|','
name|'items'
op|'['
number|'1'
op|':'
number|'4'
op|']'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=3&limit=0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|','
name|'max_limit'
op|'='
number|'2000'
op|')'
op|','
name|'items'
op|'['
number|'3'
op|':'
op|']'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=3&limit=2500'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|','
name|'max_limit'
op|'='
number|'2000'
op|')'
op|','
name|'items'
op|'['
number|'3'
op|':'
op|']'
op|')'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=3000&limit=10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|','
name|'max_limit'
op|'='
number|'2000'
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_negative_limit
dedent|''
name|'def'
name|'test_limiter_negative_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test a negative limit. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=-3000'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'common'
op|'.'
name|'limited'
op|','
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiter_negative_offset
dedent|''
name|'def'
name|'test_limiter_negative_offset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test a negative offset. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?offset=-30'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'common'
op|'.'
name|'limited'
op|','
name|'self'
op|'.'
name|'tiny'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PaginationParamsTest
dedent|''
dedent|''
name|'class'
name|'PaginationParamsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Unit tests for the `nova.api.openstack.common.get_pagination_params`\n    method which takes in a request object and returns \'marker\' and \'limit\'\n    GET params.\n    """'
newline|'\n'
nl|'\n'
DECL|member|test_no_params
name|'def'
name|'test_no_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test no params. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_valid_marker
dedent|''
name|'def'
name|'test_valid_marker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test valid marker param. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?marker=1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
op|','
op|'{'
string|"'marker'"
op|':'
number|'1'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_marker
dedent|''
name|'def'
name|'test_invalid_marker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test invalid marker param. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?marker=-2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'common'
op|'.'
name|'get_pagination_params'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_valid_limit
dedent|''
name|'def'
name|'test_valid_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test valid limit param. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
op|','
op|'{'
string|"'limit'"
op|':'
number|'10'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_limit
dedent|''
name|'def'
name|'test_invalid_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test invalid limit param. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=-2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'common'
op|'.'
name|'get_pagination_params'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_valid_limit_and_marker
dedent|''
name|'def'
name|'test_valid_limit_and_marker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Test valid limit and marker parameters. """'
newline|'\n'
name|'req'
op|'='
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/?limit=20&marker=40'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
op|','
nl|'\n'
op|'{'
string|"'marker'"
op|':'
number|'40'
op|','
string|"'limit'"
op|':'
number|'20'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MiscFunctionsTest
dedent|''
dedent|''
name|'class'
name|'MiscFunctionsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href
indent|'    '
name|'def'
name|'test_remove_version_from_href'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v1.1/images'"
newline|'\n'
name|'expected'
op|'='
string|"'http://www.testsite.com/images'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'remove_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href_2
dedent|''
name|'def'
name|'test_remove_version_from_href_2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v1.1/'"
newline|'\n'
name|'expected'
op|'='
string|"'http://www.testsite.com/'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'remove_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href_3
dedent|''
name|'def'
name|'test_remove_version_from_href_3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v10.10'"
newline|'\n'
name|'expected'
op|'='
string|"'http://www.testsite.com'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'remove_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href_4
dedent|''
name|'def'
name|'test_remove_version_from_href_4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v1.1/images/v10.5'"
newline|'\n'
name|'expected'
op|'='
string|"'http://www.testsite.com/images/v10.5'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'remove_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href_bad_request
dedent|''
name|'def'
name|'test_remove_version_from_href_bad_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/1.1/images'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
nl|'\n'
name|'common'
op|'.'
name|'remove_version_from_href'
op|','
nl|'\n'
name|'fixture'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href_bad_request_2
dedent|''
name|'def'
name|'test_remove_version_from_href_bad_request_2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v/images'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
nl|'\n'
name|'common'
op|'.'
name|'remove_version_from_href'
op|','
nl|'\n'
name|'fixture'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_version_from_href_bad_request_3
dedent|''
name|'def'
name|'test_remove_version_from_href_bad_request_3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v1.1images'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
nl|'\n'
name|'common'
op|'.'
name|'remove_version_from_href'
op|','
nl|'\n'
name|'fixture'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_id_from_href
dedent|''
name|'def'
name|'test_get_id_from_href'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/dir/45'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'get_id_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'expected'
op|'='
number|'45'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_id_from_href_bad_request
dedent|''
name|'def'
name|'test_get_id_from_href_bad_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://45'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
nl|'\n'
name|'common'
op|'.'
name|'get_id_from_href'
op|','
nl|'\n'
name|'fixture'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_from_href
dedent|''
name|'def'
name|'test_get_version_from_href'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v1.1/images'"
newline|'\n'
name|'expected'
op|'='
string|"'1.1'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'get_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_from_href_2
dedent|''
name|'def'
name|'test_get_version_from_href_2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/v1.1'"
newline|'\n'
name|'expected'
op|'='
string|"'1.1'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'get_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_from_href_default
dedent|''
name|'def'
name|'test_get_version_from_href_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
string|"'http://www.testsite.com/images'"
newline|'\n'
name|'expected'
op|'='
string|"'1.0'"
newline|'\n'
name|'actual'
op|'='
name|'common'
op|'.'
name|'get_version_from_href'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataXMLDeserializationTest
dedent|''
dedent|''
name|'class'
name|'MetadataXMLDeserializationTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|deserializer
indent|'    '
name|'deserializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_body'
op|'='
string|'"""\n        <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n            <meta key=\'123\'>asdf</meta>\n            <meta key=\'567\'>jkl;</meta>\n        </metadata>"""'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request_body'
op|','
string|"'create'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"body"'
op|':'
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"123"'
op|':'
string|'"asdf"'
op|','
string|'"567"'
op|':'
string|'"jkl;"'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'output'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_empty
dedent|''
name|'def'
name|'test_create_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_body'
op|'='
string|'"""\n        <metadata xmlns="http://docs.openstack.org/compute/api/v1.1"/>"""'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request_body'
op|','
string|"'create'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"body"'
op|':'
op|'{'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'output'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all
dedent|''
name|'def'
name|'test_update_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_body'
op|'='
string|'"""\n        <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n            <meta key=\'123\'>asdf</meta>\n            <meta key=\'567\'>jkl;</meta>\n        </metadata>"""'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request_body'
op|','
string|"'update_all'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"body"'
op|':'
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"123"'
op|':'
string|'"asdf"'
op|','
string|'"567"'
op|':'
string|'"jkl;"'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'output'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update
dedent|''
name|'def'
name|'test_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_body'
op|'='
string|'"""\n        <meta xmlns="http://docs.openstack.org/compute/api/v1.1"\n              key=\'123\'>asdf</meta>"""'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request_body'
op|','
string|"'update'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"body"'
op|':'
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"123"'
op|':'
string|'"asdf"'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'output'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataXMLSerializationTest
dedent|''
dedent|''
name|'class'
name|'MetadataXMLSerializationTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_index
indent|'    '
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'one'"
op|':'
string|"'two'"
op|','
nl|'\n'
string|"'three'"
op|':'
string|"'four'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'index'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n            <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n                <meta key="three">\n                    four\n                </meta>\n                <meta key="one">\n                    two\n                </meta>\n            </metadata>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_null
dedent|''
name|'def'
name|'test_index_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
name|'None'
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'index'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n            <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n                <meta key="None">\n                    None\n                </meta>\n            </metadata>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_unicode
dedent|''
name|'def'
name|'test_index_unicode'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"u'three'"
op|':'
string|"u'Jos\\xe9'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'index'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'u"""\n            <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n                <meta key="three">\n                    Jos\\xe9\n                </meta>\n            </metadata>\n        """'
op|'.'
name|'encode'
op|'('
string|'"UTF-8"'
op|')'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'meta'"
op|':'
op|'{'
nl|'\n'
string|"'one'"
op|':'
string|"'two'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'show'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n            <meta xmlns="http://docs.openstack.org/compute/api/v1.1" key="one">\n                two\n            </meta>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all
dedent|''
name|'def'
name|'test_update_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'key6'"
op|':'
string|"'value6'"
op|','
nl|'\n'
string|"'key4'"
op|':'
string|"'value4'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'update_all'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n            <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n                <meta key="key6">\n                    value6\n                </meta>\n                <meta key="key4">\n                    value4\n                </meta>\n            </metadata>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item
dedent|''
name|'def'
name|'test_update_item'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'meta'"
op|':'
op|'{'
nl|'\n'
string|"'one'"
op|':'
string|"'two'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'update'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n            <meta xmlns="http://docs.openstack.org/compute/api/v1.1" key="one">\n                two\n            </meta>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'key9'"
op|':'
string|"'value9'"
op|','
nl|'\n'
string|"'key2'"
op|':'
string|"'value2'"
op|','
nl|'\n'
string|"'key1'"
op|':'
string|"'value1'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|','
string|"'create'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n            <metadata xmlns="http://docs.openstack.org/compute/api/v1.1">\n                <meta key="key2">\n                    value2\n                </meta>\n                <meta key="key9">\n                    value9\n                </meta>\n                <meta key="key1">\n                    value1\n                </meta>\n            </metadata>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'None'
op|','
string|"'delete'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
