begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2012 IBM Corp.'
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
nl|'\n'
DECL|class|VirtAPI
name|'class'
name|'VirtAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|instance_update
indent|'    '
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform an instance update operation on behalf of a virt driver\n        :param context: security context\n        :param instance_uuid: uuid of the instance to be updated\n        :param updates: dict of attribute=value pairs to change\n\n        Returns: orig_instance, new_instance\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_by_uuid
dedent|''
name|'def'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Look up an instance by uuid\n        :param context: security context\n        :param instance_uuid: uuid of the instance to be fetched\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_host
dedent|''
name|'def'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find all instances on a given host\n        :param context: security context\n        :param host: host running instances to be returned\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_get_by_host
dedent|''
name|'def'
name|'aggregate_get_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of aggregates to which the specified host belongs\n        :param context: security context\n        :param host: the host for which aggregates should be returned\n        :param key: optionally filter by hosts with the given metadata key\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_get
dedent|''
name|'def'
name|'aggregate_metadata_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get metadata for the specified aggregate\n        :param context: security context\n        :param aggregate_id: id of aggregate for which metadata is to\n                             be returned\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_add
dedent|''
name|'def'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate_id'
op|','
name|'metadata'
op|','
nl|'\n'
name|'set_delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add/update metadata for specified aggregate\n        :param context: security context\n        :param aggregate_id: id of aggregate on which to update metadata\n        :param metadata: dict of metadata to add/update\n        :param set_delete: if True, only add\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_delete
dedent|''
name|'def'
name|'aggregate_metadata_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the given metadata key from specified aggregate\n        :param context: security context\n        :param aggregate_id: id of aggregate from which to delete metadata\n        :param key: metadata key to delete\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_group_get_by_instance
dedent|''
name|'def'
name|'security_group_get_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the security group for a specified instance\n        :param context: security context\n        :param instance_uuid: instance defining the security group we want\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_group_rule_get_by_security_group
dedent|''
name|'def'
name|'security_group_rule_get_by_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the rules associated with a specified security group\n        :param context: security context\n        :param security_group_id: the security group for which the rules\n                                  should be returned\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|provider_fw_rule_get_all
dedent|''
name|'def'
name|'provider_fw_rule_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the provider firewall rules\n        :param context: security context\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|agent_build_get_by_triple
dedent|''
name|'def'
name|'agent_build_get_by_triple'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'hypervisor'
op|','
name|'os'
op|','
name|'architecture'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get information about the available agent builds for a given\n        hypervisor, os, and architecture\n        :param context: security context\n        :param hypervisor: agent hypervisor type\n        :param os: agent operating system type\n        :param architecture: agent architecture\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
