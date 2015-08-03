begin_unit
comment|'#    Copyright 2013 Red Hat, Inc'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|OPTIONAL_FIELDS
name|'OPTIONAL_FIELDS'
op|'='
op|'['
string|"'extra_specs'"
op|','
string|"'projects'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'Flavor'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|Flavor
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added save_projects(), save_extra_specs(), removed'
nl|'\n'
comment|'#              remoteable from save()'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
name|'fields'
op|'.'
name|'FloatField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
number|'1.0'
op|')'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'extra_specs'"
op|':'
name|'fields'
op|'.'
name|'DictOfStringsField'
op|'('
op|')'
op|','
nl|'\n'
string|"'projects'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'super'
op|'('
name|'Flavor'
op|','
name|'self'
op|')'
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
name|'self'
op|'.'
name|'_orig_extra_specs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_orig_projects'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'flavor'
op|','
name|'db_flavor'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'expected_attrs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'expected_attrs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'flavor'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'for'
name|'name'
op|','
name|'field'
name|'in'
name|'flavor'
op|'.'
name|'fields'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
name|'in'
name|'OPTIONAL_FIELDS'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'value'
op|'='
name|'db_flavor'
op|'['
name|'name'
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'field'
op|','
name|'fields'
op|'.'
name|'IntegerField'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'value'
name|'if'
name|'value'
name|'is'
name|'not'
name|'None'
name|'else'
number|'0'
newline|'\n'
dedent|''
name|'flavor'
op|'['
name|'name'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'extra_specs'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'extra_specs'
op|'='
name|'db_flavor'
op|'['
string|"'extra_specs'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'projects'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'_load_projects'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'flavor'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'flavor'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|_load_projects
name|'def'
name|'_load_projects'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'projects'
op|'='
op|'['
name|'x'
op|'['
string|"'project_id'"
op|']'
name|'for'
name|'x'
name|'in'
nl|'\n'
name|'db'
op|'.'
name|'flavor_access_get_by_flavor_id'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'flavorid'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'projects'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|obj_load_attr
dedent|''
name|'def'
name|'obj_load_attr'
op|'('
name|'self'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Only projects could be lazy-loaded right now'
nl|'\n'
indent|'        '
name|'if'
name|'attrname'
op|'!='
string|"'projects'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'obj_load_attr'"
op|','
name|'reason'
op|'='
string|"'unable to load %s'"
op|'%'
name|'attrname'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_load_projects'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|obj_reset_changes
dedent|''
name|'def'
name|'obj_reset_changes'
op|'('
name|'self'
op|','
name|'fields'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Flavor'
op|','
name|'self'
op|')'
op|'.'
name|'obj_reset_changes'
op|'('
name|'fields'
op|'='
name|'fields'
op|')'
newline|'\n'
name|'if'
name|'fields'
name|'is'
name|'None'
name|'or'
string|"'extra_specs'"
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_orig_extra_specs'
op|'='
op|'('
name|'dict'
op|'('
name|'self'
op|'.'
name|'extra_specs'
op|')'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'extra_specs'"
op|')'
nl|'\n'
name|'else'
op|'{'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'fields'
name|'is'
name|'None'
name|'or'
string|"'projects'"
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_orig_projects'
op|'='
op|'('
name|'list'
op|'('
name|'self'
op|'.'
name|'projects'
op|')'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'projects'"
op|')'
nl|'\n'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|obj_what_changed
dedent|''
dedent|''
name|'def'
name|'obj_what_changed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'changes'
op|'='
name|'super'
op|'('
name|'Flavor'
op|','
name|'self'
op|')'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
newline|'\n'
name|'if'
op|'('
string|"'extra_specs'"
name|'in'
name|'self'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'extra_specs'
op|'!='
name|'self'
op|'.'
name|'_orig_extra_specs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'changes'
op|'.'
name|'add'
op|'('
string|"'extra_specs'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'projects'"
name|'in'
name|'self'
name|'and'
name|'self'
op|'.'
name|'projects'
op|'!='
name|'self'
op|'.'
name|'_orig_projects'
op|':'
newline|'\n'
indent|'            '
name|'changes'
op|'.'
name|'add'
op|'('
string|"'projects'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'changes'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_obj_from_primitive
name|'def'
name|'_obj_from_primitive'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'objver'
op|','
name|'primitive'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'='
name|'super'
op|'('
name|'Flavor'
op|','
name|'cls'
op|')'
op|'.'
name|'_obj_from_primitive'
op|'('
name|'context'
op|','
name|'objver'
op|','
nl|'\n'
name|'primitive'
op|')'
newline|'\n'
name|'changes'
op|'='
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'extra_specs'"
name|'not'
name|'in'
name|'changes'
op|':'
newline|'\n'
comment|'# This call left extra_specs "clean" so update our tracker'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_orig_extra_specs'
op|'='
op|'('
name|'dict'
op|'('
name|'self'
op|'.'
name|'extra_specs'
op|')'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'extra_specs'"
op|')'
nl|'\n'
name|'else'
op|'{'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'projects'"
name|'not'
name|'in'
name|'changes'
op|':'
newline|'\n'
comment|'# This call left projects "clean" so update our tracker'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_orig_projects'
op|'='
op|'('
name|'list'
op|'('
name|'self'
op|'.'
name|'projects'
op|')'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'projects'"
op|')'
nl|'\n'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavor'
op|'='
name|'db'
op|'.'
name|'flavor_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_flavor'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'extra_specs'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_name
name|'def'
name|'get_by_name'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavor'
op|'='
name|'db'
op|'.'
name|'flavor_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_flavor'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'extra_specs'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_flavor_id
name|'def'
name|'get_by_flavor_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'flavor_id'
op|','
name|'read_deleted'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavor'
op|'='
name|'db'
op|'.'
name|'flavor_get_by_flavor_id'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
nl|'\n'
name|'read_deleted'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_flavor'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'extra_specs'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|add_access
name|'def'
name|'add_access'
op|'('
name|'self'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'projects'"
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'add_access'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'projects modified'"
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'flavor_access_add'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'flavorid'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_load_projects'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|remove_access
name|'def'
name|'remove_access'
op|'('
name|'self'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'projects'"
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'remove_access'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'projects modified'"
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'flavor_access_remove'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'flavorid'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_load_projects'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'expected_attrs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'OPTIONAL_FIELDS'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attr'
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'                '
name|'expected_attrs'
op|'.'
name|'append'
op|'('
name|'attr'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'projects'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'projects'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'db_flavor'
op|'='
name|'db'
op|'.'
name|'flavor_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'updates'
op|','
name|'projects'
op|'='
name|'projects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_flavor'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save_projects
name|'def'
name|'save_projects'
op|'('
name|'self'
op|','
name|'to_add'
op|'='
name|'None'
op|','
name|'to_delete'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or delete projects.\n\n        :param:to_add: A list of projects to add\n        :param:to_delete: A list of projects to remove\n        """'
newline|'\n'
nl|'\n'
name|'to_add'
op|'='
name|'to_add'
name|'if'
name|'to_add'
name|'is'
name|'not'
name|'None'
name|'else'
op|'['
op|']'
newline|'\n'
name|'to_delete'
op|'='
name|'to_delete'
name|'if'
name|'to_delete'
name|'is'
name|'not'
name|'None'
name|'else'
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'project_id'
name|'in'
name|'to_add'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'flavor_access_add'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'flavorid'
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'project_id'
name|'in'
name|'to_delete'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'flavor_access_remove'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'flavorid'
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'projects'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save_extra_specs
name|'def'
name|'save_extra_specs'
op|'('
name|'self'
op|','
name|'to_add'
op|'='
name|'None'
op|','
name|'to_delete'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or delete extra_specs.\n\n        :param:to_add: A dict of new keys to add/update\n        :param:to_delete: A list of keys to remove\n        """'
newline|'\n'
nl|'\n'
name|'to_add'
op|'='
name|'to_add'
name|'if'
name|'to_add'
name|'is'
name|'not'
name|'None'
name|'else'
op|'{'
op|'}'
newline|'\n'
name|'to_delete'
op|'='
name|'to_delete'
name|'if'
name|'to_delete'
name|'is'
name|'not'
name|'None'
name|'else'
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'to_add'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'flavor_extra_specs_update_or_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'flavorid'
op|','
nl|'\n'
name|'to_add'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'to_delete'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'flavor_extra_specs_delete'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'flavorid'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'extra_specs'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'projects'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'projects'"
op|','
name|'None'
op|')'
newline|'\n'
name|'extra_specs'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'extra_specs'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'save'"
op|','
name|'reason'
op|'='
string|"'read-only fields were changed'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'extra_specs'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'deleted_keys'
op|'='
op|'('
name|'set'
op|'('
name|'self'
op|'.'
name|'_orig_extra_specs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'-'
nl|'\n'
name|'set'
op|'('
name|'extra_specs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'added_keys'
op|'='
name|'self'
op|'.'
name|'extra_specs'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'added_keys'
op|'='
name|'deleted_keys'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'projects'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'deleted_projects'
op|'='
name|'set'
op|'('
name|'self'
op|'.'
name|'_orig_projects'
op|')'
op|'-'
name|'set'
op|'('
name|'projects'
op|')'
newline|'\n'
name|'added_projects'
op|'='
name|'set'
op|'('
name|'projects'
op|')'
op|'-'
name|'set'
op|'('
name|'self'
op|'.'
name|'_orig_projects'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'added_projects'
op|'='
name|'deleted_projects'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): The first remotable method we call will reset'
nl|'\n'
comment|'# our of the original values for projects and extra_specs. Thus,'
nl|'\n'
comment|'# we collect the added/deleted lists for both above and /then/'
nl|'\n'
comment|'# call these methods to update them.'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'added_keys'
name|'or'
name|'deleted_keys'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'save_extra_specs'
op|'('
name|'self'
op|'.'
name|'extra_specs'
op|','
name|'deleted_keys'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'added_projects'
name|'or'
name|'deleted_projects'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'save_projects'
op|'('
name|'added_projects'
op|','
name|'deleted_projects'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'flavor_destroy'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|FlavorList
name|'class'
name|'FlavorList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'Flavor'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|','
op|'('
string|"'1.1'"
op|','
string|"'1.1'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'inactive'
op|'='
name|'False'
op|','
name|'filters'
op|'='
name|'None'
op|','
nl|'\n'
name|'sort_key'
op|'='
string|"'flavorid'"
op|','
name|'sort_dir'
op|'='
string|"'asc'"
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_flavors'
op|'='
name|'db'
op|'.'
name|'flavor_get_all'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
name|'inactive'
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|','
name|'sort_key'
op|'='
name|'sort_key'
op|','
nl|'\n'
name|'sort_dir'
op|'='
name|'sort_dir'
op|','
name|'limit'
op|'='
name|'limit'
op|','
nl|'\n'
name|'marker'
op|'='
name|'marker'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Flavor'
op|','
nl|'\n'
name|'db_flavors'
op|','
name|'expected_attrs'
op|'='
op|'['
string|"'extra_specs'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
