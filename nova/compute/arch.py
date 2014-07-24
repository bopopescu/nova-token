begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
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
string|'"""Constants and helper APIs for dealing with CPU architectures\n\nThe constants provide the standard names for all known processor\narchitectures. Many have multiple variants to deal with big-endian\nvs little-endian modes, as well as 32 vs 64 bit word sizes. These\nnames are chosen to be identical to the architecture names expected\nby libvirt, so if ever adding new ones, ensure it matches libvirt\'s\nexpectation.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|ALPHA
name|'ALPHA'
op|'='
string|'"alpha"'
newline|'\n'
DECL|variable|ARMV6
name|'ARMV6'
op|'='
string|'"armv6"'
newline|'\n'
DECL|variable|ARMV7
name|'ARMV7'
op|'='
string|'"armv7l"'
newline|'\n'
DECL|variable|ARMV7B
name|'ARMV7B'
op|'='
string|'"armv7b"'
newline|'\n'
nl|'\n'
DECL|variable|AARCH64
name|'AARCH64'
op|'='
string|'"aarch64"'
newline|'\n'
DECL|variable|CRIS
name|'CRIS'
op|'='
string|'"cris"'
newline|'\n'
DECL|variable|I686
name|'I686'
op|'='
string|'"i686"'
newline|'\n'
DECL|variable|IA64
name|'IA64'
op|'='
string|'"ia64"'
newline|'\n'
DECL|variable|LM32
name|'LM32'
op|'='
string|'"lm32"'
newline|'\n'
nl|'\n'
DECL|variable|M68K
name|'M68K'
op|'='
string|'"m68k"'
newline|'\n'
DECL|variable|MICROBLAZE
name|'MICROBLAZE'
op|'='
string|'"microblaze"'
newline|'\n'
DECL|variable|MICROBLAZEEL
name|'MICROBLAZEEL'
op|'='
string|'"microblazeel"'
newline|'\n'
DECL|variable|MIPS
name|'MIPS'
op|'='
string|'"mips"'
newline|'\n'
DECL|variable|MIPSEL
name|'MIPSEL'
op|'='
string|'"mipsel"'
newline|'\n'
nl|'\n'
DECL|variable|MIPS64
name|'MIPS64'
op|'='
string|'"mips64"'
newline|'\n'
DECL|variable|MIPS64EL
name|'MIPS64EL'
op|'='
string|'"mips64el"'
newline|'\n'
DECL|variable|OPENRISC
name|'OPENRISC'
op|'='
string|'"openrisc"'
newline|'\n'
DECL|variable|PARISC
name|'PARISC'
op|'='
string|'"parisc"'
newline|'\n'
DECL|variable|PARISC64
name|'PARISC64'
op|'='
string|'"parisc64"'
newline|'\n'
nl|'\n'
DECL|variable|PPC
name|'PPC'
op|'='
string|'"ppc"'
newline|'\n'
DECL|variable|PPCLE
name|'PPCLE'
op|'='
string|'"ppcle"'
newline|'\n'
DECL|variable|PPC64
name|'PPC64'
op|'='
string|'"ppc64"'
newline|'\n'
DECL|variable|PPC64LE
name|'PPC64LE'
op|'='
string|'"ppc64le"'
newline|'\n'
DECL|variable|PPCEMB
name|'PPCEMB'
op|'='
string|'"ppcemb"'
newline|'\n'
nl|'\n'
DECL|variable|S390
name|'S390'
op|'='
string|'"s390"'
newline|'\n'
DECL|variable|S390X
name|'S390X'
op|'='
string|'"s390x"'
newline|'\n'
DECL|variable|SH4
name|'SH4'
op|'='
string|'"sh4"'
newline|'\n'
DECL|variable|SH4EB
name|'SH4EB'
op|'='
string|'"sh4eb"'
newline|'\n'
DECL|variable|SPARC
name|'SPARC'
op|'='
string|'"sparc"'
newline|'\n'
nl|'\n'
DECL|variable|SPARC64
name|'SPARC64'
op|'='
string|'"sparc64"'
newline|'\n'
DECL|variable|UNICORE32
name|'UNICORE32'
op|'='
string|'"unicore32"'
newline|'\n'
DECL|variable|X86_64
name|'X86_64'
op|'='
string|'"x86_64"'
newline|'\n'
DECL|variable|XTENSA
name|'XTENSA'
op|'='
string|'"xtensa"'
newline|'\n'
DECL|variable|XTENSAEB
name|'XTENSAEB'
op|'='
string|'"xtensaeb"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALL
name|'ALL'
op|'='
op|'['
nl|'\n'
name|'ALPHA'
op|','
nl|'\n'
name|'ARMV6'
op|','
nl|'\n'
name|'ARMV7'
op|','
nl|'\n'
name|'ARMV7B'
op|','
nl|'\n'
nl|'\n'
name|'AARCH64'
op|','
nl|'\n'
name|'CRIS'
op|','
nl|'\n'
name|'I686'
op|','
nl|'\n'
name|'IA64'
op|','
nl|'\n'
name|'LM32'
op|','
nl|'\n'
nl|'\n'
name|'M68K'
op|','
nl|'\n'
name|'MICROBLAZE'
op|','
nl|'\n'
name|'MICROBLAZEEL'
op|','
nl|'\n'
name|'MIPS'
op|','
nl|'\n'
name|'MIPSEL'
op|','
nl|'\n'
nl|'\n'
name|'MIPS64'
op|','
nl|'\n'
name|'MIPS64EL'
op|','
nl|'\n'
name|'OPENRISC'
op|','
nl|'\n'
name|'PARISC'
op|','
nl|'\n'
name|'PARISC64'
op|','
nl|'\n'
nl|'\n'
name|'PPC'
op|','
nl|'\n'
name|'PPCLE'
op|','
nl|'\n'
name|'PPC64'
op|','
nl|'\n'
name|'PPC64LE'
op|','
nl|'\n'
name|'PPCEMB'
op|','
nl|'\n'
nl|'\n'
name|'S390'
op|','
nl|'\n'
name|'S390X'
op|','
nl|'\n'
name|'SH4'
op|','
nl|'\n'
name|'SH4EB'
op|','
nl|'\n'
name|'SPARC'
op|','
nl|'\n'
nl|'\n'
name|'SPARC64'
op|','
nl|'\n'
name|'UNICORE32'
op|','
nl|'\n'
name|'X86_64'
op|','
nl|'\n'
name|'XTENSA'
op|','
nl|'\n'
name|'XTENSAEB'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|from_host
name|'def'
name|'from_host'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the architecture of the host OS\n\n    :returns: the canonicalized host architecture\n    """'
newline|'\n'
nl|'\n'
name|'return'
name|'canonicalize'
op|'('
name|'os'
op|'.'
name|'uname'
op|'('
op|')'
op|'['
number|'4'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid
dedent|''
name|'def'
name|'is_valid'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if a string is a valid architecture\n\n    :param name: architecture name to validate\n\n    :returns: True if @name is valid\n    """'
newline|'\n'
nl|'\n'
name|'return'
name|'name'
name|'in'
name|'ALL'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|canonicalize
dedent|''
name|'def'
name|'canonicalize'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Canonicalize the architecture name\n\n    :param name: architecture name to canonicalize\n\n    :returns: a canonical architecture name\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'newname'
op|'='
name|'name'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'newname'
name|'in'
op|'('
string|'"i386"'
op|','
string|'"i486"'
op|','
string|'"i586"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'newname'
op|'='
name|'I686'
newline|'\n'
nl|'\n'
comment|'# Xen mistake from Icehouse or earlier'
nl|'\n'
dedent|''
name|'if'
name|'newname'
name|'in'
op|'('
string|'"x86_32"'
op|','
string|'"x86_32p"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'newname'
op|'='
name|'I686'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'is_valid'
op|'('
name|'newname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidArchitectureName'
op|'('
name|'arch'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'newname'
newline|'\n'
dedent|''
endmarker|''
end_unit
