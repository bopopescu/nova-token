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
nl|'\n'
name|'from'
name|'setuptools'
name|'import'
name|'setup'
op|','
name|'find_packages'
newline|'\n'
name|'from'
name|'setuptools'
op|'.'
name|'command'
op|'.'
name|'sdist'
name|'import'
name|'sdist'
newline|'\n'
name|'from'
name|'sphinx'
op|'.'
name|'setup_command'
name|'import'
name|'BuildDoc'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|local_BuildDoc
name|'class'
name|'local_BuildDoc'
op|'('
name|'BuildDoc'
op|')'
op|':'
newline|'\n'
DECL|member|run
indent|'    '
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'builder'
name|'in'
op|'['
string|"'html'"
op|','
string|"'man'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'builder'
op|'='
name|'builder'
newline|'\n'
name|'self'
op|'.'
name|'finalize_options'
op|'('
op|')'
newline|'\n'
name|'BuildDoc'
op|'.'
name|'run'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|class|local_sdist
dedent|''
dedent|''
dedent|''
name|'class'
name|'local_sdist'
op|'('
name|'sdist'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Customized sdist hook - builds the ChangeLog file from VC first"""'
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
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
string|"'.bzr'"
op|')'
op|':'
newline|'\n'
comment|"# We're in a bzr branch"
nl|'\n'
indent|'            '
name|'env'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'env'
op|'['
string|"'BZR_PLUGIN_PATH'"
op|']'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|"'./bzrplugins'"
op|')'
newline|'\n'
name|'log_cmd'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
op|'['
string|'"bzr"'
op|','
string|'"log"'
op|','
string|'"--novalog"'
op|']'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
name|'env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'changelog'
op|'='
name|'log_cmd'
op|'.'
name|'communicate'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'with'
name|'open'
op|'('
string|'"ChangeLog"'
op|','
string|'"w"'
op|')'
name|'as'
name|'changelog_file'
op|':'
newline|'\n'
indent|'                '
name|'changelog_file'
op|'.'
name|'write'
op|'('
name|'changelog'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'sdist'
op|'.'
name|'run'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'setup'
op|'('
name|'name'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'2011.1'"
op|','
nl|'\n'
name|'description'
op|'='
string|"'cloud computing fabric controller'"
op|','
nl|'\n'
name|'author'
op|'='
string|"'OpenStack'"
op|','
nl|'\n'
name|'author_email'
op|'='
string|"'nova@lists.launchpad.net'"
op|','
nl|'\n'
name|'url'
op|'='
string|"'http://www.openstack.org/'"
op|','
nl|'\n'
name|'cmdclass'
op|'='
op|'{'
string|"'sdist'"
op|':'
name|'local_sdist'
op|','
nl|'\n'
string|"'build_sphinx'"
op|':'
name|'local_BuildDoc'
op|'}'
op|','
nl|'\n'
name|'packages'
op|'='
name|'find_packages'
op|'('
name|'exclude'
op|'='
op|'['
string|"'bin'"
op|','
string|"'smoketests'"
op|']'
op|')'
op|','
nl|'\n'
name|'scripts'
op|'='
op|'['
string|"'bin/nova-api'"
op|','
nl|'\n'
string|"'bin/nova-compute'"
op|','
nl|'\n'
string|"'bin/nova-dhcpbridge'"
op|','
nl|'\n'
string|"'bin/nova-import-canonical-imagestore'"
op|','
nl|'\n'
string|"'bin/nova-instancemonitor'"
op|','
nl|'\n'
string|"'bin/nova-manage'"
op|','
nl|'\n'
string|"'bin/nova-network'"
op|','
nl|'\n'
string|"'bin/nova-objectstore'"
op|','
nl|'\n'
string|"'bin/nova-scheduler'"
op|','
nl|'\n'
string|"'bin/nova-volume'"
op|','
nl|'\n'
string|"'tools/nova-debug'"
op|']'
op|')'
newline|'\n'
endmarker|''
end_unit
