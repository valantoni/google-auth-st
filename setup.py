from setuptools import setup, find_packages

setup(
    name='google-auth-st',
    version='0.2',
    packages=find_packages(),
    description='Librería para añadir autenticación con Google en aplicaciones web con el framework de Streamlit.',
<<<<<<< HEAD
    long_description=open('README.md',encoding='utf-8').read(),
=======
    long_description=open('README.md', encoding = 'utf-8').read(),
>>>>>>> cb8faabe321a4660f3a03efe185566e4aedf6568
    long_description_content_type='text/markdown',  
    author='Toni Dev',
    author_email='classtonidev@gmail.com',
    url='https://github.com/valantoni/google-auth-st.git',
    install_requires=[
        'streamlit',
        'httpx_oauth',
        'PyJWT'
    ],
)
