from setuptools import setup, find_packages

setup(
    name="mcqgen",
    version="0.0.1",
    author='venu lucky',
    author_email='venulucky951@gmail.com',
    packages=find_packages(),
    install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
)
