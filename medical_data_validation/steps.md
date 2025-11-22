# Medical Data Validation Workshop - Steps Summary

**Step 1:** Create initial data structure (list of medical records) and basic validate function to check if data is a list or tuple.

**Step 2:** Add check for is_invalid variable and return False if invalid sequence.

**Step 3:** Add key_set for expected keys and initialize is_invalid to False.

**Step 4:** Add for loop to iterate over data.

**Step 5:** Check if each item is a dict, print error and set is_invalid if not.

**Step 6:** Check if dict keys match key_set, print error and set is_invalid if not.

**Step 7:** Move return statements outside the loop.

**Step 8:** Add print "Valid format." when data is valid.

**Step 9:** Create find_invalid_records function stub.

**Step 10:** Add call to find_invalid_records in validate function.

**Step 11:** Update find_invalid_records to take parameters.

**Step 12:** Create empty constraints dictionary in find_invalid_records.

**Step 13:** Add patient_id key to constraints with isinstance check.

**Step 14:** Add age key to constraints with isinstance check.

**Step 15:** Add gender key to constraints with isinstance check.

**Step 16:** Add diagnosis key to constraints with isinstance check.

**Step 17:** Add medications key to constraints with isinstance check.

**Step 18:** Add last_visit_id key to constraints with isinstance check.

**Step 19:** Add import re at top of file.

**Step 20:** Update patient_id constraint to include re.search for pattern 'p'.

**Step 21:** Add re.IGNORECASE to re.search.

**Step 22:** Change to r'p' and add raw string.

**Step 23:** Add patient_id key with isinstance and regex check.

**Step 24:** Import re module.

**Step 25:** Update patient_id to use fullmatch instead of search.

**Step 26:** Add IGNORECASE to fullmatch.

**Step 27:** Update pattern from 'p' to 'p\d'.

**Step 28:** Update pattern to 'p\d+'.

**Step 29:** Switch to re.fullmatch with r'p\d+'.

**Step 30:** Add age key with isinstance and age >= 18.

**Step 31:** Add gender key with isinstance, lower(), and in ('male', 'female').

**Step 32:** Add diagnosis key allowing str or None.

**Step 33:** Add medications key with isinstance(list) and all elements str.

**Step 34:** Add medications with list comprehension for isinstance checks.

**Step 35:** Add all() for medications string check.

**Step 36:** Add last_visit_id key with isinstance and fullmatch 'v\d+'.

**Step 37:** Change return to list of invalid keys using list comprehension.

**Step 38:** Add if not value in list comprehension (already had).

**Step 39:** Remove print statement.

**Step 40:** Add invalid_records = find_invalid_records(**dictionary) in validate loop.

**Step 41:** Add continue after setting is_invalid in both if statements.

**Step 42:** Add for loop to print unexpected format messages for invalid records.

The medical data validation system is now complete, validating patient records for proper structure, types, and patterns, and providing detailed error messages for invalid data.
