begin_unit
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'faults'
newline|'\n'
nl|'\n'
DECL|class|TestFaults
name|'class'
name|'TestFaults'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_fault_parts
indent|'    '
name|'def'
name|'test_fault_parts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
newline|'\n'
name|'f'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'scram'"
op|')'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
name|'first_two_words'
op|'='
name|'resp'
op|'.'
name|'body'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
op|')'
op|'['
op|':'
number|'2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'first_two_words'
op|','
op|'['
string|"'<badRequest'"
op|','
string|'\'code="400">\''
op|']'
op|')'
newline|'\n'
name|'body_without_spaces'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'resp'
op|'.'
name|'body'
op|'.'
name|'split'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'<message>scram</message>'"
name|'in'
name|'body_without_spaces'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_retry_header
dedent|''
name|'def'
name|'test_retry_header'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'explanation'
op|'='
string|"'sorry'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'4'
op|'}'
op|')'
newline|'\n'
name|'f'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'f'
op|')'
newline|'\n'
name|'first_two_words'
op|'='
name|'resp'
op|'.'
name|'body'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
op|')'
op|'['
op|':'
number|'2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'first_two_words'
op|','
op|'['
string|"'<overLimit'"
op|','
string|'\'code="413">\''
op|']'
op|')'
newline|'\n'
name|'body_sans_spaces'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'resp'
op|'.'
name|'body'
op|'.'
name|'split'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'<message>sorry</message>'"
name|'in'
name|'body_sans_spaces'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'<retryAfter>4</retryAfter>'"
name|'in'
name|'body_sans_spaces'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'headers'
op|'['
string|"'Retry-After'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
