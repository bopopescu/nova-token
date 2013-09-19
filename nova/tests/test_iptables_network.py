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
string|'"""Unit Tests for network code."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IptablesManagerTestCase
name|'class'
name|'IptablesManagerTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|binary_name
indent|'    '
name|'binary_name'
op|'='
name|'linux_net'
op|'.'
name|'get_binary_name'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|sample_filter
name|'sample_filter'
op|'='
op|'['
string|"'#Generated by iptables-save on Fri Feb 18 15:17:05 2011'"
op|','
nl|'\n'
string|"'*filter'"
op|','
nl|'\n'
string|"':INPUT ACCEPT [2223527:305688874]'"
op|','
nl|'\n'
string|"':FORWARD ACCEPT [0:0]'"
op|','
nl|'\n'
string|"':OUTPUT ACCEPT [2172501:140856656]'"
op|','
nl|'\n'
string|"':iptables-top-rule - [0:0]'"
op|','
nl|'\n'
string|"':iptables-bottom-rule - [0:0]'"
op|','
nl|'\n'
string|"':%s-FORWARD - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-INPUT - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-local - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-OUTPUT - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':nova-filter-top - [0:0]'"
op|','
nl|'\n'
string|"'[0:0] -A FORWARD -j nova-filter-top'"
op|','
nl|'\n'
string|"'[0:0] -A OUTPUT -j nova-filter-top'"
op|','
nl|'\n'
string|"'[0:0] -A nova-filter-top -j %s-local'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A INPUT -j %s-INPUT'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A OUTPUT -j %s-OUTPUT'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A FORWARD -j %s-FORWARD'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A INPUT -i virbr0 -p udp -m udp --dport 53 '"
nl|'\n'
string|"'-j ACCEPT'"
op|','
nl|'\n'
string|"'[0:0] -A INPUT -i virbr0 -p tcp -m tcp --dport 53 '"
nl|'\n'
string|"'-j ACCEPT'"
op|','
nl|'\n'
string|"'[0:0] -A INPUT -i virbr0 -p udp -m udp --dport 67 '"
nl|'\n'
string|"'-j ACCEPT'"
op|','
nl|'\n'
string|"'[0:0] -A INPUT -i virbr0 -p tcp -m tcp --dport 67 '"
nl|'\n'
string|"'-j ACCEPT'"
op|','
nl|'\n'
string|"'[0:0] -A FORWARD -s 192.168.122.0/24 -i virbr0 '"
nl|'\n'
string|"'-j ACCEPT'"
op|','
nl|'\n'
string|"'[0:0] -A FORWARD -i virbr0 -o virbr0 -j ACCEPT'"
op|','
nl|'\n'
string|"'[0:0] -A FORWARD -o virbr0 -j REJECT --reject-with '"
nl|'\n'
string|"'icmp-port-unreachable'"
op|','
nl|'\n'
string|"'[0:0] -A FORWARD -i virbr0 -j REJECT --reject-with '"
nl|'\n'
string|"'icmp-port-unreachable'"
op|','
nl|'\n'
string|"'COMMIT'"
op|','
nl|'\n'
string|"'# Completed on Fri Feb 18 15:17:05 2011'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|sample_nat
name|'sample_nat'
op|'='
op|'['
string|"'# Generated by iptables-save on Fri Feb 18 15:17:05 2011'"
op|','
nl|'\n'
string|"'*nat'"
op|','
nl|'\n'
string|"':PREROUTING ACCEPT [3936:762355]'"
op|','
nl|'\n'
string|"':INPUT ACCEPT [2447:225266]'"
op|','
nl|'\n'
string|"':OUTPUT ACCEPT [63491:4191863]'"
op|','
nl|'\n'
string|"':POSTROUTING ACCEPT [63112:4108641]'"
op|','
nl|'\n'
string|"':%s-OUTPUT - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-snat - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-PREROUTING - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-float-snat - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-POSTROUTING - [0:0]'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':nova-postrouting-bottom - [0:0]'"
op|','
nl|'\n'
string|"'[0:0] -A PREROUTING -j %s-PREROUTING'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A OUTPUT -j %s-OUTPUT'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A POSTROUTING -j %s-POSTROUTING'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A nova-postrouting-bottom '"
nl|'\n'
string|"'-j %s-snat'"
op|'%'
op|'('
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A %s-snat '"
nl|'\n'
string|"'-j %s-float-snat'"
op|'%'
op|'('
name|'binary_name'
op|','
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"'[0:0] -A POSTROUTING -j nova-postrouting-bottom'"
op|','
nl|'\n'
string|"'COMMIT'"
op|','
nl|'\n'
string|"'# Completed on Fri Feb 18 15:17:05 2011'"
op|']'
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
name|'IptablesManagerTestCase'
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
name|'manager'
op|'='
name|'linux_net'
op|'.'
name|'IptablesManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_duplicate_rules_no_dirty
dedent|''
name|'def'
name|'test_duplicate_rules_no_dirty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
newline|'\n'
name|'table'
op|'.'
name|'dirty'
op|'='
name|'False'
newline|'\n'
name|'num_rules'
op|'='
name|'len'
op|'('
name|'table'
op|'.'
name|'rules'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'FORWARD'"
op|','
string|"'-s 1.2.3.4/5 -j DROP'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'table'
op|'.'
name|'rules'
op|')'
op|','
name|'num_rules'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'table'
op|'.'
name|'dirty'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'dirty'
op|'='
name|'False'
newline|'\n'
name|'num_rules'
op|'='
name|'len'
op|'('
name|'table'
op|'.'
name|'rules'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'FORWARD'"
op|','
string|"'-s 1.2.3.4/5 -j DROP'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'table'
op|'.'
name|'rules'
op|')'
op|','
name|'num_rules'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'table'
op|'.'
name|'dirty'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_clean_tables_no_apply
dedent|''
name|'def'
name|'test_clean_tables_no_apply'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'table'
name|'in'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'.'
name|'dirty'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'for'
name|'table'
name|'in'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv6'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'.'
name|'dirty'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|error_apply
dedent|''
name|'def'
name|'error_apply'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
op|')'
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
name|'manager'
op|','
string|"'_apply'"
op|','
name|'error_apply'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_rules_are_wrapped
dedent|''
name|'def'
name|'test_filter_rules_are_wrapped'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_filter'
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'FORWARD'"
op|','
string|"'-s 1.2.3.4/5 -j DROP'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|','
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'[0:0] -A %s-FORWARD '"
nl|'\n'
string|"'-s 1.2.3.4/5 -j DROP'"
op|'%'
name|'self'
op|'.'
name|'binary_name'
name|'in'
name|'new_lines'
op|')'
newline|'\n'
nl|'\n'
name|'table'
op|'.'
name|'remove_rule'
op|'('
string|"'FORWARD'"
op|','
string|"'-s 1.2.3.4/5 -j DROP'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|','
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'[0:0] -A %s-FORWARD '"
nl|'\n'
string|"'-s 1.2.3.4/5 -j DROP'"
op|'%'
name|'self'
op|'.'
name|'binary_name'
nl|'\n'
name|'not'
name|'in'
name|'new_lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_rules_regex
dedent|''
name|'def'
name|'test_remove_rules_regex'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_nat'
newline|'\n'
name|'table'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'nat'"
op|']'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'float-snat'"
op|','
string|"'-s 10.0.0.1 -j SNAT --to 10.10.10.10'"
nl|'\n'
string|"' -d 10.0.0.1'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'float-snat'"
op|','
string|"'-s 10.0.0.1 -j SNAT --to 10.10.10.10'"
nl|'\n'
string|"' -o eth0'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'PREROUTING'"
op|','
string|"'-d 10.10.10.10 -j DNAT --to 10.0.0.1'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'OUTPUT'"
op|','
string|"'-d 10.10.10.10 -j DNAT --to 10.0.0.1'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'float-snat'"
op|','
string|"'-s 10.0.0.10 -j SNAT --to 10.10.10.11'"
nl|'\n'
string|"' -d 10.0.0.10'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'float-snat'"
op|','
string|"'-s 10.0.0.10 -j SNAT --to 10.10.10.11'"
nl|'\n'
string|"' -o eth0'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'PREROUTING'"
op|','
string|"'-d 10.10.10.11 -j DNAT --to 10.0.0.10'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'OUTPUT'"
op|','
string|"'-d 10.10.10.11 -j DNAT --to 10.0.0.10'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|','
string|"'nat'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'new_lines'
op|')'
op|'-'
name|'len'
op|'('
name|'current_lines'
op|')'
op|','
number|'8'
op|')'
newline|'\n'
name|'regex'
op|'='
string|"'.*\\s+%s(/32|\\s+|$)'"
newline|'\n'
name|'num_removed'
op|'='
name|'table'
op|'.'
name|'remove_rules_regex'
op|'('
name|'regex'
op|'%'
string|"'10.10.10.10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_removed'
op|','
number|'4'
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|','
string|"'nat'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'new_lines'
op|')'
op|'-'
name|'len'
op|'('
name|'current_lines'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'num_removed'
op|'='
name|'table'
op|'.'
name|'remove_rules_regex'
op|'('
name|'regex'
op|'%'
string|"'10.10.10.11'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_removed'
op|','
number|'4'
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|','
string|"'nat'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'new_lines'
op|','
name|'current_lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nat_rules
dedent|''
name|'def'
name|'test_nat_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_nat'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'nat'"
op|']'
op|','
nl|'\n'
string|"'nat'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
op|'['
string|"':%s-OUTPUT - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-float-snat - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-snat - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-PREROUTING - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-POSTROUTING - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'in'
name|'new_lines'
op|','
string|'"One of our chains went"'
nl|'\n'
string|'" missing."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'seen_lines'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'not'
name|'in'
name|'seen_lines'
op|','
nl|'\n'
string|'"Duplicate line: %s"'
op|'%'
name|'line'
op|')'
newline|'\n'
name|'seen_lines'
op|'.'
name|'add'
op|'('
name|'line'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'last_postrouting_line'
op|'='
string|"''"
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'line'
op|'.'
name|'startswith'
op|'('
string|"'[0:0] -A POSTROUTING'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'last_postrouting_line'
op|'='
name|'line'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-j nova-postrouting-bottom'"
name|'in'
name|'last_postrouting_line'
op|','
nl|'\n'
string|'"Last POSTROUTING rule does not jump to "'
nl|'\n'
string|'"nova-postouting-bottom: %s"'
op|'%'
name|'last_postrouting_line'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'chain'
name|'in'
op|'['
string|"'POSTROUTING'"
op|','
string|"'PREROUTING'"
op|','
string|"'OUTPUT'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'[0:0] -A %s -j %s-%s'"
op|'%'
nl|'\n'
op|'('
name|'chain'
op|','
name|'self'
op|'.'
name|'binary_name'
op|','
name|'chain'
op|')'
name|'in'
name|'new_lines'
op|','
nl|'\n'
string|'"Built-in chain %s not wrapped"'
op|'%'
op|'('
name|'chain'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_rules
dedent|''
dedent|''
name|'def'
name|'test_filter_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_filter'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|','
nl|'\n'
string|"'nat'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
op|'['
string|"':%s-FORWARD - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-INPUT - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-local - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|','
nl|'\n'
string|"':%s-OUTPUT - [0:0]'"
op|'%'
op|'('
name|'self'
op|'.'
name|'binary_name'
op|')'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'in'
name|'new_lines'
op|','
string|'"One of our chains went"'
nl|'\n'
string|'" missing."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'seen_lines'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'not'
name|'in'
name|'seen_lines'
op|','
nl|'\n'
string|'"Duplicate line: %s"'
op|'%'
name|'line'
op|')'
newline|'\n'
name|'seen_lines'
op|'.'
name|'add'
op|'('
name|'line'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'chain'
name|'in'
op|'['
string|"'FORWARD'"
op|','
string|"'OUTPUT'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'line'
op|'.'
name|'startswith'
op|'('
string|"'[0:0] -A %s'"
op|'%'
name|'chain'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-j nova-filter-top'"
name|'in'
name|'line'
op|','
nl|'\n'
string|'"First %s rule does not "'
nl|'\n'
string|'"jump to nova-filter-top"'
op|'%'
name|'chain'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'[0:0] -A nova-filter-top '"
nl|'\n'
string|"'-j %s-local'"
op|'%'
name|'self'
op|'.'
name|'binary_name'
name|'in'
name|'new_lines'
op|','
nl|'\n'
string|'"nova-filter-top does not jump to wrapped local chain"'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'chain'
name|'in'
op|'['
string|"'INPUT'"
op|','
string|"'OUTPUT'"
op|','
string|"'FORWARD'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'[0:0] -A %s -j %s-%s'"
op|'%'
nl|'\n'
op|'('
name|'chain'
op|','
name|'self'
op|'.'
name|'binary_name'
op|','
name|'chain'
op|')'
name|'in'
name|'new_lines'
op|','
nl|'\n'
string|'"Built-in chain %s not wrapped"'
op|'%'
op|'('
name|'chain'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_missing_table
dedent|''
dedent|''
name|'def'
name|'test_missing_table'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
op|'['
op|']'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|','
nl|'\n'
string|"'filter'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
op|'['
string|"'*filter'"
op|','
nl|'\n'
string|"'COMMIT'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'in'
name|'new_lines'
op|','
string|'"One of iptables key lines"'
nl|'\n'
string|'"went missing."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'new_lines'
op|')'
op|'>'
number|'4'
op|','
string|'"No iptables rules added"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"#Generated by nova"'
op|'=='
name|'new_lines'
op|'['
number|'0'
op|']'
name|'and'
nl|'\n'
string|'"*filter"'
op|'=='
name|'new_lines'
op|'['
number|'1'
op|']'
name|'and'
nl|'\n'
string|'"COMMIT"'
op|'=='
name|'new_lines'
op|'['
op|'-'
number|'2'
op|']'
name|'and'
nl|'\n'
string|'"#Completed by nova"'
op|'=='
name|'new_lines'
op|'['
op|'-'
number|'1'
op|']'
op|','
nl|'\n'
string|'"iptables rules not generated in the correct order"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_iptables_top_order
dedent|''
name|'def'
name|'test_iptables_top_order'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test iptables_top_regex'
nl|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'sample_filter'
op|')'
newline|'\n'
name|'current_lines'
op|'['
number|'12'
op|':'
number|'12'
op|']'
op|'='
op|'['
string|"'[0:0] -A FORWARD -j iptables-top-rule'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'iptables_top_regex'
op|'='
string|"'-j iptables-top-rule'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|','
nl|'\n'
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'current_lines'
op|','
name|'new_lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_iptables_bottom_order
dedent|''
name|'def'
name|'test_iptables_bottom_order'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test iptables_bottom_regex'
nl|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'sample_filter'
op|')'
newline|'\n'
name|'current_lines'
op|'['
number|'26'
op|':'
number|'26'
op|']'
op|'='
op|'['
string|"'[0:0] -A FORWARD -j iptables-bottom-rule'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'iptables_bottom_regex'
op|'='
string|"'-j iptables-bottom-rule'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|','
nl|'\n'
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'current_lines'
op|','
name|'new_lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_iptables_preserve_order
dedent|''
name|'def'
name|'test_iptables_preserve_order'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test both iptables_top_regex and iptables_bottom_regex'
nl|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'sample_filter'
op|')'
newline|'\n'
name|'current_lines'
op|'['
number|'12'
op|':'
number|'12'
op|']'
op|'='
op|'['
string|"'[0:0] -A FORWARD -j iptables-top-rule'"
op|']'
newline|'\n'
name|'current_lines'
op|'['
number|'27'
op|':'
number|'27'
op|']'
op|'='
op|'['
string|"'[0:0] -A FORWARD -j iptables-bottom-rule'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'iptables_top_regex'
op|'='
string|"'-j iptables-top-rule'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'iptables_bottom_regex'
op|'='
string|"'-j iptables-bottom-rule'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|','
nl|'\n'
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'current_lines'
op|','
name|'new_lines'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
