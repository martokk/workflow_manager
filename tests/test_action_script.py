from workflow_manager.action_script import ActionScript


class TestActionScript(ActionScript):
    def script(self, **kwargs: object) -> str:
        return f"working {kwargs=}"


def test_script() -> None:
    assert TestActionScript().script() == "working kwargs={}"


def test_run() -> None:
    assert TestActionScript().run() == "working kwargs={}"


def test_script_with_args() -> None:
    assert (
        TestActionScript().script(
            foo="bar",
        )
        == "working kwargs={'foo': 'bar'}"
    )


def test_run_with_args() -> None:
    assert (
        TestActionScript().run(
            foo="bar",
        )
        == "working kwargs={'foo': 'bar'}"
    )
