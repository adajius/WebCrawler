import urllib.request
import urllib.error
import csv

def mycrawler():
    """
        This function crawls a web page from allrecipes.com to extract information aboout a recipe
        List of recipes can be read from CSV file called SomeNode.csv or typed in manually
        Results are stored in new CSV file called output.csv
        :return:
    """

    
    from bs4 import BeautifulSoup

    # specify the url or read from CSV file
    # quote_page = "http://allrecipes.com/recipe/45426/lentil-and-sausage-soup/?internalSource=hn_carousel%2001_Lentil%20and%20Sausage%20Soup&referringId=16982&referringContentType=recipe%20hub&referringPosition=carousel%2001"

    with open('SomeNode.csv', newline='') as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            quote_page = row[0]
            page = urllib.request.urlopen(quote_page)
            soup = BeautifulSoup(page, 'html.parser')

            # calories
            name_cal = soup.find("span", attrs={"class": "calorie-count"})
            cal = name_cal.span.contents
            print ("NAME BOX", cal)

            # calories desc
            name_cal_desc = soup.find("span", attrs={"class": "calorie-count__desc"})
            cal_desc = name_cal_desc.contents
            print ("NAME BOX", cal_desc)

            for i in cal:
                for j in cal_desc:
                    output = str(i), j.string.strip()
                    print("JJ", j)
                    print(output)
              
            with open('output.csv', 'w') as myFile:
                writer = csv.writer(myFile)
                writer.writerows([output])


mycrawler()
