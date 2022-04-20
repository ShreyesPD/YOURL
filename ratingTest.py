import mysql.connector

class ratingData:
	def __init__(self):
		self.mydb =mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='1234!@#$',
                                port='3306',
                                database='project'
                            )
		self.Ecursor = self.mydb.cursor()

		
class inputRating(ratingData):
	def __init__(self,url):
		super().__init__()
		self.url = url
	
	def rateURL(self, value,user):
		self.value = value
		#self.url = url
		self.user = user
		if (value >= 0 and value <=5):
			self.sql = "UPDATE profile SET url=%s , rating=%s where email_id=%s"
			self.val = [self.url, self.value, self.user]
			self.Ecursor.execute(self.sql, self.val)
			self.mydb.commit()
			self.Ecursor.close()
			self.mydb.close()
			print("Exit")

#inputRating("gcq.ac.in").rateURL(4.5,"yashdesaai@gmail.com")

class outputRating(ratingData):
	def __init__(self,url):
		super().__init__()
		self.url = url
		#return getRating()
	
	def getRating(self):
		self.sql = "SELECT avg(rating) FROM profile WHERE url = %s"
		self.Ecursor.execute(self.sql, [self.url])
		self.myresult = self.Ecursor.fetchall()
		"""for ele in self.myresult:
			if(ele == 5):
				self.total5 += 1
			elif(ele == 4):
				self.total4 += 1
			elif(ele == 3):
				self.total3 += 1
			elif(ele == 2):
				self.total2 += 1
			elif(ele == 1):
				self.total1 += 1
		self.total = (self.total5 * 5) + (self.total4 * 4) + (self.total3 * 3) + (self.total2 * 2) + (self.total1 * 1)
		self.responseTotal = self.total5 + self.total4 + self.total3 + self.total2 + self.total1
		self.fiveStarRate = self.total / self.responseTotal
		#return self.fiveStarRate"""
		print(self.myresult)
		self.Ecursor.close()

outputRating("gcq.ac.in").getRating()
