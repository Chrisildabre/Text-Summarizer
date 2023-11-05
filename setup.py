import setuptools
with open("README.md", 'r', encoding='UTF-8') as f:
    long_description = f.read()

__version__ ="0.0.0"
REPO_Name = "Text-Summarizer"
AUTHOR_USER_NAME ="Chrisildabre"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL ="chrisildabre@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP APP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}",
    project_urls={
        "BUG Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
   
)