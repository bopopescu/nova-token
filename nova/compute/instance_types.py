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
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 Ken Pepple'
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
string|'"""Built-in instance properties."""'
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
name|'db'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.instance_types'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
name|'name'
op|','
name|'memory'
op|','
name|'vcpus'
op|','
name|'local_gb'
op|','
name|'flavorid'
op|','
name|'swap'
op|'='
number|'0'
op|','
nl|'\n'
name|'rxtx_quota'
op|'='
number|'0'
op|','
name|'rxtx_cap'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates instance types."""'
newline|'\n'
name|'for'
name|'option'
name|'in'
op|'['
name|'memory'
op|','
name|'vcpus'
op|','
name|'local_gb'
op|','
name|'flavorid'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'int'
op|'('
name|'option'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInputException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"create arguments must be positive integers"'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
op|'('
name|'int'
op|'('
name|'memory'
op|')'
op|'<='
number|'0'
op|')'
name|'or'
op|'('
name|'int'
op|'('
name|'vcpus'
op|')'
op|'<='
number|'0'
op|')'
name|'or'
op|'('
name|'int'
op|'('
name|'local_gb'
op|')'
op|'<'
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInputException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"create arguments must be positive integers"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'instance_type_create'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
name|'name'
op|','
nl|'\n'
name|'memory_mb'
op|'='
name|'memory'
op|','
nl|'\n'
name|'vcpus'
op|'='
name|'vcpus'
op|','
nl|'\n'
name|'local_gb'
op|'='
name|'local_gb'
op|','
nl|'\n'
name|'flavorid'
op|'='
name|'flavorid'
op|','
nl|'\n'
name|'swap'
op|'='
name|'swap'
op|','
nl|'\n'
name|'rxtx_quota'
op|'='
name|'rxtx_quota'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
name|'rxtx_cap'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB error: %s'"
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Cannot create instance_type with "'
nl|'\n'
string|'"name %(name)s and flavorid %(flavorid)s"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy
dedent|''
dedent|''
name|'def'
name|'destroy'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Marks instance types as deleted."""'
newline|'\n'
name|'if'
name|'name'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInputException'
op|'('
name|'_'
op|'('
string|'"No instance type specified"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_type_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Instance type %s not found for deletion'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown instance type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|purge
dedent|''
dedent|''
dedent|''
name|'def'
name|'purge'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Removes instance types from database."""'
newline|'\n'
name|'if'
name|'name'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInputException'
op|'('
name|'_'
op|'('
string|'"No instance type specified"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_type_purge'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Instance type %s not found for purge'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown instance type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_all_types
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_all_types'
op|'('
name|'inactive'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all non-deleted instance_types.\n\n    Pass true as argument if you want deleted instance types returned also.\n\n    """'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_type_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'inactive'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|get_all_flavors
dedent|''
name|'get_all_flavors'
op|'='
name|'get_all_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_default_instance_type
name|'def'
name|'get_default_instance_type'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the default instance type."""'
newline|'\n'
name|'name'
op|'='
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_instance_type_by_name'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown instance type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_type
dedent|''
dedent|''
name|'def'
name|'get_instance_type'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single instance type by id."""'
newline|'\n'
name|'if'
name|'id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_type_get_by_id'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown instance type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_type_by_name
dedent|''
dedent|''
name|'def'
name|'get_instance_type_by_name'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single instance type by name."""'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_type_get_by_name'
op|'('
name|'ctxt'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown instance type: %s"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): flavor-specific code should probably be in the API that uses'
nl|'\n'
comment|'#               flavors.'
nl|'\n'
DECL|function|get_instance_type_by_flavor_id
dedent|''
dedent|''
name|'def'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve instance type by flavor_id."""'
newline|'\n'
name|'if'
name|'flavor_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_type_get_by_flavor_id'
op|'('
name|'ctxt'
op|','
name|'flavor_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB error: %s'"
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown flavor: %s"'
op|')'
op|'%'
name|'flavor_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
