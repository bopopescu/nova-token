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
name|'functools'
newline|'\n'
name|'import'
name|'sys'
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
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'num_retries'"
op|','
string|"'nova.image.glance'"
op|','
name|'group'
op|'='
string|"'glance'"
op|')'
newline|'\n'
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
nl|'\n'
DECL|class|GlanceStore
name|'class'
name|'GlanceStore'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_call_glance_plugin
indent|'    '
name|'def'
name|'_call_glance_plugin'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
name|'fn'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'glance_api_servers'
op|'='
name|'glance'
op|'.'
name|'get_api_servers'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|pick_glance
name|'def'
name|'pick_glance'
op|'('
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'g_host'
op|','
name|'g_port'
op|','
name|'g_use_ssl'
op|'='
name|'glance_api_servers'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'kwargs'
op|'['
string|"'glance_host'"
op|']'
op|'='
name|'g_host'
newline|'\n'
name|'kwargs'
op|'['
string|"'glance_port'"
op|']'
op|'='
name|'g_port'
newline|'\n'
name|'kwargs'
op|'['
string|"'glance_use_ssl'"
op|']'
op|'='
name|'g_use_ssl'
newline|'\n'
name|'return'
name|'g_host'
newline|'\n'
nl|'\n'
DECL|function|retry_cb
dedent|''
name|'def'
name|'retry_cb'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'exc'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'exc_info'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'exc'
op|'.'
name|'message'
op|','
name|'exc_info'
op|'='
name|'exc_info'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'exc'
op|','
name|'exc_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'cb'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'retry_cb'
op|','
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'session'
op|'.'
name|'call_plugin_serialized_with_retry'
op|'('
nl|'\n'
string|"'glance'"
op|','
name|'fn'
op|','
name|'CONF'
op|'.'
name|'glance'
op|'.'
name|'num_retries'
op|','
name|'pick_glance'
op|','
name|'cb'
op|','
op|'**'
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_params
dedent|''
name|'def'
name|'_make_params'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'session'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'sr_path'"
op|':'
name|'vm_utils'
op|'.'
name|'get_sr_path'
op|'('
name|'session'
op|')'
op|','
nl|'\n'
string|"'extra_headers'"
op|':'
name|'glance'
op|'.'
name|'generate_identity_headers'
op|'('
name|'context'
op|')'
op|'}'
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
name|'self'
op|'.'
name|'_make_params'
op|'('
name|'context'
op|','
name|'session'
op|','
name|'image_id'
op|')'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdis'
op|'='
name|'self'
op|'.'
name|'_call_glance_plugin'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
nl|'\n'
string|"'download_vhd'"
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PluginRetriesExceeded'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'CouldNotFetchImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'image_id'
op|','
name|'vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_make_params'
op|'('
name|'context'
op|','
name|'session'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'params'
op|'['
string|"'vdi_uuids'"
op|']'
op|'='
name|'vdi_uuids'
newline|'\n'
nl|'\n'
name|'props'
op|'='
name|'params'
op|'['
string|"'properties'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'props'
op|'['
string|"'auto_disk_config'"
op|']'
op|'='
name|'instance'
op|'['
string|"'auto_disk_config'"
op|']'
newline|'\n'
name|'props'
op|'['
string|"'os_type'"
op|']'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'os_type'"
op|','
name|'None'
op|')'
name|'or'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'default_os_type'
op|')'
newline|'\n'
nl|'\n'
name|'compression_level'
op|'='
name|'vm_utils'
op|'.'
name|'get_compression_level'
op|'('
op|')'
newline|'\n'
name|'if'
name|'compression_level'
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'['
string|"'xenapi_image_compression_level'"
op|']'
op|'='
name|'compression_level'
newline|'\n'
nl|'\n'
dedent|''
name|'auto_disk_config'
op|'='
name|'utils'
op|'.'
name|'get_auto_disk_config_from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'utils'
op|'.'
name|'is_auto_disk_config_disabled'
op|'('
name|'auto_disk_config'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'['
string|'"auto_disk_config"'
op|']'
op|'='
string|'"disabled"'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_call_glance_plugin'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
nl|'\n'
string|"'upload_vhd'"
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PluginRetriesExceeded'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'CouldNotUploadImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
