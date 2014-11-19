begin_unit
comment|'# Copyright (c) 2012, Cloudscaling'
nl|'\n'
comment|'# All Rights Reserved.'
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
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
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
name|'import'
name|'ast'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'import'
name|'pep8'
newline|'\n'
nl|'\n'
string|'"""\nGuidelines for writing new hacking checks\n\n - Use only for Nova specific tests. OpenStack general tests\n   should be submitted to the common \'hacking\' module.\n - Pick numbers in the range N3xx. Find the current test with\n   the highest allocated number and then pick the next value.\n - Keep the test method code in the source file ordered based\n   on the N3xx value.\n - List the new rule in the top level HACKING.rst file\n - Add test cases for each new rule to nova/tests/test_hacking.py\n\n"""'
newline|'\n'
nl|'\n'
DECL|variable|UNDERSCORE_IMPORT_FILES
name|'UNDERSCORE_IMPORT_FILES'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|variable|session_check
name|'session_check'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"\\w*def [a-zA-Z0-9].*[(].*session.*[)]"'
op|')'
newline|'\n'
DECL|variable|cfg_re
name|'cfg_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r".*\\scfg\\."'
op|')'
newline|'\n'
DECL|variable|vi_header_re
name|'vi_header_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"^#\\s+vim?:.+"'
op|')'
newline|'\n'
DECL|variable|virt_file_re
name|'virt_file_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"\\./nova/(?:tests/)?virt/(\\w+)/"'
op|')'
newline|'\n'
DECL|variable|virt_import_re
name|'virt_import_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"^\\s*(?:import|from) nova\\.(?:tests\\.)?virt\\.(\\w+)"'
op|')'
newline|'\n'
DECL|variable|virt_config_re
name|'virt_config_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"CONF\\.import_opt\\(\'.*?\', \'nova\\.virt\\.(\\w+)(\'|.)"'
op|')'
newline|'\n'
DECL|variable|author_tag_re
name|'author_tag_re'
op|'='
op|'('
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^\\s*#\\s*@?(a|A)uthor:"'
op|')'
op|','
nl|'\n'
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^\\.\\.\\s+moduleauthor::"'
op|')'
op|')'
newline|'\n'
DECL|variable|asse_trueinst_re
name|'asse_trueinst_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*assertTrue\\(isinstance\\((\\w|\\.|\\\'|\\"|\\[|\\])+, "'
nl|'\n'
string|'"(\\w|\\.|\\\'|\\"|\\[|\\])+\\)\\)"'
op|')'
newline|'\n'
DECL|variable|asse_equal_type_re
name|'asse_equal_type_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*assertEqual\\(type\\((\\w|\\.|\\\'|\\"|\\[|\\])+\\), "'
nl|'\n'
string|'"(\\w|\\.|\\\'|\\"|\\[|\\])+\\)"'
op|')'
newline|'\n'
DECL|variable|asse_equal_end_with_none_re
name|'asse_equal_end_with_none_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"assertEqual\\(.*?,\\s+None\\)$"'
op|')'
newline|'\n'
DECL|variable|asse_equal_start_with_none_re
name|'asse_equal_start_with_none_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"assertEqual\\(None,"'
op|')'
newline|'\n'
DECL|variable|conf_attribute_set_re
name|'conf_attribute_set_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"CONF\\.[a-z0-9_.]+\\s*=\\s*\\w"'
op|')'
newline|'\n'
DECL|variable|log_translation
name|'log_translation'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*LOG\\.(audit|error|critical)\\(\\s*(\'|\\")"'
op|')'
newline|'\n'
DECL|variable|log_translation_info
name|'log_translation_info'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*LOG\\.(info)\\(\\s*(_\\(|\'|\\")"'
op|')'
newline|'\n'
DECL|variable|log_translation_exception
name|'log_translation_exception'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*LOG\\.(exception)\\(\\s*(_\\(|\'|\\")"'
op|')'
newline|'\n'
DECL|variable|log_translation_LW
name|'log_translation_LW'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*LOG\\.(warning)\\(\\s*(_\\(|\'|\\")"'
op|')'
newline|'\n'
DECL|variable|log_warn
name|'log_warn'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*LOG\\.(warn)\\(\\s*(\'|\\"|_)"'
op|')'
newline|'\n'
DECL|variable|translated_log
name|'translated_log'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*LOG\\.(audit|error|info|critical|exception)"'
nl|'\n'
string|'"\\(\\s*_\\(\\s*(\'|\\")"'
op|')'
newline|'\n'
DECL|variable|mutable_default_args
name|'mutable_default_args'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"^\\s*def .+\\((.+=\\{\\}|.+=\\[\\])"'
op|')'
newline|'\n'
DECL|variable|string_translation
name|'string_translation'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"[^_]*_\\(\\s*(\'|\\")"'
op|')'
newline|'\n'
DECL|variable|underscore_import_check
name|'underscore_import_check'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"(.)*import _(.)*"'
op|')'
newline|'\n'
comment|'# We need this for cases where they have created their own _ function.'
nl|'\n'
DECL|variable|custom_underscore_check
name|'custom_underscore_check'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"(.)*_\\s*=\\s*(.)*"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseASTChecker
name|'class'
name|'BaseASTChecker'
op|'('
name|'ast'
op|'.'
name|'NodeVisitor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provides a simple framework for writing AST-based checks.\n\n    Subclasses should implement visit_* methods like any other AST visitor\n    implementation. When they detect an error for a particular node the\n    method should call ``self.add_error(offending_node)``. Details about\n    where in the code the error occurred will be pulled from the node\n    object.\n\n    Subclasses should also provide a class variable named CHECK_DESC to\n    be used for the human readable error message.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'tree'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This object is created automatically by pep8.\n\n        :param tree: an AST tree\n        :param filename: name of the file being analyzed\n                         (ignored by our checks)\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_tree'
op|'='
name|'tree'
newline|'\n'
name|'self'
op|'.'
name|'_errors'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called automatically by pep8."""'
newline|'\n'
name|'self'
op|'.'
name|'visit'
op|'('
name|'self'
op|'.'
name|'_tree'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_errors'
newline|'\n'
nl|'\n'
DECL|member|add_error
dedent|''
name|'def'
name|'add_error'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add an error caused by a node to the list of errors for pep8."""'
newline|'\n'
name|'message'
op|'='
name|'message'
name|'or'
name|'self'
op|'.'
name|'CHECK_DESC'
newline|'\n'
name|'error'
op|'='
op|'('
name|'node'
op|'.'
name|'lineno'
op|','
name|'node'
op|'.'
name|'col_offset'
op|','
name|'message'
op|','
name|'self'
op|'.'
name|'__class__'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_errors'
op|'.'
name|'append'
op|'('
name|'error'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_call_names
dedent|''
name|'def'
name|'_check_call_names'
op|'('
name|'self'
op|','
name|'call_node'
op|','
name|'names'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'call_node'
op|','
name|'ast'
op|'.'
name|'Call'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'call_node'
op|'.'
name|'func'
op|','
name|'ast'
op|'.'
name|'Name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'call_node'
op|'.'
name|'func'
op|'.'
name|'id'
name|'in'
name|'names'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_no_db_in_virt
dedent|''
dedent|''
name|'def'
name|'import_no_db_in_virt'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for db calls from nova/virt\n\n    As of grizzly-2 all the database calls have been removed from\n    nova/virt, and we want to keep it that way.\n\n    N307\n    """'
newline|'\n'
name|'if'
string|'"nova/virt"'
name|'in'
name|'filename'
name|'and'
name|'not'
name|'filename'
op|'.'
name|'endswith'
op|'('
string|'"fake.py"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"from nova import db"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
number|'0'
op|','
string|'"N307: nova.db import not allowed in nova/virt/*"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_db_session_in_public_api
dedent|''
dedent|''
dedent|''
name|'def'
name|'no_db_session_in_public_api'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
string|'"db/api.py"'
name|'in'
name|'filename'
name|'or'
string|'"db/sqlalchemy/api.py"'
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'session_check'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
number|'0'
op|','
string|'"N309: public db api methods may not accept session"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|use_timeutils_utcnow
dedent|''
dedent|''
dedent|''
name|'def'
name|'use_timeutils_utcnow'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
comment|'# tools are OK to use the standard datetime module'
nl|'\n'
indent|'    '
name|'if'
string|'"/tools/"'
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'msg'
op|'='
string|'"N310: timeutils.utcnow() must be used instead of datetime.%s()"'
newline|'\n'
nl|'\n'
name|'datetime_funcs'
op|'='
op|'['
string|"'now'"
op|','
string|"'utcnow'"
op|']'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'datetime_funcs'
op|':'
newline|'\n'
indent|'        '
name|'pos'
op|'='
name|'logical_line'
op|'.'
name|'find'
op|'('
string|"'datetime.%s'"
op|'%'
name|'f'
op|')'
newline|'\n'
name|'if'
name|'pos'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
name|'pos'
op|','
name|'msg'
op|'%'
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_virt_name
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_virt_name'
op|'('
name|'regex'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'m'
op|'='
name|'regex'
op|'.'
name|'match'
op|'('
name|'data'
op|')'
newline|'\n'
name|'if'
name|'m'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'driver'
op|'='
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
newline|'\n'
comment|'# Ignore things we mis-detect as virt drivers in the regex'
nl|'\n'
name|'if'
name|'driver'
name|'in'
op|'['
string|'"test_virt_drivers"'
op|','
string|'"driver"'
op|','
string|'"firewall"'
op|','
nl|'\n'
string|'"disk"'
op|','
string|'"api"'
op|','
string|'"imagecache"'
op|','
string|'"cpu"'
op|','
string|'"hardware"'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
comment|'# TODO(berrange): remove once bugs 1261826 and 126182 are'
nl|'\n'
comment|'# fixed, or baremetal driver is removed, which is first.'
nl|'\n'
dedent|''
name|'if'
name|'driver'
op|'=='
string|'"baremetal"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_no_virt_driver_import_deps
dedent|''
name|'def'
name|'import_no_virt_driver_import_deps'
op|'('
name|'physical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check virt drivers\' modules aren\'t imported by other drivers\n\n    Modules under each virt driver\'s directory are\n    considered private to that virt driver. Other drivers\n    in Nova must not access those drivers. Any code that\n    is to be shared should be refactored into a common\n    module\n\n    N311\n    """'
newline|'\n'
name|'thisdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_file_re'
op|','
name|'filename'
op|')'
newline|'\n'
name|'thatdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_import_re'
op|','
name|'physical_line'
op|')'
newline|'\n'
name|'if'
op|'('
name|'thatdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
op|'!='
name|'thatdriver'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
number|'0'
op|','
string|'"N311: importing code from other virt drivers forbidden"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_no_virt_driver_config_deps
dedent|''
dedent|''
name|'def'
name|'import_no_virt_driver_config_deps'
op|'('
name|'physical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check virt drivers\' config vars aren\'t used by other drivers\n\n    Modules under each virt driver\'s directory are\n    considered private to that virt driver. Other drivers\n    in Nova must not use their config vars. Any config vars\n    that are to be shared should be moved into a common module\n\n    N312\n    """'
newline|'\n'
name|'thisdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_file_re'
op|','
name|'filename'
op|')'
newline|'\n'
name|'thatdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_config_re'
op|','
name|'physical_line'
op|')'
newline|'\n'
name|'if'
op|'('
name|'thatdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
op|'!='
name|'thatdriver'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
number|'0'
op|','
string|'"N312: using config vars from other virt drivers forbidden"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|capital_cfg_help
dedent|''
dedent|''
name|'def'
name|'capital_cfg_help'
op|'('
name|'logical_line'
op|','
name|'tokens'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg'
op|'='
string|'"N313: capitalize help string"'
newline|'\n'
nl|'\n'
name|'if'
name|'cfg_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'t'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'tokens'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tokens'
op|'['
name|'t'
op|']'
op|'['
number|'1'
op|']'
op|'=='
string|'"help"'
op|':'
newline|'\n'
indent|'                '
name|'txt'
op|'='
name|'tokens'
op|'['
name|'t'
op|'+'
number|'2'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'txt'
op|')'
op|'>'
number|'1'
name|'and'
name|'txt'
op|'['
number|'1'
op|']'
op|'.'
name|'islower'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_vi_headers
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'no_vi_headers'
op|'('
name|'physical_line'
op|','
name|'line_number'
op|','
name|'lines'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for vi editor configuration in source files.\n\n    By default vi modelines can only appear in the first or\n    last 5 lines of a source file.\n\n    N314\n    """'
newline|'\n'
comment|'# NOTE(gilliard): line_number is 1-indexed'
nl|'\n'
name|'if'
name|'line_number'
op|'<='
number|'5'
name|'or'
name|'line_number'
op|'>'
name|'len'
op|'('
name|'lines'
op|')'
op|'-'
number|'5'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vi_header_re'
op|'.'
name|'match'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
op|','
string|'"N314: Don\'t put vi configuration in source files"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_author_tags
dedent|''
dedent|''
dedent|''
name|'def'
name|'no_author_tags'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'regex'
name|'in'
name|'author_tag_re'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'regex'
op|'.'
name|'match'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'physical_line'
op|'='
name|'physical_line'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'pos'
op|'='
name|'physical_line'
op|'.'
name|'find'
op|'('
string|"'moduleauthor'"
op|')'
newline|'\n'
name|'if'
name|'pos'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'pos'
op|'='
name|'physical_line'
op|'.'
name|'find'
op|'('
string|"'author'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'pos'
op|','
string|'"N315: Don\'t use author tags"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_true_instance
dedent|''
dedent|''
dedent|''
name|'def'
name|'assert_true_instance'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for assertTrue(isinstance(a, b)) sentences\n\n    N316\n    """'
newline|'\n'
name|'if'
name|'asse_trueinst_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N316: assertTrue(isinstance(a, b)) sentences not allowed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_equal_type
dedent|''
dedent|''
name|'def'
name|'assert_equal_type'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for assertEqual(type(A), B) sentences\n\n    N317\n    """'
newline|'\n'
name|'if'
name|'asse_equal_type_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N317: assertEqual(type(A), B) sentences not allowed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_equal_none
dedent|''
dedent|''
name|'def'
name|'assert_equal_none'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for assertEqual(A, None) or assertEqual(None, A) sentences\n\n    N318\n    """'
newline|'\n'
name|'res'
op|'='
op|'('
name|'asse_equal_start_with_none_re'
op|'.'
name|'search'
op|'('
name|'logical_line'
op|')'
name|'or'
nl|'\n'
name|'asse_equal_end_with_none_re'
op|'.'
name|'search'
op|'('
name|'logical_line'
op|')'
op|')'
newline|'\n'
name|'if'
name|'res'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N318: assertEqual(A, None) or assertEqual(None, A) "'
nl|'\n'
string|'"sentences not allowed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_translate_debug_logs
dedent|''
dedent|''
name|'def'
name|'no_translate_debug_logs'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for \'LOG.debug(_(\'\n\n    As per our translation policy,\n    https://wiki.openstack.org/wiki/LoggingStandards#Log_Translation\n    we shouldn\'t translate debug level logs.\n\n    * This check assumes that \'LOG\' is a logger.\n    * Use filename so we can start enforcing this in specific folders instead\n      of needing to do so all at once.\n\n    N319\n    """'
newline|'\n'
name|'if'
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"LOG.debug(_("'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N319 Don\'t translate debug level logs"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_setting_conf_directly_in_tests
dedent|''
dedent|''
name|'def'
name|'no_setting_conf_directly_in_tests'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for setting CONF.* attributes directly in tests\n\n    The value can leak out of tests affecting how subsequent tests run.\n    Using self.flags(option=value) is the preferred method to temporarily\n    set config options in tests.\n\n    N320\n    """'
newline|'\n'
name|'if'
string|"'nova/tests/'"
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'conf_attribute_set_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
newline|'\n'
name|'if'
name|'res'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
number|'0'
op|','
string|'"N320: Setting CONF.* attributes directly in tests is "'
nl|'\n'
string|'"forbidden. Use self.flags(option=value) instead"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_log_translations
dedent|''
dedent|''
dedent|''
name|'def'
name|'validate_log_translations'
op|'('
name|'logical_line'
op|','
name|'physical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
comment|'# Translations are not required in the test directory'
nl|'\n'
comment|'# and the Xen utilities'
nl|'\n'
indent|'    '
name|'if'
op|'('
string|'"nova/tests"'
name|'in'
name|'filename'
name|'or'
nl|'\n'
string|'"plugins/xenserver/xenapi/etc/xapi.d"'
name|'in'
name|'filename'
name|'or'
nl|'\n'
comment|'# TODO(Mike_D):Needs to be remove with:'
nl|'\n'
comment|'# I075ab2a522272f2082c292dfedc877abd8ebe328'
nl|'\n'
string|'"nova/virt"'
name|'in'
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'pep8'
op|'.'
name|'noqa'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'msg'
op|'='
string|'"N328: LOG.info messages require translations `_LI()`!"'
newline|'\n'
name|'if'
name|'log_translation_info'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'='
string|'"N329: LOG.exception messages require translations `_LE()`!"'
newline|'\n'
name|'if'
name|'log_translation_exception'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'='
string|'"N330: LOG.warning messages require translations `_LW()`!"'
newline|'\n'
name|'if'
name|'log_translation_LW'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'='
string|'"N331: Use LOG.warning due to compatibility with py3"'
newline|'\n'
name|'if'
name|'log_warn'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'='
string|'"N321: Log messages require translations!"'
newline|'\n'
name|'if'
name|'log_translation'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_mutable_default_args
dedent|''
dedent|''
name|'def'
name|'no_mutable_default_args'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg'
op|'='
string|'"N322: Method\'s default argument shouldn\'t be mutable!"'
newline|'\n'
name|'if'
name|'mutable_default_args'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_explicit_underscore_import
dedent|''
dedent|''
name|'def'
name|'check_explicit_underscore_import'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for explicit import of the _ function\n\n    We need to ensure that any files that are using the _() function\n    to translate logs are explicitly importing the _ function.  We\n    can\'t trust unit test to catch whether the import has been\n    added so we need to check for it here.\n    """'
newline|'\n'
nl|'\n'
comment|'# Build a list of the files that have _ imported.  No further'
nl|'\n'
comment|'# checking needed once it is found.'
nl|'\n'
name|'if'
name|'filename'
name|'in'
name|'UNDERSCORE_IMPORT_FILES'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'underscore_import_check'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
name|'or'
nl|'\n'
name|'custom_underscore_check'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'UNDERSCORE_IMPORT_FILES'
op|'.'
name|'append'
op|'('
name|'filename'
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'translated_log'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
name|'or'
nl|'\n'
name|'string_translation'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N323: Found use of _() without explicit import of _ !"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|use_jsonutils
dedent|''
dedent|''
name|'def'
name|'use_jsonutils'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
comment|'# the code below that path is not meant to be executed from neutron'
nl|'\n'
comment|"# tree where jsonutils module is present, so don't enforce its usage"
nl|'\n'
comment|'# for this subdirectory'
nl|'\n'
indent|'    '
name|'if'
string|'"plugins/xenserver"'
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
comment|'# tools are OK to use the standard json module'
nl|'\n'
dedent|''
name|'if'
string|'"/tools/"'
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'msg'
op|'='
string|'"N324: jsonutils.%(fun)s must be used instead of json.%(fun)s"'
newline|'\n'
nl|'\n'
name|'if'
string|'"json."'
name|'in'
name|'logical_line'
op|':'
newline|'\n'
indent|'        '
name|'json_funcs'
op|'='
op|'['
string|"'dumps('"
op|','
string|"'dump('"
op|','
string|"'loads('"
op|','
string|"'load('"
op|']'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'json_funcs'
op|':'
newline|'\n'
indent|'            '
name|'pos'
op|'='
name|'logical_line'
op|'.'
name|'find'
op|'('
string|"'json.%s'"
op|'%'
name|'f'
op|')'
newline|'\n'
name|'if'
name|'pos'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'yield'
op|'('
name|'pos'
op|','
name|'msg'
op|'%'
op|'{'
string|"'fun'"
op|':'
name|'f'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_assert_called_once
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'check_assert_called_once'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg'
op|'='
op|'('
string|'"N327: assert_called_once is a no-op. please use assert_called_"'
nl|'\n'
string|'"once_with to test with explicit parameters or an assertEqual with"'
nl|'\n'
string|'" call_count."'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'nova/tests/'"
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'pos'
op|'='
name|'logical_line'
op|'.'
name|'find'
op|'('
string|"'.assert_called_once('"
op|')'
newline|'\n'
name|'if'
name|'pos'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
name|'pos'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CheckForStrUnicodeExc
dedent|''
dedent|''
dedent|''
name|'class'
name|'CheckForStrUnicodeExc'
op|'('
name|'BaseASTChecker'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks for the use of str() or unicode() on an exception.\n\n    This currently only handles the case where str() or unicode()\n    is used in the scope of an exception handler.  If the exception\n    is passed into a function, returned from an assertRaises, or\n    used on an exception created in the same scope, this does not\n    catch it.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|CHECK_DESC
name|'CHECK_DESC'
op|'='
op|'('
string|"'N325 str() and unicode() cannot be used on an '"
nl|'\n'
string|"'exception.  Remove or use six.text_type()'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'tree'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CheckForStrUnicodeExc'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'tree'
op|','
name|'filename'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'already_checked'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|visit_TryExcept
dedent|''
name|'def'
name|'visit_TryExcept'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'handler'
name|'in'
name|'node'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'handler'
op|'.'
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'name'
op|'.'
name|'append'
op|'('
name|'handler'
op|'.'
name|'name'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'super'
op|'('
name|'CheckForStrUnicodeExc'
op|','
name|'self'
op|')'
op|'.'
name|'generic_visit'
op|'('
name|'node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'self'
op|'.'
name|'name'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'super'
op|'('
name|'CheckForStrUnicodeExc'
op|','
name|'self'
op|')'
op|'.'
name|'generic_visit'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|visit_Call
dedent|''
dedent|''
dedent|''
name|'def'
name|'visit_Call'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_check_call_names'
op|'('
name|'node'
op|','
op|'['
string|"'str'"
op|','
string|"'unicode'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'node'
name|'not'
name|'in'
name|'self'
op|'.'
name|'already_checked'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'already_checked'
op|'.'
name|'append'
op|'('
name|'node'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'node'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
op|','
name|'ast'
op|'.'
name|'Name'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'node'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
name|'in'
name|'self'
op|'.'
name|'name'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'add_error'
op|'('
name|'node'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'super'
op|'('
name|'CheckForStrUnicodeExc'
op|','
name|'self'
op|')'
op|'.'
name|'generic_visit'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CheckForTransAdd
dedent|''
dedent|''
name|'class'
name|'CheckForTransAdd'
op|'('
name|'BaseASTChecker'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks for the use of concatenation on a translated string.\n\n    Translations should not be concatenated with other strings, but\n    should instead include the string being added to the translated\n    string to give the translators the most information.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|CHECK_DESC
name|'CHECK_DESC'
op|'='
op|'('
string|"'N326 Translated messages cannot be concatenated.  '"
nl|'\n'
string|"'String should be included in translated message.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|TRANS_FUNC
name|'TRANS_FUNC'
op|'='
op|'['
string|"'_'"
op|','
string|"'_LI'"
op|','
string|"'_LW'"
op|','
string|"'_LE'"
op|','
string|"'_LC'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|visit_BinOp
name|'def'
name|'visit_BinOp'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'node'
op|'.'
name|'op'
op|','
name|'ast'
op|'.'
name|'Add'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_check_call_names'
op|'('
name|'node'
op|'.'
name|'left'
op|','
name|'self'
op|'.'
name|'TRANS_FUNC'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'add_error'
op|'('
name|'node'
op|'.'
name|'left'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'_check_call_names'
op|'('
name|'node'
op|'.'
name|'right'
op|','
name|'self'
op|'.'
name|'TRANS_FUNC'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'add_error'
op|'('
name|'node'
op|'.'
name|'right'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'super'
op|'('
name|'CheckForTransAdd'
op|','
name|'self'
op|')'
op|'.'
name|'generic_visit'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|factory
dedent|''
dedent|''
name|'def'
name|'factory'
op|'('
name|'register'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'register'
op|'('
name|'import_no_db_in_virt'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_db_session_in_public_api'
op|')'
newline|'\n'
name|'register'
op|'('
name|'use_timeutils_utcnow'
op|')'
newline|'\n'
name|'register'
op|'('
name|'import_no_virt_driver_import_deps'
op|')'
newline|'\n'
name|'register'
op|'('
name|'import_no_virt_driver_config_deps'
op|')'
newline|'\n'
name|'register'
op|'('
name|'capital_cfg_help'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_vi_headers'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_author_tags'
op|')'
newline|'\n'
name|'register'
op|'('
name|'assert_true_instance'
op|')'
newline|'\n'
name|'register'
op|'('
name|'assert_equal_type'
op|')'
newline|'\n'
name|'register'
op|'('
name|'assert_equal_none'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_translate_debug_logs'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_setting_conf_directly_in_tests'
op|')'
newline|'\n'
name|'register'
op|'('
name|'validate_log_translations'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_mutable_default_args'
op|')'
newline|'\n'
name|'register'
op|'('
name|'check_explicit_underscore_import'
op|')'
newline|'\n'
name|'register'
op|'('
name|'use_jsonutils'
op|')'
newline|'\n'
name|'register'
op|'('
name|'check_assert_called_once'
op|')'
newline|'\n'
name|'register'
op|'('
name|'CheckForStrUnicodeExc'
op|')'
newline|'\n'
name|'register'
op|'('
name|'CheckForTransAdd'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
