from elem import Elem, Text
from elements import *
from Page import Page
import unittest
import re
import os
class TestPage(unittest.TestCase):
    def test_valid_simple_html(self):
        html = Html([Head(Title(Text("Hello"))), Body(H1(Text("Title")))])
        page = Page(html)
        self.assertTrue(page.is_valid())

    def test_invalid_html_structure(self):
        html = Html(Head(Title(Text("Hello"))))
        page = Page(html)
        self.assertFalse(page.is_valid())

    def test_invalid_head_content(self):
        html = Html([Head([Title(Text("Hello")), H1(Text("Extra"))]), Body()])
        page = Page(html)
        self.assertFalse(page.is_valid())

    def test_valid_complex_structure(self):
        table = Table([
            Tr([Th(Text("Header 1")), Th(Text("Header 2"))]),
            Tr([Td(Text("Data 1")), Td(Text("Data 2"))])
        ])
        div = Div([
            H1(Text("Title")),
            table,
            Ul([
                Li(Text("Item 1")),
                Li(Text("Item 2"))
            ])
        ])
        html = Html([
            Head(Title(Text("Test Page"))),
            Body(div)
        ])
        page = Page(html)
        self.assertTrue(page.is_valid())

    def test_invalid_mixed_tr_content(self):
        table = Table(Tr([Th(Text("Header")), Td(Text("Data"))]))
        html = Html([Head(Title(Text("Test"))), Body(table)])
        page = Page(html)
        self.assertFalse(page.is_valid())

    def test_invalid_list_content(self):
        ul = Ul([Li(Text("Valid")), Text("Invalid")])
        html = Html([Head(Title(Text("Test"))), Body(ul)])
        page = Page(html)
        self.assertFalse(page.is_valid())

    def test_valid_span_content(self):
        span = Span([Text("Text"), P(Text("Paragraph"))])
        html = Html([Head(Title(Text("Test"))), Body(span)])
        page = Page(html)
        self.assertTrue(page.is_valid())

    def test_doctype_output(self):
        html = Html([Head(Title(Text("Test"))), Body(H1(Text("Title")))])
        page = Page(html)
        self.assertTrue(str(page).startswith("<!DOCTYPE html>"))

        div = Div(Text("Content"))
        page = Page(div)
        self.assertFalse(str(page).startswith("<!DOCTYPE html>"))

    def test_write_to_file(self):
        html = Html([Head(Title(Text("Test"))), Body(H1(Text("Title")))])
        page = Page(html)
        page.write_to_file("test_output.html")
        
        with open("test_output.html", "r") as f:
            content = f.read()
            # Remove whitespace and newlines for comparison
            content = re.sub(r'\s+', '', content)
            self.assertIn("<title>Test</title>", content)

if __name__ == '__main__':
    unittest.main(verbosity=2)