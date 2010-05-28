begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
string|'"""\n@file setup.py\n@author Andy McCurdy\n@date 2/12/2010\n@brief Setuptools configuration for redis client\n"""'
newline|'\n'
nl|'\n'
DECL|variable|version
name|'version'
op|'='
string|"'1.36'"
newline|'\n'
nl|'\n'
DECL|variable|sdict
name|'sdict'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'redis'"
op|','
nl|'\n'
string|"'version'"
op|':'
name|'version'
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'Python client for Redis key-value store'"
op|','
nl|'\n'
string|"'long_description'"
op|':'
string|"'Python client for Redis key-value store'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'http://github.com/andymccurdy/redis-py'"
op|','
nl|'\n'
string|"'download_url'"
op|':'
string|"'http://cloud.github.com/downloads/andymccurdy/redis-py/redis-%s.tar.gz'"
op|'%'
name|'version'
op|','
nl|'\n'
string|"'author'"
op|':'
string|"'Andy McCurdy'"
op|','
nl|'\n'
string|"'author_email'"
op|':'
string|"'sedrik@gmail.com'"
op|','
nl|'\n'
string|"'maintainer'"
op|':'
string|"'Andy McCurdy'"
op|','
nl|'\n'
string|"'maintainer_email'"
op|':'
string|"'sedrik@gmail.com'"
op|','
nl|'\n'
string|"'keywords'"
op|':'
op|'['
string|"'Redis'"
op|','
string|"'key-value store'"
op|']'
op|','
nl|'\n'
string|"'license'"
op|':'
string|"'MIT'"
op|','
nl|'\n'
string|"'packages'"
op|':'
op|'['
string|"'redis'"
op|']'
op|','
nl|'\n'
string|"'test_suite'"
op|':'
string|"'tests.all_tests'"
op|','
nl|'\n'
string|"'classifiers'"
op|':'
op|'['
nl|'\n'
string|"'Development Status :: 4 - Beta'"
op|','
nl|'\n'
string|"'Environment :: Console'"
op|','
nl|'\n'
string|"'Intended Audience :: Developers'"
op|','
nl|'\n'
string|"'License :: OSI Approved :: MIT License'"
op|','
nl|'\n'
string|"'Operating System :: OS Independent'"
op|','
nl|'\n'
string|"'Programming Language :: Python'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'setuptools'
name|'import'
name|'setup'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'distutils'
op|'.'
name|'core'
name|'import'
name|'setup'
newline|'\n'
nl|'\n'
dedent|''
name|'setup'
op|'('
op|'**'
name|'sdict'
op|')'
newline|'\n'
nl|'\n'
endmarker|''
end_unit
