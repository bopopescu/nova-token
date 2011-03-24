begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
string|'"""\r\nStubouts for the test suite\r\n"""'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'vmwareapi_conn'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vmware_images'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|fake_get_vim_object
name|'def'
name|'fake_get_vim_object'
op|'('
name|'arg'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Stubs out the VMWareAPISession\'s get_vim_object method."""'
newline|'\r\n'
name|'return'
name|'fake'
op|'.'
name|'FakeVim'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|fake_is_vim_object
dedent|''
name|'def'
name|'fake_is_vim_object'
op|'('
name|'arg'
op|','
name|'module'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Stubs out the VMWareAPISession\'s is_vim_object method."""'
newline|'\r\n'
name|'return'
name|'isinstance'
op|'('
name|'module'
op|','
name|'fake'
op|'.'
name|'FakeVim'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|set_stubs
dedent|''
name|'def'
name|'set_stubs'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Set the stubs."""'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmware_images'
op|','
string|"'fetch_image'"
op|','
name|'fake'
op|'.'
name|'fake_fetch_image'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmware_images'
op|','
string|"'get_vmdk_size_and_properties'"
op|','
nl|'\r\n'
name|'fake'
op|'.'
name|'fake_get_vmdk_size_and_properties'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmware_images'
op|','
string|"'upload_image'"
op|','
name|'fake'
op|'.'
name|'fake_upload_image'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmwareapi_conn'
op|'.'
name|'VMWareAPISession'
op|','
string|'"_get_vim_object"'
op|','
nl|'\r\n'
name|'fake_get_vim_object'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmwareapi_conn'
op|'.'
name|'VMWareAPISession'
op|','
string|'"_is_vim_object"'
op|','
nl|'\r\n'
name|'fake_is_vim_object'
op|')'
newline|'\r\n'
dedent|''
endmarker|''
end_unit
