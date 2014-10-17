begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
name|'textwrap'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'pep8'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'hacking'
name|'import'
name|'checks'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HackingTestCase
name|'class'
name|'HackingTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This class tests the hacking checks in nova.hacking.checks by passing\n    strings to the check methods like the pep8/flake8 parser would. The parser\n    loops over each line in the file and then passes the parameters to the\n    check method. The parameter names in the check method dictate what type of\n    object is passed to the check method. The parameter types are::\n\n        logical_line: A processed line with the following modifications:\n            - Multi-line statements converted to a single line.\n            - Stripped left and right.\n            - Contents of strings replaced with "xxx" of same length.\n            - Comments removed.\n        physical_line: Raw line of text from the input file.\n        lines: a list of the raw lines from the input file\n        tokens: the tokens that contribute to this logical line\n        line_number: line number in the input file\n        total_lines: number of lines in the input file\n        blank_lines: blank lines before this one\n        indent_char: indentation character in this file (" " or "\\t")\n        indent_level: indentation (with tabs expanded to multiples of 8)\n        previous_indent_level: indentation on previous line\n        previous_logical: previous logical line\n        filename: Path of the file being run through pep8\n\n    When running a test on a check method the return will be False/None if\n    there is no violation in the sample input. If there is an error a tuple is\n    returned with a position in the line, and a message. So to check the result\n    just assertTrue if the check is expected to fail and assertFalse if it\n    should pass.\n    """'
newline|'\n'
DECL|member|test_virt_driver_imports
name|'def'
name|'test_virt_driver_imports'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'expect'
op|'='
op|'('
number|'0'
op|','
string|'"N311: importing code from other virt drivers forbidden"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expect'
op|','
name|'checks'
op|'.'
name|'import_no_virt_driver_import_deps'
op|'('
nl|'\n'
string|'"from nova.virt.libvirt import utils as libvirt_utils"'
op|','
nl|'\n'
string|'"./nova/virt/xenapi/driver.py"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expect'
op|','
name|'checks'
op|'.'
name|'import_no_virt_driver_import_deps'
op|'('
nl|'\n'
string|'"import nova.virt.libvirt.utils as libvirt_utils"'
op|','
nl|'\n'
string|'"./nova/virt/xenapi/driver.py"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'import_no_virt_driver_import_deps'
op|'('
nl|'\n'
string|'"from nova.virt.libvirt import utils as libvirt_utils"'
op|','
nl|'\n'
string|'"./nova/virt/libvirt/driver.py"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'import_no_virt_driver_import_deps'
op|'('
nl|'\n'
string|'"import nova.virt.firewall"'
op|','
nl|'\n'
string|'"./nova/virt/libvirt/firewall.py"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_virt_driver_config_vars
dedent|''
name|'def'
name|'test_virt_driver_config_vars'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'checks'
op|'.'
name|'import_no_virt_driver_config_deps'
op|'('
nl|'\n'
string|'"CONF.import_opt(\'volume_drivers\', "'
nl|'\n'
string|'"\'nova.virt.libvirt.driver\', group=\'libvirt\')"'
op|','
nl|'\n'
string|'"./nova/virt/xenapi/driver.py"'
op|')'
op|','
name|'tuple'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'import_no_virt_driver_config_deps'
op|'('
nl|'\n'
string|'"CONF.import_opt(\'volume_drivers\', "'
nl|'\n'
string|'"\'nova.virt.libvirt.driver\', group=\'libvirt\')"'
op|','
nl|'\n'
string|'"./nova/virt/libvirt/volume.py"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_vi_headers
dedent|''
name|'def'
name|'test_no_vi_headers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'lines'
op|'='
op|'['
string|"'Line 1\\n'"
op|','
string|"'Line 2\\n'"
op|','
string|"'Line 3\\n'"
op|','
string|"'Line 4\\n'"
op|','
string|"'Line 5\\n'"
op|','
nl|'\n'
string|"'Line 6\\n'"
op|','
string|"'Line 7\\n'"
op|','
string|"'Line 8\\n'"
op|','
string|"'Line 9\\n'"
op|','
string|"'Line 10\\n'"
op|','
nl|'\n'
string|"'Line 11\\n'"
op|','
string|"'Line 12\\n'"
op|','
string|"'Line 13\\n'"
op|','
string|"'Line14\\n'"
op|','
string|"'Line15\\n'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'no_vi_headers'
op|'('
nl|'\n'
string|'"Test string foo"'
op|','
number|'1'
op|','
name|'lines'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_vi_headers'
op|'('
nl|'\n'
string|'"# vim: et tabstop=4 shiftwidth=4 softtabstop=4"'
op|','
nl|'\n'
number|'2'
op|','
name|'lines'
op|')'
op|')'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'no_vi_headers'
op|'('
nl|'\n'
string|'"# vim: et tabstop=4 shiftwidth=4 softtabstop=4"'
op|','
nl|'\n'
number|'6'
op|','
name|'lines'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'no_vi_headers'
op|'('
nl|'\n'
string|'"# vim: et tabstop=4 shiftwidth=4 softtabstop=4"'
op|','
nl|'\n'
number|'9'
op|','
name|'lines'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_vi_headers'
op|'('
nl|'\n'
string|'"# vim: et tabstop=4 shiftwidth=4 softtabstop=4"'
op|','
nl|'\n'
number|'14'
op|','
name|'lines'
op|')'
op|')'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'no_vi_headers'
op|'('
nl|'\n'
string|'"Test end string for vi"'
op|','
nl|'\n'
number|'15'
op|','
name|'lines'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_author_tags
dedent|''
name|'def'
name|'test_no_author_tags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# author: jogo"'
op|')'
op|','
name|'tuple'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# @author: jogo"'
op|')'
op|','
name|'tuple'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# @Author: jogo"'
op|')'
op|','
name|'tuple'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# Author: jogo"'
op|')'
op|','
name|'tuple'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'".. moduleauthor:: jogo"'
op|')'
op|','
nl|'\n'
name|'tuple'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# authorization of this"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# author: jogo"'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'"# Author: jogo"'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'checks'
op|'.'
name|'no_author_tags'
op|'('
string|'".. moduleauthor:: jogo"'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_assert_true_instance
dedent|''
name|'def'
name|'test_assert_true_instance'
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
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_true_instance'
op|'('
nl|'\n'
string|'"self.assertTrue(isinstance(e, "'
nl|'\n'
string|'"exception.BuildAbortException))"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_true_instance'
op|'('
string|'"self.assertTrue()"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_assert_equal_type
dedent|''
name|'def'
name|'test_assert_equal_type'
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
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_equal_type'
op|'('
nl|'\n'
string|'"self.assertEqual(type(als[\'QuicAssist\']), list)"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_equal_type'
op|'('
string|'"self.assertTrue()"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_assert_equal_none
dedent|''
name|'def'
name|'test_assert_equal_none'
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
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_equal_none'
op|'('
nl|'\n'
string|'"self.assertEqual(A, None)"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_equal_none'
op|'('
nl|'\n'
string|'"self.assertEqual(None, A)"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'assert_equal_none'
op|'('
string|'"self.assertIsNone()"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_translate_debug_logs
dedent|''
name|'def'
name|'test_no_translate_debug_logs'
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
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_translate_debug_logs'
op|'('
nl|'\n'
string|'"LOG.debug(_(\'foo\'))"'
op|','
string|'"nova/scheduler/foo.py"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_translate_debug_logs'
op|'('
nl|'\n'
string|'"LOG.debug(\'foo\')"'
op|','
string|'"nova/scheduler/foo.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_translate_debug_logs'
op|'('
nl|'\n'
string|'"LOG.info(_(\'foo\'))"'
op|','
string|'"nova/scheduler/foo.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_setting_conf_directly_in_tests
dedent|''
name|'def'
name|'test_no_setting_conf_directly_in_tests'
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
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_setting_conf_directly_in_tests'
op|'('
nl|'\n'
string|'"CONF.option = 1"'
op|','
string|'"nova/tests/test_foo.py"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_setting_conf_directly_in_tests'
op|'('
nl|'\n'
string|'"CONF.group.option = 1"'
op|','
string|'"nova/tests/test_foo.py"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_setting_conf_directly_in_tests'
op|'('
nl|'\n'
string|'"CONF.option = foo = 1"'
op|','
string|'"nova/tests/test_foo.py"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|"# Shouldn't fail with comparisons"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_setting_conf_directly_in_tests'
op|'('
nl|'\n'
string|'"CONF.option == \'foo\'"'
op|','
string|'"nova/tests/test_foo.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_setting_conf_directly_in_tests'
op|'('
nl|'\n'
string|'"CONF.option != 1"'
op|','
string|'"nova/tests/test_foo.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|"# Shouldn't fail since not in nova/tests/"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_setting_conf_directly_in_tests'
op|'('
nl|'\n'
string|'"CONF.option = 1"'
op|','
string|'"nova/compute/foo.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_log_translations
dedent|''
name|'def'
name|'test_log_translations'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logs'
op|'='
op|'['
string|"'audit'"
op|','
string|"'error'"
op|','
string|"'info'"
op|','
string|"'warn'"
op|','
string|"'warning'"
op|','
string|"'critical'"
op|','
nl|'\n'
string|"'exception'"
op|']'
newline|'\n'
name|'levels'
op|'='
op|'['
string|"'_LI'"
op|','
string|"'_LW'"
op|','
string|"'_LE'"
op|','
string|"'_LC'"
op|']'
newline|'\n'
name|'debug'
op|'='
string|'"LOG.debug(\'OK\')"'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'checks'
op|'.'
name|'validate_log_translations'
op|'('
name|'debug'
op|','
name|'debug'
op|','
string|"'f'"
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'log'
name|'in'
name|'logs'
op|':'
newline|'\n'
indent|'            '
name|'bad'
op|'='
string|'\'LOG.%s("Bad")\''
op|'%'
name|'log'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'checks'
op|'.'
name|'validate_log_translations'
op|'('
name|'bad'
op|','
name|'bad'
op|','
string|"'f'"
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'ok'
op|'='
string|'"LOG.%s(_(\'OK\'))"'
op|'%'
name|'log'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'checks'
op|'.'
name|'validate_log_translations'
op|'('
name|'ok'
op|','
name|'ok'
op|','
string|"'f'"
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'ok'
op|'='
string|'"LOG.%s(\'OK\')    # noqa"'
op|'%'
name|'log'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'checks'
op|'.'
name|'validate_log_translations'
op|'('
name|'ok'
op|','
name|'ok'
op|','
string|"'f'"
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'ok'
op|'='
string|'"LOG.%s(variable)"'
op|'%'
name|'log'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'checks'
op|'.'
name|'validate_log_translations'
op|'('
name|'ok'
op|','
name|'ok'
op|','
string|"'f'"
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'level'
name|'in'
name|'levels'
op|':'
newline|'\n'
indent|'                '
name|'ok'
op|'='
string|'"LOG.%s(%s(\'OK\'))"'
op|'%'
op|'('
name|'log'
op|','
name|'level'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
nl|'\n'
name|'checks'
op|'.'
name|'validate_log_translations'
op|'('
name|'ok'
op|','
name|'ok'
op|','
string|"'f'"
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_mutable_default_args
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_no_mutable_default_args'
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
number|'1'
op|','
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_mutable_default_args'
op|'('
nl|'\n'
string|'" def fake_suds_context(calls={}):"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_mutable_default_args'
op|'('
nl|'\n'
string|'"def get_info_from_bdm(virt_type, bdm, mapping=[])"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_mutable_default_args'
op|'('
nl|'\n'
string|'"defined = []"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'no_mutable_default_args'
op|'('
nl|'\n'
string|'"defined, undefined = [], {}"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_explicit_underscore_import
dedent|''
name|'def'
name|'test_check_explicit_underscore_import'
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
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"LOG.info(_(\'My info message\'))"'
op|','
nl|'\n'
string|'"cinder/tests/other_files.py"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"msg = _(\'My message\')"'
op|','
nl|'\n'
string|'"cinder/tests/other_files.py"'
op|')'
op|')'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"from cinder.i18n import _"'
op|','
nl|'\n'
string|'"cinder/tests/other_files.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"LOG.info(_(\'My info message\'))"'
op|','
nl|'\n'
string|'"cinder/tests/other_files.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"msg = _(\'My message\')"'
op|','
nl|'\n'
string|'"cinder/tests/other_files.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"from cinder.i18n import _, _LW"'
op|','
nl|'\n'
string|'"cinder/tests/other_files2.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"msg = _(\'My message\')"'
op|','
nl|'\n'
string|'"cinder/tests/other_files2.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"_ = translations.ugettext"'
op|','
nl|'\n'
string|'"cinder/tests/other_files3.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'check_explicit_underscore_import'
op|'('
nl|'\n'
string|'"msg = _(\'My message\')"'
op|','
nl|'\n'
string|'"cinder/tests/other_files3.py"'
op|')'
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_jsonutils
dedent|''
name|'def'
name|'test_use_jsonutils'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|__get_msg
indent|'        '
name|'def'
name|'__get_msg'
op|'('
name|'fun'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
string|'"N324: jsonutils.%(fun)s must be used instead of "'
nl|'\n'
string|'"json.%(fun)s"'
op|'%'
op|'{'
string|"'fun'"
op|':'
name|'fun'
op|'}'
op|')'
newline|'\n'
name|'return'
op|'['
op|'('
number|'0'
op|','
name|'msg'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'method'
name|'in'
op|'('
string|"'dump'"
op|','
string|"'dumps'"
op|','
string|"'load'"
op|','
string|"'loads'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'__get_msg'
op|'('
name|'method'
op|')'
op|','
nl|'\n'
name|'list'
op|'('
name|'checks'
op|'.'
name|'use_jsonutils'
op|'('
string|'"json.%s("'
op|'%'
name|'method'
op|','
nl|'\n'
string|'"./nova/virt/xenapi/driver.py"'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'use_jsonutils'
op|'('
string|'"json.%s("'
op|'%'
name|'method'
op|','
nl|'\n'
string|'"./plugins/xenserver/script.py"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'use_jsonutils'
op|'('
string|'"jsonx.%s("'
op|'%'
name|'method'
op|','
nl|'\n'
string|'"./nova/virt/xenapi/driver.py"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'len'
op|'('
name|'list'
op|'('
name|'checks'
op|'.'
name|'use_jsonutils'
op|'('
string|'"json.dumb"'
op|','
nl|'\n'
string|'"./nova/virt/xenapi/driver.py"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# We are patching pep8 so that only the check under test is actually'
nl|'\n'
comment|'# installed.'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'pep8._checks'"
op|','
nl|'\n'
op|'{'
string|"'physical_line'"
op|':'
op|'{'
op|'}'
op|','
string|"'logical_line'"
op|':'
op|'{'
op|'}'
op|','
string|"'tree'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
DECL|member|_run_check
name|'def'
name|'_run_check'
op|'('
name|'self'
op|','
name|'code'
op|','
name|'checker'
op|','
name|'filename'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pep8'
op|'.'
name|'register_check'
op|'('
name|'checker'
op|')'
newline|'\n'
nl|'\n'
name|'lines'
op|'='
name|'textwrap'
op|'.'
name|'dedent'
op|'('
name|'code'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'splitlines'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'checker'
op|'='
name|'pep8'
op|'.'
name|'Checker'
op|'('
name|'filename'
op|'='
name|'filename'
op|','
name|'lines'
op|'='
name|'lines'
op|')'
newline|'\n'
name|'checker'
op|'.'
name|'check_all'
op|'('
op|')'
newline|'\n'
name|'checker'
op|'.'
name|'report'
op|'.'
name|'_deferred_print'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'return'
name|'checker'
op|'.'
name|'report'
op|'.'
name|'_deferred_print'
newline|'\n'
nl|'\n'
DECL|member|_assert_has_errors
dedent|''
name|'def'
name|'_assert_has_errors'
op|'('
name|'self'
op|','
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'None'
op|','
nl|'\n'
name|'filename'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actual_errors'
op|'='
op|'['
name|'e'
op|'['
op|':'
number|'3'
op|']'
name|'for'
name|'e'
name|'in'
nl|'\n'
name|'self'
op|'.'
name|'_run_check'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'filename'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_errors'
name|'or'
op|'['
op|']'
op|','
name|'actual_errors'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_assert_called_once
dedent|''
name|'def'
name|'test_assert_called_once'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'checker'
op|'='
name|'checks'
op|'.'
name|'check_assert_called_once'
newline|'\n'
name|'code'
op|'='
string|'"""\n               mock = Mock()\n               mock.method(1, 2, 3, test=\'wow\')\n               mock.method.assert_called_once()\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|'('
number|'3'
op|','
number|'11'
op|','
string|"'N327'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|','
nl|'\n'
name|'filename'
op|'='
string|"'nova/tests/test_assert.py'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_str_unicode_exception
dedent|''
name|'def'
name|'test_str_unicode_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'checker'
op|'='
name|'checks'
op|'.'
name|'CheckForStrUnicodeExc'
newline|'\n'
name|'code'
op|'='
string|'"""\n               def f(a, b):\n                   try:\n                       p = str(a) + str(b)\n                   except ValueError as e:\n                       p = str(e)\n                   return p\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|'('
number|'5'
op|','
number|'16'
op|','
string|"'N325'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
nl|'\n'
name|'code'
op|'='
string|'"""\n               def f(a, b):\n                   try:\n                       p = unicode(a) + str(b)\n                   except ValueError as e:\n                       p = e\n                   return p\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
nl|'\n'
name|'code'
op|'='
string|'"""\n               def f(a, b):\n                   try:\n                       p = str(a) + str(b)\n                   except ValueError as e:\n                       p = unicode(e)\n                   return p\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|'('
number|'5'
op|','
number|'20'
op|','
string|"'N325'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
nl|'\n'
name|'code'
op|'='
string|'"""\n               def f(a, b):\n                   try:\n                       p = str(a) + str(b)\n                   except ValueError as e:\n                       try:\n                           p  = unicode(a) + unicode(b)\n                       except ValueError as ve:\n                           p = str(e) + str(ve)\n                       p = e\n                   return p\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|'('
number|'8'
op|','
number|'20'
op|','
string|"'N325'"
op|')'
op|','
op|'('
number|'8'
op|','
number|'29'
op|','
string|"'N325'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
nl|'\n'
name|'code'
op|'='
string|'"""\n               def f(a, b):\n                   try:\n                       p = str(a) + str(b)\n                   except ValueError as e:\n                       try:\n                           p  = unicode(a) + unicode(b)\n                       except ValueError as ve:\n                           p = str(e) + unicode(ve)\n                       p = str(e)\n                   return p\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|'('
number|'8'
op|','
number|'20'
op|','
string|"'N325'"
op|')'
op|','
op|'('
number|'8'
op|','
number|'33'
op|','
string|"'N325'"
op|')'
op|','
op|'('
number|'9'
op|','
number|'16'
op|','
string|"'N325'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trans_add
dedent|''
name|'def'
name|'test_trans_add'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'checker'
op|'='
name|'checks'
op|'.'
name|'CheckForTransAdd'
newline|'\n'
name|'code'
op|'='
string|'"""\n               def fake_tran(msg):\n                   return msg\n\n\n               _ = fake_tran\n               _LI = _\n               _LW = _\n               _LE = _\n               _LC = _\n\n\n               def f(a, b):\n                   msg = _(\'test\') + \'add me\'\n                   msg = _LI(\'test\') + \'add me\'\n                   msg = _LW(\'test\') + \'add me\'\n                   msg = _LE(\'test\') + \'add me\'\n                   msg = _LC(\'test\') + \'add me\'\n                   msg = \'add to me\' + _(\'test\')\n                   return msg\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|'('
number|'13'
op|','
number|'10'
op|','
string|"'N326'"
op|')'
op|','
op|'('
number|'14'
op|','
number|'10'
op|','
string|"'N326'"
op|')'
op|','
op|'('
number|'15'
op|','
number|'10'
op|','
string|"'N326'"
op|')'
op|','
nl|'\n'
op|'('
number|'16'
op|','
number|'10'
op|','
string|"'N326'"
op|')'
op|','
op|'('
number|'17'
op|','
number|'10'
op|','
string|"'N326'"
op|')'
op|','
op|'('
number|'18'
op|','
number|'24'
op|','
string|"'N326'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
nl|'\n'
name|'code'
op|'='
string|'"""\n               def f(a, b):\n                   msg = \'test\' + \'add me\'\n                   return msg\n               """'
newline|'\n'
name|'errors'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assert_has_errors'
op|'('
name|'code'
op|','
name|'checker'
op|','
name|'expected_errors'
op|'='
name|'errors'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
