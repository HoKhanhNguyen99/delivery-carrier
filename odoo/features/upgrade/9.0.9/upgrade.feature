# -*- coding: utf-8 -*-
@upgrade_from_9.0.8
Feature: upgrade to 9.0.9

  Scenario: upgrade
    Given I update the module list
    Given I install the required modules with dependencies:
      | name                                          |
      | specific_account                              |              
      | specific_reports                              |
      | specific_partner                              |
      | project_timesheet                             |
      | specific_timesheet_activities                 |
      | specific_stock                                |
      | specific_timesheet                            |
    Then my modules should have been installed and models reloaded
    
  @transit_location
  Scenario: Configure dedicated transit location for supplier in China
    Given I find an "stock.location" with oid: scenario.location_transit_cn
    And having:
      | key     | value                             |
      | name    | Swisslux AG: Departure from China |      

  @push_rules
  Scenario: Add a global push rule to receive goods from transit location
    Given I find an "stock.location.path" with oid: scenario.location_path_transit_to_slx
    And having:
      | key     | value |
      | delay   | 0     |
  
  @procurement_rule
  Scenario: Configure the propagation of procurement order on "buy" rule
    Given I find an "procurement.rule" with name: Swisslux AG:  Buy
    And having:
      | key                         | value     |
      | propagate                   | True      |
      | group_propagation_option    | propagate |

  @journal
  Scenario Outline: create new financial journal
    Given I need a "account.journal" with oid: <journal_oid>
    And having:
      | key                         | value                     |
      | name                        | <journal_name>            |
      | code                        | <journal_code>            |
      | type                        | <journal_type>            |
      | company_id                  | by oid: base.main_company |
      | currency_id                 | <currency>                |
      | update_posted               | True                      |
      | show_on_dashboard           | True                      |
      | default_debit_account_id    | <acc_code>                |
      | default_credit_account_id   | <acc_code>                |      

    Examples: Financial Journals
      | journal_oid             | journal_name  | journal_code  | journal_type  | currency          | acc_code      |
      | scenario.vendor_usd     | Vendor USD    | VUSD          | purchase      | by oid: base.USD  | false         |
      | scenario.vendor_eur     | Vendor EUR    | VEUR          | purchase      | by oid: base.EUR  | false         |
      | scenario.afex           | AFEX          | AFEX          | bank          | false             | by code: 1024 |
  
    
    Then I set the version of the instance to "9.0.9"
