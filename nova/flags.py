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
string|'"""\nPackage-level global flags are defined here, the rest are defined\nwhere they\'re used.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'from'
name|'gflags'
name|'import'
op|'*'
newline|'\n'
nl|'\n'
comment|'# This keeps pylint from barfing on the imports'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'FLAGS'
newline|'\n'
DECL|variable|DEFINE_string
name|'DEFINE_string'
op|'='
name|'DEFINE_string'
newline|'\n'
DECL|variable|DEFINE_integer
name|'DEFINE_integer'
op|'='
name|'DEFINE_integer'
newline|'\n'
DECL|variable|DEFINE_bool
name|'DEFINE_bool'
op|'='
name|'DEFINE_bool'
newline|'\n'
nl|'\n'
comment|'# __GLOBAL FLAGS ONLY__'
nl|'\n'
comment|'# Define any app-specific flags in their own files, docs at:'
nl|'\n'
comment|'# http://code.google.com/p/python-gflags/source/browse/trunk/gflags.py#39'
nl|'\n'
nl|'\n'
name|'DEFINE_integer'
op|'('
string|"'s3_port'"
op|','
number|'3333'
op|','
string|"'s3 port'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'s3_internal_port'"
op|','
number|'3334'
op|','
string|"'s3 port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'s3_host'"
op|','
string|"'127.0.0.1'"
op|','
string|"'s3 host'"
op|')'
newline|'\n'
comment|"#DEFINE_string('cloud_topic', 'cloud', 'the topic clouds listen on')"
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'compute_topic'"
op|','
string|"'compute'"
op|','
string|"'the topic compute nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'storage_topic'"
op|','
string|"'storage'"
op|','
string|"'the topic storage nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'fake_libvirt'"
op|','
name|'False'
op|','
nl|'\n'
string|"'whether to use a fake libvirt or not'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'verbose'"
op|','
name|'False'
op|','
string|"'show debug output'"
op|')'
newline|'\n'
name|'DEFINE_boolean'
op|'('
string|"'fake_rabbit'"
op|','
name|'False'
op|','
string|"'use a fake rabbit'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'fake_network'"
op|','
name|'False'
op|','
string|"'should we use fake network devices and addresses'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'fake_users'"
op|','
name|'False'
op|','
string|"'use fake users'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_host'"
op|','
string|"'localhost'"
op|','
string|"'rabbit host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_port'"
op|','
number|'5672'
op|','
string|"'rabbit port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_userid'"
op|','
string|"'guest'"
op|','
string|"'rabbit userid'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_password'"
op|','
string|"'guest'"
op|','
string|"'rabbit password'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_virtual_host'"
op|','
string|"'/'"
op|','
string|"'rabbit virtual host'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'control_exchange'"
op|','
string|"'nova'"
op|','
string|"'the main exchange to connect to'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_url'"
op|','
nl|'\n'
string|"'http://127.0.0.1:8773/services/Cloud'"
op|','
nl|'\n'
string|"'Url to ec2 api server'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'default_image'"
op|','
nl|'\n'
string|"'ami-11111'"
op|','
nl|'\n'
string|"'default image to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_kernel'"
op|','
nl|'\n'
string|"'aki-11111'"
op|','
nl|'\n'
string|"'default kernel to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_ramdisk'"
op|','
nl|'\n'
string|"'ari-11111'"
op|','
nl|'\n'
string|"'default ramdisk to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_instance_type'"
op|','
nl|'\n'
string|"'m1.small'"
op|','
nl|'\n'
string|"'default instance type to use, testing only'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'vpn_image_id'"
op|','
string|"'ami-CLOUDPIPE'"
op|','
string|"'AMI for cloudpipe vpn server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'vpn_key_suffix'"
op|','
nl|'\n'
string|"'-key'"
op|','
nl|'\n'
string|"'Suffix to add to project name for vpn key'"
op|')'
newline|'\n'
nl|'\n'
comment|'# UNUSED'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'node_availability_zone'"
op|','
nl|'\n'
string|"'nova'"
op|','
nl|'\n'
string|"'availability zone of this node'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'node_name'"
op|','
nl|'\n'
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
string|"'name of this node'"
op|')'
newline|'\n'
nl|'\n'
endmarker|''
end_unit
