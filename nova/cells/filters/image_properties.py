begin_unit
comment|'# Copyright (c) 2012-2013 Rackspace Hosting'
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
string|'"""\nImage properties filter.\n\nImage metadata named \'hypervisor_version_requires\' with a version specification\nmay be specified to ensure the build goes to a cell which has hypervisors of\nthe required version.\n\nIf either the version requirement on the image or the hypervisor capability\nof the cell is not present, this filter returns without filtering out the\ncells.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'distutils'
name|'import'
name|'versionpredicate'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'filters'
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
DECL|class|ImagePropertiesFilter
name|'class'
name|'ImagePropertiesFilter'
op|'('
name|'filters'
op|'.'
name|'BaseCellFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Image properties filter. Works by specifying the hypervisor required in\n    the image metadata and the supported hypervisor version in cell\n    capabilities.\n    """'
newline|'\n'
nl|'\n'
DECL|member|filter_all
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'cells'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Override filter_all() which operates on the full list\n        of cells...\n        """'
newline|'\n'
name|'request_spec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'image_properties'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'image'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'hypervisor_version_requires'
op|'='
name|'image_properties'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'hypervisor_version_requires'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'hypervisor_version_requires'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cells'
newline|'\n'
nl|'\n'
dedent|''
name|'filtered_cells'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cell'
name|'in'
name|'cells'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'cell'
op|'.'
name|'capabilities'
op|'.'
name|'get'
op|'('
string|"'prominent_hypervisor_version'"
op|')'
newline|'\n'
name|'if'
name|'version'
op|':'
newline|'\n'
indent|'                '
name|'l'
op|'='
name|'list'
op|'('
name|'version'
op|')'
newline|'\n'
name|'version'
op|'='
name|'str'
op|'('
name|'l'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'version'
name|'or'
name|'self'
op|'.'
name|'_matches_version'
op|'('
name|'version'
op|','
nl|'\n'
name|'hypervisor_version_requires'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'filtered_cells'
op|'.'
name|'append'
op|'('
name|'cell'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'filtered_cells'
newline|'\n'
nl|'\n'
DECL|member|_matches_version
dedent|''
name|'def'
name|'_matches_version'
op|'('
name|'self'
op|','
name|'version'
op|','
name|'version_requires'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'predicate'
op|'='
name|'versionpredicate'
op|'.'
name|'VersionPredicate'
op|'('
nl|'\n'
string|"'prop (%s)'"
op|'%'
name|'version_requires'
op|')'
newline|'\n'
name|'return'
name|'predicate'
op|'.'
name|'satisfied_by'
op|'('
name|'version'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
