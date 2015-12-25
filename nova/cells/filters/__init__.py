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
string|'"""\nCell scheduler filters\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'policy'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseCellFilter
name|'class'
name|'BaseCellFilter'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for cell filters."""'
newline|'\n'
nl|'\n'
DECL|member|authorized
name|'def'
name|'authorized'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return whether or not the context is authorized for this filter\n        based on policy.\n        The policy action is "cells_scheduler_filter:<name>" where <name>\n        is the name of the filter class.\n        """'
newline|'\n'
name|'name'
op|'='
string|"'cells_scheduler_filter:'"
op|'+'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'ctxt'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'ctxt'
op|'.'
name|'user_id'
op|'}'
newline|'\n'
name|'return'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'ctxt'
op|','
name|'name'
op|','
name|'target'
op|','
name|'do_raise'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_filter_one
dedent|''
name|'def'
name|'_filter_one'
op|'('
name|'self'
op|','
name|'cell'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'cell_passes'
op|'('
name|'cell'
op|','
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_passes
dedent|''
name|'def'
name|'cell_passes'
op|'('
name|'self'
op|','
name|'cell'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if the CellState passes the filter, otherwise False.\n        Override this in a subclass.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellFilterHandler
dedent|''
dedent|''
name|'class'
name|'CellFilterHandler'
op|'('
name|'filters'
op|'.'
name|'BaseFilterHandler'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CellFilterHandler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'BaseCellFilter'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|all_filters
dedent|''
dedent|''
name|'def'
name|'all_filters'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a list of filter classes found in this directory.\n\n    This method is used as the default for available scheduler filters\n    and should return a list of all filter classes available.\n    """'
newline|'\n'
name|'return'
name|'CellFilterHandler'
op|'('
op|')'
op|'.'
name|'get_all_classes'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
