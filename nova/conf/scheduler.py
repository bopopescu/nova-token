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
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|host_subset_size_opt
name|'host_subset_size_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"scheduler_host_subset_size"'
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
string|'"New instances will be scheduled on a host chosen randomly from "'
nl|'\n'
string|'"a subset of the N best hosts. This property defines the subset "'
nl|'\n'
string|'"size that a host is chosen from. A value of 1 chooses the first "'
nl|'\n'
string|'"host returned by the weighing functions.  This value must be at "'
nl|'\n'
string|'"least 1. Any value less than 1 will be ignored, and 1 will be "'
nl|'\n'
string|'"used instead"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|bm_default_filter_opt
name|'bm_default_filter_opt'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"baremetal_scheduler_default_filters"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|'"RetryFilter"'
op|','
nl|'\n'
string|'"AvailabilityZoneFilter"'
op|','
nl|'\n'
string|'"ComputeFilter"'
op|','
nl|'\n'
string|'"ComputeCapabilitiesFilter"'
op|','
nl|'\n'
string|'"ImagePropertiesFilter"'
op|','
nl|'\n'
string|'"ExactRamFilter"'
op|','
nl|'\n'
string|'"ExactDiskFilter"'
op|','
nl|'\n'
string|'"ExactCoreFilter"'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Which filter class names to use for filtering baremetal hosts "'
nl|'\n'
string|'"when not specified in the request."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|use_bm_filters_opt
name|'use_bm_filters_opt'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"scheduler_use_baremetal_filters"'
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
string|'"Flag to decide whether to use "'
nl|'\n'
string|'"baremetal_scheduler_default_filters or not."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|host_mgr_avail_filt_opt
name|'host_mgr_avail_filt_opt'
op|'='
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|'"scheduler_available_filters"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|'"nova.scheduler.filters.all_filters"'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Filter classes available to the scheduler which may be "'
nl|'\n'
string|'"specified more than once.  An entry of "'
nl|'\n'
string|'"\'nova.scheduler.filters.all_filters\' maps to all filters "'
nl|'\n'
string|'"included with nova."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|host_mgr_default_filt_opt
name|'host_mgr_default_filt_opt'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"scheduler_default_filters"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|'"RetryFilter"'
op|','
nl|'\n'
string|'"AvailabilityZoneFilter"'
op|','
nl|'\n'
string|'"RamFilter"'
op|','
nl|'\n'
string|'"DiskFilter"'
op|','
nl|'\n'
string|'"ComputeFilter"'
op|','
nl|'\n'
string|'"ComputeCapabilitiesFilter"'
op|','
nl|'\n'
string|'"ImagePropertiesFilter"'
op|','
nl|'\n'
string|'"ServerGroupAntiAffinityFilter"'
op|','
nl|'\n'
string|'"ServerGroupAffinityFilter"'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Which filter class names to use for filtering hosts when not "'
nl|'\n'
string|'"specified in the request."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|host_mgr_sched_wgt_cls_opt
name|'host_mgr_sched_wgt_cls_opt'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"scheduler_weight_classes"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|'"nova.scheduler.weights.all_weighers"'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Which weight class names to use for weighing hosts"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|host_mgr_tracks_inst_chg_opt
name|'host_mgr_tracks_inst_chg_opt'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"scheduler_tracks_instance_changes"'
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
string|'"Determines if the Scheduler tracks changes to instances to help "'
nl|'\n'
string|'"with its filtering decisions."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|rpc_sched_topic_opt
name|'rpc_sched_topic_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"scheduler_topic"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"scheduler"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The topic scheduler nodes listen on"'
op|')'
newline|'\n'
nl|'\n'
comment|'# This option specifies an option group, so register separately'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"scheduler"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Set a version cap for messages sent to scheduler services"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|scheduler_json_config_location_opt
name|'scheduler_json_config_location_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|'"scheduler_json_config_location"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'""'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Absolute path to scheduler configuration JSON file."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|sched_driver_host_mgr_opt
name|'sched_driver_host_mgr_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"scheduler_host_manager"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"nova.scheduler.host_manager.HostManager"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The scheduler host manager class to use"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|driver_opt
name|'driver_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"scheduler_driver"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"nova.scheduler.filter_scheduler.FilterScheduler"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Default driver to use for the scheduler"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|driver_period_opt
name|'driver_period_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"scheduler_driver_task_period"'
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
string|'"How often (in seconds) to run periodic tasks in the scheduler "'
nl|'\n'
string|'"driver of your choice. Please note this is likely to interact "'
nl|'\n'
string|'"with the value of service_down_time, but exactly how they "'
nl|'\n'
string|'"interact will depend on your choice of scheduler driver."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|disk_allocation_ratio_opt
name|'disk_allocation_ratio_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"disk_allocation_ratio"'
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
string|'"Virtual disk to physical disk allocation ratio"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|isolated_img_opt
name|'isolated_img_opt'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"isolated_images"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Images to run on isolated host"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|isolated_host_opt
name|'isolated_host_opt'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"isolated_hosts"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Host reserved for specific images"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|restrict_iso_host_img_opt
name|'restrict_iso_host_img_opt'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|'"restrict_isolated_hosts_to_isolated_images"'
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
string|'"Whether to force isolated hosts to run only isolated images"'
op|')'
newline|'\n'
nl|'\n'
comment|'# These opts are registered as a separate OptGroup'
nl|'\n'
DECL|variable|trusted_opts
name|'trusted_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"attestation_server"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Attestation server HTTP"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"attestation_server_ca_file"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Attestation server Cert file for Identity verification"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"attestation_port"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"8443"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Attestation server port"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"attestation_api_url"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"/OpenAttestationWebServices/V1.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Attestation web API URL"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"attestation_auth_blob"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Attestation authorization blob - must change"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"attestation_auth_timeout"'
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
string|'"Attestation status cache valid period length"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"attestation_insecure_ssl"'
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
string|'"Disable SSL cert verification for Attestation service"'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|max_io_ops_per_host_opt
name|'max_io_ops_per_host_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"max_io_ops_per_host"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Tells filters to ignore hosts that have this many or more "'
nl|'\n'
string|'"instances currently in build, resize, snapshot, migrate, rescue "'
nl|'\n'
string|'"or unshelve task states"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|agg_img_prop_iso_namespace_opt
name|'agg_img_prop_iso_namespace_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|'"aggregate_image_properties_isolation_namespace"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Force the filter to consider only keys matching the given "'
nl|'\n'
string|'"namespace."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|agg_img_prop_iso_separator_opt
name|'agg_img_prop_iso_separator_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|'"aggregate_image_properties_isolation_separator"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"."'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The separator used between the namespace and keys"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|max_instances_per_host_opt
name|'max_instances_per_host_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"max_instances_per_host"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'50'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Ignore hosts that have too many instances"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ram_weight_mult_opt
name|'ram_weight_mult_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"ram_weight_multiplier"'
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
string|'"Multiplier used for weighing ram. Negative numbers mean to "'
nl|'\n'
string|'"stack vs spread."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|io_ops_weight_mult_opt
name|'io_ops_weight_mult_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"io_ops_weight_multiplier"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Multiplier used for weighing host io ops. Negative numbers mean "'
nl|'\n'
string|'"a preference to choose light workload compute hosts."'
op|')'
newline|'\n'
nl|'\n'
comment|'# These opts are registered as a separate OptGroup'
nl|'\n'
DECL|variable|metrics_weight_opts
name|'metrics_weight_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"weight_multiplier"'
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
string|'"Multiplier used for weighing metrics."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"weight_setting"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"How the metrics are going to be weighed. This should be in "'
nl|'\n'
string|'"the form of \'<name1>=<ratio1>, <name2>=<ratio2>, ...\', "'
nl|'\n'
string|'"where <nameX> is one of the metrics to be weighed, and "'
nl|'\n'
string|'"<ratioX> is the corresponding ratio. So for "'
nl|'\n'
string|'"\'name1=1.0, name2=-1.0\' The final weight would be "'
nl|'\n'
string|'"name1.value * 1.0 + name2.value * -1.0."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"required"'
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
string|'"How to treat the unavailable metrics. When a metric is NOT "'
nl|'\n'
string|'"available for a host, if it is set to be True, it would "'
nl|'\n'
string|'"raise an exception, so it is recommended to use the "'
nl|'\n'
string|'"scheduler filter MetricFilter to filter out those hosts. If "'
nl|'\n'
string|'"it is set to be False, the unavailable metric would be "'
nl|'\n'
string|'"treated as a negative factor in weighing process, the "'
nl|'\n'
string|'"returned value would be set by the option "'
nl|'\n'
string|'"weight_of_unavailable."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"weight_of_unavailable"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'float'
op|'('
op|'-'
number|'10000.0'
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The final weight value to be returned if required is set to "'
nl|'\n'
string|'"False and any one of the metrics set by weight_setting is "'
nl|'\n'
string|'"unavailable."'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|scheduler_max_att_opt
name|'scheduler_max_att_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"scheduler_max_attempts"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|min
name|'min'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Maximum number of attempts to schedule an instance"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|soft_affinity_weight_opt
name|'soft_affinity_weight_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'soft_affinity_weight_multiplier'"
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
string|"'Multiplier used for weighing hosts '"
nl|'\n'
string|"'for group soft-affinity. Only a '"
nl|'\n'
string|"'positive value is meaningful. Negative '"
nl|'\n'
string|"'means that the behavior will change to '"
nl|'\n'
string|"'the opposite, which is soft-anti-affinity.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|soft_anti_affinity_weight_opt
name|'soft_anti_affinity_weight_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
nl|'\n'
string|"'soft_anti_affinity_weight_multiplier'"
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
string|"'Multiplier used for weighing hosts '"
nl|'\n'
string|"'for group soft-anti-affinity. Only a '"
nl|'\n'
string|"'positive value is meaningful. Negative '"
nl|'\n'
string|"'means that the behavior will change to '"
nl|'\n'
string|"'the opposite, which is soft-affinity.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|SIMPLE_OPTS
name|'SIMPLE_OPTS'
op|'='
op|'['
name|'host_subset_size_opt'
op|','
nl|'\n'
name|'bm_default_filter_opt'
op|','
nl|'\n'
name|'use_bm_filters_opt'
op|','
nl|'\n'
name|'host_mgr_avail_filt_opt'
op|','
nl|'\n'
name|'host_mgr_default_filt_opt'
op|','
nl|'\n'
name|'host_mgr_sched_wgt_cls_opt'
op|','
nl|'\n'
name|'host_mgr_tracks_inst_chg_opt'
op|','
nl|'\n'
name|'rpc_sched_topic_opt'
op|','
nl|'\n'
name|'sched_driver_host_mgr_opt'
op|','
nl|'\n'
name|'driver_opt'
op|','
nl|'\n'
name|'driver_period_opt'
op|','
nl|'\n'
name|'scheduler_json_config_location_opt'
op|','
nl|'\n'
name|'disk_allocation_ratio_opt'
op|','
nl|'\n'
name|'isolated_img_opt'
op|','
nl|'\n'
name|'isolated_host_opt'
op|','
nl|'\n'
name|'restrict_iso_host_img_opt'
op|','
nl|'\n'
name|'max_io_ops_per_host_opt'
op|','
nl|'\n'
name|'agg_img_prop_iso_namespace_opt'
op|','
nl|'\n'
name|'agg_img_prop_iso_separator_opt'
op|','
nl|'\n'
name|'max_instances_per_host_opt'
op|','
nl|'\n'
name|'ram_weight_mult_opt'
op|','
nl|'\n'
name|'io_ops_weight_mult_opt'
op|','
nl|'\n'
name|'scheduler_max_att_opt'
op|','
nl|'\n'
name|'soft_affinity_weight_opt'
op|','
nl|'\n'
name|'soft_anti_affinity_weight_opt'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'SIMPLE_OPTS'
op|','
nl|'\n'
op|'['
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
name|'trusted_opts'
op|','
nl|'\n'
name|'metrics_weight_opts'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'SIMPLE_OPTS'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|'"upgrade_levels"'
op|')'
newline|'\n'
name|'trust_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|'"trusted_computing"'
op|','
nl|'\n'
name|'title'
op|'='
string|'"Trust parameters"'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_group'
op|'('
name|'trust_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'trusted_opts'
op|','
name|'group'
op|'='
name|'trust_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'metrics_weight_opts'
op|','
name|'group'
op|'='
string|'"metrics"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|'"DEFAULT"'
op|':'
name|'SIMPLE_OPTS'
op|','
nl|'\n'
string|'"upgrade_levels"'
op|':'
op|'['
name|'rpcapi_cap_opt'
op|']'
op|','
nl|'\n'
string|'"trusted_computing"'
op|':'
name|'trusted_opts'
op|','
nl|'\n'
string|'"metrics"'
op|':'
name|'metrics_weight_opts'
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit