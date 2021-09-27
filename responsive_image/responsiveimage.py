import re
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class ResponsiveImage(BasePlugin):

    config_scheme = (
        ('default_quality', config_options.Type(int, default=95)),
        ('widths', config_options.Type(list, default=[320, 540, 960])),
        ('base_path', config_options.Type(str, default="assets")),
        ('output_path_format', config_options.Type(str, default="assets/resized/%{filename}-%{width}x%{height}.%{extension}")),
    )

    # Config
    default_quality = 0
    widths = []
    base_path = ""
    output_path_format = ""
    
    def on_config(self, config):
        self.default_quality = self.config.get("default_quality")
        self.widths = self.config.get("widths")
        self.base_path = self.config.get("base_path")
        self.output_path_format = self.config.get("output_path_format")
        
        # print(self.default_quality)
        # print(self.widths)
        # print(self.widths[0])
        # print(self.base_path)
        # print(self.output_path_format)
        
    
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
            
        # load settings             - 50%
        # find strings              - 100%
        # extract args
        # feed image into resizer
        # generate new string

        return markdown
