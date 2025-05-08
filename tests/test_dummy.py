import os

def test_env_check():
    print("GITHUB_ACTIONS =", os.getenv("GITHUB_ACTIONS"))
