from pipeline.temporalcv import make_fake_todays

actual_output = make_fake_todays(365)

expected_output = ("[datetime.datetime(2014, 1, 1, 0, 0), "
                   "datetime.datetime(2015, 1, 1, 0, 0), "
                   "datetime.datetime(2016, 1, 1, 0, 0)]")

if str(actual_output) == expected_output:
    print("tests pass")
else:
    print("tests don't pass")