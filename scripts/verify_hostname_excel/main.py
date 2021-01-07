import pandas

mail_df = pandas.read_csv(r"files\\mail_Car_New_Machines.csv")
car_df  = pandas.read_excel(r"files\\Servers_On_Car.xls", header=5, usecols=[4,5,6])

hostnames_car = car_df["Hostname"].dropna()

hostnames_mail = mail_df["Hostname"].drop_duplicates()

novos = []

for host in hostnames_mail:
  if host not in hostnames_car.array:
    novos.append(host)

print("Estes hosts não estão presentes no excel:\n{}".format(novos))