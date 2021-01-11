"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='Python Weather Project',
    version='1.0',
    description='A weather Python project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TestowanieAutomatyczneUG/projekt2-SzymonWilczewski',
    author='Szymon Wilczewski',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='weather, setuptools, development',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=['peppercorn'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={

    },
    data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'weather=weather:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/TestowanieAutomatyczneUG/projekt2-SzymonWilczewski',
    },
)
