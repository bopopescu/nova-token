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
nl|'\n'
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
name|'DEFINE_string'
op|'('
string|"'region'"
op|','
string|"'nova'"
op|','
string|"'Region to use'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'test_image'"
op|','
string|"'ami-tty'"
op|','
string|"'Image to use for launch tests'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'use_ipv6'"
op|','
name|'True'
op|','
string|"'use the ipv6 or not'"
op|')'
newline|'\n'
endmarker|''
end_unit
