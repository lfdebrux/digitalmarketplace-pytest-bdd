from pytest_bdd import given, then, when, scenarios
from pytest_bdd.parsers import parse


scenarios(
    "features/digital-outcomes-and-specialists/find-an-individual-specialist.feature"
)


@given(parse("I have a {lot_name} requirement for a '{title}'"))
def requirement(lot_name, title):
    return {"title": title}


@when(parse("I create a {lot_name} requirement for a '{title}'"))
def create_requirement(lot_name, title):
    print(f"creating requirement '{title}' in the '{lot_name}' lot")
    pass


@when("I publish my requirement")
def publish_requirement(requirement):
    print(f"publishing requirement '{requirement['title']}'")
    pass


@when("I write my requirements")
def fill_in_requirement(requirement):
    pass


@when("I write the description of work")
def fill_in_description_of_work(requirement):
    pass


@when("I set how I'll evaluate suppliers")
def fill_in_shortlist_and_evaluation_process(requirement):
    pass


@then("I have a draft requirement")
def should_have_draft_requirement(requirement):
    pass


@then("I can publish my requirement")
def should_be_able_to_publish_requirement(requirement):
    pass


@then("I can see my requirement in the list of opportunities for the framework")
def should_have_requirement_in_published_opportunities(requirement):
    pass


@then("I cannot edit my requirement")
def should_not_be_able_to_edit_requirement(requirement):
    pass
