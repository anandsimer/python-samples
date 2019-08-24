import redis


class MyRedis:

    def __init__(self):
        self.redis_host = 'localhost'
        self.redis_port = 6379
        self.redis_password = ''
        self.con = self.get_connection()

    def get_connection(self):
        # password can be None
        # decode_responses will enable redis to respond string literals (
        # else byte literals are returned).
        con = redis.StrictRedis(
            host=self.redis_host,
            password=self.redis_password,
            port=self.redis_port,
            decode_responses=True
        )
        return con

    def put_data_on_redis(self):
        # Putting a string message redis
        self.con.set('Welcome', 'Hello World!')

        # Putting a dictionary on redis
        rainbow = {'red': 50, 'blue': 100, 'green': 150}
        self.con.hmset('my_rainbow_dict', rainbow)

    def get_data_from_redis(self):
        # fetch the value with the associated key
        print(self.con.get('Welcome'))

        # fetch the value associated with the key in a dict
        print(self.con.hget("my_rainbow_dict", 'red'))

        # fetch whole dictionary
        print(self.con.hgetall("my_rainbow_dict"))


if __name__ == '__main__':
    myredis = MyRedis()
    myredis.put_data_on_redis()
    myredis.get_data_from_redis()
