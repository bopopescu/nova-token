begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
DECL|variable|V
name|'V'
op|'='
string|'"0.9"'
newline|'\n'
nl|'\n'
name|'from'
name|'distutils'
op|'.'
name|'core'
name|'import'
name|'setup'
newline|'\n'
name|'setup'
op|'('
name|'name'
op|'='
string|"'lockfile'"
op|','
nl|'\n'
DECL|variable|author
name|'author'
op|'='
string|"'Skip Montanaro'"
op|','
nl|'\n'
DECL|variable|author_email
name|'author_email'
op|'='
string|"'skip@pobox.com'"
op|','
nl|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'http://smontanaro.dyndns.org/python/'"
op|','
nl|'\n'
DECL|variable|download_url
name|'download_url'
op|'='
op|'('
string|"'http://smontanaro.dyndns.org/python/lockfile-%s.tar.gz'"
op|'%'
nl|'\n'
name|'V'
op|')'
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
name|'V'
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|'"Platform-independent file locking module"'
op|','
nl|'\n'
DECL|variable|long_description
name|'long_description'
op|'='
name|'open'
op|'('
string|'"README"'
op|')'
op|'.'
name|'read'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|packages
name|'packages'
op|'='
op|'['
string|"'lockfile'"
op|']'
op|','
nl|'\n'
DECL|variable|license
name|'license'
op|'='
string|"'MIT License'"
op|','
nl|'\n'
DECL|variable|classifiers
name|'classifiers'
op|'='
op|'['
nl|'\n'
string|"'Development Status :: 4 - Beta'"
op|','
nl|'\n'
string|"'Intended Audience :: Developers'"
op|','
nl|'\n'
string|"'License :: OSI Approved :: MIT License'"
op|','
nl|'\n'
string|"'Operating System :: MacOS'"
op|','
nl|'\n'
string|"'Operating System :: Microsoft :: Windows :: Windows NT/2000'"
op|','
nl|'\n'
string|"'Operating System :: POSIX'"
op|','
nl|'\n'
string|"'Programming Language :: Python'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 2.4'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 2.5'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 2.6'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 2.7'"
op|','
nl|'\n'
string|"'Programming Language :: Python :: 3.0'"
op|','
nl|'\n'
string|"'Topic :: Software Development :: Libraries :: Python Modules'"
op|','
nl|'\n'
op|']'
nl|'\n'
op|')'
newline|'\n'
endmarker|''
end_unit
