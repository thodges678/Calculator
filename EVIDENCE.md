# Coursework evidence

Use these headings to organise your own results and explanations. Replace
bracketed prompts and remove unused prompts. Supplied headings are permitted
reuse; the evidence and explanation must be your own. Refer to short saved
logs rather than pasting entire CI logs.

Staff will not open your private GitHub repository. Save PR pages and CI
runs as PDFs or screenshots, with short log excerpts, in `evidence/` and
give their paths below alongside the URLs.

Complete and commit this file with your other documentation before the final
release checks. Record the final release hash, CI run and fresh-checkout outcome
in the separately submitted `SUBMISSION.txt`, outside the repository, and
submit the final CI run as a separate PDF or screenshot.

## 1. Starting point and Git review

- Starting commit: [59dbd9338f8d6f9af7189835a5e5aa79bc314aac]
- Reused lab files, tests and examples: 
    [calculator.py -Allows for input of two numbers and a operations of add, subtract, mutliply     or  divide
    run.sh - Bash file to allow calculator to be run from ./run.sh
    check.sh - Bash file to display whether a test is passed
    test_calculator.py - Pytest file to test calculator functions
    requirements-dev.txt - Contains required software to run the code
    REQUIREMENTS.md - Contains 6 requirements for calculator.py
    README.md - Contains brief description of how use calculator and what it does
    .gitignore - Contains files to be ignored by git]
- Feature branch and PR: 
    [Coursework,(https://github.com/thodges678/Calculator/pull/3), Inital Feature Branch PR.pdf]
- Self-review: 
    [Added Evidence files before-commit.txt holding the commit hash, and local-before.txt holding the test result.
    As well as the test_batch_calculator.py file and editing EVIDENCE.md]

## 2. Test failure, diagnosis and fix

Plan this before fixing the chosen missing requirement or defect. An initially
missing feature is acceptable; retain the test in the final suite.

- Requirement and retained test: [
    R1 - Addition, test_batch_calculator.py -                                 test_proccess_addition]
- Expected result and actual failure: [
    Expected result - "OK", 13, "" 
    Actual failure - NotImplementedError]
- Before/fix commits: [Before - cfd59fa3dd49c2a86973f0123cf929fd26928eac
                       Fix - a2c88dae97497fed3ffa7de049d172f10743534f ]
- Failing/passing local runs: [
    Command python3 -m pytest -v > evidence/local-before.txt 2>&1 Outcome - Test failed with NotImplementedError, Test passed Log Pathes - evidence/local-before.txt, evidence/local-after.txt ]
- Failing/passing CI runs: 
    [Before - URL(https://github.com/thodges678/Calculator/actions/runs/44670624222) evidence/ci-before-commit.pdf, evidence/ci-before-commit-log-exert.txt
    After - URL https://github.com/thodges678/Calculator/actions/runs/44929071654 commit - a2c88dae97497fed3ffa7de049d172f10743534f, evidence/ci-after.pdf, evidence/ci-after.txt]
- CI diagnosis: 
    [event- push , runner- ubuntu-latest, job- tests, failed step - Run the tests, Log message - NotImplementedError, Error: Process completed with exit code 1]
- Cause and implementation fix: 
    [Tests job raised a NotImplementedError as addition wasn't implemented. Procces_calculation function within batch_calculator.py was subsequently updated to accomdate the wanted behaviour. Tests assertion was unchanged and went from failing to passing between the two commits]

## 3. Repeatable checks and local hook

- Common check script: [
    Path - scripts/check.sh. Run locally with ./scripts/check.sh
    Ci calls it with ./scripts/check.sh after installing dependencies
    The script runs the pytest tests on both calculator.py and batch_calculator.py. The set -e command ensures that the script exits with non-zero on the first failure.
    Hook -]
- Prerequisites and hook installation: [commands or README reference]
- Blocked commit attempt: [short transcript, base commit and working-tree state]
- Permitted commit after the fix: [short transcript and resulting hash]
- Hook limitations and independent CI checks: [your explanation]

The hook may use the same failure case as section 2 or another case. A blocked
commit attempt has no new commit hash; identify its base commit and changes.

## 4. Native and container batch runs

- Native normal/mixed runs: [
    commands: python3 batch_runner.py data/normal.csv results.csv > evidence/native-normal-summary.txt 2> evidence/native-normal-errors.txt
    python3 batch_runner.py data/mixed.csv mixed-results.csv > evidence/native-mixed-summary.txt 2> evidence/native-mixed-errors.txt  
    Normal - evidence/native-normal-summary.txt + evidence/native-normal-errors.txt
    Mixed - evidence/native-mixed-summary.txt + evidence/native-mixed-errors.txt]
- Container build/run commands and image tag: [README reference or commands]
- Input/output transfer: [how files enter and leave the container]
- Mixed-run interpretation: [
Native run: 
    The mixed.csv file was able to be fully processed giving the summary that 8 records were procssed, 4 succeded, 4 failed. [native-mixed-summary.txt]
    This is the desired output for the input file and displays the the program is working as intended.

    Record 2 failed with the DIVISION_BY_ZERO Error due to the input (divide, 9, 0) [native-mixed-errors.txt]
    However, the following record 3 (multiply, 4, 5) succeeded and the rest of the file was able to be processed.

Container run: 

]
- Python version and Docker environment: [what you used]

## 5. Container checks in CI during development

- Checked-out source commit and CI run: [hash, URL and saved file in evidence/]
- Test gate, image build and smoke-test outcomes: [steps and results]
- Smoke fixture and expected-output check: [paths and what is asserted]
- Failure handling: [why failed tests stop the build and wrong output fails CI]

## 6. Reproduction notes

- Checkout tested during development: [commit]
- Documented setup and commands tried: [README reference]
- Outcome and any limitations: [your results]

The final fresh checkout must test the declared release commit. Record its
outcome in `SUBMISSION.txt` after the documentation is committed, CI passes
and the final commit is tagged. Do not create another commit just to insert
that commit's own hash or CI-run URL into this file.
