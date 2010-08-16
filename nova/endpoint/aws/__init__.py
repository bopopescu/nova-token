begin_unit
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
comment|'# TODO(gundlach): temp'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI entry point for all AWS API requests."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
name|'None'
op|','
string|'"{all:.*}"'
op|','
name|'controller'
op|'='
string|'"dummy"'
op|')'
newline|'\n'
nl|'\n'
name|'targets'
op|'='
op|'{'
string|'"dummy"'
op|':'
name|'self'
op|'.'
name|'dummy'
op|'}'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|','
name|'targets'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|dummy
name|'def'
name|'dummy'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
comment|'#TODO(gundlach)'
nl|'\n'
indent|'        '
name|'msg'
op|'='
string|'"dummy response -- please hook up __init__() to cloud.py instead"'
newline|'\n'
name|'return'
name|'repr'
op|'('
op|'{'
string|"'dummy'"
op|':'
name|'msg'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
name|'repr'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
