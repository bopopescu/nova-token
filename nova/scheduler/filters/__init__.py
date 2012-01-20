begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
string|'"""\nThere are three filters included: AllHosts, InstanceType & JSON.\n\nAllHosts just returns the full, unfiltered list of hosts.\nInstanceType is a hard coded matching mechanism based on flavor criteria.\nJSON is an ad-hoc filter grammar.\n\nWhy JSON? The requests for instances may come in through the\nREST interface from a user or a parent Zone.\nCurrently InstanceTypes are used for specifing the type of instance desired.\nSpecific Nova users have noted a need for a more expressive way of specifying\ninstance requirements. Since we don\'t want to get into building full DSL,\nthis filter is a simple form as an example of how this could be done.\nIn reality, most consumers will use the more rigid filters such as the\nInstanceType filter.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'abstract_filter'
name|'import'
name|'AbstractHostFilter'
newline|'\n'
name|'from'
name|'all_hosts_filter'
name|'import'
name|'AllHostsFilter'
newline|'\n'
name|'from'
name|'compute_filter'
name|'import'
name|'ComputeFilter'
newline|'\n'
name|'from'
name|'json_filter'
name|'import'
name|'JsonFilter'
newline|'\n'
name|'from'
name|'ram_filter'
name|'import'
name|'RamFilter'
newline|'\n'
endmarker|''
end_unit
