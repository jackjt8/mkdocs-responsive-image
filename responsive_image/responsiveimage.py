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
        
        print( "Default Quality: %s" % (self.default_quality) )
        print( "Widths: %s" % (self.widths) )
        print( "Base_path: %s" % (self.base_path) )
        print( "Output_path_format: %s" % (self.output_path_format) )
        
    
    def on_page_markdown(self, markdown, **kwargs):
        temp_responsive_tag = ""

        pattern = re.compile(r"\{\% responsive_image.*.\%\}")
        for m in re.finditer(pattern, markdown):
            s = m.start()
            e = m.end()
            print( "###" )
            print( 'Responsive Image tag match "%s" at %d:%d' % (markdown[s:e], s, e ) )
            # extract tag
            temp_responsive_tag = markdown[s:e]
            # blank path/alttext/title
            temp_image_path = ""
            temp_image_alttext = ""
            temp_image_title = ""
            ### markdown = markdown.replace(markdown[s:e], "REPLACED")
            # extract args
            temp_image_path, temp_image_alttext, temp_image_title = self.extract_tag_args(temp_responsive_tag)
            print( "return_block" )
            print(temp_image_path)
            print(temp_image_alttext)
            print(temp_image_title)
            print( "###" )
            
        # load settings             - 50%
        # find strings              - 100%
        # extract args              - 100%
        # read image
        # feed image into resizer
        # generate new string

        return markdown
        
    def extract_tag_args(self, responsive_tag):
        image_path = ""
        image_alttext = ""
        image_title = ""
         
        # get path
        image_path = self.do_regex(r"path: \"(.*?)\"", responsive_tag)

        # # get alt text
        image_alttext = self.do_regex(r"alt: \"(.*?)\"", responsive_tag)
        
        # # get title
        image_title = self.do_regex(r"title: \"(.*?)\"", responsive_tag)
        
        return image_path, image_alttext, image_title
            
    def do_regex(self, pattern_str, body):
        pattern = re.compile(pattern_str)
        result = re.search(pattern, body)
        
        if result:
            print ( "Return of do_regex for patten \"%s\" is \"%s\"" % (pattern_str, result.group(1)) )
            return result.group(1)
        else:
            #no result
            return ""
   


# END OF FILE
