from pipeline.temporalcv import make_fake_todays

print("Actual output:")
print(make_fake_todays(365))

print("Expected output:")
print("[datetime.datetime(2014, 1, 1, 0, 0), ")
print("datetime.datetime(2015, 1, 1, 0, 0), ")
print("datetime.datetime(2016, 1, 1, 0, 0)]")