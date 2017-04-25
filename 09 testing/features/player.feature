# Created by ma at 11.04.2017
Feature: Player

  Scenario: Creating Player

    Given a new player
    Then he should have hp
    And he should have name

    Given a new player
    Then he should have hp = 100