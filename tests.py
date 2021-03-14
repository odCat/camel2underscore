#!python

#   Copyright 2021 Mihai Gătejescu
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import unittest

import camel2underscore as c2u


class TestCamel2Underscore(unittest.TestCase):

    def test_convert_camel_2_underscore(self):
        a_list = ['TestInput1', 'Test2Input', 'Test22Test',
                  'TestThisTest', '1NOTIs21']
        expected = ('test_input_1\ntest_2_input\ntest_22_test\n'
                    'test_this_test\n1_not_is_21')
        self.assertEqual(expected, c2u.convert_camel_2_underline(a_list))

    def test_first_character_is_underscore(self):
        self.assertTrue(c2u.first_char_is_underscore('_assert1'))
        self.assertFalse(c2u.first_char_is_underscore('assert2'))

    def test_last_character_is_underscore(self):
        self.assertTrue(c2u.last_char_is_underscore('assert1_'))
        self.assertFalse(c2u.last_char_is_underscore('assert2'))

    def test_remove_first_character(self):
        self.assertEqual('', c2u.remove_first_character(''))
        self.assertEqual('', c2u.remove_first_character('a'))
        self.assertEqual('bcd', c2u.remove_first_character('abcd'))

    def test_remove_last_character(self):
        self.assertEqual('', c2u.remove_last_character(''))
        self.assertEqual('', c2u.remove_last_character('a'))
        self.assertEqual('abc', c2u.remove_last_character('abcd'))

    def test_is_underscore_notation(self):
        self.assertTrue(c2u.is_underscore_notation('Is_Underscore'))
        # self.assertFalse(c2u.is_underscore_notation('_IsNotUnderscore_'))
        self.assertFalse(c2u.is_underscore_notation('IsNotUnderscore'))

    def test_read_input_from_file(self):
        expected = ['TestInput1', 'Test2Input', 'Test22Test',
                    'TestThisTest', '1NOTIs21']
        self.assertEqual(expected, c2u.read_input_from_file())

    def test_make_printable(self):
        expected = 'test'
        data = '__TeSt__'
        self.assertEqual(expected, c2u.remove_underscores_from_start_and_end(data))

    def test_text_to_code(self):
        expected = "'test1',\n'test2'\n"
        data = 'test1\ntest2\n'
        self.assertEqual(expected, c2u.convert_text_to_code(data))

    def test_list_to_text(self):
        data = ['value1', 'value2', 'value3']
        expected = 'value1\nvalue2\nvalue3\n'
        self.assertEqual(expected, c2u.list_to_text(data))

    def test_convert_code_to_text(self):
        data = "'value1',\n'value2',\n'value3'\n"
        expected = 'value1\nvalue2\nvalue3'
        self.assertEqual(expected, c2u.convert_code_to_text(data))


if __name__ == '__main__':
    unittest.main()

# TODO
# Improve is underscore test