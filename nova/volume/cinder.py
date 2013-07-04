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
string|'"""\nHandles all requests relating to volumes + cinder.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'cinderclient'
name|'import'
name|'exceptions'
name|'as'
name|'cinder_exception'
newline|'\n'
name|'from'
name|'cinderclient'
name|'import'
name|'service_catalog'
newline|'\n'
name|'from'
name|'cinderclient'
op|'.'
name|'v1'
name|'import'
name|'client'
name|'as'
name|'cinder_client'
newline|'\n'
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
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
nl|'\n'
DECL|variable|cinder_opts
name|'cinder_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cinder_catalog_info'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'volume:cinder:publicURL'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Info to match when looking for cinder in the service '"
nl|'\n'
string|"'catalog. Format is : separated values of the form: '"
nl|'\n'
string|"'<service_type>:<service_name>:<endpoint_type>'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cinder_endpoint_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Override service catalog lookup with template for cinder '"
nl|'\n'
string|"'endpoint e.g. http://localhost:8776/v1/%(project_id)s'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'os_region_name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'region name of this node'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cinder_ca_certificates_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Location of ca certicates file to use for cinder client '"
nl|'\n'
string|"'requests.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'cinder_http_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of cinderclient retries on failed http calls'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'cinder_api_insecure'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allow to perform insecure SSL requests to cinder'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'cinder_cross_az_attach'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allow attach between instance and volume in different '"
nl|'\n'
string|"'availability zones.'"
op|')'
op|','
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
name|'cinder_opts'
op|')'
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
nl|'\n'
DECL|function|cinderclient
name|'def'
name|'cinderclient'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# FIXME: the cinderclient ServiceCatalog object is mis-named.'
nl|'\n'
comment|'#        It actually contains the entire access blob.'
nl|'\n'
comment|'# Only needed parts of the service catalog are passed in, see'
nl|'\n'
comment|'# nova/context.py.'
nl|'\n'
indent|'    '
name|'compat_catalog'
op|'='
op|'{'
nl|'\n'
string|"'access'"
op|':'
op|'{'
string|"'serviceCatalog'"
op|':'
name|'context'
op|'.'
name|'service_catalog'
name|'or'
op|'['
op|']'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'sc'
op|'='
name|'service_catalog'
op|'.'
name|'ServiceCatalog'
op|'('
name|'compat_catalog'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'cinder_endpoint_template'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
name|'CONF'
op|'.'
name|'cinder_endpoint_template'
op|'%'
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'CONF'
op|'.'
name|'cinder_catalog_info'
newline|'\n'
name|'service_type'
op|','
name|'service_name'
op|','
name|'endpoint_type'
op|'='
name|'info'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
comment|'# extract the region if set in configuration'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'os_region_name'
op|':'
newline|'\n'
indent|'            '
name|'attr'
op|'='
string|"'region'"
newline|'\n'
name|'filter_value'
op|'='
name|'CONF'
op|'.'
name|'os_region_name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'attr'
op|'='
name|'None'
newline|'\n'
name|'filter_value'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'url'
op|'='
name|'sc'
op|'.'
name|'url_for'
op|'('
name|'attr'
op|'='
name|'attr'
op|','
nl|'\n'
name|'filter_value'
op|'='
name|'filter_value'
op|','
nl|'\n'
name|'service_type'
op|'='
name|'service_type'
op|','
nl|'\n'
name|'service_name'
op|'='
name|'service_name'
op|','
nl|'\n'
name|'endpoint_type'
op|'='
name|'endpoint_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Cinderclient connection created using URL: %s'"
op|')'
op|'%'
name|'url'
op|')'
newline|'\n'
nl|'\n'
name|'c'
op|'='
name|'cinder_client'
op|'.'
name|'Client'
op|'('
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'context'
op|'.'
name|'auth_token'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'auth_url'
op|'='
name|'url'
op|','
nl|'\n'
name|'insecure'
op|'='
name|'CONF'
op|'.'
name|'cinder_api_insecure'
op|','
nl|'\n'
name|'retries'
op|'='
name|'CONF'
op|'.'
name|'cinder_http_retries'
op|','
nl|'\n'
name|'cacert'
op|'='
name|'CONF'
op|'.'
name|'cinder_ca_certificates_file'
op|')'
newline|'\n'
comment|'# noauth extracts user_id:project_id from auth_token'
nl|'\n'
name|'c'
op|'.'
name|'client'
op|'.'
name|'auth_token'
op|'='
name|'context'
op|'.'
name|'auth_token'
name|'or'
string|"'%s:%s'"
op|'%'
op|'('
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'c'
op|'.'
name|'client'
op|'.'
name|'management_url'
op|'='
name|'url'
newline|'\n'
name|'return'
name|'c'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_untranslate_volume_summary_view
dedent|''
name|'def'
name|'_untranslate_volume_summary_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for volumes summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'vol'
op|'.'
name|'id'
newline|'\n'
name|'d'
op|'['
string|"'status'"
op|']'
op|'='
name|'vol'
op|'.'
name|'status'
newline|'\n'
name|'d'
op|'['
string|"'size'"
op|']'
op|'='
name|'vol'
op|'.'
name|'size'
newline|'\n'
name|'d'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'vol'
op|'.'
name|'availability_zone'
newline|'\n'
name|'d'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'vol'
op|'.'
name|'created_at'
newline|'\n'
nl|'\n'
comment|'# TODO(jdg): The calling code expects attach_time and'
nl|'\n'
comment|'#            mountpoint to be set. When the calling'
nl|'\n'
comment|'#            code is more defensive this can be'
nl|'\n'
comment|'#            removed.'
nl|'\n'
name|'d'
op|'['
string|"'attach_time'"
op|']'
op|'='
string|'""'
newline|'\n'
name|'d'
op|'['
string|"'mountpoint'"
op|']'
op|'='
string|'""'
newline|'\n'
nl|'\n'
name|'if'
name|'vol'
op|'.'
name|'attachments'
op|':'
newline|'\n'
indent|'        '
name|'att'
op|'='
name|'vol'
op|'.'
name|'attachments'
op|'['
number|'0'
op|']'
newline|'\n'
name|'d'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'attached'"
newline|'\n'
name|'d'
op|'['
string|"'instance_uuid'"
op|']'
op|'='
name|'att'
op|'['
string|"'server_id'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'att'
op|'['
string|"'device'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'detached'"
newline|'\n'
nl|'\n'
dedent|''
name|'d'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'vol'
op|'.'
name|'display_name'
newline|'\n'
name|'d'
op|'['
string|"'display_description'"
op|']'
op|'='
name|'vol'
op|'.'
name|'display_description'
newline|'\n'
nl|'\n'
comment|'# TODO(jdg): Information may be lost in this translation'
nl|'\n'
name|'d'
op|'['
string|"'volume_type_id'"
op|']'
op|'='
name|'vol'
op|'.'
name|'volume_type'
newline|'\n'
name|'d'
op|'['
string|"'snapshot_id'"
op|']'
op|'='
name|'vol'
op|'.'
name|'snapshot_id'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'volume_metadata'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'vol'
op|'.'
name|'metadata'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'volume_metadata'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'vol'
op|','
string|"'volume_image_metadata'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'volume_image_metadata'"
op|']'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'vol'
op|'.'
name|'volume_image_metadata'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_untranslate_snapshot_summary_view
dedent|''
name|'def'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'context'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for snapshots summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'id'
newline|'\n'
name|'d'
op|'['
string|"'status'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'status'
newline|'\n'
name|'d'
op|'['
string|"'progress'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'progress'
newline|'\n'
name|'d'
op|'['
string|"'size'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'size'
newline|'\n'
name|'d'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'created_at'
newline|'\n'
name|'d'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'display_name'
newline|'\n'
name|'d'
op|'['
string|"'display_description'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'display_description'
newline|'\n'
name|'d'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'volume_id'
newline|'\n'
name|'d'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'project_id'
newline|'\n'
name|'d'
op|'['
string|"'volume_size'"
op|']'
op|'='
name|'snapshot'
op|'.'
name|'size'
newline|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|translate_volume_exception
dedent|''
name|'def'
name|'translate_volume_exception'
op|'('
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Transforms the exception for the volume but keeps its traceback intact.\n    """'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'self'
op|','
name|'ctx'
op|','
name|'volume_id'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'method'
op|'('
name|'self'
op|','
name|'ctx'
op|','
name|'volume_id'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cinder_exception'
op|'.'
name|'ClientException'
op|':'
newline|'\n'
indent|'            '
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'exc_trace'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'cinder_exception'
op|'.'
name|'NotFound'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'exc_value'
op|'='
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'cinder_exception'
op|'.'
name|'BadRequest'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'exc_value'
op|'='
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'exc_value'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'exc_value'
op|','
name|'None'
op|','
name|'exc_trace'
newline|'\n'
dedent|''
name|'return'
name|'res'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|translate_snapshot_exception
dedent|''
name|'def'
name|'translate_snapshot_exception'
op|'('
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Transforms the exception for the snapshot but keeps its traceback\n       intact.\n    """'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'self'
op|','
name|'ctx'
op|','
name|'snapshot_id'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'method'
op|'('
name|'self'
op|','
name|'ctx'
op|','
name|'snapshot_id'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cinder_exception'
op|'.'
name|'ClientException'
op|':'
newline|'\n'
indent|'            '
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'exc_trace'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'exc_value'
op|','
name|'cinder_exception'
op|'.'
name|'NotFound'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'exc_value'
op|'='
name|'exception'
op|'.'
name|'SnapshotNotFound'
op|'('
name|'snapshot_id'
op|'='
name|'snapshot_id'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'exc_value'
op|','
name|'None'
op|','
name|'exc_trace'
newline|'\n'
dedent|''
name|'return'
name|'res'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the volume manager."""'
newline|'\n'
nl|'\n'
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'get'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'return'
name|'_untranslate_volume_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'search_opts'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'list'
op|'('
name|'detailed'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rval'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'rval'
op|'.'
name|'append'
op|'('
name|'_untranslate_volume_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'rval'
newline|'\n'
nl|'\n'
DECL|member|check_attached
dedent|''
name|'def'
name|'check_attached'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Raise exception if volume in use."""'
newline|'\n'
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'!='
string|'"in-use"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"status must be \'in-use\'"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_attach
dedent|''
dedent|''
name|'def'
name|'check_attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): abstract status checking?'
nl|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'!='
string|'"available"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"status must be \'available\'"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|'"attached"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"already attached"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'instance'
name|'and'
name|'not'
name|'CONF'
op|'.'
name|'cinder_cross_az_attach'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'['
string|"'availability_zone'"
op|']'
op|'!='
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance and volume not in same availability_zone"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_detach
dedent|''
dedent|''
dedent|''
name|'def'
name|'check_detach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): abstract status checking?'
nl|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'=='
string|'"available"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"already detached"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|reserve_volume
name|'def'
name|'reserve_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'reserve'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|unreserve_volume
name|'def'
name|'unreserve_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'unreserve'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|begin_detaching
name|'def'
name|'begin_detaching'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'begin_detaching'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|roll_detaching
name|'def'
name|'roll_detaching'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'roll_detaching'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_uuid'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'attach'
op|'('
name|'volume_id'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|detach
name|'def'
name|'detach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'detach'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|initialize_connection
name|'def'
name|'initialize_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'initialize_connection'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'connector'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|terminate_connection
name|'def'
name|'terminate_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'terminate_connection'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'connector'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'size'
op|','
name|'name'
op|','
name|'description'
op|','
name|'snapshot'
op|'='
name|'None'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'None'
op|','
name|'volume_type'
op|'='
name|'None'
op|','
name|'metadata'
op|'='
name|'None'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'snapshot'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'snapshot_id'
op|'='
name|'snapshot'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'snapshot_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'snapshot_id'
op|'='
name|'snapshot_id'
op|','
nl|'\n'
name|'display_name'
op|'='
name|'name'
op|','
nl|'\n'
name|'display_description'
op|'='
name|'description'
op|','
nl|'\n'
name|'volume_type'
op|'='
name|'volume_type'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'availability_zone'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'imageRef'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'create'
op|'('
name|'size'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'_untranslate_volume_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cinder_exception'
op|'.'
name|'BadRequest'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volumes'
op|'.'
name|'delete'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'fields'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_snapshot_exception'
newline|'\n'
DECL|member|get_snapshot
name|'def'
name|'get_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volume_snapshots'
op|'.'
name|'get'
op|'('
name|'snapshot_id'
op|')'
newline|'\n'
name|'return'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_snapshots
dedent|''
name|'def'
name|'get_all_snapshots'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volume_snapshots'
op|'.'
name|'list'
op|'('
name|'detailed'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rvals'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'rvals'
op|'.'
name|'append'
op|'('
name|'_untranslate_snapshot_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'rvals'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|create_snapshot
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volume_snapshots'
op|'.'
name|'create'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'False'
op|','
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'description'
op|')'
newline|'\n'
name|'return'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|create_snapshot_force
name|'def'
name|'create_snapshot_force'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volume_snapshots'
op|'.'
name|'create'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'True'
op|','
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'description'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'context'
op|','
name|'item'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_snapshot_exception'
newline|'\n'
DECL|member|delete_snapshot
name|'def'
name|'delete_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinderclient'
op|'('
name|'context'
op|')'
op|'.'
name|'volume_snapshots'
op|'.'
name|'delete'
op|'('
name|'snapshot_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|get_volume_metadata
name|'def'
name|'get_volume_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|delete_volume_metadata
name|'def'
name|'delete_volume_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|update_volume_metadata
name|'def'
name|'update_volume_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'metadata'
op|','
name|'delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'translate_volume_exception'
newline|'\n'
DECL|member|get_volume_metadata_value
name|'def'
name|'get_volume_metadata_value'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
