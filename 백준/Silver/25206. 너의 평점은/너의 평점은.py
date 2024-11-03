total_credits = 0.0
score_by_subject = 0.0

rate_list = {
  "A+": 4.5,
  "A0": 4.0,
  "B+": 3.5,
  "B0": 3.0,
  "C+": 2.5,
  "C0": 2.0,
  "D+": 1.5,
  "D0": 1.0,
  "F": 0.0,
}

for _ in range(0, 20):
  subject, credit, rate = input().split()
  
  if rate == 'P':
    continue
  else:
    total_credits += float(credit)
    score_by_subject += rate_list[rate] * float(credit)

print("%.6lf" % (score_by_subject / total_credits))