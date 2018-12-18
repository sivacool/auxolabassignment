nohup python3 server.py &> server.out&
nohup python3 loadbalancer.py &> loadbalancer.out&

locust -c 10 -r 5 -t 1m --no-web --host http://localhost:5000 --csv=log