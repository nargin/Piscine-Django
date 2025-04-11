#!/usr/bin/python3
import html


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        # Use html.escape to safely handle special characters in text content
        return html.escape(super().__str__()).replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    ValidationError = Exception

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = []
        self.tag_type = tag_type
        self.depth = 0
        self.indentation: str = '  '
        if content:
            self.add_content(content)

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        indent = self.indentation * self.depth
        if self.tag_type == 'double':
            result = indent + f"<{self.tag}{self.__make_attr()}>"
            content_str = self.__make_content()
            if content_str:
                result += '\n' + content_str
            result += '\n' + indent + f"</{self.tag}>"
        elif self.tag_type == 'simple':
            result = indent + f"<{self.tag}{self.__make_attr()} />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if not self.content:
            return ''

        result_parts = []
        child_indent = self.indentation * (self.depth + 1)
        for elem in self.content:
            if isinstance(elem, Text):
                result_parts.append(child_indent + str(elem))
            elif isinstance(elem, Elem):
                result_parts.append(elem.__str__())

        return '\n'.join(result_parts)

    def _update_depth(self, new_depth):
        """Recursively update the depth of this element and its children."""
        self.depth = new_depth
        for item in self.content:
            if isinstance(item, Elem):
                # Recursively call for child Elem instances
                item._update_depth(new_depth + 1)

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        
        contents_to_add = []
        if type(content) == list:
            contents_to_add = content
        else:
            contents_to_add = [content]

        for item in contents_to_add:
            if isinstance(item, Text) and not str(item).strip():
                continue
            if isinstance(item, Elem):
                # Set depth relative to parent AND update descendants recursively
                item._update_depth(self.depth + 1)
            self.content.append(item)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    html = Elem(tag='html', content=[
        Elem(tag='head', content=[
            Elem(tag='title', content=Text('Hello Ground!'))
        ]),
        Elem(tag='body', content=[
            Elem(tag='h1', content=Text('Oh no, not again!')),
            Elem(tag='div', content=[
                Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple'),
            ])
        ])
    ])
    # print(html)
    print(Elem())
    print(Text(''))
    print(Text('foo'))
    print(Text('\n'))
    print(Text('foo\nbar'))
    print(Text('<'))
    print(Text('>'))
    print(Text('"'))
    
