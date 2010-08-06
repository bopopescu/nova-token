begin_unit
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'wsgi'
newline|'\n'
name|'eventlet'
op|'.'
name|'patcher'
op|'.'
name|'monkey_patch'
op|'('
name|'all'
op|'='
name|'False'
op|','
name|'socket'
op|'='
name|'True'
op|')'
newline|'\n'
name|'import'
name|'carrot'
op|'.'
name|'connection'
newline|'\n'
name|'import'
name|'carrot'
op|'.'
name|'messaging'
newline|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
nl|'\n'
comment|'# See http://pythonpaste.org/webob/ for usage'
nl|'\n'
name|'from'
name|'webob'
op|'.'
name|'dec'
name|'import'
name|'wsgify'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
op|','
name|'Request'
op|','
name|'Response'
newline|'\n'
nl|'\n'
DECL|class|WSGILayer
name|'class'
name|'WSGILayer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
comment|'# Subclasses will probably want to implement __call__ like this:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# @wsgify'
nl|'\n'
comment|'# def __call__(self, req):'
nl|'\n'
comment|'#   # Any of the following objects work as responses:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   # Option 1: simple string'
nl|'\n'
comment|"#   resp = 'message\\n'"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   # Option 2: a nicely formatted HTTP exception page'
nl|'\n'
comment|"#   resp = exc.HTTPForbidden(detail='Nice try')"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   # Option 3: a webob Response object (in case you need to play with'
nl|'\n'
comment|'#   # headers, or you want to be treated like an iterable, or or or)'
nl|'\n'
comment|"#   resp = Response(); resp.app_iter = open('somefile')"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   # Option 4: any wsgi app to be run next'
nl|'\n'
comment|'#   resp = self.application'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   # Option 5: you can get a Response object for a wsgi app, too, to'
nl|'\n'
comment|'#   # play with headers etc'
nl|'\n'
comment|'#   resp = req.get_response(self.application)'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   # You can then just return your response...'
nl|'\n'
comment|'#   return resp         # option 1'
nl|'\n'
comment|'#   # ... or set req.response and return None.'
nl|'\n'
comment|'#   req.response = resp # option 2'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# See the end of http://pythonpaste.org/webob/modules/dec.html '
nl|'\n'
comment|'# for more info.'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
string|'"You must implement __call__"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Debug
dedent|''
dedent|''
name|'class'
name|'Debug'
op|'('
name|'WSGILayer'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'req'
op|'.'
name|'environ'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'k'
op|','
string|'"="'
op|','
name|'v'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
DECL|class|Auth
dedent|''
dedent|''
name|'class'
name|'Auth'
op|'('
name|'WSGILayer'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
string|"'openstack.auth.token'"
name|'in'
name|'req'
op|'.'
name|'environ'
op|':'
newline|'\n'
comment|'# Check auth params here'
nl|'\n'
indent|'            '
name|'if'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.auth.token'"
op|']'
op|'='
string|"'12345'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'detail'
op|'='
string|'"Go away"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'response'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
name|'response'
op|'.'
name|'headers'
op|'['
string|"'X-Openstack-Auth'"
op|']'
op|'='
string|"'Success'"
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'WSGILayer'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Router'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_connect'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'match'
op|'='
name|'self'
op|'.'
name|'map'
op|'.'
name|'match'
op|'('
name|'req'
op|'.'
name|'path_info'
op|')'
newline|'\n'
name|'if'
name|'match'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
dedent|''
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.match'"
op|']'
op|'='
name|'match'
newline|'\n'
name|'return'
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_connect
dedent|''
name|'def'
name|'_connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
string|'"You must implement _connect"'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FileRouter
dedent|''
dedent|''
name|'class'
name|'FileRouter'
op|'('
name|'Router'
op|')'
op|':'
newline|'\n'
DECL|member|_connect
indent|'    '
name|'def'
name|'_connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'map'
op|'.'
name|'connect'
op|'('
name|'None'
op|','
string|"'/files/{file}'"
op|','
name|'controller'
op|'='
name|'File'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'.'
name|'connect'
op|'('
name|'None'
op|','
string|"'/rfiles/{file}'"
op|','
name|'controller'
op|'='
name|'Reverse'
op|'('
name|'File'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Message
dedent|''
dedent|''
name|'class'
name|'Message'
op|'('
name|'WSGILayer'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'message\\n'"
newline|'\n'
nl|'\n'
DECL|class|Reverse
dedent|''
dedent|''
name|'class'
name|'Reverse'
op|'('
name|'WSGILayer'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inner_resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
name|'print'
string|'"+"'
op|'*'
number|'80'
newline|'\n'
name|'Debug'
op|'('
op|')'
op|'('
name|'req'
op|')'
newline|'\n'
name|'print'
string|'"*"'
op|'*'
number|'80'
newline|'\n'
name|'resp'
op|'='
name|'Response'
op|'('
op|')'
newline|'\n'
name|'resp'
op|'.'
name|'app_iter'
op|'='
name|'itertools'
op|'.'
name|'imap'
op|'('
name|'lambda'
name|'x'
op|':'
name|'x'
op|'['
op|':'
op|':'
op|'-'
number|'1'
op|']'
op|','
name|'inner_resp'
op|'.'
name|'app_iter'
op|')'
newline|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
DECL|class|File
dedent|''
dedent|''
name|'class'
name|'File'
op|'('
name|'WSGILayer'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'myfile'
op|'='
name|'open'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.match'"
op|']'
op|'['
string|"'file'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'req'
op|'.'
name|'response'
op|'='
name|'Response'
op|'('
op|')'
newline|'\n'
name|'req'
op|'.'
name|'response'
op|'.'
name|'app_iter'
op|'='
name|'myfile'
newline|'\n'
nl|'\n'
DECL|variable|sock
dedent|''
dedent|''
name|'sock'
op|'='
name|'eventlet'
op|'.'
name|'listen'
op|'('
op|'('
string|"'localhost'"
op|','
number|'12345'
op|')'
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'server'
op|'('
name|'sock'
op|','
name|'Debug'
op|'('
name|'Auth'
op|'('
name|'FileRouter'
op|'('
name|'Message'
op|'('
op|')'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
endmarker|''
end_unit
