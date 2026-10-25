def check (score, doc, income, failed): 
   if score < 70:
      return "Reject", "score is less than 70"
   if doc == False:
      return "Reject", "document incomplete"
   if income >= 50000:
      return "Reject", "income is 50000 or more"
   if failed > 0:
      return "Reject", "failed one or more courses"
   return "ELIGIBLE", "all conditions met"

print("C1: Pass")
print("Input: score=80, doc=True, income=30000, failed=0")
print("Expected: ELIGIBLE")
result, reason = check(80, True, 30000, 0)
print("Actual:", result)
print("Reason:", reason)
print()

print("C2: Income fails")
print("Input: score=85, docs=True, income=90000, failed=0")
print("Expected: REJECT")
result, reason = check(85, True, 90000, 0)
print("Actual:", result)
print("Reason:", reason)
print()

print("C3: Failed course")
print("Input: score=85, docs=True, income=30000, failed=2")
print("Expected: REJECT")
result, reason = check(85, True, 30000, 2)
print("Actual:", result)
print("Reason:", reason)
print()

print("C4: Boundary (score exactly 70)")
print("Input: score=70, docs=True, income=30000, failed=0")
print("Expected: ELIGIBLE")
result, reason = check(70, True, 30000, 0)
print("Actual:", result)
print("Reason:", reason)
print()
