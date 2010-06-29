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
comment|'# Copyright 2010 Anso Labs, LLC'
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
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
name|'FLAGS'
op|'.'
name|'fake_libvirt'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_network'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_users'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
endmarker|''
end_unit
