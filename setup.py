from setuptools import setup, find_packages

# Load dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="iai_chat",
    version="0.1.0",
    description="A chat application with FastAPI backend and Streamlit frontend",
    author="Laurin Lötscher",
    author_email="laurin.loetscher@stud.hslu.ch",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.10.6",
    entry_points={
        "console_scripts": [
            "iai-chat-server=backend.chat_server:app",
            "iai-chat-client=frontend.chat_client:main",
        ],
    },
    test_suite="pytest",
    tests_require=["pytest", "pytest-asyncio"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
