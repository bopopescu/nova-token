begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration. '
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2010 Anso Labs, LLC'
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
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
nl|'\n'
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
name|'import'
name|'objectstore'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|oss_tempdir
name|'oss_tempdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'prefix'
op|'='
string|"'test_oss-'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|"# delete tempdirs from previous runs (we don't delete after test to allow"
nl|'\n'
comment|'# checking the contents after running tests)'
nl|'\n'
name|'for'
name|'path'
name|'in'
name|'glob'
op|'.'
name|'glob'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'oss_tempdir'
op|','
string|"'../test_oss-*'"
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'path'
op|'!='
name|'oss_tempdir'
op|':'
newline|'\n'
indent|'        '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# create bucket/images path'
nl|'\n'
dedent|''
dedent|''
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'oss_tempdir'
op|','
string|"'images'"
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'oss_tempdir'
op|','
string|"'buckets'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|ObjectStoreTestCase
name|'class'
name|'ObjectStoreTestCase'
op|'('
name|'test'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ObjectStoreTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'fake_users'
op|'='
name|'True'
op|','
nl|'\n'
name|'buckets_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'oss_tempdir'
op|','
string|"'buckets'"
op|')'
op|','
nl|'\n'
name|'images_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'oss_tempdir'
op|','
string|"'images'"
op|')'
op|','
nl|'\n'
name|'ca_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'CA'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'um'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'user1'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'user2'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'admin_user'"
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'um'
op|'.'
name|'create_project'
op|'('
string|"'proj1'"
op|','
string|"'user1'"
op|','
string|"'a proj'"
op|','
op|'['
string|"'user1'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'um'
op|'.'
name|'create_project'
op|'('
string|"'proj2'"
op|','
string|"'user2'"
op|','
string|"'a proj'"
op|','
op|'['
string|"'user2'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
DECL|class|Context
name|'class'
name|'Context'
op|'('
name|'object'
op|')'
op|':'
name|'pass'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'Context'
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
name|'self'
op|'.'
name|'um'
op|'.'
name|'delete_project'
op|'('
string|"'proj1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'um'
op|'.'
name|'delete_project'
op|'('
string|"'proj2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'user1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'user2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'admin_user'"
op|')'
newline|'\n'
name|'super'
op|'('
name|'ObjectStoreTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_buckets
dedent|''
name|'def'
name|'test_buckets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_user'
op|'('
string|"'user1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_project'
op|'('
string|"'proj1'"
op|')'
newline|'\n'
name|'objectstore'
op|'.'
name|'bucket'
op|'.'
name|'Bucket'
op|'.'
name|'create'
op|'('
string|"'new_bucket'"
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bucket'
op|'='
name|'objectstore'
op|'.'
name|'bucket'
op|'.'
name|'Bucket'
op|'('
string|"'new_bucket'"
op|')'
newline|'\n'
nl|'\n'
comment|'# creator is authorized to use bucket'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'bucket'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# another user is not authorized'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_user'
op|'('
string|"'user2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_project'
op|'('
string|"'proj2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'bucket'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'=='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# admin is authorized to use bucket'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_user'
op|'('
string|"'admin_user'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'bucket'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# new buckets are empty'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'bucket'
op|'.'
name|'list_keys'
op|'('
op|')'
op|'['
string|"'Contents'"
op|']'
op|'=='
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# storing keys works'
nl|'\n'
name|'bucket'
op|'['
string|"'foo'"
op|']'
op|'='
string|'"bar"'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'len'
op|'('
name|'bucket'
op|'.'
name|'list_keys'
op|'('
op|')'
op|'['
string|"'Contents'"
op|']'
op|')'
op|'=='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'bucket'
op|'['
string|"'foo'"
op|']'
op|'.'
name|'read'
op|'('
op|')'
op|'=='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
comment|'# md5 of key works'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'bucket'
op|'['
string|"'foo'"
op|']'
op|'.'
name|'md5'
op|'=='
name|'hashlib'
op|'.'
name|'md5'
op|'('
string|"'bar'"
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# deleting non-empty bucket throws exception'
nl|'\n'
name|'exception'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'bucket'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'exception'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'exception'
op|')'
newline|'\n'
nl|'\n'
comment|'# deleting key'
nl|'\n'
name|'del'
name|'bucket'
op|'['
string|"'foo'"
op|']'
newline|'\n'
nl|'\n'
comment|'# deleting empty button'
nl|'\n'
name|'bucket'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# accessing deleted bucket throws exception'
nl|'\n'
name|'exception'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'objectstore'
op|'.'
name|'bucket'
op|'.'
name|'Bucket'
op|'('
string|"'new_bucket'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'exception'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'exception'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_images
dedent|''
name|'def'
name|'test_images'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_user'
op|'('
string|"'user1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_project'
op|'('
string|"'proj1'"
op|')'
newline|'\n'
nl|'\n'
comment|'# create a bucket for our bundle'
nl|'\n'
name|'objectstore'
op|'.'
name|'bucket'
op|'.'
name|'Bucket'
op|'.'
name|'create'
op|'('
string|"'image_bucket'"
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bucket'
op|'='
name|'objectstore'
op|'.'
name|'bucket'
op|'.'
name|'Bucket'
op|'('
string|"'image_bucket'"
op|')'
newline|'\n'
nl|'\n'
comment|'# upload an image manifest/parts'
nl|'\n'
name|'bundle_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'bundle'"
op|')'
newline|'\n'
name|'for'
name|'path'
name|'in'
name|'glob'
op|'.'
name|'glob'
op|'('
name|'bundle_path'
op|'+'
string|"'/*'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bucket'
op|'['
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'path'
op|')'
op|']'
op|'='
name|'open'
op|'('
name|'path'
op|','
string|"'rb'"
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# register an image'
nl|'\n'
dedent|''
name|'objectstore'
op|'.'
name|'image'
op|'.'
name|'Image'
op|'.'
name|'create'
op|'('
string|"'i-testing'"
op|','
string|"'image_bucket/1mb.manifest.xml'"
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
comment|'# verify image'
nl|'\n'
name|'my_img'
op|'='
name|'objectstore'
op|'.'
name|'image'
op|'.'
name|'Image'
op|'('
string|"'i-testing'"
op|')'
newline|'\n'
name|'result_image_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'my_img'
op|'.'
name|'path'
op|','
string|"'image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'os'
op|'.'
name|'stat'
op|'('
name|'result_image_file'
op|')'
op|'.'
name|'st_size'
op|','
number|'1048576'
op|')'
newline|'\n'
nl|'\n'
name|'sha'
op|'='
name|'hashlib'
op|'.'
name|'sha1'
op|'('
name|'open'
op|'('
name|'result_image_file'
op|')'
op|'.'
name|'read'
op|'('
op|')'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sha'
op|','
string|"'3b71f43ff30f4b15b5cd85dd9e95ebc7e84eb5a3'"
op|')'
newline|'\n'
nl|'\n'
comment|'# verify image permissions'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_user'
op|'('
string|"'user2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'um'
op|'.'
name|'get_project'
op|'('
string|"'proj2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'my_img'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'=='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# class ApiObjectStoreTestCase(test.BaseTestCase):'
nl|'\n'
comment|'#     def setUp(self):'
nl|'\n'
comment|'#         super(ApiObjectStoreTestCase, self).setUp()'
nl|'\n'
comment|'#         FLAGS.fake_users   = True'
nl|'\n'
comment|"#         FLAGS.buckets_path = os.path.join(tempdir, 'buckets')"
nl|'\n'
comment|"#         FLAGS.images_path  = os.path.join(tempdir, 'images')"
nl|'\n'
comment|"#         FLAGS.ca_path = os.path.join(os.path.dirname(__file__), 'CA')"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         self.users = users.UserManager.instance()'
nl|'\n'
comment|'#         self.app  = handler.Application(self.users)'
nl|'\n'
comment|'#'
nl|'\n'
comment|"#         self.host = '127.0.0.1'"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         self.conn = boto.s3.connection.S3Connection('
nl|'\n'
comment|'#             aws_access_key_id=user.access,'
nl|'\n'
comment|'#             aws_secret_access_key=user.secret,'
nl|'\n'
comment|'#             is_secure=False,'
nl|'\n'
comment|'#             calling_format=boto.s3.connection.OrdinaryCallingFormat(),'
nl|'\n'
comment|'#             port=FLAGS.s3_port,'
nl|'\n'
comment|'#             host=FLAGS.s3_host)'
nl|'\n'
comment|'#'
nl|'\n'
comment|"#         self.mox.StubOutWithMock(self.ec2, 'new_http_connection')"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     def tearDown(self):'
nl|'\n'
comment|'#         FLAGS.Reset()'
nl|'\n'
comment|'#         super(ApiObjectStoreTestCase, self).tearDown()'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     def test_describe_instances(self):'
nl|'\n'
comment|'#         self.expect_http()'
nl|'\n'
comment|'#         self.mox.ReplayAll()'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         self.assertEqual(self.ec2.get_all_instances(), [])'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
