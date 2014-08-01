begin_unit
comment|'# coding=utf-8'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2014 Red Hat, Inc.'
nl|'\n'
comment|'# Copyright 2013 Hewlett-Packard Development Company, L.P.'
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
string|'"""\nA driver wrapping the Ironic API, such that Nova may provision\nbare metal resources.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
name|'as'
name|'virt_driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'api_version'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Version of Ironic API service endpoint.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'api_endpoint'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'URL for Ironic API endpoint.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'admin_username'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Ironic keystone admin name'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'admin_password'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Ironic keystone admin password.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'admin_auth_token'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Ironic keystone auth token.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'admin_url'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Keystone public API endpoint.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'client_log_level'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Log level override for ironicclient. Set this in '"
nl|'\n'
string|'\'order to override the global "default_log_levels", \''
nl|'\n'
string|'\'"verbose", and "debug" settings.\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'admin_tenant_name'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Ironic keystone tenant name.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'api_max_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
op|'('
string|"'How many retries when a request does conflict.'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'api_retry_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
op|'('
string|"'How often to retry in seconds when a request '"
nl|'\n'
string|"'does conflict'"
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ironic_group
name|'ironic_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'ironic'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Ironic Options'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_group'
op|'('
name|'ironic_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'opts'
op|','
name|'ironic_group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicDriver
name|'class'
name|'IronicDriver'
op|'('
name|'virt_driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Hypervisor driver for Ironic - bare metal provisioning."""'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
