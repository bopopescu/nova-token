begin_unit
comment|'# Copyright 2015 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'testscenarios'
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
name|'tests'
name|'import'
name|'fixtures'
name|'as'
name|'nova_fixtures'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'policy_fixture'
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
nl|'\n'
DECL|class|SecgroupsFullstack
name|'class'
name|'SecgroupsFullstack'
op|'('
name|'testscenarios'
op|'.'
name|'WithScenarios'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests for security groups\n\n    TODO: describe security group API\n\n    TODO: define scope\n\n    """'
newline|'\n'
DECL|variable|REQUIRES_LOCKING
name|'REQUIRES_LOCKING'
op|'='
name|'True'
newline|'\n'
DECL|variable|_image_ref_parameter
name|'_image_ref_parameter'
op|'='
string|"'imageRef'"
newline|'\n'
DECL|variable|_flavor_ref_parameter
name|'_flavor_ref_parameter'
op|'='
string|"'flavorRef'"
newline|'\n'
nl|'\n'
comment|'# This test uses ``testscenarios`` which matrix multiplies the'
nl|'\n'
comment|'# test across the scenarios listed below setting the attributres'
nl|'\n'
comment|'# in the dictionary on ``self`` for each scenario.'
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
nl|'\n'
op|'('
string|"'v2'"
op|','
op|'{'
nl|'\n'
string|"'api_major_version'"
op|':'
string|"'v2'"
op|'}'
op|')'
op|','
nl|'\n'
comment|'# test v2.1 base microversion'
nl|'\n'
op|'('
string|"'v2_1'"
op|','
op|'{'
nl|'\n'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|','
nl|'\n'
op|']'
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
name|'super'
op|'('
name|'SecgroupsFullstack'
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
name|'useFixture'
op|'('
name|'policy_fixture'
op|'.'
name|'RealPolicyFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'api_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'nova_fixtures'
op|'.'
name|'OSAPIFixture'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'api_fixture'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
comment|'# the image fake backend needed for image discovery'
nl|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(sdague): refactor this method into the API client, we're"
nl|'\n'
comment|'# going to use it a lot'
nl|'\n'
DECL|member|_build_minimal_create_server_request
dedent|''
name|'def'
name|'_build_minimal_create_server_request'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_images'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"Image: %s"'
op|'%'
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_image_ref_parameter'
name|'in'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'image_href'
op|'='
name|'image'
op|'['
name|'self'
op|'.'
name|'_image_ref_parameter'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'image_href'
op|'='
name|'image'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_href'
op|'='
string|"'http://fake.server/%s'"
op|'%'
name|'image_href'
newline|'\n'
nl|'\n'
comment|'# We now have a valid imageId'
nl|'\n'
dedent|''
name|'server'
op|'['
name|'self'
op|'.'
name|'_image_ref_parameter'
op|']'
op|'='
name|'image_href'
newline|'\n'
nl|'\n'
comment|'# Set a valid flavorId'
nl|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_flavors'
op|'('
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'server'
op|'['
name|'self'
op|'.'
name|'_flavor_ref_parameter'
op|']'
op|'='
op|'('
string|"'http://fake.server/%s'"
nl|'\n'
op|'%'
name|'flavor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|'='
name|'name'
newline|'\n'
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_fuzz
dedent|''
name|'def'
name|'test_security_group_fuzz'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test security group doesn\'t explode with a 500 on bad input.\n\n        Originally reported with bug\n        https://bugs.launchpad.net/nova/+bug/1239723\n\n        """'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
string|'"sg-fuzz"'
op|')'
newline|'\n'
comment|'# security groups must be passed as a list, this is an invalid'
nl|'\n'
comment|'# format. The jsonschema in v2.1 caught it automatically, but'
nl|'\n'
comment|'# in v2 we used to throw a 500.'
nl|'\n'
name|'server'
op|'['
string|"'security_groups'"
op|']'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"sec"'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'/servers'"
op|','
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
op|','
nl|'\n'
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
