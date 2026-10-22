#Thread

'''for i in range(1,5):
    print(i)

for j in range(1,5):
    print(j)'''


'''a=10
b=20
print("a value is ",a," b vaue is",b)

print(f"a value is {a} b value is {b}")'''




'''import threading
import time



def first():

    for i in range(5):
        print(f"Loop 1: {i}")

        time.sleep(2)  #1000 mii 1 sec
    
def second():
    for i in range(5):
        print(f"Loop 2: {i}")
        time.sleep(2)





# create threads


t1 = threading.Thread(target=first,"saree)
t2 = threading.Thread(target=second)

# start threads
t1.start()
t2.start()

# wait for both to finish
t1.join()
t2.join()

print("Both loops finished")'''




'''import threading
import time




def place_order(product_name):

    print(f"Order placed for: {product_name}")
    time.sleep(2)  # simulate processing time
    print(f"Order confirmed: {product_name}")





# take input from user
products = []  #sare,shirt


n = int(input("Enter number of products: "))

for i in range(n):

    name = input(f"Enter product {i+1} name: ")
    products.append(name)

# create threads for each product

threads = []  #

for i in products:  #["saree","shirt"]
    t = threading.Thread(target=place_order, args=(i,))
    threads.append(t)
    t.start()

# wait for all threads
for t in threads:
    t.join()

print("All orders completed!")'''

#bank=>def __init__   with,depo,balance

#zomato=>def __init__  dell




import threading
import time




'''class BankAccount:

    def __init__(self, name, acc_no, balance):
        
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.lock = threading.Lock()




    def deposit(self, amount):
        with self.lock:
            time.sleep(2)

            if amount > 0:

                self.balance =self.balance+amount
                print("Deposited:", amount)
                print("Balance:", self.balance)
            else:
                print("Invalid amount")



    def withdrawal(self, amount):
        with self.lock:
            time.sleep(2)

            if amount > 0 and amount <= self.balance:

                self.balance =self.balance-amount
                print("Withdrawn:", amount)
                print("Balance:", self.balance)


            else:
                print("Insufficient balance or invalid amount")

    def check_balance(self):
        with self.lock:
            print("Name:", self.name)
            print("Account Number:", self.acc_no)
            print("Current Balance:", self.balance)





account = BankAccount("Susmitha", 12345, 10000)

account2 = BankAccount("viji", 123456, 20000)


account.check_balance()

t1 = threading.Thread(target=account.deposit, args=(2000,))
t2 = threading.Thread(target=account.withdrawal, args=(3000,))

t1.start()
t2.start()

t1.join()
t2.join()

account.check_balance()'''



from collections import deque



#LIFO
c=[200,400,700]

b=deque(c)

b.append("hii")
b.appendleft(900)
b.pop()
b.popleft()


#stack pop last lifo
#fifo

a=[100,"java","react"]
a.append(800)


print(b)



