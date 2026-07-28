# Hands-On 3: Test Automation Process & Framework Types

## Task 1: Automation Decision and Test Case Selection
1. **5 Criteria for Automation:** 
   * 1. **Repetitive:** The test runs frequently. 
   * 2. **High-Risk:** Tests critical business paths. 
   * 3. **Regression:** Needs testing after every change. 
   * 4. **Data-Driven:** Requires testing the same flow with massive amounts of varying data.
   * 5. **Stable:** The feature's UI or behavior is not rapidly changing.
   * *Applying to POST /api/courses/:* This endpoint is a core feature, highly repetitive, critical to the system, and stable, making it an excellent candidate for automation[cite: 3].
2. **Test Case Decisions:**
   * (a) Regression test for CRUD: **Automate**. Justification: Repetitive and high-risk[cite: 3].
   * (b) Exploratory testing: **Manual**. Justification: Cannot be automated; relies on human intuition[cite: 3].
   * (c) Performance test: **Automate**. Justification: Impossible to simulate 100 concurrent users manually[cite: 3].
   * (d) UI test for login form: **Manual** (or Automate conditionally). Justification: UI-heavy and rapidly changing tests are poor candidates for early automation[cite: 3].
   * (e) Verify API Swagger docs: **Manual**. Justification: One-time or infrequent visual check[cite: 3].
   * (f) Smoke test post-deploy: **Automate**. Justification: Needs to run rapidly and repetitively after every single deployment[cite: 3].
3. **Automation ROI Calculation:**
   * Test automation ROI measures the return on investment for the time spent automating[cite: 3].
   * Manual run = 30 mins. Automation creation = 240 mins. Automation maintenance = 6 mins (20% of 30 mins).
   * Time saved per run = 24 mins (30 mins - 6 mins). 
   * 240 mins / 24 mins = 10. The automation pays for itself after the **10th run**[cite: 3].
4. **Flaky Tests:**
   * A flaky test is one that sometimes passes and sometimes fails without any code changes, which undermines confidence in the test suite[cite: 3]. 
   * Example: A script fails because a page loaded 1 second too slow.
   * 3 Strategies: 1) Avoid hard-coded sleep() calls, 2) Use explicit waits, 3) Ensure isolated test data for each run[cite: 3].

## Task 2: Compare Automation Framework Types
5. **Framework Comparisons:**
   * **Linear:** Record and playback step-by-step. Advantage: Fast to create. Disadvantage: Zero reusability. Use: Quick throwaway scripts[cite: 3].
   * **Modular:** Breaking application into reusable functions. Advantage: High reusability. Disadvantage: Hardcoded data. Use: Stable apps with repetitive flows[cite: 3].
   * **Data-Driven:** Separating test logic from test data. Advantage: Run one script with hundreds of inputs. Disadvantage: Complex setup. Use: Form submissions[cite: 3].
   * **Keyword-Driven:** Test steps defined by external keywords. Advantage: Non-technical users can write tests. Disadvantage: Heavy framework overhead. Use: Teams with many manual testers[cite: 3].
   * **Hybrid:** Combines Modular and Data-Driven. Advantage: Maximum flexibility and reusability. Disadvantage: High initial setup time. Use: Large enterprise apps like the Course Management system[cite: 3].
6. **Recommendation:** 
   * The **Hybrid framework** is recommended because it provides the reusability needed for the 20 test cases, the parameterization needed for 50 logins, and can incorporate keywords for non-technical members[cite: 3].
7. **Hybrid Folder Structure:**
   * `/tests/` - Contains actual test execution files[cite: 3].
   * `/pages/` - Contains page object files separating UI logic[cite: 3].
   * `/data/` - Contains test data files (JSON/CSV) for data-driven testing[cite: 3].
   * `/utils/` - Contains utility files and helper functions[cite: 3].
   * `/config/` - Contains environment and framework configuration files[cite: 3].