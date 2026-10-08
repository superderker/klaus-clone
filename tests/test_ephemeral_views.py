import os
import klaus
from dulwich.repo import Repo

def test_ephemeral_repo_tree_and_diff(ephemeral_repo):
    """
    Test that klaus correctly renders tree views, blobs, and commit diffs for an ephemeral repo.
    """
    app = klaus.make_app([ephemeral_repo], site_name="Test Site")
    client = app.test_client()

    repo_name = os.path.basename(ephemeral_repo.rstrip("/"))

    # Retrieve HEAD commit SHA from dulwich
    dulwich_repo = Repo(ephemeral_repo)
    head_sha = dulwich_repo.head().decode("utf-8")

    # 1. Index page
    res = client.get("/")
    assert res.status_code == 200
    assert repo_name.encode() in res.data

    # 2. Repository history / commit list
    res = client.get(f"/{repo_name}/", follow_redirects=True)
    assert res.status_code == 200

    # 3. Root tree view
    res = client.get(f"/{repo_name}/tree/{head_sha}/", follow_redirects=True)
    assert res.status_code == 200

    # 4. Commit view / diff
    res = client.get(f"/{repo_name}/commit/{head_sha}/", follow_redirects=True)
    assert res.status_code == 200

    # 5. File blob view
    res = client.get(f"/{repo_name}/blob/{head_sha}/README.md", follow_redirects=True)
    assert res.status_code == 200