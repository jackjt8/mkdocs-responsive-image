import re
from mkdocs.plugins import BasePlugin


class ResponsiveImage(BasePlugin):

    def on_page_markdown(self, markdown, **kwargs):

        # Now we'll search on the text each occurrence
        # of the tag {{dolly}} and we'll replace it with some
        # random lyrics.
        # This class method (on_page_markdown) will be called each
        # time mkdocs needs to start processing a page before
        # rendering it in HTML.

        # For sake of simplicity, we won't use regular
        # expressions in this example to search and replace text.

        # markdown = markdown.replace("{{dolly}}", random_lyrics())
        
        # for matchedtext in re.findall(r'^.*\{%*.%\}.*$', markdown):
            # markdown = markdown.replace(matchedtext, "REPLACED")

        # However if you prefer to use regex, please comment the
        # previous line of code and uncomment the following ones:

        # markdown = re.sub(r"\{\{(\s)*dolly(\s)*\}\}",
        #                   random_lyrics(),
        #                   markdown,
        #                   flags=re.IGNORECASE)
        #pattern = re.compile(r"\{\{(\s)*dolly(\s)*\}\}")
        pattern = re.compile(r"\{\% responsive_image.*.\%\}")
        for m in re.finditer(pattern, markdown):
            s = m.start()
            e = m.end()
            print( "###" )
            print( 'String match "%s" at %d:%d' % (markdown[s:e], s, e ) )
            markdown = markdown.replace(markdown[s:e], "REPLACED")
            print( "###" )

        return markdown
