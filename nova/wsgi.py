begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""Utility methods for working with WSGI servers."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'wsgi'
newline|'\n'
name|'import'
name|'greenlet'
newline|'\n'
name|'import'
name|'routes'
op|'.'
name|'middleware'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'paste'
name|'import'
name|'deploy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.wsgi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Server
name|'class'
name|'Server'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server class to manage a WSGI server, serving a WSGI application."""'
newline|'\n'
nl|'\n'
DECL|variable|default_pool_size
name|'default_pool_size'
op|'='
number|'1000'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'app'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'port'
op|'='
name|'None'
op|','
name|'pool_size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize, but do not start, a WSGI server.\n\n        :param name: Pretty name for logging.\n        :param app: The WSGI application to serve.\n        :param host: IP address to serve the application.\n        :param port: Port number to server the application.\n        :param pool_size: Maximum number of eventlets to spawn concurrently.\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'app'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
name|'or'
string|'"0.0.0.0"'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'port'
name|'or'
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'_server'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_tcp_server'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_socket'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_pool'
op|'='
name|'eventlet'
op|'.'
name|'GreenPool'
op|'('
name|'pool_size'
name|'or'
name|'self'
op|'.'
name|'default_pool_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"eventlet.wsgi.server"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wsgi_logger'
op|'='
name|'logging'
op|'.'
name|'WritableLogger'
op|'('
name|'self'
op|'.'
name|'_logger'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start
dedent|''
name|'def'
name|'_start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run the blocking eventlet WSGI server.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'server'
op|'('
name|'self'
op|'.'
name|'_socket'
op|','
nl|'\n'
name|'self'
op|'.'
name|'app'
op|','
nl|'\n'
name|'custom_pool'
op|'='
name|'self'
op|'.'
name|'_pool'
op|','
nl|'\n'
name|'log'
op|'='
name|'self'
op|'.'
name|'_wsgi_logger'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|','
name|'backlog'
op|'='
number|'128'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start serving a WSGI application.\n\n        :param backlog: Maximum number of queued connections.\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_socket'
op|'='
name|'eventlet'
op|'.'
name|'listen'
op|'('
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
op|','
name|'backlog'
op|'='
name|'backlog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_server'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'_start'
op|')'
newline|'\n'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
op|'='
name|'self'
op|'.'
name|'_socket'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Started %(name)s on %(host)s:%(port)s"'
op|')'
op|'%'
name|'self'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop this server.\n\n        This is not a very nice action, as currently the method by which a\n        server is stopped is by killing it\'s eventlet.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Stopping WSGI server."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_server'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_tcp_server'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Stopping raw TCP server."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_tcp_server'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_tcp
dedent|''
dedent|''
name|'def'
name|'start_tcp'
op|'('
name|'self'
op|','
name|'listener'
op|','
name|'port'
op|','
name|'host'
op|'='
string|"'0.0.0.0'"
op|','
name|'key'
op|'='
name|'None'
op|','
name|'backlog'
op|'='
number|'128'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run a raw TCP server with the given application."""'
newline|'\n'
name|'arg0'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Starting TCP server %(arg0)s on %(host)s:%(port)s'"
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'socket'
op|'='
name|'eventlet'
op|'.'
name|'listen'
op|'('
op|'('
name|'host'
op|','
name|'port'
op|')'
op|','
name|'backlog'
op|'='
name|'backlog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_tcp_server'
op|'='
name|'self'
op|'.'
name|'_pool'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_run_tcp'
op|','
name|'listener'
op|','
name|'socket'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Block, until the server has stopped.\n\n        Waits on the server\'s eventlet to finish, then returns.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"WSGI server has stopped."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_run_tcp
dedent|''
dedent|''
name|'def'
name|'_run_tcp'
op|'('
name|'self'
op|','
name|'listener'
op|','
name|'socket'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start a raw TCP server in a new green thread."""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'new_sock'
op|','
name|'address'
op|'='
name|'socket'
op|'.'
name|'accept'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pool'
op|'.'
name|'spawn_n'
op|'('
name|'listener'
op|','
name|'new_sock'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'SystemExit'
op|','
name|'KeyboardInterrupt'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Request
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Request'
op|'('
name|'webob'
op|'.'
name|'Request'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Application
dedent|''
name|'class'
name|'Application'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base WSGI application wrapper. Subclasses need to implement __call__."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Used for paste app factories in paste.deploy config files.\n\n        Any local configuration (that is, values under the [app:APPNAME]\n        section of the paste config) will be passed into the `__init__` method\n        as kwargs.\n\n        A hypothetical configuration would look like:\n\n            [app:wadl]\n            latest_version = 1.3\n            paste.app_factory = nova.api.fancy_api:Wadl.factory\n\n        which would result in a call to the `Wadl` class as\n\n            import nova.api.fancy_api\n            fancy_api.Wadl(latest_version=\'1.3\')\n\n        You could of course re-implement the `factory` method in subclasses,\n        but using the kwarg passing it shouldn\'t be necessary.\n\n        """'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|'**'
name|'local_config'
op|')'
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
indent|'        '
string|'r"""Subclasses will probably want to implement __call__ like this:\n\n        @webob.dec.wsgify(RequestClass=Request)\n        def __call__(self, req):\n          # Any of the following objects work as responses:\n\n          # Option 1: simple string\n          res = \'message\\n\'\n\n          # Option 2: a nicely formatted HTTP exception page\n          res = exc.HTTPForbidden(detail=\'Nice try\')\n\n          # Option 3: a webob Response object (in case you need to play with\n          # headers, or you want to be treated like an iterable, or or or)\n          res = Response();\n          res.app_iter = open(\'somefile\')\n\n          # Option 4: any wsgi app to be run next\n          res = self.application\n\n          # Option 5: you can get a Response object for a wsgi app, too, to\n          # play with headers etc\n          res = req.get_response(self.application)\n\n          # You can then just return your response...\n          return res\n          # ... or set req.response and return None.\n          req.response = res\n\n        See the end of http://pythonpaste.org/webob/modules/dec.html\n        for more info.\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|"'You must implement __call__'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Middleware
dedent|''
dedent|''
name|'class'
name|'Middleware'
op|'('
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base WSGI middleware.\n\n    These classes require an application to be\n    initialized that will be called next.  By default the middleware will\n    simply call its wrapped app, or you can override __call__ to customize its\n    behavior.\n\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Used for paste app factories in paste.deploy config files.\n\n        Any local configuration (that is, values under the [filter:APPNAME]\n        section of the paste config) will be passed into the `__init__` method\n        as kwargs.\n\n        A hypothetical configuration would look like:\n\n            [filter:analytics]\n            redis_host = 127.0.0.1\n            paste.filter_factory = nova.api.analytics:Analytics.factory\n\n        which would result in a call to the `Analytics` class as\n\n            import nova.api.analytics\n            analytics.Analytics(app_from_paste, redis_host=\'127.0.0.1\')\n\n        You could of course re-implement the `factory` method in subclasses,\n        but using the kwarg passing it shouldn\'t be necessary.\n\n        """'
newline|'\n'
DECL|function|_factory
name|'def'
name|'_factory'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'('
name|'app'
op|','
op|'**'
name|'local_config'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_factory'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
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
DECL|member|process_request
dedent|''
name|'def'
name|'process_request'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called on each request.\n\n        If this returns None, the next application down the stack will be\n        executed. If it returns a response then that response will be returned\n        and execution will stop here.\n\n        """'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|process_response
dedent|''
name|'def'
name|'process_response'
op|'('
name|'self'
op|','
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Do whatever you\'d like to the response."""'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'Request'
op|')'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'process_request'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'response'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
newline|'\n'
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
name|'return'
name|'self'
op|'.'
name|'process_response'
op|'('
name|'response'
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
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper class for debugging a WSGI application.\n\n    Can be inserted into any WSGI application chain to get information\n    about the request and response.\n\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'Request'
op|')'
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
name|'print'
op|'('
string|"'*'"
op|'*'
number|'40'
op|')'
op|'+'
string|"' REQUEST ENVIRON'"
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
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
name|'key'
op|','
string|"'='"
op|','
name|'value'
newline|'\n'
dedent|''
name|'print'
newline|'\n'
name|'resp'
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
nl|'\n'
name|'print'
op|'('
string|"'*'"
op|'*'
number|'40'
op|')'
op|'+'
string|"' RESPONSE HEADERS'"
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'resp'
op|'.'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'key'
op|','
string|"'='"
op|','
name|'value'
newline|'\n'
dedent|''
name|'print'
newline|'\n'
nl|'\n'
name|'resp'
op|'.'
name|'app_iter'
op|'='
name|'self'
op|'.'
name|'print_generator'
op|'('
name|'resp'
op|'.'
name|'app_iter'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|print_generator
name|'def'
name|'print_generator'
op|'('
name|'app_iter'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Iterator that prints the contents of a wrapper string."""'
newline|'\n'
name|'print'
op|'('
string|"'*'"
op|'*'
number|'40'
op|')'
op|'+'
string|"' BODY'"
newline|'\n'
name|'for'
name|'part'
name|'in'
name|'app_iter'
op|':'
newline|'\n'
indent|'            '
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'part'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'part'
newline|'\n'
dedent|''
name|'print'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI middleware that maps incoming requests to WSGI apps."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a router for the given routes.Mapper.\n\n        Each route in `mapper` must specify a \'controller\', which is a\n        WSGI app to call.  You\'ll probably want to specify an \'action\' as\n        well and have your controller be an object that can route\n        the request to the action-specific method.\n\n        Examples:\n          mapper = routes.Mapper()\n          sc = ServerController()\n\n          # Explicit mapping of one route to a controller+action\n          mapper.connect(None, \'/svrlist\', controller=sc, action=\'list\')\n\n          # Actions are all implicitly defined\n          mapper.resource(\'server\', \'servers\', controller=sc)\n\n          # Pointing to an arbitrary WSGI app.  You can specify the\n          # {path_info:.*} parameter so the target app can be handed just that\n          # section of the URL.\n          mapper.connect(None, \'/v1.0/{path_info:.*}\', controller=BlogApp())\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'='
name|'mapper'
newline|'\n'
name|'self'
op|'.'
name|'_router'
op|'='
name|'routes'
op|'.'
name|'middleware'
op|'.'
name|'RoutesMiddleware'
op|'('
name|'self'
op|'.'
name|'_dispatch'
op|','
nl|'\n'
name|'self'
op|'.'
name|'map'
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
op|'('
name|'RequestClass'
op|'='
name|'Request'
op|')'
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
string|'"""Route the incoming request to a controller based on self.map.\n\n        If no match, return a 404.\n\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_router'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'Request'
op|')'
newline|'\n'
DECL|member|_dispatch
name|'def'
name|'_dispatch'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Dispatch the request to the appropriate controller.\n\n        Called by self._router after matching the incoming request to a route\n        and putting the information into req.environ.  Either returns 404\n        or the routed WSGI app\'s response.\n\n        """'
newline|'\n'
name|'match'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'app'
op|'='
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'return'
name|'app'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Loader
dedent|''
dedent|''
name|'class'
name|'Loader'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used to load WSGI applications from paste configurations."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'config_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize the loader, and attempt to find the config.\n\n        :param config_path: Full or relative path to the paste config.\n        :returns: None\n\n        """'
newline|'\n'
name|'config_path'
op|'='
name|'config_path'
name|'or'
name|'FLAGS'
op|'.'
name|'api_paste_config'
newline|'\n'
name|'self'
op|'.'
name|'config_path'
op|'='
name|'utils'
op|'.'
name|'find_config'
op|'('
name|'config_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|load_app
dedent|''
name|'def'
name|'load_app'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the paste URLMap wrapped WSGI application.\n\n        :param name: Name of the application to load.\n        :returns: Paste URLMap object wrapping the requested application.\n        :raises: `nova.exception.PasteAppNotFound`\n\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'deploy'
op|'.'
name|'loadapp'
op|'('
string|'"config:%s"'
op|'%'
name|'self'
op|'.'
name|'config_path'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'LookupError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'err'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PasteAppNotFound'
op|'('
name|'name'
op|'='
name|'name'
op|','
name|'path'
op|'='
name|'self'
op|'.'
name|'config_path'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
