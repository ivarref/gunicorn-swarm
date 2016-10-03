# gunicorn-swarm

Try to run [Gunicorn](http://gunicorn.org/) as a [Docker swarm](https://docs.docker.com/engine/swarm/) service. 
As far as I know this does not currently work correctly. 
See details below for how to reproduce the issue:

    $ virtualenv venv
    
    $ ./venv/bin/pip install -r ./requirements.txt

    # set up docker swarm and create initial service

    $ docker swarm init --advertise-addr 127.0.0.1

    $ docker build --tag=web:latest .

    $ docker service create --publish 8080:8080 --replicas 2 --name my_web --update-delay 10s web:latest

At this point you should open a new terminal and start executing hammer.py:

    $ ./venv/bin/python ./hammer.py

Then you should build and deploy a new server:

    $ ./redeploy_server.sh

At this point hammer.py will probably crash with a stacktrace like this:

    File "hammer.py", line 15, in <module>
        response = requests.get('http://localhost:8080/')
    File "/home/ire/code/gunicorn-swarm/venv/local/lib/python2.7/site-packages/requests/api.py", line 70, in get
        return request('get', url, params=params, **kwargs)
    File "/home/ire/code/gunicorn-swarm/venv/local/lib/python2.7/site-packages/requests/api.py", line 56, in request
        return session.request(method=method, url=url, **kwargs)
    File "/home/ire/code/gunicorn-swarm/venv/local/lib/python2.7/site-packages/requests/sessions.py", line 475, in request
        resp = self.send(prep, **send_kwargs)
    File "/home/ire/code/gunicorn-swarm/venv/local/lib/python2.7/site-packages/requests/sessions.py", line 596, in send
        r = adapter.send(request, **kwargs)
    File "/home/ire/code/gunicorn-swarm/venv/local/lib/python2.7/site-packages/requests/adapters.py", line 473, in send
        raise ConnectionError(err, request=request)
    requests.exceptions.ConnectionError: ('Connection aborted.', error(104, 'Connection reset by peer'))
