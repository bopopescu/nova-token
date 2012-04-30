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
comment|'# Importing full names to not pollute the namespace and cause possible'
nl|'\n'
comment|"# collisions with use of 'from nova.volume import <foo>' elsewhere."
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'importutils'
newline|'\n'
nl|'\n'
DECL|variable|API
name|'API'
op|'='
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'importutils'
op|'.'
name|'import_class'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'volume_api_class'
op|')'
newline|'\n'
endmarker|''
end_unit
