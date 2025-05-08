import os

def test_env_check():
    print("GITHUB_ACTIONS =", os.getenv("GITHUB_ACTIONS"))
    print("MORPHEUS_HOST =", os.getenv("MORPHEUS_HOST"))
    assert os.getenv("MORPHEUS_HOST") is not None
