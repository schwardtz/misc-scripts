import csv, urllib
with open('photos.csv') as csvfile:
    imagereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for idx, row in enumerate(imagereader):
        imgId= row[0].split(',')[1].strip('"')
        usrId= row[0].split(',')[0]
        urllib.urlretrieve("http://images.gotinder.com/"+imgId+"/"+usrId+".jpg",str(idx)+"_"+imgId+".jpg")
