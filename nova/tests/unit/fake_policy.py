begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'policy_data'
op|'='
string|'"""\n{\n    "admin_api": "is_admin:True",\n\n    "cells_scheduler_filter:TargetCellFilter": "is_admin:True",\n\n    "context_is_admin": "role:admin or role:administrator",\n    "compute:create": "",\n    "compute:create:attach_network": "",\n    "compute:create:attach_volume": "",\n\n    "compute:get": "",\n    "compute:get_all": "",\n    "compute:get_all_tenants": "",\n\n    "compute:update": "",\n\n    "compute:get_instance_metadata": "",\n    "compute:get_all_instance_metadata": "",\n    "compute:get_all_instance_system_metadata": "",\n    "compute:update_instance_metadata": "",\n    "compute:delete_instance_metadata": "",\n\n    "compute:get_instance_faults": "",\n    "compute:get_diagnostics": "",\n    "compute:get_instance_diagnostics": "",\n\n    "compute:get_lock": "",\n    "compute:lock": "",\n    "compute:unlock": "",\n    "compute:unlock_override": "is_admin:True",\n\n    "compute:get_vnc_console": "",\n    "compute:get_spice_console": "",\n    "compute:get_rdp_console": "",\n    "compute:get_serial_console": "",\n    "compute:get_console_output": "",\n\n    "compute:associate_floating_ip": "",\n    "compute:reset_network": "",\n    "compute:inject_network_info": "",\n    "compute:add_fixed_ip": "",\n    "compute:remove_fixed_ip": "",\n\n    "compute:attach_volume": "",\n    "compute:detach_volume": "",\n\n    "compute:attach_interface": "",\n    "compute:detach_interface": "",\n\n    "compute:set_admin_password": "",\n\n    "compute:rescue": "",\n    "compute:unrescue": "",\n\n    "compute:suspend": "",\n    "compute:resume": "",\n\n    "compute:pause": "",\n    "compute:unpause": "",\n\n    "compute:start": "",\n    "compute:stop": "",\n\n    "compute:resize": "",\n    "compute:confirm_resize": "",\n    "compute:revert_resize": "",\n\n    "compute:rebuild": "",\n\n    "compute:reboot": "",\n\n    "compute:snapshot": "",\n    "compute:backup": "",\n\n    "compute:shelve": "",\n    "compute:shelve_offload": "",\n    "compute:unshelve": "",\n\n    "compute:security_groups:add_to_instance": "",\n    "compute:security_groups:remove_from_instance": "",\n\n    "compute:delete": "",\n    "compute:soft_delete": "",\n    "compute:force_delete": "",\n    "compute:restore": "",\n    "compute:swap_volume": "",\n\n    "compute:volume_snapshot_create": "",\n    "compute:volume_snapshot_delete": "",\n\n    "os_compute_api:servers:confirm_resize": "",\n    "os_compute_api:servers:create": "",\n    "os_compute_api:servers:create:attach_network": "",\n    "os_compute_api:servers:create:attach_volume": "",\n    "os_compute_api:servers:create:forced_host": "",\n    "os_compute_api:servers:delete": "",\n    "os_compute_api:servers:detail": "",\n    "os_compute_api:servers:detail:get_all_tenants": "",\n    "os_compute_api:servers:index": "",\n    "os_compute_api:servers:index:get_all_tenants": "",\n    "os_compute_api:servers:reboot": "",\n    "os_compute_api:servers:rebuild": "",\n    "os_compute_api:servers:resize": "",\n    "os_compute_api:servers:revert_resize": "",\n    "os_compute_api:servers:show": "",\n    "os_compute_api:servers:create_image": "",\n    "os_compute_api:servers:update": "",\n    "os_compute_api:servers:start": "",\n    "os_compute_api:servers:stop": "",\n    "os_compute_api:os-access-ips": "",\n    "compute_extension:accounts": "",\n    "compute_extension:admin_actions:pause": "",\n    "compute_extension:admin_actions:unpause": "",\n    "compute_extension:admin_actions:suspend": "",\n    "compute_extension:admin_actions:resume": "",\n    "compute_extension:admin_actions:lock": "",\n    "compute_extension:admin_actions:unlock": "",\n    "compute_extension:admin_actions:resetNetwork": "",\n    "compute_extension:admin_actions:injectNetworkInfo": "",\n    "compute_extension:admin_actions:createBackup": "",\n    "compute_extension:admin_actions:migrateLive": "",\n    "compute_extension:admin_actions:resetState": "",\n    "compute_extension:admin_actions:migrate": "",\n    "os_compute_api:os-admin-actions:reset_network": "",\n    "os_compute_api:os-admin-actions:inject_network_info": "",\n    "os_compute_api:os-admin-actions:reset_state": "",\n    "os_compute_api:os-admin-password": "",\n    "compute_extension:aggregates": "rule:admin_api",\n    "os_compute_api:os-aggregates:index": "rule:admin_api",\n    "os_compute_api:os-aggregates:create": "rule:admin_api",\n    "os_compute_api:os-aggregates:show": "rule:admin_api",\n    "os_compute_api:os-aggregates:update": "rule:admin_api",\n    "os_compute_api:os-aggregates:delete": "rule:admin_api",\n    "os_compute_api:os-aggregates:add_host": "rule:admin_api",\n    "os_compute_api:os-aggregates:remove_host": "rule:admin_api",\n    "os_compute_api:os-aggregates:set_metadata": "rule:admin_api",\n    "compute_extension:agents": "",\n    "os_compute_api:os-agents": "",\n    "compute_extension:attach_interfaces": "",\n    "os_compute_api:os-attach-interfaces": "",\n    "compute_extension:baremetal_nodes": "",\n    "os_compute_api:os-baremetal-nodes": "",\n    "compute_extension:cells": "",\n    "compute_extension:cells:create": "rule:admin_api",\n    "compute_extension:cells:delete": "rule:admin_api",\n    "compute_extension:cells:update": "rule:admin_api",\n    "compute_extension:cells:sync_instances": "rule:admin_api",\n    "os_compute_api:os-cells": "",\n    "os_compute_api:os-cells:create": "rule:admin_api",\n    "os_compute_api:os-cells:delete": "rule:admin_api",\n    "os_compute_api:os-cells:update": "rule:admin_api",\n    "os_compute_api:os-cells:sync_instances": "rule:admin_api",\n    "compute_extension:certificates": "",\n    "os_compute_api:os-certificates:create": "",\n    "os_compute_api:os-certificates:show": "",\n    "compute_extension:cloudpipe": "",\n    "os_compute_api:os-cloudpipe": "",\n    "compute_extension:cloudpipe_update": "",\n    "compute_extension:config_drive": "",\n    "os_compute_api:os-config-drive": "",\n    "compute_extension:console_output": "",\n    "os_compute_api:os-console-output": "",\n    "compute_extension:consoles": "",\n    "os_compute_api:os-remote-consoles": "",\n    "os_compute_api:os-consoles": "",\n    "os_compute_api:os-consoles:create": "",\n    "os_compute_api:os-consoles:delete": "",\n    "os_compute_api:os-consoles:index": "",\n    "os_compute_api:os-consoles:show": "",\n    "compute_extension:createserverext": "",\n    "os_compute_api:os-create-backup": "",\n    "compute_extension:deferred_delete": "",\n    "os_compute_api:os-deferred-delete": "",\n    "compute_extension:disk_config": "",\n    "os_compute_api:os-disk-config": "",\n    "compute_extension:evacuate": "is_admin:True",\n    "os_compute_api:os-evacuate": "is_admin:True",\n    "compute_extension:extended_server_attributes": "",\n    "os_compute_api:os-extended-server-attributes": "",\n    "compute_extension:extended_status": "",\n    "os_compute_api:os-extended-status": "",\n    "compute_extension:extended_availability_zone": "",\n    "os_compute_api:os-extended-availability-zone": "",\n    "compute_extension:extended_ips": "",\n    "compute_extension:extended_ips_mac": "",\n    "compute_extension:extended_vif_net": "",\n    "compute_extension:extended_volumes": "",\n    "os_compute_api:ips:index": "",\n    "os_compute_api:ips:show": "",\n    "os_compute_api:os-extended-volumes": "",\n    "os_compute_api:extensions:discoverable": "",\n    "compute_extension:fixed_ips": "",\n    "os_compute_api:os-fixed-ips": "",\n    "compute_extension:flavor_access": "",\n    "compute_extension:flavor_access:addTenantAccess": "",\n    "compute_extension:flavor_access:removeTenantAccess": "",\n    "os_compute_api:os-flavor-access": "",\n    "os_compute_api:os-flavor-access:remove_tenant_access": "",\n    "os_compute_api:os-flavor-access:add_tenant_access": "",\n    "compute_extension:flavor_disabled": "",\n    "os_compute_api:os-flavor-disabled": "",\n    "compute_extension:flavor_rxtx": "",\n    "os_compute_api:os-flavor-rxtx": "",\n    "compute_extension:flavor_swap": "",\n    "compute_extension:flavorextradata": "",\n    "compute_extension:flavorextraspecs:index": "",\n    "compute_extension:flavorextraspecs:show": "",\n    "compute_extension:flavorextraspecs:create": "is_admin:True",\n    "compute_extension:flavorextraspecs:update": "is_admin:True",\n    "compute_extension:flavorextraspecs:delete": "is_admin:True",\n    "os_compute_api:os-flavor-extra-specs:index": "",\n    "os_compute_api:os-flavor-extra-specs:show": "",\n    "os_compute_api:os-flavor-extra-specs:create": "is_admin:True",\n    "os_compute_api:os-flavor-extra-specs:update": "is_admin:True",\n    "os_compute_api:os-flavor-extra-specs:delete": "is_admin:True",\n    "compute_extension:flavormanage": "",\n    "os_compute_api:os-flavor-manage": "",\n    "os_compute_api:os-flavors:discoverable": "",\n    "compute_extension:floating_ip_dns": "",\n    "os_compute_api:os-floating-ip-dns": "",\n    "compute_extension:floating_ip_pools": "",\n    "os_compute_api:os-floating-ip-pools": "",\n    "compute_extension:floating_ips": "",\n    "os_compute_api:os-floating-ips": "",\n    "compute_extension:floating_ips_bulk": "",\n    "os_compute_api:os-floating-ips-bulk": "",\n    "compute_extension:fping": "",\n    "compute_extension:fping:all_tenants": "is_admin:True",\n    "os_compute_api:os-fping": "",\n    "os_compute_api:os-fping:all_tenants": "is_admin:True",\n    "compute_extension:hide_server_addresses": "",\n    "os_compute_api:os-hide-server-addresses": "",\n    "compute_extension:hosts": "",\n    "os_compute_api:os-hosts": "rule:admin_api",\n    "compute_extension:hypervisors": "rule:admin_api",\n    "os_compute_api:os-hypervisors": "rule:admin_api",\n    "compute_extension:image_size": "",\n    "os_compute_api:image-size": "",\n    "compute_extension:instance_actions": "",\n    "os_compute_api:os-instance-actions": "",\n    "compute_extension:instance_actions:events": "is_admin:True",\n    "os_compute_api:os-instance-actions:events": "is_admin:True",\n    "compute_extension:instance_usage_audit_log": "rule:admin_api",\n    "os_compute_api:os-instance-usage-audit-log": "",\n    "compute_extension:keypairs": "",\n    "compute_extension:keypairs:index": "",\n    "compute_extension:keypairs:show": "",\n    "compute_extension:keypairs:create": "",\n    "compute_extension:keypairs:delete": "",\n\n    "os_compute_api:os-keypairs": "",\n    "os_compute_api:os-keypairs:index": "",\n    "os_compute_api:os-keypairs:show": "",\n    "os_compute_api:os-keypairs:create": "",\n    "os_compute_api:os-keypairs:delete": "",\n    "os_compute_api:os-lock-server:lock": "",\n    "os_compute_api:os-lock-server:unlock": "",\n    "os_compute_api:os-migrate-server:migrate": "",\n    "os_compute_api:os-migrate-server:migrate_live": "",\n    "compute_extension:multinic": "",\n    "os_compute_api:os-multinic": "",\n    "compute_extension:networks": "",\n    "compute_extension:networks:view": "",\n    "os_compute_api:os-networks": "",\n    "os_compute_api:os-networks:view": "",\n    "compute_extension:networks_associate": "",\n    "os_compute_api:os-networks-associate": "",\n    "compute_extension:os-tenant-networks": "",\n    "os_compute_api:os-tenant-networks": "",\n    "os_compute_api:os-pause-server:pause": "",\n    "os_compute_api:os-pause-server:unpause": "",\n    "os_compute_api:os-pci:pci_servers": "",\n    "os_compute_api:os-pci:index": "",\n    "os_compute_api:os-pci:detail": "",\n    "os_compute_api:os-pci:show": "",\n    "compute_extension:quotas:show": "",\n    "compute_extension:quotas:update": "",\n    "compute_extension:quotas:delete": "",\n    "os_compute_api:os-quota-sets:show": "",\n    "os_compute_api:os-quota-sets:update": "",\n    "os_compute_api:os-quota-sets:delete": "",\n    "os_compute_api:os-quota-sets:detail": "",\n    "os_compute_api:os-quota-sets:defaults": "",\n    "compute_extension:quota_classes": "",\n    "os_compute_api:os-quota-class-sets": "",\n    "compute_extension:rescue": "",\n    "os_compute_api:os-rescue": "",\n    "compute_extension:security_group_default_rules": "",\n    "os_compute_api:os-security-group-default-rules": "",\n    "compute_extension:security_groups": "",\n    "os_compute_api:os-security-groups": "",\n    "compute_extension:server_diagnostics": "",\n    "os_compute_api:os-server-diagnostics": "",\n    "compute_extension:server_groups": "",\n    "compute_extension:server_password": "",\n    "os_compute_api:os-server-password": "",\n    "compute_extension:server_usage": "",\n    "os_compute_api:os-server-usage": "",\n    "os_compute_api:os-server-groups": "",\n    "compute_extension:services": "",\n    "os_compute_api:os-services": "",\n    "compute_extension:shelve": "",\n    "compute_extension:shelveOffload": "",\n    "os_compute_api:os-shelve:shelve": "",\n    "os_compute_api:os-shelve:shelve_offload": "",\n    "compute_extension:simple_tenant_usage:show": "",\n    "compute_extension:simple_tenant_usage:list": "",\n    "os_compute_api:os-simple-tenant-usage:show": "",\n    "os_compute_api:os-simple-tenant-usage:list": "",\n    "compute_extension:unshelve": "",\n    "os_compute_api:os-shelve:unshelve": "",\n    "os_compute_api:os-suspend-server:suspend": "",\n    "os_compute_api:os-suspend-server:resume": "",\n    "compute_extension:users": "",\n    "compute_extension:virtual_interfaces": "",\n    "os_compute_api:os-virtual-interfaces": "",\n    "compute_extension:virtual_storage_arrays": "",\n    "compute_extension:volumes": "",\n    "compute_extension:volume_attachments:index": "",\n    "compute_extension:volume_attachments:show": "",\n    "compute_extension:volume_attachments:create": "",\n    "compute_extension:volume_attachments:update": "",\n    "compute_extension:volume_attachments:delete": "",\n    "os_compute_api:os-volumes": "",\n    "os_compute_api:os-volumes-attachments:index": "",\n    "os_compute_api:os-volumes-attachments:show": "",\n    "os_compute_api:os-volumes-attachments:create": "",\n    "os_compute_api:os-volumes-attachments:update": "",\n    "os_compute_api:os-volumes-attachments:delete": "",\n    "compute_extension:volumetypes": "",\n    "compute_extension:zones": "",\n    "compute_extension:availability_zone:list": "",\n    "os_compute_api:os-availability-zone:list": "",\n    "compute_extension:availability_zone:detail": "",\n    "os_compute_api:os-availability-zone:detail": "",\n    "compute_extension:used_limits_for_admin": "is_admin:True",\n    "os_compute_api:os-used-limits": "is_admin:True",\n    "compute_extension:migrations:index": "is_admin:True",\n    "os_compute_api:os-migrations:index": "is_admin:True",\n    "compute_extension:os-assisted-volume-snapshots:create": "",\n    "compute_extension:os-assisted-volume-snapshots:delete": "",\n    "os_compute_api:os-assisted-volume-snapshots:create": "",\n    "os_compute_api:os-assisted-volume-snapshots:delete": "",\n    "compute_extension:console_auth_tokens": "is_admin:True",\n    "os_compute_api:os-console-auth-tokens": "is_admin:True",\n    "compute_extension:os-server-external-events:create": "rule:admin_api",\n    "os_compute_api:os-server-external-events:create": "rule:admin_api",\n    "os_compute_api:server-metadata:create": "",\n    "os_compute_api:server-metadata:update": "",\n    "os_compute_api:server-metadata:update_all": "",\n    "os_compute_api:server-metadata:delete": "",\n    "os_compute_api:server-metadata:show": "",\n    "os_compute_api:server-metadata:index": "",\n\n    "network:get_all": "",\n    "network:get": "",\n    "network:create": "",\n    "network:delete": "",\n    "network:associate": "",\n    "network:disassociate": "",\n    "network:get_vifs_by_instance": "",\n    "network:get_vif_by_mac_address": "",\n    "network:allocate_for_instance": "",\n    "network:deallocate_for_instance": "",\n    "network:validate_networks": "",\n    "network:get_instance_uuids_by_ip_filter": "",\n    "network:get_instance_id_by_floating_address": "",\n    "network:setup_networks_on_host": "",\n\n    "network:get_floating_ip": "",\n    "network:get_floating_ip_pools": "",\n    "network:get_floating_ip_by_address": "",\n    "network:get_floating_ips_by_project": "",\n    "network:get_floating_ips_by_fixed_address": "",\n    "network:allocate_floating_ip": "",\n    "network:associate_floating_ip": "",\n    "network:disassociate_floating_ip": "",\n    "network:release_floating_ip": "",\n    "network:migrate_instance_start": "",\n    "network:migrate_instance_finish": "",\n\n    "network:get_fixed_ip": "",\n    "network:get_fixed_ip_by_address": "",\n    "network:add_fixed_ip_to_instance": "",\n    "network:remove_fixed_ip_from_instance": "",\n    "network:add_network_to_project": "",\n    "network:get_instance_nw_info": "",\n\n    "network:get_dns_domains": "",\n    "network:add_dns_entry": "",\n    "network:modify_dns_entry": "",\n    "network:delete_dns_entry": "",\n    "network:get_dns_entries_by_address": "",\n    "network:get_dns_entries_by_name": "",\n    "network:create_private_dns_domain": "",\n    "network:create_public_dns_domain": "",\n    "network:delete_dns_domain": "",\n    "network:attach_external_network": "rule:admin_api"\n}\n"""'
newline|'\n'
endmarker|''
end_unit
