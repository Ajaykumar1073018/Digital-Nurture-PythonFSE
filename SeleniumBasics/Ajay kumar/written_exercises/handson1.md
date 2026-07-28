# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System
1. **Testing Types for Course Management API:**
   * **Unit Testing:** Testing a single Python function in isolation, such as testing the `get_password_hash` function to ensure it properly hashes a string[cite: 3].
   * **Integration Testing:** Testing two components working together, such as testing the API endpoint connected to a test database to ensure data is saved correctly[cite: 3].
   * **System Testing:** Testing a full end-to-end flow, from sending a POST request to `/api/courses/` down to verifying the database transaction and the final JSON response[cite: 3].
   * **User Acceptance Testing (UAT):** Testing from the perspective of an actual college admin user to ensure the API meets business requirements and workflows[cite: 3].
2. **Classification:** 
   * The four test cases listed above are classified as **Functional** testing because they verify if the system does what it should[cite: 3]. 
   * **Non-Functional Example:** A performance test checking how fast the `/api/courses/` endpoint responds under a load of 100 concurrent users[cite: 3].
3. **Black-Box vs. White-Box:**
   * **Black-Box Testing:** Testing without any knowledge of the internal code structure, evaluating only inputs and outputs. This is typically performed by a QA tester[cite: 3].
   * **White-Box Testing:** Testing with full knowledge of the internal code and architecture. This is typically performed by a developer[cite: 3].
4. **Test Cases for POST /api/courses/**

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC_01 | Create valid course | Admin is authenticated | 1. Send POST with valid JSON body (name, code, credits). | Returns 201 Created with course data. | | |
| TC_02 | Create duplicate course | Course "CS101" exists | 1. Send POST with code "CS101". | Returns 400/409 Error. | | |
| TC_03 | Missing required field | Admin is authenticated | 1. Send POST missing "name" field. | Returns 400/422 Bad Request. | | |

## Task 2: Defect Lifecycle & Severity Classification
5. **Defect Lifecycle:** New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed[cite: 3]. If a bug is invalid, it goes from Open -> Rejected[cite: 3]. If it will be fixed in a later release, it goes from Open -> Deferred[cite: 3].
6. **Defect Classification:**
   * **(a) 500 Internal Server Error:** Severity: Critical, Priority: P1. Justification: Complete failure of a core function blocking further testing[cite: 3].
   * **(b) Course names truncated:** Severity: Medium, Priority: P3. Justification: System functions but data is lost or altered inappropriately[cite: 3].
   * **(c) Swagger typo:** Severity: Low, Priority: P4. Justification: Cosmetic issue that does not affect functionality[cite: 3].
   * **(d) Intermittent 401:** Severity: High, Priority: P2. Justification: Affects authentication and indicates deeper instability, even if hard to reproduce[cite: 3].
7. **Defect Report for Bug (a):**
   * **Defect ID:** BUG-101
   * **Title:** POST /api/courses/ returns 500 Internal Server Error for all requests
   * **Environment:** QA / Localhost
   * **Build Version:** v1.0.0
   * **Severity:** Critical
   * **Priority:** P1
   * **Steps to Reproduce:** 1. Authenticate as Admin. 2. Send POST request to /api/courses/ with valid payload.
   * **Expected Result:** API returns 201 Created and saves the course.
   * **Actual Result:** API returns 500 Internal Server Error.
   * **Attachments:** screenshot of 500 error[cite: 3].
8. **Severity vs. Priority:** Severity measures the defect's impact on the system, while Priority measures how urgently it needs to be fixed[cite: 3]. **Example:** A cosmetic typo on the CEO's main dashboard might have Low Severity (doesn't break the app) but High Priority (looks highly unprofessional to leadership)[cite: 3].