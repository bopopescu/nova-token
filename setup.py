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
nl|'\n'
name|'setup'
op|'('
name|'name'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
string|"'0.9.1'"
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|"'cloud computing fabric controller'"
op|','
nl|'\n'
DECL|variable|author
name|'author'
op|'='
string|"'OpenStack'"
op|','
nl|'\n'
DECL|variable|author_email
name|'author_email'
op|'='
string|"'nova@lists.launchpad.net'"
op|','
nl|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'http://www.openstack.org/'"
op|','
nl|'\n'
DECL|variable|packages
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
DECL|variable|scripts
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
string|"'bin/nova-rsapi'"
op|','
nl|'\n'
string|"'bin/nova-volume'"
op|','
nl|'\n'
op|']'
nl|'\n'
op|')'
newline|'\n'
endmarker|''
end_unit
