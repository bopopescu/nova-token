begin_unit
comment|'# Copyright 2012 OpenStack Foundation.'
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
string|'"""\nNetwork-related utilities and helper functions.\n"""'
newline|'\n'
nl|'\n'
comment|'# TODO(jd) Use six.moves once'
nl|'\n'
comment|'# https://bitbucket.org/gutworth/six/pull-request/28'
nl|'\n'
comment|'# is merged'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'urllib'
op|'.'
name|'parse'
newline|'\n'
DECL|variable|SplitResult
name|'SplitResult'
op|'='
name|'urllib'
op|'.'
name|'parse'
op|'.'
name|'SplitResult'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'urlparse'
newline|'\n'
DECL|variable|SplitResult
name|'SplitResult'
op|'='
name|'urlparse'
op|'.'
name|'SplitResult'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
name|'import'
name|'parse'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_host_port
name|'def'
name|'parse_host_port'
op|'('
name|'address'
op|','
name|'default_port'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Interpret a string as a host:port pair.\n\n    An IPv6 address MUST be escaped if accompanied by a port,\n    because otherwise ambiguity ensues: 2001:db8:85a3::8a2e:370:7334\n    means both [2001:db8:85a3::8a2e:370:7334] and\n    [2001:db8:85a3::8a2e:370]:7334.\n\n    >>> parse_host_port(\'server01:80\')\n    (\'server01\', 80)\n    >>> parse_host_port(\'server01\')\n    (\'server01\', None)\n    >>> parse_host_port(\'server01\', default_port=1234)\n    (\'server01\', 1234)\n    >>> parse_host_port(\'[::1]:80\')\n    (\'::1\', 80)\n    >>> parse_host_port(\'[::1]\')\n    (\'::1\', None)\n    >>> parse_host_port(\'[::1]\', default_port=1234)\n    (\'::1\', 1234)\n    >>> parse_host_port(\'2001:db8:85a3::8a2e:370:7334\', default_port=1234)\n    (\'2001:db8:85a3::8a2e:370:7334\', 1234)\n\n    """'
newline|'\n'
name|'if'
name|'address'
op|'['
number|'0'
op|']'
op|'=='
string|"'['"
op|':'
newline|'\n'
comment|'# Escaped ipv6'
nl|'\n'
indent|'        '
name|'_host'
op|','
name|'_port'
op|'='
name|'address'
op|'['
number|'1'
op|':'
op|']'
op|'.'
name|'split'
op|'('
string|"']'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'_host'
newline|'\n'
name|'if'
string|"':'"
name|'in'
name|'_port'
op|':'
newline|'\n'
indent|'            '
name|'port'
op|'='
name|'_port'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'port'
op|'='
name|'default_port'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'address'
op|'.'
name|'count'
op|'('
string|"':'"
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|','
name|'port'
op|'='
name|'address'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# 0 means ipv4, >1 means ipv6.'
nl|'\n'
comment|'# We prohibit unescaped ipv6 addresses with port.'
nl|'\n'
indent|'            '
name|'host'
op|'='
name|'address'
newline|'\n'
name|'port'
op|'='
name|'default_port'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'('
name|'host'
op|','
name|'None'
name|'if'
name|'port'
name|'is'
name|'None'
name|'else'
name|'int'
op|'('
name|'port'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ModifiedSplitResult
dedent|''
name|'class'
name|'ModifiedSplitResult'
op|'('
name|'SplitResult'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Split results class for urlsplit."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(dims): The functions below are needed for Python 2.6.x.'
nl|'\n'
comment|'# We can remove these when we drop support for 2.6.x.'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|hostname
name|'def'
name|'hostname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'netloc'
op|'='
name|'self'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"'@'"
op|','
number|'1'
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'host'
op|','
name|'port'
op|'='
name|'parse_host_port'
op|'('
name|'netloc'
op|')'
newline|'\n'
name|'return'
name|'host'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|port
name|'def'
name|'port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'netloc'
op|'='
name|'self'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"'@'"
op|','
number|'1'
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'host'
op|','
name|'port'
op|'='
name|'parse_host_port'
op|'('
name|'netloc'
op|')'
newline|'\n'
name|'return'
name|'port'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|urlsplit
dedent|''
dedent|''
name|'def'
name|'urlsplit'
op|'('
name|'url'
op|','
name|'scheme'
op|'='
string|"''"
op|','
name|'allow_fragments'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse a URL using urlparse.urlsplit(), splitting query and fragments.\n    This function papers over Python issue9374 when needed.\n\n    The parameters are the same as urlparse.urlsplit.\n    """'
newline|'\n'
name|'scheme'
op|','
name|'netloc'
op|','
name|'path'
op|','
name|'query'
op|','
name|'fragment'
op|'='
name|'parse'
op|'.'
name|'urlsplit'
op|'('
nl|'\n'
name|'url'
op|','
name|'scheme'
op|','
name|'allow_fragments'
op|')'
newline|'\n'
name|'if'
name|'allow_fragments'
name|'and'
string|"'#'"
name|'in'
name|'path'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|','
name|'fragment'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'#'"
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'?'"
name|'in'
name|'path'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|','
name|'query'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'?'"
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ModifiedSplitResult'
op|'('
name|'scheme'
op|','
name|'netloc'
op|','
nl|'\n'
name|'path'
op|','
name|'query'
op|','
name|'fragment'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
