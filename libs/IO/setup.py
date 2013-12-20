from distutils.core import setup, Extension

cIO = Extension('cIO', sources=['module.m','Installer.m', 'ImageSequence.m', 'AnimatedGif.m', 'Video.m'], extra_link_args=['-framework', 'AppKit', '-framework', 'Foundation', '-framework', 'Security', '-framework', 'AVFoundation', '-framework', 'CoreMedia', '-framework', 'CoreVideo'])
setup (name = "IO",
       version = "1.0",
       author = "Christian Swinehart",
       description = "Image and video export routines.",
       ext_modules = [cIO])