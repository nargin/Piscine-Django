from elem import Elem, Text
from elements import *

class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise TypeError("Page constructor argument must be an Elem instance")
        self.elem = elem

    def is_valid(self):
        return self._validate_node(self.elem)

    def _validate_node(self, node):
        # Check if node is Text
        if isinstance(node, Text):
            return True

        # Check if node type is valid
        valid_types = {'html', 'head', 'body', 'title', 'meta', 'img', 'table', 
                      'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 
                      'div', 'span', 'hr', 'br'}
        
        if not isinstance(node, (Html, Head, Body, Title, Meta, Img, Table,
                               Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span,
                               Hr, Br, Text)):
            return False

        # Handle empty content
        if node.content is None:
            return True

        # Convert single content to list for uniform handling
        children = node.content if isinstance(node.content, list) else [node.content]
        
        # Specific validation rules for each element type
        if isinstance(node, Html):
            if len(children) != 2 or not isinstance(children[0], Head) or not isinstance(children[1], Body):
                return False

        elif isinstance(node, Head):
            if len(children) != 1 or not isinstance(children[0], Title):
                return False

        elif isinstance(node, (Body, Div)):
            for child in children:
                if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text, P)):
                    return False

        elif isinstance(node, (Title, H1, H2, Li, Th, Td)):
            if len(children) != 1 or not isinstance(children[0], Text):
                return False

        elif isinstance(node, P):
            for child in children:
                if not isinstance(child, Text):
                    return False

        elif isinstance(node, Span):
            for child in children:
                if not isinstance(child, (Text, P)):
                    return False

        elif isinstance(node, (Ul, Ol)):
            if len(children) < 1:
                return False
            for child in children:
                if not isinstance(child, Li):
                    return False

        elif isinstance(node, Tr):
            if len(children) < 1:
                return False
            has_th = False
            has_td = False
            for child in children:
                if isinstance(child, Th):
                    has_th = True
                elif isinstance(child, Td):
                    has_td = True
                else:
                    return False
            if has_th and has_td:  # Th and Td must be mutually exclusive
                return False

        elif isinstance(node, Table):
            for child in children:
                if not isinstance(child, Tr):
                    return False

        # Recursively validate all children
        for child in children:
            if not self._validate_node(child):
                return False

        return True

    def __str__(self):
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>\n" + self.elem.__str__()
        return self.elem.__str__()

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))
