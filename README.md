# mkdocs-responsive-image

A MkDocs plugin for automatically resizing images.

**WIP Plugin**

Status -

```
        # load settings             - 50%	- might need to tweak
        # find strings              - 100%
        # extract args              - 100%
        # read image				- 0%
        # feed image into resizer	- 0%
        # generate html				- 0%
```


## Quick start

If you want to try this plugin as-it-is, follow these steps:

1. Download this repo and (eventually) unzip it in a folder

2. Inside the project folder, execute the command 
   `python setup.py develop` to install 
   the plugin on your local machine. 

3. Go to your mkdocs project folder, edit the `mkdocs.yml` file 
   and add these few lines at the end:

   ```yaml
   plugins:
       - responsive-image
   ```
   
## Configuration

```
plugins:
	- responsive-image:
		# Set to 95 internal
        default_quality: 90
		
        widths: 320, 640, 768, 1024, 1366, 1600, 1920, 3840
        
        # The base directory where assets are stored. This is used to determine the
        # `dirname` value in `output_path_format` below.
        base_path: assets
        
        # [Optional, Default: assets/resized/%{filename}-%{width}x%{height}.%{extension}]
        # The template used when generating filenames for resized images. Must be a
        # relative path.
        #
        # Parameters available are:
        #   %{dirname}     Directory of the file relative to `base_path` (assets/sub/dir/some-file.jpg => sub/dir)
        #   %{basename}    Basename of the file (assets/some-file.jpg => some-file.jpg)
        #   %{filename}    Basename without the extension (assets/some-file.jpg => some-file)
        #   %{extension}   Extension of the file (assets/some-file.jpg => jpg)
        #   %{width}       Width of the resized image
        #   %{height}      Height of the resized image
        #
        output_path_format: assets/resized/%{width}/%{dirname}/%{basename}
```

## Usage

```
{% responsive_image path: "assets/image.jpg" alt: "Lorem ipsum..." title: "Lorem ipsum..." %}
```