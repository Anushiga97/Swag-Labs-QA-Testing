# Swag Labs QA Testing

This repository contains comprehensive QA testing documentation for the Swag Labs e-commerce website. As part of my role as a QA tester, I have included detailed test case documentation, execution results, bug reports, an automated test script along with instructions to run it, and a summary report.

## Project Description

**Project Name:** Swag Labs QA Testing

**Description:** Detailed manual and automated test cases for the Swag Labs e-commerce website, including test case documentation, execution results, bug reports, and a summary report.

## Scope of Testing

- Functional Testing
- Usability Testing
- Performance Testing
- Automated Testing

## Tools and Methods

- Test cases were written and executed using standard QA practices.
- Automated tests were scripted using - Selenium Web driver.
- Bug tracking and reporting were done using - Jira and Bugzilla.

## Significant Findings

- Summarize any critical bugs or issues found-
  
 1.Navigation functionality issues - (Bug 1-After click on the Header swag labs name icon, that not navigate to the homepage or any other links).
 2.Sidebar options failing to perform - (Bug 2- Reset App State option is not working  and Bug 5- Logout confirmation pop-up message is not displayed).
 3.Serious flaws in the checkout process allow to complete the order without product selection - (Bugs 3- User unable to add the quantity of the product while click the Add to cart button and Bug 4-User able to place the order without adding any product to the Cart ).

- Note any recommendations for future testing or improvements-

  1.Immediate Fixes for Critical Bugs: Prioritize addressing the critical and high severity bugs to ensure functionalities.
  2.Improved Error Handling: Make sure the application shows clear messages and prevents users from moving forward if they haven't completed necessary steps specially during checkout.
  3.Test Coverage: Add automated tests for important user actions like adding items to the cart and checking out.
  4.User Confirmation Steps: Add confirmation messages for important actions like logging out actions.
  5.Thorough Regression Testing: After finding the identified issues, perform regression test to ensure that fixes do not introduce new bugs.

## Files Included

- `SWAGsystem_Anushiga.xlsx`: The detailed manual test cases for Swag Labs.
- `SWAGsystem_Anushiga.xlsx`: Results of the executed test cases.
- `SWAGsystem_Anushiga.xlsx`: A document summarizing the bugs found during testing.
- ``: The automated test script.
- ``: Instructions to run the automated test script.
- `SWAGsystem_Anushiga.xlsx`: A summary report of the testing efforts and results.

