import setuptools

# 1. Fonction pour lire les requirements
def get_requirements(file_path: str) -> list[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e .")]
    return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-To-End-MLOPS-Project"
AUTHOR_USER_NAME = "meriem-amrane"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "meriem.amrane07@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"), # <--- N'oubliez pas la virgule ici !
    install_requires=get_requirements("requirements.txt") # <--- Maintenant ça fonctionnera
)