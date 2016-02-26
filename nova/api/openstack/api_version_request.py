begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
name|'re'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
comment|'# Define the minimum and maximum version of the API across all of the'
nl|'\n'
comment|'# REST API. The format of the version is:'
nl|'\n'
comment|'# X.Y where:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - X will only be changed if a significant backwards incompatible API'
nl|'\n'
comment|'# change is made which affects the API as whole. That is, something'
nl|'\n'
comment|'# that is only very very rarely incremented.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - Y when you make any change to the API. Note that this includes'
nl|'\n'
comment|'# semantic changes which may not affect the input or output formats or'
nl|'\n'
comment|'# even originate in the API code layer. We are not distinguishing'
nl|'\n'
comment|'# between backwards compatible and backwards incompatible changes in'
nl|'\n'
comment|'# the versioning system. It must be made clear in the documentation as'
nl|'\n'
comment|'# to what is a backwards compatible change and what is a backwards'
nl|'\n'
comment|'# incompatible one.'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# You must update the API version history string below with a one or'
nl|'\n'
comment|'# two line description as well as update rest_api_version_history.rst'
nl|'\n'
name|'REST_API_VERSION_HISTORY'
op|'='
string|'"""REST API Version History:\n\n    * 2.1 - Initial version. Equivalent to v2.0 code\n    * 2.2 - Adds (keypair) type parameter for os-keypairs plugin\n            Fixes success status code for create/delete a keypair method\n    * 2.3 - Exposes additional os-extended-server-attributes\n            Exposes delete_on_termination for os-extended-volumes\n    * 2.4 - Exposes reserved field in os-fixed-ips.\n    * 2.5 - Allow server search option ip6 for non-admin\n    * 2.6 - Consolidate the APIs for getting remote consoles\n    * 2.7 - Check flavor type before add tenant access.\n    * 2.8 - Add new protocol for VM console (mks)\n    * 2.9 - Exposes lock information in server details.\n    * 2.10 - Allow admins to query, create and delete keypairs owned by any\n             user.\n    * 2.11 - Exposes forced_down attribute for os-services\n    * 2.12 - Exposes VIF net-id in os-virtual-interfaces\n    * 2.13 - Add project id and user id information for os-server-groups API\n    * 2.14 - Remove onSharedStorage from evacuate request body and remove\n             adminPass from the response body\n    * 2.15 - Add soft-affinity and soft-anti-affinity policies\n    * 2.16 - Exposes host_status for servers/detail and servers/{server_id}\n    * 2.17 - Add trigger_crash_dump to server actions\n    * 2.18 - Makes project_id optional in v2.1\n    * 2.19 - Allow user to set and get the server description\n    * 2.20 - Add attach and detach volume operations for instances in shelved\n             and shelved_offloaded state\n    * 2.21 - Make os-instance-actions read deleted instances\n    * 2.22 - Add API to force live migration to complete\n    * 2.23 - Add index/show API for server migrations.\n             Also add migration_type for /os-migrations and add ref link for it\n             when the migration is an in progress live migration.\n"""'
newline|'\n'
nl|'\n'
comment|'# The minimum and maximum versions of the API supported'
nl|'\n'
comment|'# The default api version request is defined to be the'
nl|'\n'
comment|'# the minimum version of the API supported.'
nl|'\n'
comment|'# Note(cyeoh): This only applies for the v2.1 API once microversions'
nl|'\n'
comment|'# support is fully merged. It does not affect the V2 API.'
nl|'\n'
DECL|variable|_MIN_API_VERSION
name|'_MIN_API_VERSION'
op|'='
string|'"2.1"'
newline|'\n'
DECL|variable|_MAX_API_VERSION
name|'_MAX_API_VERSION'
op|'='
string|'"2.23"'
newline|'\n'
DECL|variable|DEFAULT_API_VERSION
name|'DEFAULT_API_VERSION'
op|'='
name|'_MIN_API_VERSION'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(cyeoh): min and max versions declared as functions so we can'
nl|'\n'
comment|'# mock them for unittests. Do not use the constants directly anywhere'
nl|'\n'
comment|'# else.'
nl|'\n'
DECL|function|min_api_version
name|'def'
name|'min_api_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'APIVersionRequest'
op|'('
name|'_MIN_API_VERSION'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|max_api_version
dedent|''
name|'def'
name|'max_api_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'APIVersionRequest'
op|'('
name|'_MAX_API_VERSION'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_supported
dedent|''
name|'def'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
name|'_MIN_API_VERSION'
op|','
nl|'\n'
name|'max_version'
op|'='
name|'_MAX_API_VERSION'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if API request version satisfies version restrictions.\n\n    :param req: request object\n    :param min_version: minimal version of API needed for correct\n           request processing\n    :param max_version: maximum version of API needed for correct\n           request processing\n\n    :returns True if request satisfies minimal and maximum API version\n             requirements. False in other case.\n    """'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'APIVersionRequest'
op|'('
name|'max_version'
op|')'
op|'>='
name|'req'
op|'.'
name|'api_version_request'
op|'>='
nl|'\n'
name|'APIVersionRequest'
op|'('
name|'min_version'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIVersionRequest
dedent|''
name|'class'
name|'APIVersionRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This class represents an API Version Request with convenience\n    methods for manipulation and comparison of version\n    numbers that we need to do to implement microversions.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'version_string'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an API version request object.\n\n        :param version_string: String representation of APIVersionRequest.\n            Correct format is \'X.Y\', where \'X\' and \'Y\' are int values.\n            None value should be used to create Null APIVersionRequest,\n            which is equal to 0.0\n        """'
newline|'\n'
name|'self'
op|'.'
name|'ver_major'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'ver_minor'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'if'
name|'version_string'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'match'
op|'='
name|'re'
op|'.'
name|'match'
op|'('
string|'r"^([1-9]\\d*)\\.([1-9]\\d*|0)$"'
op|','
nl|'\n'
name|'version_string'
op|')'
newline|'\n'
name|'if'
name|'match'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'ver_major'
op|'='
name|'int'
op|'('
name|'match'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ver_minor'
op|'='
name|'int'
op|'('
name|'match'
op|'.'
name|'group'
op|'('
number|'2'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidAPIVersionString'
op|'('
name|'version'
op|'='
name|'version_string'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Debug/Logging representation of object."""'
newline|'\n'
name|'return'
op|'('
string|'"API Version Request Major: %s, Minor: %s"'
nl|'\n'
op|'%'
op|'('
name|'self'
op|'.'
name|'ver_major'
op|','
name|'self'
op|'.'
name|'ver_minor'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_null
dedent|''
name|'def'
name|'is_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'ver_major'
op|'=='
number|'0'
name|'and'
name|'self'
op|'.'
name|'ver_minor'
op|'=='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|_format_type_error
dedent|''
name|'def'
name|'_format_type_error'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'TypeError'
op|'('
name|'_'
op|'('
string|'"\'%(other)s\' should be an instance of \'%(cls)s\'"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|'"other"'
op|':'
name|'other'
op|','
string|'"cls"'
op|':'
name|'self'
op|'.'
name|'__class__'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__lt__
dedent|''
name|'def'
name|'__lt__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'other'
op|','
name|'APIVersionRequest'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'self'
op|'.'
name|'_format_type_error'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
op|'('
name|'self'
op|'.'
name|'ver_major'
op|','
name|'self'
op|'.'
name|'ver_minor'
op|')'
op|'<'
nl|'\n'
op|'('
name|'other'
op|'.'
name|'ver_major'
op|','
name|'other'
op|'.'
name|'ver_minor'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'other'
op|','
name|'APIVersionRequest'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'self'
op|'.'
name|'_format_type_error'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
op|'('
name|'self'
op|'.'
name|'ver_major'
op|','
name|'self'
op|'.'
name|'ver_minor'
op|')'
op|'=='
nl|'\n'
op|'('
name|'other'
op|'.'
name|'ver_major'
op|','
name|'other'
op|'.'
name|'ver_minor'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__gt__
dedent|''
name|'def'
name|'__gt__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'other'
op|','
name|'APIVersionRequest'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'self'
op|'.'
name|'_format_type_error'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
op|'('
name|'self'
op|'.'
name|'ver_major'
op|','
name|'self'
op|'.'
name|'ver_minor'
op|')'
op|'>'
nl|'\n'
op|'('
name|'other'
op|'.'
name|'ver_major'
op|','
name|'other'
op|'.'
name|'ver_minor'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__le__
dedent|''
name|'def'
name|'__le__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'<'
name|'other'
name|'or'
name|'self'
op|'=='
name|'other'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ge__
dedent|''
name|'def'
name|'__ge__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'>'
name|'other'
name|'or'
name|'self'
op|'=='
name|'other'
newline|'\n'
nl|'\n'
DECL|member|matches
dedent|''
name|'def'
name|'matches'
op|'('
name|'self'
op|','
name|'min_version'
op|','
name|'max_version'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns whether the version object represents a version\n        greater than or equal to the minimum version and less than\n        or equal to the maximum version.\n\n        @param min_version: Minimum acceptable version.\n        @param max_version: Maximum acceptable version.\n        @returns: boolean\n\n        If min_version is null then there is no minimum limit.\n        If max_version is null then there is no maximum limit.\n        If self is null then raise ValueError\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'is_null'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
newline|'\n'
dedent|''
name|'if'
name|'max_version'
op|'.'
name|'is_null'
op|'('
op|')'
name|'and'
name|'min_version'
op|'.'
name|'is_null'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'max_version'
op|'.'
name|'is_null'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'min_version'
op|'<='
name|'self'
newline|'\n'
dedent|''
name|'elif'
name|'min_version'
op|'.'
name|'is_null'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'<='
name|'max_version'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'min_version'
op|'<='
name|'self'
op|'<='
name|'max_version'
newline|'\n'
nl|'\n'
DECL|member|get_string
dedent|''
dedent|''
name|'def'
name|'get_string'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Converts object to string representation which if used to create\n        an APIVersionRequest object results in the same version request.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'is_null'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
newline|'\n'
dedent|''
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'ver_major'
op|','
name|'self'
op|'.'
name|'ver_minor'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
