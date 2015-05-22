begin_unit
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nThe VMware API utility module.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_vmware'
name|'import'
name|'vim_util'
name|'as'
name|'vutil'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'suds'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
nl|'\n'
DECL|variable|vmware_opts
name|'vmware_opts'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'maximum_objects'"
op|','
name|'default'
op|'='
number|'100'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The maximum number of ObjectContent data '"
nl|'\n'
string|"'objects that should be returned in a single '"
nl|'\n'
string|"'result. A positive value will cause the '"
nl|'\n'
string|"'operation to suspend the retrieval when the '"
nl|'\n'
string|"'count of objects reaches the specified '"
nl|'\n'
string|"'maximum. The server may still limit the count '"
nl|'\n'
string|"'to something less than the configured value. '"
nl|'\n'
string|"'Any remaining objects may be retrieved with '"
nl|'\n'
string|"'additional requests.'"
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'vmware_opts'
op|','
string|"'vmware'"
op|')'
newline|'\n'
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
DECL|function|object_to_dict
name|'def'
name|'object_to_dict'
op|'('
name|'obj'
op|','
name|'list_depth'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert Suds object into serializable format.\n\n    The calling function can limit the amount of list entries that\n    are converted.\n    """'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'suds'
op|'.'
name|'sudsobject'
op|'.'
name|'asdict'
op|'('
name|'obj'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'v'
op|','
string|"'__keylist__'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'k'
op|']'
op|'='
name|'object_to_dict'
op|'('
name|'v'
op|','
name|'list_depth'
op|'='
name|'list_depth'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'v'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'k'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'used'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'v'
op|':'
newline|'\n'
indent|'                '
name|'used'
op|'='
name|'used'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'used'
op|'>'
name|'list_depth'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'item'
op|','
string|"'__keylist__'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'d'
op|'['
name|'k'
op|']'
op|'.'
name|'append'
op|'('
name|'object_to_dict'
op|'('
name|'item'
op|','
name|'list_depth'
op|'='
name|'list_depth'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'d'
op|'['
name|'k'
op|']'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_object_properties
dedent|''
name|'def'
name|'get_object_properties'
op|'('
name|'vim'
op|','
name|'collector'
op|','
name|'mobj'
op|','
name|'type'
op|','
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the properties of the Managed object specified."""'
newline|'\n'
name|'client_factory'
op|'='
name|'vim'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'if'
name|'mobj'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'usecoll'
op|'='
name|'collector'
newline|'\n'
name|'if'
name|'usecoll'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'usecoll'
op|'='
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'propertyCollector'
newline|'\n'
dedent|''
name|'property_filter_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:PropertyFilterSpec'"
op|')'
newline|'\n'
name|'property_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:PropertySpec'"
op|')'
newline|'\n'
name|'property_spec'
op|'.'
name|'all'
op|'='
op|'('
name|'properties'
name|'is'
name|'None'
name|'or'
name|'len'
op|'('
name|'properties'
op|')'
op|'=='
number|'0'
op|')'
newline|'\n'
name|'property_spec'
op|'.'
name|'pathSet'
op|'='
name|'properties'
newline|'\n'
name|'property_spec'
op|'.'
name|'type'
op|'='
name|'type'
newline|'\n'
name|'object_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:ObjectSpec'"
op|')'
newline|'\n'
name|'object_spec'
op|'.'
name|'obj'
op|'='
name|'mobj'
newline|'\n'
name|'object_spec'
op|'.'
name|'skip'
op|'='
name|'False'
newline|'\n'
name|'property_filter_spec'
op|'.'
name|'propSet'
op|'='
op|'['
name|'property_spec'
op|']'
newline|'\n'
name|'property_filter_spec'
op|'.'
name|'objectSet'
op|'='
op|'['
name|'object_spec'
op|']'
newline|'\n'
name|'options'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:RetrieveOptions'"
op|')'
newline|'\n'
name|'options'
op|'.'
name|'maxObjects'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'maximum_objects'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'RetrievePropertiesEx'
op|'('
name|'usecoll'
op|','
name|'specSet'
op|'='
op|'['
name|'property_filter_spec'
op|']'
op|','
nl|'\n'
name|'options'
op|'='
name|'options'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dynamic_property
dedent|''
name|'def'
name|'get_dynamic_property'
op|'('
name|'vim'
op|','
name|'mobj'
op|','
name|'type'
op|','
name|'property_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets a particular property of the Managed Object."""'
newline|'\n'
name|'property_dict'
op|'='
name|'get_dynamic_properties'
op|'('
name|'vim'
op|','
name|'mobj'
op|','
name|'type'
op|','
op|'['
name|'property_name'
op|']'
op|')'
newline|'\n'
name|'return'
name|'property_dict'
op|'.'
name|'get'
op|'('
name|'property_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dynamic_properties
dedent|''
name|'def'
name|'get_dynamic_properties'
op|'('
name|'vim'
op|','
name|'mobj'
op|','
name|'type'
op|','
name|'property_names'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the specified properties of the Managed Object."""'
newline|'\n'
name|'obj_content'
op|'='
name|'get_object_properties'
op|'('
name|'vim'
op|','
name|'None'
op|','
name|'mobj'
op|','
name|'type'
op|','
name|'property_names'
op|')'
newline|'\n'
name|'if'
name|'obj_content'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'obj_content'
op|','
string|"'token'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cancel_retrieve'
op|'('
name|'vim'
op|','
name|'obj_content'
op|'.'
name|'token'
op|')'
newline|'\n'
dedent|''
name|'property_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'obj_content'
op|'.'
name|'objects'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'obj_content'
op|'.'
name|'objects'
op|'['
number|'0'
op|']'
op|','
string|"'propSet'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'dynamic_properties'
op|'='
name|'obj_content'
op|'.'
name|'objects'
op|'['
number|'0'
op|']'
op|'.'
name|'propSet'
newline|'\n'
name|'if'
name|'dynamic_properties'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'prop'
name|'in'
name|'dynamic_properties'
op|':'
newline|'\n'
indent|'                    '
name|'property_dict'
op|'['
name|'prop'
op|'.'
name|'name'
op|']'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
comment|'# The object may have information useful for logging'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'obj_content'
op|'.'
name|'objects'
op|'['
number|'0'
op|']'
op|','
string|"'missingSet'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'m'
name|'in'
name|'obj_content'
op|'.'
name|'objects'
op|'['
number|'0'
op|']'
op|'.'
name|'missingSet'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Unable to retrieve value for %(path)s "'
nl|'\n'
string|'"Reason: %(reason)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'m'
op|'.'
name|'path'
op|','
nl|'\n'
string|"'reason'"
op|':'
name|'m'
op|'.'
name|'fault'
op|'.'
name|'localizedMessage'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'property_dict'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_objects
dedent|''
name|'def'
name|'get_objects'
op|'('
name|'vim'
op|','
name|'type'
op|','
name|'properties_to_collect'
op|'='
name|'None'
op|','
name|'all'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the list of objects of the type specified."""'
newline|'\n'
name|'return'
name|'vutil'
op|'.'
name|'get_objects'
op|'('
name|'vim'
op|','
name|'type'
op|','
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'maximum_objects'
op|','
nl|'\n'
name|'properties_to_collect'
op|','
name|'all'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_inner_objects
dedent|''
name|'def'
name|'get_inner_objects'
op|'('
name|'vim'
op|','
name|'base_obj'
op|','
name|'path'
op|','
name|'inner_type'
op|','
nl|'\n'
name|'properties_to_collect'
op|'='
name|'None'
op|','
name|'all'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the list of inner objects of the type specified."""'
newline|'\n'
name|'client_factory'
op|'='
name|'vim'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'base_type'
op|'='
name|'base_obj'
op|'.'
name|'_type'
newline|'\n'
name|'traversal_spec'
op|'='
name|'vutil'
op|'.'
name|'build_traversal_spec'
op|'('
name|'client_factory'
op|','
string|"'inner'"
op|','
nl|'\n'
name|'base_type'
op|','
name|'path'
op|','
name|'False'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'object_spec'
op|'='
name|'vutil'
op|'.'
name|'build_object_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'base_obj'
op|','
nl|'\n'
op|'['
name|'traversal_spec'
op|']'
op|')'
newline|'\n'
name|'property_spec'
op|'='
name|'vutil'
op|'.'
name|'build_property_spec'
op|'('
name|'client_factory'
op|','
name|'type_'
op|'='
name|'inner_type'
op|','
nl|'\n'
name|'properties_to_collect'
op|'='
name|'properties_to_collect'
op|','
nl|'\n'
name|'all_properties'
op|'='
name|'all'
op|')'
newline|'\n'
name|'property_filter_spec'
op|'='
name|'vutil'
op|'.'
name|'build_property_filter_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
op|'['
name|'property_spec'
op|']'
op|','
op|'['
name|'object_spec'
op|']'
op|')'
newline|'\n'
name|'options'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:RetrieveOptions'"
op|')'
newline|'\n'
name|'options'
op|'.'
name|'maxObjects'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'maximum_objects'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'RetrievePropertiesEx'
op|'('
nl|'\n'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'propertyCollector'
op|','
nl|'\n'
name|'specSet'
op|'='
op|'['
name|'property_filter_spec'
op|']'
op|','
name|'options'
op|'='
name|'options'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cancel_retrieve
dedent|''
name|'def'
name|'cancel_retrieve'
op|'('
name|'vim'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Cancels the retrieve operation."""'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'CancelRetrievePropertiesEx'
op|'('
nl|'\n'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'propertyCollector'
op|','
nl|'\n'
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|continue_to_get_objects
dedent|''
name|'def'
name|'continue_to_get_objects'
op|'('
name|'vim'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Continues to get the list of objects of the type specified."""'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'ContinueRetrievePropertiesEx'
op|'('
nl|'\n'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'propertyCollector'
op|','
nl|'\n'
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_prop_spec
dedent|''
name|'def'
name|'get_prop_spec'
op|'('
name|'client_factory'
op|','
name|'spec_type'
op|','
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the Property Spec Object."""'
newline|'\n'
name|'prop_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:PropertySpec'"
op|')'
newline|'\n'
name|'prop_spec'
op|'.'
name|'type'
op|'='
name|'spec_type'
newline|'\n'
name|'prop_spec'
op|'.'
name|'pathSet'
op|'='
name|'properties'
newline|'\n'
name|'return'
name|'prop_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_obj_spec
dedent|''
name|'def'
name|'get_obj_spec'
op|'('
name|'client_factory'
op|','
name|'obj'
op|','
name|'select_set'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the Object Spec object."""'
newline|'\n'
name|'obj_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:ObjectSpec'"
op|')'
newline|'\n'
name|'obj_spec'
op|'.'
name|'obj'
op|'='
name|'obj'
newline|'\n'
name|'obj_spec'
op|'.'
name|'skip'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'select_set'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'obj_spec'
op|'.'
name|'selectSet'
op|'='
name|'select_set'
newline|'\n'
dedent|''
name|'return'
name|'obj_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_prop_filter_spec
dedent|''
name|'def'
name|'get_prop_filter_spec'
op|'('
name|'client_factory'
op|','
name|'obj_spec'
op|','
name|'prop_spec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the Property Filter Spec Object."""'
newline|'\n'
name|'prop_filter_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:PropertyFilterSpec'"
op|')'
newline|'\n'
name|'prop_filter_spec'
op|'.'
name|'propSet'
op|'='
name|'prop_spec'
newline|'\n'
name|'prop_filter_spec'
op|'.'
name|'objectSet'
op|'='
name|'obj_spec'
newline|'\n'
name|'return'
name|'prop_filter_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_properties_for_a_collection_of_objects
dedent|''
name|'def'
name|'get_properties_for_a_collection_of_objects'
op|'('
name|'vim'
op|','
name|'type'
op|','
nl|'\n'
name|'obj_list'
op|','
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the list of properties for the collection of\n    objects of the type specified.\n    """'
newline|'\n'
name|'client_factory'
op|'='
name|'vim'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'obj_list'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'prop_spec'
op|'='
name|'get_prop_spec'
op|'('
name|'client_factory'
op|','
name|'type'
op|','
name|'properties'
op|')'
newline|'\n'
name|'lst_obj_specs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'obj'
name|'in'
name|'obj_list'
op|':'
newline|'\n'
indent|'        '
name|'lst_obj_specs'
op|'.'
name|'append'
op|'('
name|'get_obj_spec'
op|'('
name|'client_factory'
op|','
name|'obj'
op|')'
op|')'
newline|'\n'
dedent|''
name|'prop_filter_spec'
op|'='
name|'get_prop_filter_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'lst_obj_specs'
op|','
op|'['
name|'prop_spec'
op|']'
op|')'
newline|'\n'
name|'options'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:RetrieveOptions'"
op|')'
newline|'\n'
name|'options'
op|'.'
name|'maxObjects'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'maximum_objects'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'RetrievePropertiesEx'
op|'('
nl|'\n'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'propertyCollector'
op|','
nl|'\n'
name|'specSet'
op|'='
op|'['
name|'prop_filter_spec'
op|']'
op|','
name|'options'
op|'='
name|'options'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_about_info
dedent|''
name|'def'
name|'get_about_info'
op|'('
name|'vim'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the About Info from the service content."""'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'about'
newline|'\n'
dedent|''
endmarker|''
end_unit
