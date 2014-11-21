begin_unit
comment|'# -*- coding: utf-8 -*-'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# nova documentation build configuration file, created by'
nl|'\n'
comment|'# sphinx-quickstart on Sat May  1 15:17:47 2010.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This file is execfile()d with the current directory set to'
nl|'\n'
comment|'# its containing dir.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Note that not all possible configuration values are present in this'
nl|'\n'
comment|'# autogenerated file.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# All configuration values have a default; values that are commented out'
nl|'\n'
comment|'# serve to show the default.'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
comment|'# If extensions (or modules to document with autodoc) are in another directory,'
nl|'\n'
comment|'# add these directories to sys.path here. If the directory is relative to the'
nl|'\n'
comment|'# documentation root, use os.path.abspath to make it absolute, like shown here.'
nl|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|"'../../'"
op|')'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|"'../'"
op|')'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|"'./'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# -- General configuration ----------------------------------------------------'
nl|'\n'
nl|'\n'
comment|'# Add any Sphinx extension module names here, as strings. They can be'
nl|'\n'
comment|"# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones."
nl|'\n'
nl|'\n'
DECL|variable|extensions
name|'extensions'
op|'='
op|'['
string|"'sphinx.ext.autodoc'"
op|','
nl|'\n'
string|"'ext.nova_todo'"
op|','
nl|'\n'
string|"'sphinx.ext.coverage'"
op|','
nl|'\n'
string|"'sphinx.ext.pngmath'"
op|','
nl|'\n'
string|"'sphinx.ext.ifconfig'"
op|','
nl|'\n'
string|"'sphinx.ext.graphviz'"
op|','
nl|'\n'
string|"'oslosphinx'"
op|','
nl|'\n'
string|'"ext.support_matrix"'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|todo_include_todos
name|'todo_include_todos'
op|'='
name|'True'
newline|'\n'
nl|'\n'
comment|'# Add any paths that contain templates here, relative to this directory.'
nl|'\n'
comment|'# Changing the path so that the Hudson build output contains GA code'
nl|'\n'
comment|'# and the source docs do not contain the code so local, offline sphinx builds'
nl|'\n'
comment|'# are "clean."'
nl|'\n'
DECL|variable|templates_path
name|'templates_path'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'HUDSON_PUBLISH_DOCS'"
op|')'
op|':'
newline|'\n'
DECL|variable|templates_path
indent|'    '
name|'templates_path'
op|'='
op|'['
string|"'_ga'"
op|','
string|"'_templates'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|templates_path
indent|'    '
name|'templates_path'
op|'='
op|'['
string|"'_templates'"
op|']'
newline|'\n'
nl|'\n'
comment|'# The suffix of source filenames.'
nl|'\n'
DECL|variable|source_suffix
dedent|''
name|'source_suffix'
op|'='
string|"'.rst'"
newline|'\n'
nl|'\n'
comment|'# The encoding of source files.'
nl|'\n'
comment|"#source_encoding = 'utf-8'"
nl|'\n'
nl|'\n'
comment|'# The master toctree document.'
nl|'\n'
DECL|variable|master_doc
name|'master_doc'
op|'='
string|"'index'"
newline|'\n'
nl|'\n'
comment|'# General information about the project.'
nl|'\n'
DECL|variable|project
name|'project'
op|'='
string|"u'nova'"
newline|'\n'
DECL|variable|copyright
name|'copyright'
op|'='
string|"u'2010-present, OpenStack Foundation'"
newline|'\n'
nl|'\n'
comment|"# The version info for the project you're documenting, acts as replacement for"
nl|'\n'
comment|'# |version| and |release|, also used in various other places throughout the'
nl|'\n'
comment|'# built documents.'
nl|'\n'
comment|'#'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'version'
name|'import'
name|'version_info'
newline|'\n'
comment|'# The full version, including alpha/beta/rc tags.'
nl|'\n'
DECL|variable|release
name|'release'
op|'='
name|'version_info'
op|'.'
name|'release_string'
op|'('
op|')'
newline|'\n'
comment|'# The short X.Y version.'
nl|'\n'
DECL|variable|version
name|'version'
op|'='
name|'version_info'
op|'.'
name|'version_string'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# The language for content autogenerated by Sphinx. Refer to documentation'
nl|'\n'
comment|'# for a list of supported languages.'
nl|'\n'
comment|'#language = None'
nl|'\n'
nl|'\n'
comment|'# There are two options for replacing |today|: either, you set today to some'
nl|'\n'
comment|'# non-false value, then it is used:'
nl|'\n'
comment|"#today = ''"
nl|'\n'
comment|'# Else, today_fmt is used as the format for a strftime call.'
nl|'\n'
comment|"#today_fmt = '%B %d, %Y'"
nl|'\n'
nl|'\n'
comment|"# List of documents that shouldn't be included in the build."
nl|'\n'
DECL|variable|unused_docs
name|'unused_docs'
op|'='
op|'['
nl|'\n'
string|"'api_ext/rst_extension_template'"
op|','
nl|'\n'
string|"'vmwareapi_readme'"
op|','
nl|'\n'
string|"'installer'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|"# List of directories, relative to source directory, that shouldn't be searched"
nl|'\n'
comment|'# for source files.'
nl|'\n'
DECL|variable|exclude_trees
name|'exclude_trees'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# The reST default role (used for this markup: `text`) to use'
nl|'\n'
comment|'# for all documents.'
nl|'\n'
comment|'#default_role = None'
nl|'\n'
nl|'\n'
comment|"# If true, '()' will be appended to :func: etc. cross-reference text."
nl|'\n'
comment|'#add_function_parentheses = True'
nl|'\n'
nl|'\n'
comment|'# If true, the current module name will be prepended to all description'
nl|'\n'
comment|'# unit titles (such as .. function::).'
nl|'\n'
DECL|variable|add_module_names
name|'add_module_names'
op|'='
name|'False'
newline|'\n'
nl|'\n'
comment|'# If true, sectionauthor and moduleauthor directives will be shown in the'
nl|'\n'
comment|'# output. They are ignored by default.'
nl|'\n'
DECL|variable|show_authors
name|'show_authors'
op|'='
name|'False'
newline|'\n'
nl|'\n'
comment|'# The name of the Pygments (syntax highlighting) style to use.'
nl|'\n'
DECL|variable|pygments_style
name|'pygments_style'
op|'='
string|"'sphinx'"
newline|'\n'
nl|'\n'
comment|'# A list of ignored prefixes for module index sorting.'
nl|'\n'
DECL|variable|modindex_common_prefix
name|'modindex_common_prefix'
op|'='
op|'['
string|"'nova.'"
op|']'
newline|'\n'
nl|'\n'
comment|'# -- Options for man page output ----------------------------------------------'
nl|'\n'
nl|'\n'
comment|'# Grouping the document tree for man pages.'
nl|'\n'
comment|"# List of tuples 'sourcefile', 'target', u'title', u'Authors name', 'manual'"
nl|'\n'
nl|'\n'
DECL|variable|man_pages
name|'man_pages'
op|'='
op|'['
nl|'\n'
op|'('
string|"'man/nova-all'"
op|','
string|"'nova-all'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-api-ec2'"
op|','
string|"'nova-api-ec2'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-api-metadata'"
op|','
string|"'nova-api-metadata'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-api-os-compute'"
op|','
string|"'nova-api-os-compute'"
op|','
nl|'\n'
string|"u'Cloud controller fabric'"
op|','
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-api'"
op|','
string|"'nova-api'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-cert'"
op|','
string|"'nova-cert'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-compute'"
op|','
string|"'nova-compute'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-console'"
op|','
string|"'nova-console'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-consoleauth'"
op|','
string|"'nova-consoleauth'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-dhcpbridge'"
op|','
string|"'nova-dhcpbridge'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-manage'"
op|','
string|"'nova-manage'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-network'"
op|','
string|"'nova-network'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-novncproxy'"
op|','
string|"'nova-novncproxy'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-spicehtml5proxy'"
op|','
string|"'nova-spicehtml5proxy'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-serialproxy'"
op|','
string|"'nova-serialproxy'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-objectstore'"
op|','
string|"'nova-objectstore'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-rootwrap'"
op|','
string|"'nova-rootwrap'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-scheduler'"
op|','
string|"'nova-scheduler'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-xvpvncproxy'"
op|','
string|"'nova-xvpvncproxy'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'man/nova-conductor'"
op|','
string|"'nova-conductor'"
op|','
string|"u'Cloud controller fabric'"
op|','
nl|'\n'
op|'['
string|"u'OpenStack'"
op|']'
op|','
number|'1'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|'# -- Options for HTML output --------------------------------------------------'
nl|'\n'
nl|'\n'
comment|'# The theme to use for HTML and HTML Help pages.  Major themes that come with'
nl|'\n'
comment|"# Sphinx are currently 'default' and 'sphinxdoc'."
nl|'\n'
comment|'# html_theme_path = ["."]'
nl|'\n'
comment|"# html_theme = '_theme'"
nl|'\n'
nl|'\n'
comment|'# Theme options are theme-specific and customize the look and feel of a theme'
nl|'\n'
comment|'# further.  For a list of options available for each theme, see the'
nl|'\n'
comment|'# documentation.'
nl|'\n'
comment|'#html_theme_options = {}'
nl|'\n'
nl|'\n'
comment|'# Add any paths that contain custom themes here, relative to this directory.'
nl|'\n'
comment|'#html_theme_path = []'
nl|'\n'
nl|'\n'
comment|'# The name for this set of Sphinx documents.  If None, it defaults to'
nl|'\n'
comment|'# "<project> v<release> documentation".'
nl|'\n'
comment|'#html_title = None'
nl|'\n'
nl|'\n'
comment|'# A shorter title for the navigation bar.  Default is the same as html_title.'
nl|'\n'
comment|'#html_short_title = None'
nl|'\n'
nl|'\n'
comment|'# The name of an image file (relative to this directory) to place at the top'
nl|'\n'
comment|'# of the sidebar.'
nl|'\n'
comment|'#html_logo = None'
nl|'\n'
nl|'\n'
comment|'# The name of an image file (within the static path) to use as favicon of the'
nl|'\n'
comment|'# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32'
nl|'\n'
comment|'# pixels large.'
nl|'\n'
comment|'#html_favicon = None'
nl|'\n'
nl|'\n'
comment|'# Add any paths that contain custom static files (such as style sheets) here,'
nl|'\n'
comment|'# relative to this directory. They are copied after the builtin static files,'
nl|'\n'
comment|'# so a file named "default.css" will overwrite the builtin "default.css".'
nl|'\n'
DECL|variable|html_static_path
name|'html_static_path'
op|'='
op|'['
string|"'_static'"
op|']'
newline|'\n'
nl|'\n'
comment|"# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,"
nl|'\n'
comment|'# using the given strftime format.'
nl|'\n'
comment|"#html_last_updated_fmt = '%b %d, %Y'"
nl|'\n'
name|'git_cmd'
op|'='
string|'"git log --pretty=format:\'%ad, commit %h\' --date=local -n1"'
newline|'\n'
DECL|variable|html_last_updated_fmt
name|'html_last_updated_fmt'
op|'='
name|'os'
op|'.'
name|'popen'
op|'('
name|'git_cmd'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# If true, SmartyPants will be used to convert quotes and dashes to'
nl|'\n'
comment|'# typographically correct entities.'
nl|'\n'
comment|'#html_use_smartypants = True'
nl|'\n'
nl|'\n'
comment|'# Custom sidebar templates, maps document names to template names.'
nl|'\n'
comment|'#html_sidebars = {}'
nl|'\n'
nl|'\n'
comment|'# Additional templates that should be rendered to pages, maps page names to'
nl|'\n'
comment|'# template names.'
nl|'\n'
comment|'#html_additional_pages = {}'
nl|'\n'
nl|'\n'
comment|'# If false, no module index is generated.'
nl|'\n'
comment|'#html_use_modindex = True'
nl|'\n'
nl|'\n'
comment|'# If false, no index is generated.'
nl|'\n'
comment|'#html_use_index = True'
nl|'\n'
nl|'\n'
comment|'# If true, the index is split into individual pages for each letter.'
nl|'\n'
comment|'#html_split_index = False'
nl|'\n'
nl|'\n'
comment|'# If true, links to the reST sources are added to the pages.'
nl|'\n'
comment|'#html_show_sourcelink = True'
nl|'\n'
nl|'\n'
comment|'# If true, an OpenSearch description file will be output, and all pages will'
nl|'\n'
comment|'# contain a <link> tag referring to it.  The value of this option must be the'
nl|'\n'
comment|'# base URL from which the finished HTML is served.'
nl|'\n'
comment|"#html_use_opensearch = ''"
nl|'\n'
nl|'\n'
comment|'# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").'
nl|'\n'
comment|"#html_file_suffix = ''"
nl|'\n'
nl|'\n'
comment|'# Output file base name for HTML help builder.'
nl|'\n'
DECL|variable|htmlhelp_basename
name|'htmlhelp_basename'
op|'='
string|"'novadoc'"
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# -- Options for LaTeX output -------------------------------------------------'
nl|'\n'
nl|'\n'
comment|"# The paper size ('letter' or 'a4')."
nl|'\n'
comment|"#latex_paper_size = 'letter'"
nl|'\n'
nl|'\n'
comment|"# The font size ('10pt', '11pt' or '12pt')."
nl|'\n'
comment|"#latex_font_size = '10pt'"
nl|'\n'
nl|'\n'
comment|'# Grouping the document tree into LaTeX files. List of tuples'
nl|'\n'
comment|'# (source start file, target name, title, author, documentclass'
nl|'\n'
comment|'# [howto/manual]).'
nl|'\n'
DECL|variable|latex_documents
name|'latex_documents'
op|'='
op|'['
nl|'\n'
op|'('
string|"'index'"
op|','
string|"'Nova.tex'"
op|','
string|"u'Nova Documentation'"
op|','
nl|'\n'
string|"u'OpenStack Foundation'"
op|','
string|"'manual'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|'# The name of an image file (relative to this directory) to place at the top of'
nl|'\n'
comment|'# the title page.'
nl|'\n'
comment|'#latex_logo = None'
nl|'\n'
nl|'\n'
comment|'# For "manual" documents, if this is true, then toplevel headings are parts,'
nl|'\n'
comment|'# not chapters.'
nl|'\n'
comment|'#latex_use_parts = False'
nl|'\n'
nl|'\n'
comment|'# Additional stuff for the LaTeX preamble.'
nl|'\n'
comment|"#latex_preamble = ''"
nl|'\n'
nl|'\n'
comment|'# Documents to append as an appendix to all manuals.'
nl|'\n'
comment|'#latex_appendices = []'
nl|'\n'
nl|'\n'
comment|'# If false, no module index is generated.'
nl|'\n'
comment|'#latex_use_modindex = True'
nl|'\n'
endmarker|''
end_unit
