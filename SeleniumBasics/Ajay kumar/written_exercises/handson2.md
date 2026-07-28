# Hands-On 2: SDLC vs TDLC & Agile QA Integration

## Task 1: V-Model Mapping
1. **V-Model Diagram:**
   * **Left Side (Development):** Requirements -> System Design -> Architecture Design -> Module Design -> Coding[cite: 3].
   * **Right Side (Testing):** Unit Testing (bottom) -> Integration Testing -> System Testing -> Acceptance Testing (top)[cite: 3].
2. **Test Artifact Mapping:**
   * Requirements Phase -> Acceptance Test plan is prepared[cite: 3].
   * System Design Phase -> System Test plan is prepared[cite: 3].
   * Architecture Design Phase -> Integration Test plan is prepared[cite: 3].
   * Module Design Phase -> Unit Test plan is prepared[cite: 3].
3. **Entry & Exit Criteria:**
   * **Unit Testing:** Entry - Module code is complete. Exit - All unit tests pass, no critical bugs.
   * **Integration Testing:** Entry - Modules are unit tested and integrated. Exit - All interfaces between modules function correctly.
   * **System Testing:** Entry - Integration testing complete, full environment ready. Exit - Defect count is below threshold, 100% test execution.
   * **Acceptance Testing:** Entry - System testing complete, no open critical/high defects[cite: 3]. Exit - Business stakeholders sign off.
4. **Early QA Engagement Points:**
   * During the **Requirements** phase to catch ambiguities before code is written[cite: 3].
   * During the **System Design** phase to plan testing data and environments early.

## Task 2: Agile QA and Shift-Left Testing
5. **Waterfall Problems:** 1) Testing happens too late, meaning defects are expensive to fix. 2) Requirements might be misunderstood, resulting in the wrong product being built. 3) QA becomes a bottleneck at the end of the project[cite: 3].
6. **QA in Agile Ceremonies:**
   * **Sprint Planning:** Defining acceptance criteria for stories[cite: 3].
   * **Daily Standup:** Raising blocking issues[cite: 3].
   * **Sprint Review:** Executing demo testing for stakeholders[cite: 3].
   * **Retrospective:** Suggesting process improvements[cite: 3].
7. **Shift-Left Practices applied to the API:** 
   * (a) Reviewing requirements for testability to ensure API inputs/outputs are clearly defined early[cite: 3].
   * (b) Writing test cases before code (TDD/BDD) so developers know exactly what the API must pass[cite: 3].
   * (c) Static code analysis to catch syntax/security errors before the code even runs[cite: 3].
   * (d) API contract testing before integration to ensure backend and frontend agree on the JSON format early[cite: 3].
8. **Acceptance Criteria (Given-When-Then):**
   * **Happy Path:** Given I am an authenticated admin, When I submit valid course details, Then a new course is created and students can enroll.
   * **Duplicate:** Given a course with code "CS101" exists, When I submit a new course with code "CS101", Then I receive an error stating the code must be unique.
   * **Missing Fields:** Given I am creating a course, When I leave the "name" field blank, Then the system blocks submission and shows a validation error[cite: 3].