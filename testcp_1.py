x = int(input("Số kWh điện mà người dùng tiêu thụ:"))
if x<=50:
    print("Số tiền điện mà người dùng phải trả: " + str((x*1.728)), "đồng")
elif x<=100:
    print(" Số tiền điện mà người dùng phải trả: " + str(50*1.728+(x-50)*1.768), "đồng")
elif x<=200:
    print("Số tiền điện mà người dùng phải trả: " + str(50*1.728+50*1.768+(x-100)*2.074), "đồng")
elif x<=300:
    print("Số tiền điện mà người dùng phải trả: " + str(50*1.728+50*1.768+100*2.074+(x-200)*2.612), "đồng")
elif x<=400:
    print("Số tiền điện mà người dùng phải trả: " + str(50*1.728+50*1.768+100*2.074+100*2.612+(x-300)*2.919), "đồng")
else:
    print("Số tiền điện mà người dùng phải trả: " + str(50*1.728+50*1.768+100*2.074+100*2.612+100*2.919+(x-400)*3.015), " đồng")