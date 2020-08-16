
import os

os.system('conda install -y blas=*=blis')

from setuptools import setup

setup(
    name='pipcondablasblis',
    version='0.1'
    )
