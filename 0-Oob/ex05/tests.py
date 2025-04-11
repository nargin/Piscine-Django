from elements import *

def tester():
    # Meta information
    meta_charset = Meta(attr={"charset": "UTF-8"})
    meta_viewport = Meta(attr={"name": "viewport", "content": "width=device-width, initial-scale=1.0"})
    page_title = Title(content=Text("Testing All HTML Elements"))
    head = Head(content=[meta_charset, meta_viewport, page_title])

    # Main content sections
    main_heading = H1(content=Text("Welcome to the HTML Elements Test Page"))
    
    # Navigation section with lists
    nav_heading = H2(content=Text("Navigation Example"))
    unordered_list = Ul(content=[
        Li(content=Text("Unordered List Item 1")),
        Li(content=Text("Unordered List Item 2"))
    ])
    ordered_list = Ol(content=[
        Li(content=Text("Ordered List Item 1")),
        Li(content=Text("Ordered List Item 2"))
    ])
    
    # Table section
    table_heading = H2(content=Text("Table Example"))
    table = Table(content=[
        Tr(content=[
            Th(content=Text("Header 1")),
            Th(content=Text("Header 2"))
        ]),
        Tr(content=[
            Td(content=Text("Data 1")),
            Td(content=Text("Data 2"))
        ])
    ])
    
    # Content section with various elements
    content_div = Div(attr={"class": "content-section"}, content=[
        P(content=Text("This is a paragraph with a ")),
        Span(content=Text("span element")),
        P(content=Text("inside it.")),
        Hr(),
        Img(attr={"src": "example.png", "alt": "Example Image"}),
        Br()
    ])
    
    # Combine all body elements
    body = Body(content=[
        main_heading,
        nav_heading,
        unordered_list,
        ordered_list,
        table_heading,
        table,
        content_div
    ])
    
    # Create the complete HTML document
    html = Html(content=[head, body])
    
    # Write the output to a file
    with open('test_output.html', 'w') as f:
        f.write(str(html))
    
    print("HTML file has been generated as 'test_output.html'")
    print("\nHTML Content:")
    print(html)

if __name__ == "__main__":
    tester()