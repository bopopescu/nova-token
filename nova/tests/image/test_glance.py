begin_unit
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
nl|'\n'
DECL|class|StubGlanceClient
name|'class'
name|'StubGlanceClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'images'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_images'
op|'='
name|'images'
newline|'\n'
nl|'\n'
DECL|member|get_image_meta
dedent|''
name|'def'
name|'get_image_meta'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_images'
op|'['
name|'id'
op|']'
newline|'\n'
nl|'\n'
DECL|class|TestGlance
dedent|''
dedent|''
name|'class'
name|'TestGlance'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test
indent|'    '
name|'def'
name|'test'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
op|'{'
string|"'xyz'"
op|':'
string|'"image"'
op|'}'
newline|'\n'
name|'client'
op|'='
name|'StubGlanceClient'
op|'('
name|'images'
op|')'
newline|'\n'
name|'service'
op|'='
name|'glance'
op|'.'
name|'GlanceImageService'
op|'('
name|'client'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
