# json files.


infile = open("volcanos.json").read()
fixed = infile.replace("Latitude", "latitude").replace("Longitude","longitude")
outfile = open("volcanos.json","w+")
outfile.write(fixed)


"""
db.students.updateMany( {}, { $rename: { "oldname": "newname" } } )
works better for the below section
"""
# infile2 = open("meteorites.json", errors = "ignore").read()
# fixed2 = infile2.replace("reclat", "latitude").replace("reclong","longitude")
# outfile2 = open("meteorites.json","w+")
# outfile2.write(fixed2)
