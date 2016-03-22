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
name|'conf'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'configdrive'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
op|'.'
name|'guestfs'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'eventhandler'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'pathutils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'vif'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'vmops'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'volumeops'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'imagecache'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'imagebackend'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'imagecache'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'storage'
op|'.'
name|'lvm'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'vif'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'aoe'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'glusterfs'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'iscsi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'iser'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'net'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'nfs'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'quobyte'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'remotefs'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'scality'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'smbfs'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'volume'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'images'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vif'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vim_util'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vm_util'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vmops'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'agent'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'client'
op|'.'
name|'session'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'image'
op|'.'
name|'bittorrent'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'pool'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vif'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vmops'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volume_utils'
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
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'configdrive'
op|'.'
name|'configdrive_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'imagecache'
op|'.'
name|'imagecache_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'guestfs'"
op|','
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
op|'.'
name|'guestfs'
op|'.'
name|'guestfs_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'hyperv'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'pathutils'
op|'.'
name|'hyperv_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'vif'
op|'.'
name|'hyperv_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'vmops'
op|'.'
name|'hyperv_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'volumeops'
op|'.'
name|'hyper_volumeops_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
op|'.'
name|'eventhandler'
op|'.'
name|'hyperv_opts'
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'libvirt'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'driver'
op|'.'
name|'libvirt_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'imagebackend'
op|'.'
name|'__imagebackend_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'imagecache'
op|'.'
name|'imagecache_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'storage'
op|'.'
name|'lvm'
op|'.'
name|'lvm_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'utils'
op|'.'
name|'libvirt_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'vif'
op|'.'
name|'libvirt_vif_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'volume'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'aoe'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'glusterfs'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'iscsi'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'iser'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'net'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'nfs'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'quobyte'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'remotefs'
op|'.'
name|'libvirt_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'scality'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
op|'.'
name|'smbfs'
op|'.'
name|'volume_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'vmware'"
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
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vim_util'
op|'.'
name|'vmware_opts'
op|']'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'driver'
op|'.'
name|'spbm_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'driver'
op|'.'
name|'vmwareapi_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vif'
op|'.'
name|'vmwareapi_vif_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vm_util'
op|'.'
name|'vmware_utils_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vmops'
op|'.'
name|'vmops_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'xenserver'"
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
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vif'
op|'.'
name|'xenapi_ovs_integration_bridge_opt'
op|']'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'driver'
op|'.'
name|'xenapi_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'image'
op|'.'
name|'bittorrent'
op|'.'
name|'xenapi_torrent_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'pool'
op|'.'
name|'xenapi_pool_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
op|'.'
name|'xenapi_vm_utils_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vmops'
op|'.'
name|'xenapi_vmops_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volume_utils'
op|'.'
name|'xenapi_volume_utils_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
