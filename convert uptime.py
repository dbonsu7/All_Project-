from datetime import timedelta
ns = 45873179636163
print(timedelta(microseconds=round(ns, -3) // 1000))
