#counties = ["Arapahoe","Denver","Jefferson"]


#if counties[1] == 'Denver':
#    print(counties[1])

#    counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#for county in counties:
#    print(county)


counties_dict = {'El Paso':461149, 'Jefferson':432438, 'Denver':463353, 'Arapahoe':422829}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):
for i in voting_data:
    print(f"County {i['county']} has this man voters: {i['registered_voters']:,}")