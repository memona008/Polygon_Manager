from distutils.core import setup
setup(
  name = 'polygon_manager',
  packages = ['polygon_manager'],
  version = '0.1.4',
  license='MIT',
  description = 'It helps in drawing polygon on video frame and save it in pkl file and provide you with multiple utilities functions of polygon',
  author = 'MemonaS',
  author_email = 'memonasultan54@gmail.com',
  url = 'https://github.com/memona008/Polygon_Manager',
  download_url = 'https://github.com/memona008/Polygon_Manager/archive/refs/tags/v0.1.4.tar.gz',
  keywords = ['polygon', 'video', 'draw polygon', 'box', 'parallelogram', 'image', 'manager', 'capture','points'],
  install_requires=[
          'numpy',
          'opencv-python',
          'shapely'
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
