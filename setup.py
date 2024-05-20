from setuptools import setup

setup(
    name='google-auth-st',
    version='1.3',
    packages= ['google_auth_st'],
    description='Librería para añadir autenticación con Google en aplicaciones web con el framework de Streamlit.',
    long_description=open('README.md',encoding='utf-8').read(),
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
