#!/usr/bin/env python
import csv, urllib, optparse

def main():
    tinderImageBaseUrl="http://images.gotinder.com"
    parser = optparse.OptionParser()
    
    parser.add_option("-f", "--filename", metavar="FILENAME", help="CSV file with photo data")
    (options, args) = parser.parse_args()
    
    if not options.filename:  
        parser.error('Filename not given')

    with open(options.filename) as csvfile:
        imagereader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for idx, row in enumerate(imagereader):
            usrId= row[1]
            imgId= row[0]
            urllib.urlretrieve(tinderImageBaseUrl+"/"+usrId+"/"+imgId+".jpg",usrId+"_"+imgId+".jpg")
            print '\rImage Number {0} retrieved'.format(idx),           
         
if __name__ == '__main__':
    main()


         
