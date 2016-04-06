begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
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
comment|'# This package got introduced during the Mitaka cycle in 2015 to'
nl|'\n'
comment|'# have a central place where the config options of Nova can be maintained.'
nl|'\n'
comment|'# For more background see the blueprint "centralize-config-options"'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
comment|'# from nova.conf import api'
nl|'\n'
comment|'# from nova.conf import api_database'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'availability_zone'
newline|'\n'
comment|'# from nova.conf import aws'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'barbican'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'cells'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'cert'
newline|'\n'
comment|'# from nova.conf import cinder'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'cloudpipe'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'configdrive'
newline|'\n'
comment|'# from nova.conf import console'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'consoleauth'
newline|'\n'
comment|'# from nova.conf import cors'
nl|'\n'
comment|'# from nova.conf import cors.subdomain'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'crypto'
newline|'\n'
comment|'# from nova.conf import database'
nl|'\n'
comment|'# from nova.conf import disk'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'ephemeral_storage'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'floating_ips'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'guestfs'
newline|'\n'
comment|'# from nova.conf import host'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'hyperv'
newline|'\n'
comment|'# from nova.conf import image'
nl|'\n'
comment|'# from nova.conf import imagecache'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'image_file_url'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'ironic'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'keymgr'
newline|'\n'
comment|'# from nova.conf import keystone_authtoken'
nl|'\n'
comment|'# from nova.conf import libvirt'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'mks'
newline|'\n'
comment|'# from nova.conf import matchmaker_redis'
nl|'\n'
comment|'# from nova.conf import metadata'
nl|'\n'
comment|'# from nova.conf import metrics'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'network'
newline|'\n'
comment|'# from nova.conf import neutron'
nl|'\n'
comment|'# from nova.conf import notification'
nl|'\n'
comment|'# from nova.conf import osapi_v21'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'pci'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'rdp'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'remote_debug'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'scheduler'
newline|'\n'
comment|'# from nova.conf import security'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'serial_console'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'service'
newline|'\n'
comment|'# from nova.conf import spice'
nl|'\n'
comment|'# from nova.conf import ssl'
nl|'\n'
comment|'# from nova.conf import trusted_computing'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'upgrade_levels'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'virt'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'vmware'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'vnc'
newline|'\n'
comment|'# from nova.conf import volume'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'workarounds'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'xenserver'
newline|'\n'
comment|'# from nova.conf import xvp'
nl|'\n'
comment|'# from nova.conf import zookeeper'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
comment|'# api.register_opts(CONF)'
nl|'\n'
comment|'# api_database.register_opts(CONF)'
nl|'\n'
name|'availability_zone'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# aws.register_opts(CONF)'
nl|'\n'
name|'barbican'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'base'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'cells'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# cinder.register_opts(CONF)'
nl|'\n'
name|'cloudpipe'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'conductor'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'configdrive'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# console.register_opts(CONF)'
nl|'\n'
name|'consoleauth'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# cors.register_opts(CONF)'
nl|'\n'
comment|'# cors.subdomain.register_opts(CONF)'
nl|'\n'
name|'crypto'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# database.register_opts(CONF)'
nl|'\n'
comment|'# disk.register_opts(CONF)'
nl|'\n'
name|'ephemeral_storage'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'floating_ips'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'glance'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'guestfs'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# host.register_opts(CONF)'
nl|'\n'
name|'hyperv'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'mks'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# image.register_opts(CONF)'
nl|'\n'
comment|'# imagecache.register_opts(CONF)'
nl|'\n'
name|'image_file_url'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'ironic'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'keymgr'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# keystone_authtoken.register_opts(CONF)'
nl|'\n'
comment|'# libvirt.register_opts(CONF)'
nl|'\n'
comment|'# matchmaker_redis.register_opts(CONF)'
nl|'\n'
comment|'# metadata.register_opts(CONF)'
nl|'\n'
comment|'# metrics.register_opts(CONF)'
nl|'\n'
name|'network'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# neutron.register_opts(CONF)'
nl|'\n'
comment|'# notification.register_opts(CONF)'
nl|'\n'
comment|'# osapi_v21.register_opts(CONF)'
nl|'\n'
name|'pci'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'rdp'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'scheduler'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# security.register_opts(CONF)'
nl|'\n'
name|'serial_console'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# spice.register_opts(CONF)'
nl|'\n'
comment|'# ssl.register_opts(CONF)'
nl|'\n'
comment|'# trusted_computing.register_opts(CONF)'
nl|'\n'
name|'upgrade_levels'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'virt'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'vmware'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'vnc'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# volume.register_opts(CONF)'
nl|'\n'
name|'workarounds'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'wsgi'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'xenserver'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# xvp.register_opts(CONF)'
nl|'\n'
comment|'# zookeeper.register_opts(CONF)'
nl|'\n'
nl|'\n'
name|'remote_debug'
op|'.'
name|'register_cli_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
endmarker|''
end_unit
