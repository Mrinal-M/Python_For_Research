import pandas as import pd
import matplotlib.pyplot as plt
import datetime

bird_data=pd.read_csv(r"C:\Users\Mrinal M\Desktop\CaseStudy\Bird\bird_tracking.csv")
Birds= bird_data.bird_name.unique()
# Eric= bird_data.bird_name== "Eric"
# Nico= bird_data.bird_name== "Nico"
# Sanne= bird_data.bird_name== "Sanne"

# xe,ye=bird_data.longitude[Eric],bird_data.latitude[Eric]
# xn,yn=bird_data.longitude[Nico],bird_data.latitude[Nico]
# xs,ys=bird_data.longitude[Sanne],bird_data.latitude[Sanne]
for bird in Birds:
    index= bird_data.bird_name==bird
    x,y=bird_data.longitude[index],bird_data.latitude[index]
    plt.plot(x,y,".")
plt.figure(figsize==(10,10))
plt.xlabel=("longitude")
plt.ylabel=("latitude")
plt.legend(loc="lower right")
plt.savfig("Bird migration.pdf")
plt.show()


