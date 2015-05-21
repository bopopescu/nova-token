begin_unit
comment|'# Copyright (C) 2014 Red Hat, Inc.'
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
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
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
string|'"""\nThis provides a sphinx extension able to render the source/support-matrix.ini\nfile into the developer documentation.\n\nIt is used via a single directive in the .rst file\n\n  .. support_matrix::\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'configparser'
newline|'\n'
nl|'\n'
name|'from'
name|'docutils'
name|'import'
name|'nodes'
newline|'\n'
name|'from'
name|'docutils'
op|'.'
name|'parsers'
name|'import'
name|'rst'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SupportMatrix
name|'class'
name|'SupportMatrix'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents the entire support matrix for Nova virt drivers\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# List of SupportMatrixFeature instances, describing'
nl|'\n'
comment|'# all the features present in Nova virt drivers'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'features'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Dict of (name, SupportMatrixTarget) enumerating'
nl|'\n'
comment|'# all the hypervisor drivers that have data recorded'
nl|'\n'
comment|"# for them in self.features. The 'name' dict key is"
nl|'\n'
comment|'# the value from the SupportMatrixTarget.key attribute'
nl|'\n'
name|'self'
op|'.'
name|'targets'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SupportMatrixFeature
dedent|''
dedent|''
name|'class'
name|'SupportMatrixFeature'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|STATUS_MANDATORY
indent|'    '
name|'STATUS_MANDATORY'
op|'='
string|'"mandatory"'
newline|'\n'
DECL|variable|STATUS_CHOICE
name|'STATUS_CHOICE'
op|'='
string|'"choice"'
newline|'\n'
DECL|variable|STATUS_CONDITION
name|'STATUS_CONDITION'
op|'='
string|'"condition"'
newline|'\n'
DECL|variable|STATUS_OPTIONAL
name|'STATUS_OPTIONAL'
op|'='
string|'"optional"'
newline|'\n'
nl|'\n'
DECL|variable|STATUS_ALL
name|'STATUS_ALL'
op|'='
op|'['
name|'STATUS_MANDATORY'
op|','
name|'STATUS_CHOICE'
op|','
nl|'\n'
name|'STATUS_CONDITION'
op|','
name|'STATUS_OPTIONAL'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'title'
op|','
name|'status'
op|'='
name|'STATUS_OPTIONAL'
op|','
nl|'\n'
name|'group'
op|'='
name|'None'
op|','
name|'notes'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|"# A unique key (eg 'foo.bar.wizz') to identify the feature"
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'key'
op|'='
name|'key'
newline|'\n'
comment|'# A human friendly short title for the feature'
nl|'\n'
name|'self'
op|'.'
name|'title'
op|'='
name|'title'
newline|'\n'
comment|'# One of the status constants'
nl|'\n'
name|'self'
op|'.'
name|'status'
op|'='
name|'status'
newline|'\n'
comment|'# Detail string if status was choice/condition'
nl|'\n'
name|'self'
op|'.'
name|'group'
op|'='
name|'group'
newline|'\n'
comment|'# Arbitrarily long string describing the feature in detail'
nl|'\n'
name|'self'
op|'.'
name|'notes'
op|'='
name|'notes'
newline|'\n'
comment|'# Dict of (name, SupportMatrixImplementation) detailing'
nl|'\n'
comment|'# the implementation for each hypervisor driver. The'
nl|'\n'
comment|"# 'name' dict key is the value from SupportMatrixTarget.key"
nl|'\n'
comment|'# for the hypervisor in question'
nl|'\n'
name|'self'
op|'.'
name|'implementations'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SupportMatrixImplementation
dedent|''
dedent|''
name|'class'
name|'SupportMatrixImplementation'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|STATUS_COMPLETE
indent|'    '
name|'STATUS_COMPLETE'
op|'='
string|'"complete"'
newline|'\n'
DECL|variable|STATUS_PARTIAL
name|'STATUS_PARTIAL'
op|'='
string|'"partial"'
newline|'\n'
DECL|variable|STATUS_MISSING
name|'STATUS_MISSING'
op|'='
string|'"missing"'
newline|'\n'
nl|'\n'
DECL|variable|STATUS_ALL
name|'STATUS_ALL'
op|'='
op|'['
name|'STATUS_COMPLETE'
op|','
name|'STATUS_PARTIAL'
op|','
name|'STATUS_MISSING'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'status'
op|'='
name|'STATUS_MISSING'
op|','
name|'notes'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# One of the status constants detailing the implementation'
nl|'\n'
comment|'# level'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'status'
op|'='
name|'status'
newline|'\n'
comment|'# Arbitrary string describing any caveats of the implementation.'
nl|'\n'
comment|"# Mandatory if status is 'partial', optional otherwise."
nl|'\n'
name|'self'
op|'.'
name|'notes'
op|'='
name|'notes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SupportMatrixTarget
dedent|''
dedent|''
name|'class'
name|'SupportMatrixTarget'
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
name|'key'
op|','
name|'title'
op|','
name|'driver'
op|','
name|'hypervisor'
op|'='
name|'None'
op|','
name|'architecture'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""":param key: Unique identifier for the hypervisor driver\n        :param title: Human friendly name of the hypervisor\n        :param driver: Name of the Nova driver\n        :param hypervisor: (optional) Name of the hypervisor, if many\n        :param architecture: (optional) Name of the architecture, if many\n        """'
newline|'\n'
name|'self'
op|'.'
name|'key'
op|'='
name|'key'
newline|'\n'
name|'self'
op|'.'
name|'title'
op|'='
name|'title'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'hypervisor'
op|'='
name|'hypervisor'
newline|'\n'
name|'self'
op|'.'
name|'architecture'
op|'='
name|'architecture'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SupportMatrixDirective
dedent|''
dedent|''
name|'class'
name|'SupportMatrixDirective'
op|'('
name|'rst'
op|'.'
name|'Directive'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|option_spec
indent|'    '
name|'option_spec'
op|'='
op|'{'
nl|'\n'
string|"'support-matrix'"
op|':'
name|'six'
op|'.'
name|'text_type'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|run
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'matrix'
op|'='
name|'self'
op|'.'
name|'_load_support_matrix'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_build_markup'
op|'('
name|'matrix'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_support_matrix
dedent|''
name|'def'
name|'_load_support_matrix'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reads the support-matrix.ini file and populates an instance\n        of the SupportMatrix class with all the data.\n\n        :returns: SupportMatrix instance\n        """'
newline|'\n'
nl|'\n'
name|'cfg'
op|'='
name|'configparser'
op|'.'
name|'SafeConfigParser'
op|'('
op|')'
newline|'\n'
name|'env'
op|'='
name|'self'
op|'.'
name|'state'
op|'.'
name|'document'
op|'.'
name|'settings'
op|'.'
name|'env'
newline|'\n'
name|'fname'
op|'='
name|'self'
op|'.'
name|'options'
op|'.'
name|'get'
op|'('
string|'"support-matrix"'
op|','
nl|'\n'
string|'"support-matrix.ini"'
op|')'
newline|'\n'
name|'rel_fpath'
op|','
name|'fpath'
op|'='
name|'env'
op|'.'
name|'relfn2path'
op|'('
name|'fname'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'fpath'
op|')'
name|'as'
name|'fp'
op|':'
newline|'\n'
indent|'            '
name|'cfg'
op|'.'
name|'readfp'
op|'('
name|'fp'
op|')'
newline|'\n'
nl|'\n'
comment|'# This ensures that the docs are rebuilt whenever the'
nl|'\n'
comment|'# .ini file changes'
nl|'\n'
dedent|''
name|'env'
op|'.'
name|'note_dependency'
op|'('
name|'rel_fpath'
op|')'
newline|'\n'
nl|'\n'
name|'matrix'
op|'='
name|'SupportMatrix'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# The 'targets' section is special - it lists all the"
nl|'\n'
comment|'# hypervisors that this file records data for'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'cfg'
op|'.'
name|'options'
op|'('
string|'"targets"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'item'
op|'.'
name|'startswith'
op|'('
string|'"driver-impl-"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# The driver string will optionally contain'
nl|'\n'
comment|'# a hypervisor and architecture qualifier'
nl|'\n'
comment|'# so we expect between 1 and 3 components'
nl|'\n'
comment|'# in the name'
nl|'\n'
dedent|''
name|'key'
op|'='
name|'item'
op|'['
number|'12'
op|':'
op|']'
newline|'\n'
name|'title'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
string|'"targets"'
op|','
name|'item'
op|')'
newline|'\n'
name|'name'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|'"-"'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'name'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'target'
op|'='
name|'SupportMatrixTarget'
op|'('
name|'key'
op|','
nl|'\n'
name|'title'
op|','
nl|'\n'
name|'name'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'name'
op|')'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'                '
name|'target'
op|'='
name|'SupportMatrixTarget'
op|'('
name|'key'
op|','
nl|'\n'
name|'title'
op|','
nl|'\n'
name|'name'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'name'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'name'
op|')'
op|'=='
number|'3'
op|':'
newline|'\n'
indent|'                '
name|'target'
op|'='
name|'SupportMatrixTarget'
op|'('
name|'key'
op|','
nl|'\n'
name|'title'
op|','
nl|'\n'
name|'name'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'name'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'name'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
string|'"\'%s\' field is malformed in \'[%s]\' section"'
op|'%'
nl|'\n'
op|'('
name|'item'
op|','
string|'"DEFAULT"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'matrix'
op|'.'
name|'targets'
op|'['
name|'key'
op|']'
op|'='
name|'target'
newline|'\n'
nl|'\n'
comment|"# All sections except 'targets' describe some feature of"
nl|'\n'
comment|'# the Nova hypervisor driver implementation'
nl|'\n'
dedent|''
name|'for'
name|'section'
name|'in'
name|'cfg'
op|'.'
name|'sections'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'section'
op|'=='
string|'"targets"'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'cfg'
op|'.'
name|'has_option'
op|'('
name|'section'
op|','
string|'"title"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|'"\'title\' field missing in \'[%s]\' section"'
op|'%'
name|'section'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'title'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
name|'section'
op|','
string|'"title"'
op|')'
newline|'\n'
nl|'\n'
name|'status'
op|'='
name|'SupportMatrixFeature'
op|'.'
name|'STATUS_OPTIONAL'
newline|'\n'
name|'if'
name|'cfg'
op|'.'
name|'has_option'
op|'('
name|'section'
op|','
string|'"status"'
op|')'
op|':'
newline|'\n'
comment|'# The value is a string  "status(group)" where'
nl|'\n'
comment|"# the 'group' part is optional"
nl|'\n'
indent|'                '
name|'status'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
name|'section'
op|','
string|'"status"'
op|')'
newline|'\n'
name|'offset'
op|'='
name|'status'
op|'.'
name|'find'
op|'('
string|'"("'
op|')'
newline|'\n'
name|'group'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'offset'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'group'
op|'='
name|'status'
op|'['
name|'offset'
op|'+'
number|'1'
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
name|'status'
op|'='
name|'status'
op|'['
number|'0'
op|':'
name|'offset'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'status'
name|'not'
name|'in'
name|'SupportMatrixFeature'
op|'.'
name|'STATUS_ALL'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|'"\'status\' field value \'%s\' in [\'%s\']"'
nl|'\n'
string|'"section must be %s"'
op|'%'
nl|'\n'
op|'('
name|'status'
op|','
name|'section'
op|','
nl|'\n'
string|'","'
op|'.'
name|'join'
op|'('
name|'SupportMatrixFeature'
op|'.'
name|'STATUS_ALL'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'notes'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'cfg'
op|'.'
name|'has_option'
op|'('
name|'section'
op|','
string|'"notes"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'notes'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
name|'section'
op|','
string|'"notes"'
op|')'
newline|'\n'
dedent|''
name|'feature'
op|'='
name|'SupportMatrixFeature'
op|'('
name|'section'
op|','
nl|'\n'
name|'title'
op|','
nl|'\n'
name|'status'
op|','
nl|'\n'
name|'group'
op|','
nl|'\n'
name|'notes'
op|')'
newline|'\n'
nl|'\n'
comment|"# Now we've got the basic feature details, we must process"
nl|'\n'
comment|'# the hypervisor driver implementation for each feature'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'cfg'
op|'.'
name|'options'
op|'('
name|'section'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'item'
op|'.'
name|'startswith'
op|'('
string|'"driver-impl-"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'key'
op|'='
name|'item'
op|'['
number|'12'
op|':'
op|']'
newline|'\n'
name|'if'
name|'key'
name|'not'
name|'in'
name|'matrix'
op|'.'
name|'targets'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|'"Driver impl \'%s\' in \'[%s]\' not declared"'
op|'%'
nl|'\n'
op|'('
name|'item'
op|','
name|'section'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'status'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
name|'section'
op|','
name|'item'
op|')'
newline|'\n'
name|'if'
name|'status'
name|'not'
name|'in'
name|'SupportMatrixImplementation'
op|'.'
name|'STATUS_ALL'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|'"\'%s\' value \'%s\' in \'[%s]\' section must be %s"'
op|'%'
nl|'\n'
op|'('
name|'item'
op|','
name|'status'
op|','
name|'section'
op|','
nl|'\n'
string|'","'
op|'.'
name|'join'
op|'('
name|'SupportMatrixImplementation'
op|'.'
name|'STATUS_ALL'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'noteskey'
op|'='
string|'"driver-notes-"'
op|'+'
name|'item'
op|'['
number|'12'
op|':'
op|']'
newline|'\n'
name|'notes'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'cfg'
op|'.'
name|'has_option'
op|'('
name|'section'
op|','
name|'noteskey'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'notes'
op|'='
name|'cfg'
op|'.'
name|'get'
op|'('
name|'section'
op|','
name|'noteskey'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'target'
op|'='
name|'matrix'
op|'.'
name|'targets'
op|'['
name|'key'
op|']'
newline|'\n'
name|'impl'
op|'='
name|'SupportMatrixImplementation'
op|'('
name|'status'
op|','
nl|'\n'
name|'notes'
op|')'
newline|'\n'
name|'feature'
op|'.'
name|'implementations'
op|'['
name|'target'
op|'.'
name|'key'
op|']'
op|'='
name|'impl'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'matrix'
op|'.'
name|'targets'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'key'
name|'not'
name|'in'
name|'feature'
op|'.'
name|'implementations'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
string|'"\'%s\' missing in \'[%s]\' section"'
op|'%'
nl|'\n'
op|'('
name|'target'
op|'.'
name|'key'
op|','
name|'section'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'matrix'
op|'.'
name|'features'
op|'.'
name|'append'
op|'('
name|'feature'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'matrix'
newline|'\n'
nl|'\n'
DECL|member|_build_markup
dedent|''
name|'def'
name|'_build_markup'
op|'('
name|'self'
op|','
name|'matrix'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs the docutils content for the support matrix\n        """'
newline|'\n'
name|'content'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_build_summary'
op|'('
name|'matrix'
op|','
name|'content'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_build_details'
op|'('
name|'matrix'
op|','
name|'content'
op|')'
newline|'\n'
name|'return'
name|'content'
newline|'\n'
nl|'\n'
DECL|member|_build_summary
dedent|''
name|'def'
name|'_build_summary'
op|'('
name|'self'
op|','
name|'matrix'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs the docutils content for the summary of\n        the support matrix.\n\n        The summary consists of a giant table, with one row\n        for each feature, and a column for each hypervisor\n        driver. It provides an \'at a glance\' summary of the\n        status of each driver\n        """'
newline|'\n'
nl|'\n'
name|'summarytitle'
op|'='
name|'nodes'
op|'.'
name|'subtitle'
op|'('
name|'text'
op|'='
string|'"Summary"'
op|')'
newline|'\n'
name|'summary'
op|'='
name|'nodes'
op|'.'
name|'table'
op|'('
op|')'
newline|'\n'
name|'cols'
op|'='
name|'len'
op|'('
name|'matrix'
op|'.'
name|'targets'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'cols'
op|'+='
number|'2'
newline|'\n'
name|'summarygroup'
op|'='
name|'nodes'
op|'.'
name|'tgroup'
op|'('
name|'cols'
op|'='
name|'cols'
op|')'
newline|'\n'
name|'summarybody'
op|'='
name|'nodes'
op|'.'
name|'tbody'
op|'('
op|')'
newline|'\n'
name|'summaryhead'
op|'='
name|'nodes'
op|'.'
name|'thead'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'cols'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'summarygroup'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'colspec'
op|'('
name|'colwidth'
op|'='
number|'1'
op|')'
op|')'
newline|'\n'
dedent|''
name|'summarygroup'
op|'.'
name|'append'
op|'('
name|'summaryhead'
op|')'
newline|'\n'
name|'summarygroup'
op|'.'
name|'append'
op|'('
name|'summarybody'
op|')'
newline|'\n'
name|'summary'
op|'.'
name|'append'
op|'('
name|'summarygroup'
op|')'
newline|'\n'
name|'content'
op|'.'
name|'append'
op|'('
name|'summarytitle'
op|')'
newline|'\n'
name|'content'
op|'.'
name|'append'
op|'('
name|'summary'
op|')'
newline|'\n'
nl|'\n'
comment|'# This sets up all the column headers - two fixed'
nl|'\n'
comment|'# columns for feature name & status'
nl|'\n'
name|'header'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
op|')'
newline|'\n'
name|'blank'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'blank'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'emphasis'
op|'('
name|'text'
op|'='
string|'"Feature"'
op|')'
op|')'
newline|'\n'
name|'header'
op|'.'
name|'append'
op|'('
name|'blank'
op|')'
newline|'\n'
name|'blank'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'blank'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'emphasis'
op|'('
name|'text'
op|'='
string|'"Status"'
op|')'
op|')'
newline|'\n'
name|'header'
op|'.'
name|'append'
op|'('
name|'blank'
op|')'
newline|'\n'
name|'summaryhead'
op|'.'
name|'append'
op|'('
name|'header'
op|')'
newline|'\n'
nl|'\n'
comment|'# then one column for each hypervisor driver'
nl|'\n'
name|'impls'
op|'='
name|'matrix'
op|'.'
name|'targets'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'impls'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'impls'
op|':'
newline|'\n'
indent|'            '
name|'target'
op|'='
name|'matrix'
op|'.'
name|'targets'
op|'['
name|'key'
op|']'
newline|'\n'
name|'implcol'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'header'
op|'.'
name|'append'
op|'('
name|'implcol'
op|')'
newline|'\n'
name|'implcol'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'strong'
op|'('
name|'text'
op|'='
name|'target'
op|'.'
name|'title'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# We now produce the body of the table, one row for'
nl|'\n'
comment|'# each feature to report on'
nl|'\n'
dedent|''
name|'for'
name|'feature'
name|'in'
name|'matrix'
op|'.'
name|'features'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# the hyperlink target name linking to details'
nl|'\n'
name|'id'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|'"[^a-zA-Z0-9_]"'
op|','
string|'"_"'
op|','
nl|'\n'
name|'feature'
op|'.'
name|'key'
op|')'
newline|'\n'
nl|'\n'
comment|'# first the to fixed columns for title/status'
nl|'\n'
name|'keycol'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'item'
op|'.'
name|'append'
op|'('
name|'keycol'
op|')'
newline|'\n'
name|'keyref'
op|'='
name|'nodes'
op|'.'
name|'reference'
op|'('
name|'refid'
op|'='
name|'id'
op|')'
newline|'\n'
name|'keytxt'
op|'='
name|'nodes'
op|'.'
name|'inline'
op|'('
op|')'
newline|'\n'
name|'keycol'
op|'.'
name|'append'
op|'('
name|'keytxt'
op|')'
newline|'\n'
name|'keytxt'
op|'.'
name|'append'
op|'('
name|'keyref'
op|')'
newline|'\n'
name|'keyref'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'strong'
op|'('
name|'text'
op|'='
name|'feature'
op|'.'
name|'title'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'statuscol'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'item'
op|'.'
name|'append'
op|'('
name|'statuscol'
op|')'
newline|'\n'
name|'statuscol'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'inline'
op|'('
nl|'\n'
name|'text'
op|'='
name|'feature'
op|'.'
name|'status'
op|','
nl|'\n'
name|'classes'
op|'='
op|'['
string|'"sp_feature_"'
op|'+'
name|'feature'
op|'.'
name|'status'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# and then one column for each hypervisor driver'
nl|'\n'
name|'impls'
op|'='
name|'matrix'
op|'.'
name|'targets'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'impls'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'impls'
op|':'
newline|'\n'
indent|'                '
name|'target'
op|'='
name|'matrix'
op|'.'
name|'targets'
op|'['
name|'key'
op|']'
newline|'\n'
name|'impl'
op|'='
name|'feature'
op|'.'
name|'implementations'
op|'['
name|'key'
op|']'
newline|'\n'
name|'implcol'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'item'
op|'.'
name|'append'
op|'('
name|'implcol'
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|'"[^a-zA-Z0-9_]"'
op|','
string|'"_"'
op|','
nl|'\n'
name|'feature'
op|'.'
name|'key'
op|'+'
string|'"_"'
op|'+'
name|'key'
op|')'
newline|'\n'
nl|'\n'
name|'implref'
op|'='
name|'nodes'
op|'.'
name|'reference'
op|'('
name|'refid'
op|'='
name|'id'
op|')'
newline|'\n'
name|'impltxt'
op|'='
name|'nodes'
op|'.'
name|'inline'
op|'('
op|')'
newline|'\n'
name|'implcol'
op|'.'
name|'append'
op|'('
name|'impltxt'
op|')'
newline|'\n'
name|'impltxt'
op|'.'
name|'append'
op|'('
name|'implref'
op|')'
newline|'\n'
nl|'\n'
name|'status'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'impl'
op|'.'
name|'status'
op|'=='
string|'"complete"'
op|':'
newline|'\n'
indent|'                    '
name|'status'
op|'='
string|'u"\\u2714"'
newline|'\n'
dedent|''
name|'elif'
name|'impl'
op|'.'
name|'status'
op|'=='
string|'"missing"'
op|':'
newline|'\n'
indent|'                    '
name|'status'
op|'='
string|'u"\\u2716"'
newline|'\n'
dedent|''
name|'elif'
name|'impl'
op|'.'
name|'status'
op|'=='
string|'"partial"'
op|':'
newline|'\n'
indent|'                    '
name|'status'
op|'='
string|'u"\\u2714"'
newline|'\n'
nl|'\n'
dedent|''
name|'implref'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'literal'
op|'('
nl|'\n'
name|'text'
op|'='
name|'status'
op|','
nl|'\n'
name|'classes'
op|'='
op|'['
string|'"sp_impl_summary"'
op|','
string|'"sp_impl_"'
op|'+'
name|'impl'
op|'.'
name|'status'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'summarybody'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_details
dedent|''
dedent|''
name|'def'
name|'_build_details'
op|'('
name|'self'
op|','
name|'matrix'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs the docutils content for the details of\n        the support matrix.\n\n        This is generated as a bullet list of features.\n        Against each feature we provide the description of\n        the feature and then the details of the hypervisor\n        impls, with any driver specific notes that exist\n        """'
newline|'\n'
nl|'\n'
name|'detailstitle'
op|'='
name|'nodes'
op|'.'
name|'subtitle'
op|'('
name|'text'
op|'='
string|'"Details"'
op|')'
newline|'\n'
name|'details'
op|'='
name|'nodes'
op|'.'
name|'bullet_list'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'content'
op|'.'
name|'append'
op|'('
name|'detailstitle'
op|')'
newline|'\n'
name|'content'
op|'.'
name|'append'
op|'('
name|'details'
op|')'
newline|'\n'
nl|'\n'
comment|"# One list entry for each feature we're reporting on"
nl|'\n'
name|'for'
name|'feature'
name|'in'
name|'matrix'
op|'.'
name|'features'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
name|'nodes'
op|'.'
name|'list_item'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'status'
op|'='
name|'feature'
op|'.'
name|'status'
newline|'\n'
name|'if'
name|'feature'
op|'.'
name|'group'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'status'
op|'+='
string|'"("'
op|'+'
name|'feature'
op|'.'
name|'group'
op|'+'
string|'")"'
newline|'\n'
nl|'\n'
comment|'# The hypervisor target name linked from summary table'
nl|'\n'
dedent|''
name|'id'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|'"[^a-zA-Z0-9_]"'
op|','
string|'"_"'
op|','
nl|'\n'
name|'feature'
op|'.'
name|'key'
op|')'
newline|'\n'
nl|'\n'
comment|'# Highlight the feature title name'
nl|'\n'
name|'item'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'strong'
op|'('
name|'text'
op|'='
name|'feature'
op|'.'
name|'title'
op|','
nl|'\n'
name|'ids'
op|'='
op|'['
name|'id'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'para'
op|'='
name|'nodes'
op|'.'
name|'paragraph'
op|'('
op|')'
newline|'\n'
name|'para'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'strong'
op|'('
name|'text'
op|'='
string|'"Status: "'
op|'+'
name|'status'
op|'+'
string|'". "'
op|')'
op|')'
newline|'\n'
name|'if'
name|'feature'
op|'.'
name|'notes'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'para'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'inline'
op|'('
name|'text'
op|'='
name|'feature'
op|'.'
name|'notes'
op|')'
op|')'
newline|'\n'
dedent|''
name|'item'
op|'.'
name|'append'
op|'('
name|'para'
op|')'
newline|'\n'
nl|'\n'
comment|'# A sub-list giving details of each hypervisor target'
nl|'\n'
name|'impls'
op|'='
name|'nodes'
op|'.'
name|'bullet_list'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'feature'
op|'.'
name|'implementations'
op|':'
newline|'\n'
indent|'                '
name|'target'
op|'='
name|'matrix'
op|'.'
name|'targets'
op|'['
name|'key'
op|']'
newline|'\n'
name|'impl'
op|'='
name|'feature'
op|'.'
name|'implementations'
op|'['
name|'key'
op|']'
newline|'\n'
name|'subitem'
op|'='
name|'nodes'
op|'.'
name|'list_item'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|'"[^a-zA-Z0-9_]"'
op|','
string|'"_"'
op|','
nl|'\n'
name|'feature'
op|'.'
name|'key'
op|'+'
string|'"_"'
op|'+'
name|'key'
op|')'
newline|'\n'
name|'subitem'
op|'+='
op|'['
nl|'\n'
name|'nodes'
op|'.'
name|'strong'
op|'('
name|'text'
op|'='
name|'target'
op|'.'
name|'title'
op|'+'
string|'": "'
op|')'
op|','
nl|'\n'
name|'nodes'
op|'.'
name|'literal'
op|'('
name|'text'
op|'='
name|'impl'
op|'.'
name|'status'
op|','
nl|'\n'
name|'classes'
op|'='
op|'['
string|'"sp_impl_"'
op|'+'
name|'impl'
op|'.'
name|'status'
op|']'
op|','
nl|'\n'
name|'ids'
op|'='
op|'['
name|'id'
op|']'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'if'
name|'impl'
op|'.'
name|'notes'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'subitem'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_create_notes_paragraph'
op|'('
name|'impl'
op|'.'
name|'notes'
op|')'
op|')'
newline|'\n'
dedent|''
name|'impls'
op|'.'
name|'append'
op|'('
name|'subitem'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'item'
op|'.'
name|'append'
op|'('
name|'impls'
op|')'
newline|'\n'
name|'details'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_notes_paragraph
dedent|''
dedent|''
name|'def'
name|'_create_notes_paragraph'
op|'('
name|'self'
op|','
name|'notes'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Constructs a paragraph which represents the implementation notes\n\n        The paragraph consists of text and clickable URL nodes if links were\n        given in the notes.\n        """'
newline|'\n'
name|'para'
op|'='
name|'nodes'
op|'.'
name|'paragraph'
op|'('
op|')'
newline|'\n'
comment|'# links could start with http:// or https://'
nl|'\n'
name|'link_idxs'
op|'='
op|'['
name|'m'
op|'.'
name|'start'
op|'('
op|')'
name|'for'
name|'m'
name|'in'
name|'re'
op|'.'
name|'finditer'
op|'('
string|"'https?://'"
op|','
name|'notes'
op|')'
op|']'
newline|'\n'
name|'start_idx'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'link_idx'
name|'in'
name|'link_idxs'
op|':'
newline|'\n'
comment|'# assume the notes start with text (could be empty)'
nl|'\n'
indent|'            '
name|'para'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'inline'
op|'('
name|'text'
op|'='
name|'notes'
op|'['
name|'start_idx'
op|':'
name|'link_idx'
op|']'
op|')'
op|')'
newline|'\n'
comment|'# create a URL node until the next text or the end of the notes'
nl|'\n'
name|'link_end_idx'
op|'='
name|'notes'
op|'.'
name|'find'
op|'('
string|'" "'
op|','
name|'link_idx'
op|')'
newline|'\n'
name|'if'
name|'link_end_idx'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
comment|'# In case the notes end with a link without a blank'
nl|'\n'
indent|'                '
name|'link_end_idx'
op|'='
name|'len'
op|'('
name|'notes'
op|')'
newline|'\n'
dedent|''
name|'uri'
op|'='
name|'notes'
op|'['
name|'link_idx'
op|':'
name|'link_end_idx'
op|'+'
number|'1'
op|']'
newline|'\n'
name|'para'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'reference'
op|'('
string|'""'
op|','
name|'uri'
op|','
name|'refuri'
op|'='
name|'uri'
op|')'
op|')'
newline|'\n'
name|'start_idx'
op|'='
name|'link_end_idx'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
comment|'# get all text after the last link (could be empty) or all of the'
nl|'\n'
comment|'# text if no link was given'
nl|'\n'
dedent|''
name|'para'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'inline'
op|'('
name|'text'
op|'='
name|'notes'
op|'['
name|'start_idx'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'para'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'support_matrix'"
op|','
name|'SupportMatrixDirective'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_stylesheet'
op|'('
string|"'support-matrix.css'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
