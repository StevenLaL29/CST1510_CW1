"""
RECORD CHECK  -  my version
===========================

Name  : Steven 
Lane  :  AI / Cyber / IT      (delete two)
Date  : 30/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter label: ")      # replace with an input() call
value = float(input("Enter value: "))     # replace with an input() call, converted with float()
limit = float(input("Enter limit: "))     # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
difference = limit - value
percentage_left = (difference / limit * 100) if limit != 0 else 0
percentage_used = float(difference / limit * 100) if limit != 0 else 0



print(difference)
print(percentage_left) # replace with your calculations
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#    if.                "WARNING" (90% or more), otherwise "OK
if percentage_used >= 100:
    status = "OVER LIMIT"
elif percentage_used >= 90:
    status = "WARNING"
else:
    status = "OK"
    print(status)  # replace with your if / else (or if / elif / else)

over_limit_count = 0
if status == "OVER LIMIT":
    over_limit_count += 1


status = ""  # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"Label: {label}")
print(f"Value: {value:.2f}")
print(f"Limit: {limit:.2f}")
print(f"Difference: {difference:.2f}")
print(f"Percentage left: {percentage_left:.2f}%")
print(f"Status: {status}")
print("=" * 34)
over_limit_count = 1 if status == "OVER LIMIT" else 0
print(f"Records over limit this session: {over_limit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
