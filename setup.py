from setuptools import setup, find_packages


setup(
    name='responsive-image',
    version='0.0.1',
    description='A MkDocs plugin for automatically resizing images.',
    long_description='',
    keywords='mkdocs',
    url='',
    author='jackjt8',
    author_email='n/a',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    
    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'responsive-image = responsive_image.responsiveimage:ResponsiveImage'
        ]
    }
)
