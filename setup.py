from setuptools import setup, find_packages

setup(
    name='google_auth_st',
    version='0.1',
    packages=find_packages(),
    description='Librería para añadir autenticación con Google en aplicaciones web con el framework de Streamlit.',
    long_description=open('README.md').read(),
    author='Toni Dev',
    author_email='classtonidev@gmail.com',
    url='URL del repositorio de tu proyecto',
    install_requires=[
        'streamlit',
        'httpx_oauth',
        'PyJWT'
    ],
)