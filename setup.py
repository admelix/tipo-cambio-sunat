import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='FactoringTotal',
    version='1.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/admelix/tipo-cambio-sunat',
    license='GNU General Public License v3.0',
    author='Jose Sakuda',
    author_email='sakudacastro@gmail.com',
    description='Toma el tipo de cambio del dia en sunat y, tambien, el tipo de cambio contable de SBS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pandas',
        'numpy',
        'lxml',
        'bs4',
        'requests'
    ],
    python_requires='>=3.6',
)