import speedtest
speed =speedtest.Speedtest()
print("Checking Upload speed....")
print("upload speed :",speed.upload())
print("Checking Download speed......")
print("Download speed :",speed.download())
print("MS :",speed.results.ping)

