# Natural Log Approximation Calculator
This code calculates the natural logarithm of a user-provided value xxx using a series expansion and compares it to the exact value using Python’s built-in log function. Here’s a breakdown:
Input validation: Ensures xxx is between 0 and 2.
Tolerance: Accepts a tolerance level for the approximation.
Logarithm approximation: Uses a series expansion to approximate ln⁡(x)\ln(x)ln(x), summing terms based on the user-defined tolerance.
Exact comparison: Computes the exact ln⁡(x)\ln(x)ln(x) using log(x) and prints both the approximation and exact value.
Difference calculation: Calculates the difference between the approximation and the exact value, displaying it in scientific notation if very small.
