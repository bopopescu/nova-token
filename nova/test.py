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
string|'"""\nBase classes for our unit tests.\nAllows overriding of flags for use of fakes,\nand some black magic for inline callbacks.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'fakerabbit'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'fake_tests'"
op|','
name|'True'
op|','
nl|'\n'
string|"'should we use everything for testing'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|skip_if_fake
name|'def'
name|'skip_if_fake'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator that skips a test if running in fake mode"""'
newline|'\n'
DECL|function|_skipper
name|'def'
name|'_skipper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wrapped skipper function"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'unittest'
op|'.'
name|'SkipTest'
op|'('
string|"'Test cannot be run in fake mode'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_skipper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TrialTestCase
dedent|''
name|'class'
name|'TrialTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case base class for all unit tests"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run before each test method to initialize test environment"""'
newline|'\n'
name|'super'
op|'('
name|'TrialTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): We need a better method for creating fixtures for tests'
nl|'\n'
comment|'#             now that we have some required db setup for the system'
nl|'\n'
comment|'#             to work properly.'
nl|'\n'
name|'self'
op|'.'
name|'start'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'if'
name|'db'
op|'.'
name|'network_count'
op|'('
name|'ctxt'
op|')'
op|'!='
number|'5'
op|':'
newline|'\n'
indent|'            '
name|'network_manager'
op|'.'
name|'VlanManager'
op|'('
op|')'
op|'.'
name|'create_networks'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'fixed_range'
op|','
nl|'\n'
number|'5'
op|','
number|'16'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'vlan_start'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'vpn_start'
op|')'
newline|'\n'
nl|'\n'
comment|"# emulate some of the mox stuff, we can't use the metaclass"
nl|'\n'
comment|'# because it screws with our generators'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flag_overrides'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'injected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_monkey_patch_attach'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_original_flags'
op|'='
name|'FLAGS'
op|'.'
name|'FlagValuesDict'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Runs after each test method to finalize/tear down test\n        environment."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'SmartUnsetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): Clean up any ips associated during the test.'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_disassociate_all_by_timeout'
op|'('
name|'ctxt'
op|','
name|'FLAGS'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'start'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'network_disassociate_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'Consumer'
op|'.'
name|'attach_to_eventlet'
op|'='
name|'self'
op|'.'
name|'originalAttach'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'injected'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'x'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AssertionError'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'                '
name|'fakerabbit'
op|'.'
name|'reset_all'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'security_group_destroy_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'super'
op|'('
name|'TrialTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'reset_flags'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|flags
dedent|''
dedent|''
name|'def'
name|'flags'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Override flag variables for a test"""'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kw'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'self'
op|'.'
name|'flag_overrides'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'reset_flags'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|"'trying to override already overriden flag: %s'"
op|'%'
name|'k'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flag_overrides'
op|'['
name|'k'
op|']'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_flags
dedent|''
dedent|''
name|'def'
name|'reset_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Resets all flag variables for the test.  Runs after each test"""'
newline|'\n'
name|'FLAGS'
op|'.'
name|'Reset'
op|'('
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_original_flags'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
comment|'#def run(self, result=None):'
nl|'\n'
comment|'#    test_method = getattr(self, self._testMethodName)'
nl|'\n'
comment|'#    setattr(self,'
nl|'\n'
comment|'#            self._testMethodName,'
nl|'\n'
comment|'#            self._maybeInlineCallbacks(test_method, result))'
nl|'\n'
comment|'#    rv = super(TrialTestCase, self).run(result)'
nl|'\n'
comment|'#    setattr(self, self._testMethodName, test_method)'
nl|'\n'
comment|'#    return rv'
nl|'\n'
nl|'\n'
comment|'#def _maybeInlineCallbacks(self, func, result):'
nl|'\n'
comment|'#    def _wrapped():'
nl|'\n'
comment|'#        g = func()'
nl|'\n'
comment|'#        if isinstance(g, defer.Deferred):'
nl|'\n'
comment|'#            return g'
nl|'\n'
comment|"#        if not hasattr(g, 'send'):"
nl|'\n'
comment|'#            return defer.succeed(g)'
nl|'\n'
nl|'\n'
comment|'#        inlined = defer.inlineCallbacks(func)'
nl|'\n'
comment|'#        d = inlined()'
nl|'\n'
comment|'#        return d'
nl|'\n'
comment|'#    _wrapped.func_name = func.func_name'
nl|'\n'
comment|'#    return _wrapped'
nl|'\n'
nl|'\n'
DECL|member|_monkey_patch_attach
dedent|''
dedent|''
name|'def'
name|'_monkey_patch_attach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'originalAttach'
op|'='
name|'rpc'
op|'.'
name|'Consumer'
op|'.'
name|'attach_to_eventlet'
newline|'\n'
nl|'\n'
DECL|function|_wrapped
name|'def'
name|'_wrapped'
op|'('
name|'innerSelf'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'self'
op|'.'
name|'originalAttach'
op|'('
name|'innerSelf'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'injected'
op|'.'
name|'append'
op|'('
name|'rv'
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
dedent|''
name|'_wrapped'
op|'.'
name|'func_name'
op|'='
name|'self'
op|'.'
name|'originalAttach'
op|'.'
name|'func_name'
newline|'\n'
name|'rpc'
op|'.'
name|'Consumer'
op|'.'
name|'attach_to_eventlet'
op|'='
name|'_wrapped'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
