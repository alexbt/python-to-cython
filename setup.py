from setuptools import setup
from Cython.Build import cythonize

setup(
    name='python to cython',
    version='1.0',
    ext_modules=cythonize(["abt/**/*.py"],
                          compiler_directives={'always_allow_keywords': True},
                          language_level="3"),
)