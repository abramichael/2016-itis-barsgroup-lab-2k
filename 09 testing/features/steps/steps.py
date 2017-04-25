from behave import given, then

from player import Player


@given(u'a new player')
def step_impl(context):
    context.player = Player()


@then(u'he should have hp')
def step_impl(context):
    assert hasattr(context.player, "hp")


@then(u'he should have name')
def step_impl(context):
    assert hasattr(context.player, "name")

@then(u'he should have hp = 100')
def step_impl(context):
    assert context.player.hp == 100