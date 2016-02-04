begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may not'
nl|'\n'
comment|'# use this file except in compliance with the License. You may obtain a copy'
nl|'\n'
comment|'# of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'availability_zones'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'baserpc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'pipelib'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'novnc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'serialproxy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'spicehtml5proxy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'tasks'
op|'.'
name|'live_migrate'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'serial'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'xvp'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'consoleauth'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'crypto'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'base'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'download'
op|'.'
name|'file'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'ipv6'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'keymgr'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'barbican'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'conf_key_mgr'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'netconf'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'notifications'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'objects'
op|'.'
name|'network'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'paths'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'quota'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'rdp'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'service'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'drivers'
op|'.'
name|'zk'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'spice'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'volume'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'cinder'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
op|'('
string|"'DEFAULT'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'tasks'
op|'.'
name|'live_migrate'
op|'.'
name|'migrate_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'consoleauth_topic_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'db'
op|'.'
name|'base'
op|'.'
name|'db_driver_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'ipv6'
op|'.'
name|'api'
op|'.'
name|'ipv6_backend_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'api'
op|'.'
name|'servicegroup_driver_opt'
op|']'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'availability_zones'
op|'.'
name|'availability_zone_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'pipelib'
op|'.'
name|'cloudpipe_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'novnc'
op|'.'
name|'opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'spicehtml5proxy'
op|'.'
name|'opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'manager'
op|'.'
name|'console_manager_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'xvp'
op|'.'
name|'xvp_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'manager'
op|'.'
name|'consoleauth_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'crypto'
op|'.'
name|'crypto_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|'.'
name|'db_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api'
op|'.'
name|'db_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'exc_log_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'netconf'
op|'.'
name|'netconf_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'notifications'
op|'.'
name|'notify_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'objects'
op|'.'
name|'network'
op|'.'
name|'network_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'paths'
op|'.'
name|'path_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'quota'
op|'.'
name|'quota_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'service'
op|'.'
name|'service_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'utils'
op|'.'
name|'monkey_patch_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'utils'
op|'.'
name|'utils_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'_volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'wsgi_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'barbican'"
op|','
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'barbican'
op|'.'
name|'barbican_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'cinder'"
op|','
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'cinder'
op|'.'
name|'cinder_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'api_database'"
op|','
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api'
op|'.'
name|'api_db_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'conductor'"
op|','
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'api'
op|'.'
name|'conductor_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'database'"
op|','
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api'
op|'.'
name|'oslo_db_options'
op|'.'
name|'database_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'glance'"
op|','
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'glance_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'image_file_url'"
op|','
op|'['
name|'nova'
op|'.'
name|'image'
op|'.'
name|'download'
op|'.'
name|'file'
op|'.'
name|'opt_group'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'keymgr'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'conf_key_mgr'
op|'.'
name|'key_mgr_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'keymgr_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'rdp'"
op|','
name|'nova'
op|'.'
name|'rdp'
op|'.'
name|'rdp_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'spice'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'spicehtml5proxy'
op|'.'
name|'opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'spice'
op|'.'
name|'spice_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'upgrade_levels'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'baserpc'
op|'.'
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'console'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'workarounds'"
op|','
name|'nova'
op|'.'
name|'utils'
op|'.'
name|'workarounds_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'zookeeper'"
op|','
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'drivers'
op|'.'
name|'zk'
op|'.'
name|'zk_driver_opts'
op|')'
nl|'\n'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
