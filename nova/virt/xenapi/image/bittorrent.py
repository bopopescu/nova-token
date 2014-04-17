begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'import'
name|'pkg_resources'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
op|'.'
name|'parse'
name|'as'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|xenapi_torrent_opts
name|'xenapi_torrent_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'torrent_base_url'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base URL for torrent files.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'torrent_seed_chance'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Probability that peer will become a seeder.'"
nl|'\n'
string|"' (1.0 = 100%)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'torrent_seed_duration'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds after downloading an image via'"
nl|'\n'
string|"' BitTorrent that it should be seeded for other peers.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'torrent_max_last_accessed'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'86400'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Cached torrent files not accessed within this number of'"
nl|'\n'
string|"' seconds can be reaped'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'torrent_listen_port_start'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'6881'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Beginning of port range to listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'torrent_listen_port_end'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'6891'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'End of port range to listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'torrent_download_stall_cutoff'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds a download can remain at the same'"
nl|'\n'
string|"' progress percentage w/o being considered a stall'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'torrent_max_seeder_processes_per_host'"
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
string|"'Maximum number of seeder processes to run concurrently'"
nl|'\n'
string|"' within a given dom0. (-1 = no limit)'"
op|')'
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'xenapi_torrent_opts'
op|','
string|"'xenserver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BittorrentStore
name|'class'
name|'BittorrentStore'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_lookup_torrent_url_fn
name|'def'
name|'_lookup_torrent_url_fn'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Load a "fetcher" func to get the right torrent URL via\n        entrypoints.\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_base_url'
op|':'
newline|'\n'
DECL|function|_default_torrent_url_fn
indent|'            '
name|'def'
name|'_default_torrent_url_fn'
op|'('
name|'instance'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'urlparse'
op|'.'
name|'urljoin'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_base_url'
op|','
nl|'\n'
string|'"%s.torrent"'
op|'%'
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_default_torrent_url_fn'
newline|'\n'
nl|'\n'
dedent|''
name|'matches'
op|'='
op|'['
name|'ep'
name|'for'
name|'ep'
name|'in'
nl|'\n'
name|'pkg_resources'
op|'.'
name|'iter_entry_points'
op|'('
string|"'nova.virt.xenapi.vm_utils'"
op|')'
nl|'\n'
name|'if'
name|'ep'
op|'.'
name|'name'
op|'=='
string|"'torrent_url'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'matches'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'Cannot create default bittorrent URL'"
nl|'\n'
string|"' without torrent_base_url set or'"
nl|'\n'
string|"' torrent URL fetcher extension'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'matches'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|'"Multiple torrent URL fetcher extensions"'
nl|'\n'
string|'" found. Failing."'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'ep'
op|'='
name|'matches'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Loading torrent URL fetcher from entry points"'
nl|'\n'
string|'" %(ep)s"'
op|')'
op|','
op|'{'
string|"'ep'"
op|':'
name|'ep'
op|'}'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'ep'
op|'.'
name|'load'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'fn'
newline|'\n'
nl|'\n'
DECL|member|download_image
dedent|''
name|'def'
name|'download_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'params'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'params'
op|'['
string|"'uuid_stack'"
op|']'
op|'='
name|'vm_utils'
op|'.'
name|'_make_uuid_stack'
op|'('
op|')'
newline|'\n'
name|'params'
op|'['
string|"'sr_path'"
op|']'
op|'='
name|'vm_utils'
op|'.'
name|'get_sr_path'
op|'('
name|'session'
op|')'
newline|'\n'
name|'params'
op|'['
string|"'torrent_seed_duration'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_seed_duration'
newline|'\n'
name|'params'
op|'['
string|"'torrent_seed_chance'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_seed_chance'
newline|'\n'
name|'params'
op|'['
string|"'torrent_max_last_accessed'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_max_last_accessed'
newline|'\n'
name|'params'
op|'['
string|"'torrent_listen_port_start'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_listen_port_start'
newline|'\n'
name|'params'
op|'['
string|"'torrent_listen_port_end'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_listen_port_end'
newline|'\n'
name|'params'
op|'['
string|"'torrent_download_stall_cutoff'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_download_stall_cutoff'
newline|'\n'
name|'params'
op|'['
string|"'torrent_max_seeder_processes_per_host'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'torrent_max_seeder_processes_per_host'
newline|'\n'
nl|'\n'
name|'lookup_fn'
op|'='
name|'self'
op|'.'
name|'_lookup_torrent_url_fn'
op|'('
op|')'
newline|'\n'
name|'params'
op|'['
string|"'torrent_url'"
op|']'
op|'='
name|'lookup_fn'
op|'('
name|'instance'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'vdis'
op|'='
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
nl|'\n'
string|"'bittorrent'"
op|','
string|"'download_vhd'"
op|','
op|'**'
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'vdis'
newline|'\n'
nl|'\n'
DECL|member|upload_image
dedent|''
name|'def'
name|'upload_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'vdi_uuids'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
