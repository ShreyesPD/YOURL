import mysql.connector

class ratingData:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234!@#$',
            port='3306',
            database='project'
        )
        self.Ecursor = self.mydb.cursor()


class inputRating(ratingData):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def rateURL(self, value,user):
        self.value = value
        self.user = user
        print(self.value,self.url,self.user)
        #self.url = url
        try:
            self.sql = "INSERT INTO rating(email_id,url,u_rating) VALUES(%s,%s,%s) "
            self.val = [self.user,self.url, self.value]
            self.Ecursor.execute(self.sql, self.val)
            self.mydb.commit()
            self.Ecursor.close()
            self.mydb.close()
            print("Exit")
        except Exception as  es:
            print(es)
            self.Ecursor.close()
            self.mydb.close()
            print("Exit")
            return False

# inputRating("gcq.ac.in").rateURL(4.5,"yashdesaai@gmail.com")

class outputRating(ratingData):
    def __init__(self, url):
        super().__init__()
        self.url = url

    # return getRating()

    def getRating(self):
        try:
            self.sql = "SELECT avg(u_rating) FROM rating WHERE url = %s"
            self.Ecursor.execute(self.sql, [self.url])
            self.myresult = self.Ecursor.fetchall()
            print(self.myresult)
            self.Ecursor.close()
            return self.myresult
        except Exception as ess:
            pass

# outputRating("gcq.ac.in").getRating()
