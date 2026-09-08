import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nikheth@20",
                database="gymdb"

            )
            return self.connection

        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for rec in records:
                print(rec)
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from member where id =%s"
            value=(id,)
            self.cursor.execute(query,value)
            record =self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def post(self,**kwargs):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="insert into member(name,mobile,place,plan,fee,joined_on) values(%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Member details Added")
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.get_object(id=id)
            values=(id,)
            record=self.cursor.fetchone()
            if record ==None:
                print("Member Not found")
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record=self.get_object()
            if record != None:
                values=(id,)
                query="delete from member where id=%s"
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member Deleted successfully")
                self.get()
            else:
                print("Member not found")
        except Exception as e:
            print(e)


    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record != None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k + "=%s ,"
                placeholder=placeholder.rstrip(",")
                query=f"update member set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member details updated")
                self.get()
            else:
                print("Member NOt found")
        except Exception as e:
            print(e)


# connection_instance=DbConnect()
# print(connection_instance.get_connection())

member_instances=GymMemberManager()
# member_instances.post(name="Nikheth",mobile="9956234501",place="Pala",plan="6 month",fee=10000,joined_on="2024-05-15")
# member_instances.get()
# member_instances.retrieve(2)
#member_instances.delete(3)
member_instances.put(2,fee=5500)