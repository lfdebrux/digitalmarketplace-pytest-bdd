@buyer @requirements
Feature: Create and publish a requirement for a Digital specialist
  In order to find individuals and teams that can provide the needed services
  As a buyer within government
  I want to be able to create and publish a requirement

  Background:
    Given a live Digital Outcomes and Specialists 3 framework
    And a buyer user named Zaphod

  Scenario: Start looking for an individual specialist
    Given I am logged in as Zaphod
    When I create a digital specialists requirement for a 'Brain Specialist'
    Then I have a draft requirement

  Scenario: Write a requirement for an individual specialist
    Given I am logged in as Zaphod
    And I have a digital specialists requirement for a 'Brain specialist'
    When I write my requirements
    And I write the description of work
    And I set how I'll evaluate suppliers
    Then I can publish my requirement

  Scenario: Publish a requirement for an individual specialist
    Given I am logged in as Zaphod
    And I have a digital specialists requirement for a 'Brain specialist'
    When I publish my requirement
    Then I can see my requirement in the list of opportunities for the framework
    And I cannot edit my requirement
