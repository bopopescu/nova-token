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
string|'"""\nUnit Tests for cells scheduler filters.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'state'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'cells'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FiltersTestCase
name|'class'
name|'FiltersTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Makes sure the proper filters are in the directory."""'
newline|'\n'
nl|'\n'
DECL|member|test_all_filters
name|'def'
name|'test_all_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_classes'
op|'='
name|'filters'
op|'.'
name|'all_filters'
op|'('
op|')'
newline|'\n'
name|'class_names'
op|'='
op|'['
name|'cls'
op|'.'
name|'__name__'
name|'for'
name|'cls'
name|'in'
name|'filter_classes'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"TargetCellFilter"'
op|','
name|'class_names'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"DifferentCellFilter"'
op|','
name|'class_names'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_FilterTestClass
dedent|''
dedent|''
name|'class'
name|'_FilterTestClass'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for testing individual filter plugins."""'
newline|'\n'
DECL|variable|filter_cls_name
name|'filter_cls_name'
op|'='
name|'None'
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
name|'_FilterTestClass'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'init'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'='
name|'fakes'
op|'.'
name|'get_message_runner'
op|'('
string|"'api-cell'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'scheduler'
newline|'\n'
name|'self'
op|'.'
name|'my_cell_state'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'CellFilterHandler'
op|'('
op|')'
newline|'\n'
name|'filter_classes'
op|'='
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
op|'['
name|'self'
op|'.'
name|'filter_cls_name'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filters'
op|'='
op|'['
name|'cls'
op|'('
op|')'
name|'for'
name|'cls'
name|'in'
name|'filter_classes'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_filter_cells
dedent|''
name|'def'
name|'_filter_cells'
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
name|'return'
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
name|'self'
op|'.'
name|'filters'
op|','
nl|'\n'
name|'cells'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagePropertiesFilter
dedent|''
dedent|''
name|'class'
name|'ImagePropertiesFilter'
op|'('
name|'_FilterTestClass'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'filter_cls_name'
op|'='
DECL|variable|filter_cls_name
string|"'nova.cells.filters.image_properties.ImagePropertiesFilter'"
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
name|'ImagePropertiesFilter'
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
name|'cell1'
op|'='
name|'models'
op|'.'
name|'Cell'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cell2'
op|'='
name|'models'
op|'.'
name|'Cell'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cell3'
op|'='
name|'models'
op|'.'
name|'Cell'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells'
op|'='
op|'['
name|'self'
op|'.'
name|'cell1'
op|','
name|'self'
op|'.'
name|'cell2'
op|','
name|'self'
op|'.'
name|'cell3'
op|']'
newline|'\n'
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'cells'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'.'
name|'capabilities'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'filter_props'
op|'='
op|'{'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|','
string|"'request_spec'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_missing_image_properties
dedent|''
name|'def'
name|'test_missing_image_properties'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'self'
op|'.'
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_missing_hypervisor_version_requires
dedent|''
name|'def'
name|'test_missing_hypervisor_version_requires'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filter_props'
op|'['
string|"'request_spec'"
op|']'
op|'='
op|'{'
string|"'image'"
op|':'
op|'{'
string|"'properties'"
op|':'
op|'{'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'cells'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'.'
name|'capabilities'
op|'='
op|'{'
string|'"prominent_hypervisor_version"'
op|':'
name|'set'
op|'('
op|'['
string|'u"6.2"'
op|']'
op|')'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'self'
op|'.'
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_missing_hypervisor_version_in_cells
dedent|''
name|'def'
name|'test_missing_hypervisor_version_in_cells'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'hypervisor_version_requires'"
op|':'
string|"'>6.2.1'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'filter_props'
op|'['
string|"'request_spec'"
op|']'
op|'='
op|'{'
string|"'image'"
op|':'
name|'image'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'cell1'
op|'.'
name|'capabilities'
op|'='
op|'{'
string|'"prominent_hypervisor_version"'
op|':'
name|'set'
op|'('
op|'['
op|']'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'self'
op|'.'
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cells_matching_hypervisor_version
dedent|''
name|'def'
name|'test_cells_matching_hypervisor_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'hypervisor_version_requires'"
op|':'
string|"'>6.0, <=6.3'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'filter_props'
op|'['
string|"'request_spec'"
op|']'
op|'='
op|'{'
string|"'image'"
op|':'
name|'image'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'cell1'
op|'.'
name|'capabilities'
op|'='
op|'{'
string|'"prominent_hypervisor_version"'
op|':'
nl|'\n'
name|'set'
op|'('
op|'['
string|'u"6.2"'
op|']'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'cell2'
op|'.'
name|'capabilities'
op|'='
op|'{'
string|'"prominent_hypervisor_version"'
op|':'
nl|'\n'
name|'set'
op|'('
op|'['
string|'u"6.3"'
op|']'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'cell3'
op|'.'
name|'capabilities'
op|'='
op|'{'
string|'"prominent_hypervisor_version"'
op|':'
nl|'\n'
name|'set'
op|'('
op|'['
string|'u"6.0"'
op|']'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'cell1'
op|','
name|'self'
op|'.'
name|'cell2'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'self'
op|'.'
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# assert again to verify filter doesn't mutate state"
nl|'\n'
comment|'# LP bug #1325705'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'cell1'
op|','
name|'self'
op|'.'
name|'cell2'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'self'
op|'.'
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTargetCellFilter
dedent|''
dedent|''
name|'class'
name|'TestTargetCellFilter'
op|'('
name|'_FilterTestClass'
op|')'
op|':'
newline|'\n'
DECL|variable|filter_cls_name
indent|'    '
name|'filter_cls_name'
op|'='
string|"'nova.cells.filters.target_cell.TargetCellFilter'"
newline|'\n'
nl|'\n'
DECL|member|test_missing_scheduler_hints
name|'def'
name|'test_missing_scheduler_hints'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells'
op|'='
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
newline|'\n'
comment|'# No filtering'
nl|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells'
op|','
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_target_cell_hint
dedent|''
name|'def'
name|'test_no_target_cell_hint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells'
op|'='
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
comment|'# No filtering'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells'
op|','
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_target_cell_specified_me
dedent|''
name|'def'
name|'test_target_cell_specified_me'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells'
op|'='
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
newline|'\n'
name|'target_cell'
op|'='
string|"'fake!cell!path'"
newline|'\n'
name|'current_cell'
op|'='
string|"'fake!cell!path'"
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'target_cell'"
op|':'
name|'target_cell'
op|'}'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
name|'current_cell'
op|','
nl|'\n'
string|"'scheduler'"
op|':'
name|'self'
op|'.'
name|'scheduler'
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
comment|'# Only myself in the list.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'my_cell_state'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_target_cell_specified_me_but_not_admin
dedent|''
name|'def'
name|'test_target_cell_specified_me_but_not_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'cells'
op|'='
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
newline|'\n'
name|'target_cell'
op|'='
string|"'fake!cell!path'"
newline|'\n'
name|'current_cell'
op|'='
string|"'fake!cell!path'"
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'target_cell'"
op|':'
name|'target_cell'
op|'}'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
name|'current_cell'
op|','
nl|'\n'
string|"'scheduler'"
op|':'
name|'self'
op|'.'
name|'scheduler'
op|','
nl|'\n'
string|"'context'"
op|':'
name|'ctxt'
op|'}'
newline|'\n'
comment|'# No filtering, because not an admin.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells'
op|','
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_target_cell_specified_not_me
dedent|''
name|'def'
name|'test_target_cell_specified_not_me'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_fake_build_instances
name|'def'
name|'_fake_build_instances'
op|'('
name|'ctxt'
op|','
name|'cell'
op|','
name|'sched_kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'['
string|"'ctxt'"
op|']'
op|'='
name|'ctxt'
newline|'\n'
name|'info'
op|'['
string|"'cell'"
op|']'
op|'='
name|'cell'
newline|'\n'
name|'info'
op|'['
string|"'sched_kwargs'"
op|']'
op|'='
name|'sched_kwargs'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'msg_runner'
op|','
string|"'build_instances'"
op|','
nl|'\n'
name|'_fake_build_instances'
op|')'
newline|'\n'
name|'cells'
op|'='
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
newline|'\n'
name|'target_cell'
op|'='
string|"'fake!cell!path'"
newline|'\n'
name|'current_cell'
op|'='
string|"'not!the!same'"
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'target_cell'"
op|':'
name|'target_cell'
op|'}'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
name|'current_cell'
op|','
nl|'\n'
string|"'scheduler'"
op|':'
name|'self'
op|'.'
name|'scheduler'
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'host_sched_kwargs'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
comment|'# None is returned to bypass further scheduling.'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
comment|'# The filter should have re-scheduled to the child cell itself.'
nl|'\n'
name|'expected_info'
op|'='
op|'{'
string|"'ctxt'"
op|':'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'cell'"
op|':'
string|"'fake!cell!path'"
op|','
nl|'\n'
string|"'sched_kwargs'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_info'
op|','
name|'info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDifferentCellFilter
dedent|''
dedent|''
name|'class'
name|'TestDifferentCellFilter'
op|'('
name|'_FilterTestClass'
op|')'
op|':'
newline|'\n'
DECL|variable|filter_cls_name
indent|'    '
name|'filter_cls_name'
op|'='
string|"'nova.cells.filters.different_cell.DifferentCellFilter'"
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
name|'TestDifferentCellFilter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# We only load one filter so we know the first one is the one we want'
nl|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
string|"'cells_scheduler_filter:DifferentCellFilter'"
op|':'
nl|'\n'
string|"''"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells'
op|'='
op|'['
name|'state'
op|'.'
name|'CellState'
op|'('
string|"'1'"
op|')'
op|','
nl|'\n'
name|'state'
op|'.'
name|'CellState'
op|'('
string|"'2'"
op|')'
op|','
nl|'\n'
name|'state'
op|'.'
name|'CellState'
op|'('
string|"'3'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_missing_scheduler_hints
dedent|''
name|'def'
name|'test_missing_scheduler_hints'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_props'
op|'='
op|'{'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
comment|'# No filtering'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_different_cell_hint
dedent|''
name|'def'
name|'test_no_different_cell_hint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
comment|'# No filtering'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_different_cell
dedent|''
name|'def'
name|'test_different_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'different_cell'"
op|':'
string|"'fake!2'"
op|'}'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
name|'filtered_cells'
op|'='
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'filter_props'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'filtered_cells'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'self'
op|'.'
name|'cells'
op|'['
number|'1'
op|']'
op|','
name|'filtered_cells'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_different_multiple_cells
dedent|''
name|'def'
name|'test_different_multiple_cells'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
nl|'\n'
op|'{'
string|"'different_cell'"
op|':'
op|'['
string|"'fake!1'"
op|','
string|"'fake!2'"
op|']'
op|'}'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
name|'filtered_cells'
op|'='
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'filter_props'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'filtered_cells'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'self'
op|'.'
name|'cells'
op|'['
number|'0'
op|']'
op|','
name|'filtered_cells'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'self'
op|'.'
name|'cells'
op|'['
number|'1'
op|']'
op|','
name|'filtered_cells'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_different_cell_specified_me_not_authorized
dedent|''
name|'def'
name|'test_different_cell_specified_me_not_authorized'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
string|"'cells_scheduler_filter:DifferentCellFilter'"
op|':'
nl|'\n'
string|"'!'"
op|'}'
op|')'
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'different_cell'"
op|':'
string|"'fake!2'"
op|'}'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'context'"
op|':'
name|'self'
op|'.'
name|'context'
op|'}'
newline|'\n'
comment|'# No filtering, because not an admin.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_filter_cells'
op|'('
name|'self'
op|'.'
name|'cells'
op|','
name|'filter_props'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
