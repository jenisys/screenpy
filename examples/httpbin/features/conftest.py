"""
Fixtures for API testing.
"""


import pytest
from screenpy import AnActor
from screenpy.abilities import MakeAPIRequests


@pytest.fixture
def Perry():
    """An actor who can make API requests."""
    the_actor = AnActor.named("Perry").who_can(MakeAPIRequests())
    yield the_actor
