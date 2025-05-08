import os

def test_env_behavior():
    github_actions_flag = os.environ.get("GITHUB_ACTIONS", "false").lower()
    loaded_env = os.environ.get("MORPHEUS_USER", None)

    print(f"GITHUB_ACTIONS: {github_actions_flag}")
    print(f"MORPHEUS_USER (should be None in Actions): {loaded_env}")

    assert github_actions_flag == "true"
    assert loaded_env is None  # It should NOT load from .env in GitHub Actions
