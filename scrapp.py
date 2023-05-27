from bs4 import BeautifulSoup #parsing html
import requests  #send HTTP request 
import os #gerer les données de repertoire

cur_dir = os.getcwd() #current work directory 

for page in range(1,26): #
  url = "https://www.jumia.com.tn/catalog/?q=smartphones" + "&page=" +str(page)+"#catalog-listing"
  furl = requests.get(url)
  jsoup = BeautifulSoup(furl.content , 'html.parser')
  products = jsoup.find_all('div' , class_ = 'info')
  productsLink=jsoup.find_all('div', class_ = 'prd')
  print(productsLink)
  for p in productsLink :
   link = jsoup.find('a')['href']
   #os.system(f"{link}  >> products.txt ")
   print(link)

  for product in products:
      Name = product.find('h3' , class_="name").text.replace('\n', '')
      Price = product.find('div' , class_= "prc").text.replace('\n', '')
      #BoutiqueName = product.find('div' , class_= "bdg").text.replace('\n', '')
      #df = pd.DataFrame({'Product Name':Name,'Price':Price}) 
      #df.to_csv(f'{cur_dir}/products.csv', index=True, encoding='utf-8')
      with open("prod.txt","a+",encoding='utf-8') as f:
        f.write(f"product name {Name} , + \n\r  price {Price} \n\r")
        f.write("\n\n\r")
        
      try:
        Rating = product.find('div', class_='stars _s').text.replace('\n', '')
        #df = pd.DataFrame({'Product Name':Name,'Price':Price,'Rating':Ratings}) 
        #df.to_csv(f'{cur_dir}/productsrate.csv', index=False, encoding='utf-8')
       
        
        
        
      except:
        Rating = 'None'

      info = [ Name, Price,Rating]
      print(info)
