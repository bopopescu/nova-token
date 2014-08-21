begin_unit
comment|'# Copyright 2014 NEC Corporation.  All rights reserved.'
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
string|'"""\nCommon parameter types for validating request Body.\n\n"""'
newline|'\n'
nl|'\n'
DECL|variable|boolean
name|'boolean'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'boolean'"
op|','
string|"'string'"
op|']'
op|','
nl|'\n'
string|"'enum'"
op|':'
op|'['
name|'True'
op|','
string|"'True'"
op|','
string|"'TRUE'"
op|','
string|"'true'"
op|','
string|"'1'"
op|','
nl|'\n'
name|'False'
op|','
string|"'False'"
op|','
string|"'FALSE'"
op|','
string|"'false'"
op|','
string|"'0'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|hostname
name|'hostname'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
comment|'# NOTE: \'host\' is defined in "services" table, and that'
nl|'\n'
comment|'# means a hostname. The hostname grammar in RFC952 does'
nl|'\n'
comment|'# not allow for underscores in hostnames. However, this'
nl|'\n'
comment|'# schema allows them, because it sometimes occurs in'
nl|'\n'
comment|'# real systems.'
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._]*$'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|hostname_or_ip_address
name|'hostname_or_ip_address'
op|'='
op|'{'
nl|'\n'
comment|'# NOTE: Allow to specify hostname, ipv4 and ipv6.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-_.:]*$'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
op|'{'
nl|'\n'
comment|"# NOTE: Nova v3 API contains some 'name' parameters such"
nl|'\n'
comment|'# as keypair, server, flavor, aggregate and so on. They are'
nl|'\n'
comment|'# stored in the DB and Nova specific parameters.'
nl|'\n'
comment|'# This definition is used for all their parameters.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
nl|'\n'
comment|'# NOTE: Allow to some spaces in middle of name.'
nl|'\n'
comment|'# Also note that the regexp below deliberately allows and'
nl|'\n'
comment|'# empty string. This is so only the constraint above'
nl|'\n'
comment|'# which enforces a minimum length for the name is triggered'
nl|'\n'
comment|'# when an empty string is tested. Otherwise it is not'
nl|'\n'
comment|'# deterministic which constraint fails and this causes issues'
nl|'\n'
comment|'# for some unittests when PYTHONHASHSEED is set randomly.'
nl|'\n'
string|"'pattern'"
op|':'
string|"'^(?! )[a-zA-Z0-9. _-]*(?<! )$'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|tcp_udp_port
name|'tcp_udp_port'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'integer'"
op|','
string|"'string'"
op|']'
op|','
string|"'pattern'"
op|':'
string|"'^[0-9]*$'"
op|','
nl|'\n'
string|"'minimum'"
op|':'
number|'0'
op|','
string|"'maximum'"
op|':'
number|'65535'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-]*$'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|admin_password
name|'admin_password'
op|'='
op|'{'
nl|'\n'
comment|'# NOTE: admin_password is the admin password of a server'
nl|'\n'
comment|"# instance, and it is not stored into nova's data base."
nl|'\n'
comment|'# In addition, users set sometimes long/strange string'
nl|'\n'
comment|'# as password. It is unnecessary to limit string length'
nl|'\n'
comment|'# and string pattern.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|image_ref
name|'image_ref'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|flavor_ref
name|'flavor_ref'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'integer'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|metadata
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'patternProperties'"
op|':'
op|'{'
nl|'\n'
string|"'^[a-zA-Z0-9-_:. ]{1,255}$'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'maxLength'"
op|':'
number|'255'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|mac_address
name|'mac_address'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^([0-9a-fA-F]{2})(:[0-9a-fA-F]{2}){5}$'"
nl|'\n'
op|'}'
newline|'\n'
endmarker|''
end_unit
