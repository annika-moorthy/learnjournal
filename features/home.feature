
Feature: homepage
  I want to test the functionality of the home page, which
  displays all of my resources. The tests creating a resource
  and deleting a resource


  Scenario: Creating a resource.
    Given we are on the home page
    When I add a new resource
    And I see "Name:"
    And I enter "test" in "box"

